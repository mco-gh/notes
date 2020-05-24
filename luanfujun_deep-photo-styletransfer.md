luanfujun/deep-photo-styletransfer

###    README.md

# [(L)](https://github.com/luanfujun/deep-photo-styletransfer#deep-photo-styletransfer)deep-photo-styletransfer

Code and data for paper "[Deep Photo Style Transfer](https://arxiv.org/abs/1703.07511)"

## [(L)](https://github.com/luanfujun/deep-photo-styletransfer#disclaimer)Disclaimer

**This software is published for academic and non-commercial use only.**

## [(L)](https://github.com/luanfujun/deep-photo-styletransfer#setup)Setup

This code is based on torch. It has been tested on Ubuntu 14.04 LTS.
Dependencies:

- [Torch](https://github.com/torch/torch7) (with [matio-ffi](https://github.com/soumith/matio-ffi.torch) and [loadcaffe](https://github.com/szagoruyko/loadcaffe))
- [Matlab](https://www.mathworks.com/) or [Octave](https://www.gnu.org/software/octave/)

CUDA backend:

- [CUDA](https://developer.nvidia.com/cuda-downloads)
- [cudnn](https://developer.nvidia.com/cudnn)

Download VGG-19:

	normalsh models/download_models.sh
	normal

Compile ` cuda_utils.cu ` (Adjust ` PREFIX ` and ` NVCC_PREFIX ` in ` makefile ` for your machine):

	normalmake clean && make
	normal

## [(L)](https://github.com/luanfujun/deep-photo-styletransfer#usage)Usage

### [(L)](https://github.com/luanfujun/deep-photo-styletransfer#quick-start)Quick start

To generate all results (in ` examples/ `) using the provided scripts, simply run

	normalrun('gen_laplacian/gen_laplacian.m')
	normal

in Matlab or Octave and then

	normalpython gen_all.py
	normal

in Python. The final output will be in ` examples/final_results/ `.

### [(L)](https://github.com/luanfujun/deep-photo-styletransfer#basic-usage)Basic usage

1. Given input and style images with semantic segmentation masks, put them in ` examples/ ` respectively. They will have the following filename form: ` examples/input/in<id>.png `, ` examples/style/tar<id>.png ` and ` examples/segmentation/in<id>.png `, ` examples/segmentation/tar<id>.png `;

2. Compute the matting Laplacian matrix using ` gen_laplacian/gen_laplacian.m ` in Matlab. The output matrix will have the following filename form: ` gen_laplacian/Input_Laplacian_3x3_1e-7_CSR<id>.mat `;

3. Run the following script to generate segmented intermediate result:

	normalth neuralstyle_seg.lua -content_image <input> -style_image <style> -content_seg <inputMask> -style_seg <styleMask> -index <id> -serial <intermediate_folder>
	normal

1. Run the following script to generate final result:

	normalth deepmatting_seg.lua -content_image <input> -style_image <style> -content_seg <inputMask> -style_seg <styleMask> -index <id> -init_image <intermediate_folder/out<id>_t_1000.png> -serial <final_folder> -f_radius 15 -f_edge 0.01
	normal

You can pass ` -backend cudnn ` and ` -cudnn_autotune ` to both Lua scripts (step 3. and 4.) to potentially improve speed and memory usage. ` libcudnn.so ` must be in your ` LD_LIBRARY_PATH `. This requires [cudnn.torch](https://github.com/soumith/cudnn.torch).

### [(L)](https://github.com/luanfujun/deep-photo-styletransfer#image-segmentation)Image segmentation

Note: In the main paper we generate all comparison results using automatic scene segmentation algorithm modified from [DilatedNet](https://arxiv.org/abs/1606.00915). Manual segmentation enables more diverse tasks hence we provide the masks in ` examples/segmentation/ `.

Here are some automatic and manual tools for creating a segmentation mask for a photo image:

#### [(L)](https://github.com/luanfujun/deep-photo-styletransfer#automatic)Automatic:

- [MIT Scene Parsing](http://sceneparsing.csail.mit.edu/)
- [SuperParsing](http://www.cs.unc.edu/~jtighe/Papers/ECCV10/)
- [Nonparametric Scene Parsing](http://people.csail.mit.edu/celiu/LabelTransfer/)
- [Berkeley Contour Detection and Image Segmentation Resources](https://www2.eecs.berkeley.edu/Research/Projects/CS/vision/grouping/resources.html)
- [CRF-RNN for Semantic Image Segmentation](https://github.com/torrvision/crfasrnn)
- [Selective Search](https://github.com/belltailjp/selective_search_py)

#### [(L)](https://github.com/luanfujun/deep-photo-styletransfer#manual)Manual:

- [Photoshop Quick Selection Tool](https://helpx.adobe.com/photoshop/using/making-quick-selections.html)
- [GIMP Selection Tool](https://docs.gimp.org/en/gimp-tools-selection.html)

## [(L)](https://github.com/luanfujun/deep-photo-styletransfer#examples)Examples

Here are some results from our algorithm (from left to right are input, style and our output):

 [![in4.png](../_resources/96af5b3700a4e8d102a2e1e65916a876.png)](https://github.com/luanfujun/deep-photo-styletransfer/blob/master/examples/input/in3.png)  [![tar3.png](../_resources/615d8fa515d6c0a509f9f873252d394e.png)](https://github.com/luanfujun/deep-photo-styletransfer/blob/master/examples/style/tar3.png)  [![best3_t_1000.png](../_resources/fecc457dc5796b5f4b28dc0d7ba8d3fa.png)](https://github.com/luanfujun/deep-photo-styletransfer/blob/master/examples/final_results/best3_t_1000.png)

 [![in4.png](../_resources/96af5b3700a4e8d102a2e1e65916a876.png)](https://github.com/luanfujun/deep-photo-styletransfer/blob/master/examples/input/in4.png)  [![tar4.png](../_resources/1e7cbde1f84760c1732ac35625e9e424.png)](https://github.com/luanfujun/deep-photo-styletransfer/blob/master/examples/style/tar4.png)  [![best4_t_1000.png](../_resources/349e487e325ad8537d920eb7f7ae83ac.png)](https://github.com/luanfujun/deep-photo-styletransfer/blob/master/examples/final_results/best4_t_1000.png)

 [![in13.png](../_resources/7e277cb451f570ed92565187c92c4f91.png)](https://github.com/luanfujun/deep-photo-styletransfer/blob/master/examples/input/in13.png)  [![tar13.png](../_resources/9380b0dfd3efa747d7a16ff01f95c28b.png)](https://github.com/luanfujun/deep-photo-styletransfer/blob/master/examples/style/tar13.png)  [![best13_t_1000.png](../_resources/7719294e16e136121453aeccf5d04266.png)](https://github.com/luanfujun/deep-photo-styletransfer/blob/master/examples/final_results/best13_t_1000.png)

 [![in9.png](../_resources/88365c0c5a03b3e8315e69c259de4654.png)](https://github.com/luanfujun/deep-photo-styletransfer/blob/master/examples/input/in9.png)  [![tar9.png](../_resources/e10a7ed5e6f5d762eaa3c751201fc316.png)](https://github.com/luanfujun/deep-photo-styletransfer/blob/master/examples/style/tar9.png)  [![best9_t_1000.png](../_resources/e41f0d3f00f78dcd847f95a95fe4581e.png)](https://github.com/luanfujun/deep-photo-styletransfer/blob/master/examples/final_results/best9_t_1000.png)

 [![in20.png](../_resources/d141627d6071731aefbe45da67870422.png)](https://github.com/luanfujun/deep-photo-styletransfer/blob/master/examples/input/in20.png)  [![tar20.png](../_resources/9c416ba6d397457aaca928fc5c15fbf2.png)](https://github.com/luanfujun/deep-photo-styletransfer/blob/master/examples/style/tar20.png)  [![best20_t_1000.png](../_resources/8d191ae4203733b3405806056371ed8b.png)](https://github.com/luanfujun/deep-photo-styletransfer/blob/master/examples/final_results/best20_t_1000.png)

 [![in1.png](../_resources/672cefc1469cbdf6c8dd087b9461ae81.png)](https://github.com/luanfujun/deep-photo-styletransfer/blob/master/examples/input/in1.png)  [![tar1.png](../_resources/ca81dd2fdf2cba4c15d4cfb167d8eda9.png)](https://github.com/luanfujun/deep-photo-styletransfer/blob/master/examples/style/tar1.png)  [![best1_t_1000.png](../_resources/45877f291ccff3d35608fc81c4f62316.png)](https://github.com/luanfujun/deep-photo-styletransfer/blob/master/examples/final_results/best1_t_1000.png)

 [![in39.png](../_resources/016a5ad62f776a6154eee6e4af941231.png)](https://github.com/luanfujun/deep-photo-styletransfer/blob/master/examples/input/in39.png)  [![tar39.png](../_resources/5e969cf65ace4410c3de73945ba4505c.png)](https://github.com/luanfujun/deep-photo-styletransfer/blob/master/examples/style/tar39.png)  [![best39_t_1000.png](../_resources/3045e8ff13f062a09da4e04bc7395209.png)](https://github.com/luanfujun/deep-photo-styletransfer/blob/master/examples/final_results/best39_t_1000.png)

 [![in57.png](../_resources/fc540af273a7cb7d716f2a586327ad00.png)](https://github.com/luanfujun/deep-photo-styletransfer/blob/master/examples/input/in57.png)  [![tar57.png](../_resources/59267e3b04e44da1344fe25ccf550380.png)](https://github.com/luanfujun/deep-photo-styletransfer/blob/master/examples/style/tar57.png)  [![best57_t_1000.png](../_resources/073c942937a2cbf878467e4b83737527.png)](https://github.com/luanfujun/deep-photo-styletransfer/blob/master/examples/final_results/best57_t_1000.png)

 [![in47.png](../_resources/42bfef322dc6c76635beef137327485d.png)](https://github.com/luanfujun/deep-photo-styletransfer/blob/master/examples/input/in47.png)  [![tar47.png](../_resources/f90f4675a928fd7096409f4a3f1ecccc.png)](https://github.com/luanfujun/deep-photo-styletransfer/blob/master/examples/style/tar47.png)  [![best47_t_1000.png](../_resources/fec35707f0999c1fadaa7260934213b1.png)](https://github.com/luanfujun/deep-photo-styletransfer/blob/master/examples/final_results/best47_t_1000.png)

 [![in58.png](../_resources/5e60cb6a8a5bf4ffa94e66637e7670c9.png)](https://github.com/luanfujun/deep-photo-styletransfer/blob/master/examples/input/in58.png)  [![tar58.png](../_resources/adb2cff4c72894fa9f7e0526c116deb1.png)](https://github.com/luanfujun/deep-photo-styletransfer/blob/master/examples/style/tar58.png)  [![best58_t_1000.png](../_resources/b162954dc196a2a2865cebeea2150340.png)](https://github.com/luanfujun/deep-photo-styletransfer/blob/master/examples/final_results/best58_t_1000.png)

 [![in51.png](../_resources/1e493fabdaca8435cf1fa3faf006d816.png)](https://github.com/luanfujun/deep-photo-styletransfer/blob/master/examples/input/in51.png)  [![tar51.png](../_resources/c5a3d81eef4b83f92253acc3dde27303.png)](https://github.com/luanfujun/deep-photo-styletransfer/blob/master/examples/style/tar51.png)  [![best51_t_1000.png](../_resources/5064250007e3a27442a4e5d7fdf0970b.png)](https://github.com/luanfujun/deep-photo-styletransfer/blob/master/examples/final_results/best51_t_1000.png)

 [![in7.png](../_resources/26cc1b968813950d6543063987ba1713.png)](https://github.com/luanfujun/deep-photo-styletransfer/blob/master/examples/input/in7.png)  [![tar7.png](../_resources/35b0f497e0dc9429cf60385dba00baf7.png)](https://github.com/luanfujun/deep-photo-styletransfer/blob/master/examples/style/tar7.png)  [![best7_t_1000.png](../_resources/b38864592e96d4ac85ccdb7dc4a166da.png)](https://github.com/luanfujun/deep-photo-styletransfer/blob/master/examples/final_results/best7_t_1000.png)

 [![in23.png](../_resources/f848b53efb1c1ff8e811a3edcbfebe0c.png)](https://github.com/luanfujun/deep-photo-styletransfer/blob/master/examples/input/in23.png)  [![in23.png](../_resources/f848b53efb1c1ff8e811a3edcbfebe0c.png)](https://github.com/luanfujun/deep-photo-styletransfer/blob/master/examples/input/in23.png)  [![best23_t_1000.png](../_resources/89575c30556300c3ad8815e4a766cf7a.png)](https://github.com/luanfujun/deep-photo-styletransfer/blob/master/examples/final_results/best23_t_1000.png)

 [![in16.png](../_resources/ae66dc184ee6bb1bd780245af0e145f8.png)](https://github.com/luanfujun/deep-photo-styletransfer/blob/master/examples/input/in16.png)  [![tar16.png](../_resources/3c7ec3944beb3c0ac932867202cf59e6.png)](https://github.com/luanfujun/deep-photo-styletransfer/blob/master/examples/style/tar16.png)  [![best16_t_1000.png](../_resources/707514ad9395760da4b1063c2e6da751.png)](https://github.com/luanfujun/deep-photo-styletransfer/blob/master/examples/final_results/best16_t_1000.png)

 [![in30.png](../_resources/6e97c8d514e1168c6dc4cdacc9f1ec76.png)](https://github.com/luanfujun/deep-photo-styletransfer/blob/master/examples/input/in30.png)  [![tar30.png](../_resources/fff195b29643992052540bc5f0d1ce21.png)](https://github.com/luanfujun/deep-photo-styletransfer/blob/master/examples/style/tar30.png)  [![best30_t_1000.png](../_resources/4b1e0adf1c4a644a86843b9fd1331249.png)](https://github.com/luanfujun/deep-photo-styletransfer/blob/master/examples/final_results/best30_t_1000.png)

 [![in2.png](../_resources/318d4cfb69346b5dddd895e04d56a9d8.png)](https://github.com/luanfujun/deep-photo-styletransfer/blob/master/examples/input/in2.png)  [![tar2.png](../_resources/124f935866bbf7147f8bc53a7d241701.png)](https://github.com/luanfujun/deep-photo-styletransfer/blob/master/examples/style/tar2.png)  [![best2_t_1000.png](../_resources/b0e956ed5206aafdabc64b3664a6a6ec.png)](https://github.com/luanfujun/deep-photo-styletransfer/blob/master/examples/final_results/best2_t_1000.png)

## [(L)](https://github.com/luanfujun/deep-photo-styletransfer#acknowledgement)Acknowledgement

- Our torch implementation is based on Justin Johnson's [code](https://github.com/jcjohnson/neural-style);
- We use Anat Levin's Matlab [code](http://www.wisdom.weizmann.ac.il/~levina/matting.tar.gz) to compute the matting Laplacian matrix.

## [(L)](https://github.com/luanfujun/deep-photo-styletransfer#citation)Citation

If you find this work useful for your research, please cite:

	normal@article{luan2017deep,
	  title={Deep Photo Style Transfer},
	  author={Luan, Fujun and Paris, Sylvain and Shechtman, Eli and Bala, Kavita},
	  journal={arXiv preprint arXiv:1703.07511},
	  year={2017}
	}
	normal

## [(L)](https://github.com/luanfujun/deep-photo-styletransfer#contact)Contact

Feel free to contact me if there is any question (Fujun Luan [fl356@cornell.edu](https://github.com/luanfujun/deep-photo-styletransfermailto:fl356@cornell.edu)).