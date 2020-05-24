Introduction · Thinc · A refreshing functional take on deep learning

# Introduction

Thinc is a **lightweight deep learning library** that offers an elegant, type-checked, functional-programming API for **composing models**, with support for layers defined in other frameworks such as **PyTorch**, **TensorFlow** or**MXNet**. You can use Thinc as an interface layer, a standalone toolkit or a flexible way to develop new models. Previous versions of Thinc have been running quietly in production in thousands of companies, via both[spaCy](https://spacy.io/) and [Prodigy](https://prodi.gy/). We wrote the new version to let users **compose, configure and deploy custom models** built with their favorite framework. The end result is a library quite different in its design, that’s easy to understand, plays well with others, and is a lot of fun to use.

* * *

[

     [type_checking.webp](../_resources/68157a2dac7329f6d0ad449028788e32.webp)](https://thinc.ai/docs/usage-type-checking)

##### Type-check your model definitions

with custom types and [`mypy`](https://mypy.readthedocs.io/en/stable/) plugin

[Read more ![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='_593c1d19 _21270d89 js-evernote-checked' width='24' height='24' style='min-width:24px' viewBox='0 0 24 24' data-evernote-id='192'%3e%3cpath d='M13.293 7.293a.999.999 0 0 0 0 1.414L15.586 11H8a1 1 0 0 0 0 2h7.586l-2.293 2.293a.999.999 0 1 0 1.414 1.414L19.414 12l-4.707-4.707a.999.999 0 0 0-1.414 0z' fill='currentColor' data-evernote-id='193' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://thinc.ai/docs/usage-type-checking)

	from thinc.api import PyTorchWrapper, TensorFlowWrapper

	pt_model = PyTorchWrapper(create_pytorch_model())
	tf_model = TensorFlowWrapper(create_tensorflow_model())
	# You can even stitch together strange hybrids
	# (not efficient, but possible)
	frankenmodel = chain(add(pt_model, tf_model), Linear(128), logistic())

##### Wrap PyTorch, TensorFlow & MXNet models for use in your network

[Read more ![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='_593c1d19 _21270d89 js-evernote-checked' width='24' height='24' style='min-width:24px' viewBox='0 0 24 24' data-evernote-id='231'%3e%3cpath d='M13.293 7.293a.999.999 0 0 0 0 1.414L15.586 11H8a1 1 0 0 0 0 2h7.586l-2.293 2.293a.999.999 0 1 0 1.414 1.414L19.414 12l-4.707-4.707a.999.999 0 0 0-1.414 0z' fill='currentColor' data-evernote-id='232' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://thinc.ai/docs/usage-frameworks)

	def CaptionRater(
	    text_encoder: Model[List[str], Floats2d],
	    image_encoder: Model[List[Path], Floats2d]
	) -> Model[Tuple[List[str], List[Path]], Floats2d]:
	    return chain(
	        concatenate(
	          chain(get_item(0), text_encoder),
	          chain(get_item(1), image_encoder)
	        ),
	        residual(ReLu(nO=300, dropout=0.2, normalize=True)),
	        Softmax(2)
	    )

##### Concise functional-programming approach to model definition

using composition rather than inheritance

[Read more ![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='_593c1d19 _21270d89 js-evernote-checked' width='24' height='24' style='min-width:24px' viewBox='0 0 24 24' data-evernote-id='309'%3e%3cpath d='M13.293 7.293a.999.999 0 0 0 0 1.414L15.586 11H8a1 1 0 0 0 0 2h7.586l-2.293 2.293a.999.999 0 1 0 1.414 1.414L19.414 12l-4.707-4.707a.999.999 0 0 0-1.414 0z' fill='currentColor' data-evernote-id='310' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://thinc.ai/docs/usage-models)

	apply_on = lambda layer, i: chain(getitem(i), layer)
	with Model.define_operators({"^": apply_on, ">>": chain, "|": concatenate}):
	    model = (
	        (text_encoder ^ 0 | image_encoder ^ 1)
	        >> residual(ReLu(nO=300, dropout=0.2, normalize=True)
	        >> Softmax(2)
	    )

##### Optional custom infix notation via operator overloading

[Read more ![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='_593c1d19 _21270d89 js-evernote-checked' width='24' height='24' style='min-width:24px' viewBox='0 0 24 24' data-evernote-id='369'%3e%3cpath d='M13.293 7.293a.999.999 0 0 0 0 1.414L15.586 11H8a1 1 0 0 0 0 2h7.586l-2.293 2.293a.999.999 0 1 0 1.414 1.414L19.414 12l-4.707-4.707a.999.999 0 0 0-1.414 0z' fill='currentColor' data-evernote-id='370' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://thinc.ai/docs/usage-models#operators)

	[optimizer]
	@optimizers = "Adam.v1"

	[optimizer.learn_rate]
	@schedules = "slanted_triangular.v1"
	max_rate = 0.1
	num_steps = 5000

##### Integrated config system

to describe trees of objects and hyperparameters

[Read more ![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='_593c1d19 _21270d89 js-evernote-checked' width='24' height='24' style='min-width:24px' viewBox='0 0 24 24' data-evernote-id='394'%3e%3cpath d='M13.293 7.293a.999.999 0 0 0 0 1.414L15.586 11H8a1 1 0 0 0 0 2h7.586l-2.293 2.293a.999.999 0 1 0 1.414 1.414L19.414 12l-4.707-4.707a.999.999 0 0 0-1.414 0z' fill='currentColor' data-evernote-id='395' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://thinc.ai/docs/usage-config)

	from thinc.api import JaxOps, set_current_ops

	def CustomOps(JaxOps):
	    def some_custom_op_my_layers_needs(...):
	        ...
	set_current_ops(CustomOps())

##### Choice of extensible backends

including [JAX](https://github.com/google/jax) support (experimental)

[Read more ![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='_593c1d19 _21270d89 js-evernote-checked' width='24' height='24' style='min-width:24px' viewBox='0 0 24 24' data-evernote-id='430'%3e%3cpath d='M13.293 7.293a.999.999 0 0 0 0 1.414L15.586 11H8a1 1 0 0 0 0 2h7.586l-2.293 2.293a.999.999 0 1 0 1.414 1.414L19.414 12l-4.707-4.707a.999.999 0 0 0-1.414 0z' fill='currentColor' data-evernote-id='431' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://thinc.ai/docs/api-backends)

	encode_sentence = chain(
	    list2ragged(),  # concatenate sequences
	    with_array(  # ignore outer sequence structure (temporarily)
	        concatenate(Embed(128, column=0), Embed(128, column=1)),
	        Mish(128, dropout=0.2, normalize=True)
	    ),
	    ParametricAttention(128),
	    reduce_mean()
	)

##### First-class support for variable-length sequences

multiple built-in sequence representations, and your layers can use any object

[Read more ![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='_593c1d19 _21270d89 js-evernote-checked' width='24' height='24' style='min-width:24px' viewBox='0 0 24 24' data-evernote-id='483'%3e%3cpath d='M13.293 7.293a.999.999 0 0 0 0 1.414L15.586 11H8a1 1 0 0 0 0 2h7.586l-2.293 2.293a.999.999 0 1 0 1.414 1.414L19.414 12l-4.707-4.707a.999.999 0 0 0-1.414 0z' fill='currentColor' data-evernote-id='484' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://thinc.ai/docs/usage-sequences)

	for i in range(10):
	    for X, Y in train_batches:
	        Yh, backprop = model.begin_update(X)
	        loss, dYh = get_loss(Yh, Y)
	        backprop(dYh)
	        model.finish_update(optimizer)

##### Low abstraction training loop

[Read more ![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='_593c1d19 _21270d89 js-evernote-checked' width='24' height='24' style='min-width:24px' viewBox='0 0 24 24' data-evernote-id='519'%3e%3cpath d='M13.293 7.293a.999.999 0 0 0 0 1.414L15.586 11H8a1 1 0 0 0 0 2h7.586l-2.293 2.293a.999.999 0 1 0 1.414 1.414L19.414 12l-4.707-4.707a.999.999 0 0 0-1.414 0z' fill='currentColor' data-evernote-id='520' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://thinc.ai/docs/usage-training)

* * *

## [#Examples & Tutorials](https://thinc.ai/docs#tutorials)

[View more ![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='_593c1d19 js-evernote-checked' width='16' height='16' style='min-width:16px' viewBox='0 0 24 24' data-evernote-id='528'%3e%3cpath d='M13.293 7.293a.999.999 0 0 0 0 1.414L15.586 11H8a1 1 0 0 0 0 2h7.586l-2.293 2.293a.999.999 0 1 0 1.414 1.414L19.414 12l-4.707-4.707a.999.999 0 0 0-1.414 0z' fill='currentColor' data-evernote-id='529' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/explosion/thinc/blob/master/examples/)

- ![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='_593c1d19 js-evernote-checked' width='14' height='14' style='min-width:14px' viewBox='0 0 24 24' fill='none' stroke='currentColor' stroke-width='2' stroke-linecap='round' stroke-linejoin='round' data-evernote-id='533'%3e%3cpath d='M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z' fill='none' data-evernote-id='534' class='js-evernote-checked'%3e%3c/path%3e%3cpolyline points='14 2 14 8 20 8' fill='none' data-evernote-id='535' class='js-evernote-checked'%3e%3c/polyline%3e%3cline x1='16' y1='13' x2='8' y2='13' data-evernote-id='536' class='js-evernote-checked'%3e%3c/line%3e%3cline x1='16' y1='17' x2='8' y2='17' data-evernote-id='537' class='js-evernote-checked'%3e%3c/line%3e%3cpolyline points='10 9 9 9 8 9' fill='none' data-evernote-id='538' class='js-evernote-checked'%3e%3c/polyline%3e%3c/svg%3e)  [**Intro to Thinc**](https://github.com/explosion/thinc/blob/master/examples/00_intro_to_thinc.ipynb) · Everything you need to know to get started. Composing and training a model on the MNIST data, using config files, registering custom functions and wrapping PyTorch, TensorFlow and MXNet models.

[![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='117' height='20' viewBox='0 0 117 20' data-evernote-id='543' class='js-evernote-checked'%3e%3cpath fill='%23555' d='M0 0h30v20H0z' data-evernote-id='544' class='js-evernote-checked'%3e%3c/path%3e%3cpath fill='%236955a1' d='M30 0h87v20H30z' data-evernote-id='545' class='js-evernote-checked'%3e%3c/path%3e%3cg fill='%23fff' text-anchor='middle' font-family='DejaVu Sans%2cVerdana%2cGeneva%2csans-serif' font-size='110' data-evernote-id='546' class='js-evernote-checked'%3e%3csvg x='4px' y='0px' width='22px' height='20px' viewBox='-2 0 28 24' style='background-color:%23fff%3bborder-radius:1px' data-evernote-id='547' class='js-evernote-checked'%3e%3cpath style='fill:%23ef9008' d='M1.977%2c16.77c-2.667-2.277-2.605-7.079%2c0-9.357C2.919%2c8.057%2c3.522%2c9.075%2c4.49%2c9.691c-1.152%2c1.6-1.146%2c3.201-0.004%2c4.803C3.522%2c15.111%2c2.918%2c16.126%2c1.977%2c16.77z' data-evernote-id='548' class='js-evernote-checked'%3e%3c/path%3e%3cpath style='fill:%23fdba18' d='M12.257%2c17.114c-1.767-1.633-2.485-3.658-2.118-6.02c0.451-2.91%2c2.139-4.893%2c4.946-5.678c2.565-0.718%2c4.964-0.217%2c6.878%2c1.819c-0.884%2c0.743-1.707%2c1.547-2.434%2c2.446C18.488%2c8.827%2c17.319%2c8.435%2c16%2c8.856c-2.404%2c0.767-3.046%2c3.241-1.494%2c5.644c-0.241%2c0.275-0.493%2c0.541-0.721%2c0.826C13.295%2c15.939%2c12.511%2c16.3%2c12.257%2c17.114z' data-evernote-id='549' class='js-evernote-checked'%3e%3c/path%3e%3cpath style='fill:%23ef9008' d='M19.529%2c9.682c0.727-0.899%2c1.55-1.703%2c2.434-2.446c2.703%2c2.783%2c2.701%2c7.031-0.005%2c9.764c-2.648%2c2.674-6.936%2c2.725-9.701%2c0.115c0.254-0.814%2c1.038-1.175%2c1.528-1.788c0.228-0.285%2c0.48-0.552%2c0.721-0.826c1.053%2c0.916%2c2.254%2c1.268%2c3.6%2c0.83C20.502%2c14.551%2c21.151%2c11.927%2c19.529%2c9.682z' data-evernote-id='550' class='js-evernote-checked'%3e%3c/path%3e%3cpath style='fill:%23fdba18' d='M4.49%2c9.691C3.522%2c9.075%2c2.919%2c8.057%2c1.977%2c7.413c2.209-2.398%2c5.721-2.942%2c8.476-1.355c0.555%2c0.32%2c0.719%2c0.606%2c0.285%2c1.128c-0.157%2c0.188-0.258%2c0.422-0.391%2c0.631c-0.299%2c0.47-0.509%2c1.067-0.929%2c1.371C8.933%2c9.539%2c8.523%2c8.847%2c8.021%2c8.746C6.673%2c8.475%2c5.509%2c8.787%2c4.49%2c9.691z' data-evernote-id='551' class='js-evernote-checked'%3e%3c/path%3e%3cpath style='fill:%23fdba18' d='M1.977%2c16.77c0.941-0.644%2c1.545-1.659%2c2.509-2.277c1.373%2c1.152%2c2.85%2c1.433%2c4.45%2c0.499c0.332-0.194%2c0.503-0.088%2c0.673%2c0.19c0.386%2c0.635%2c0.753%2c1.285%2c1.181%2c1.89c0.34%2c0.48%2c0.222%2c0.715-0.253%2c1.006C7.84%2c19.73%2c4.205%2c19.188%2c1.977%2c16.77z' data-evernote-id='552' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e%3ctext x='245' y='140' transform='scale(.1)' textLength='30' data-evernote-id='553' class='js-evernote-checked'%3e%3c/text%3e%3ctext x='725' y='140' transform='scale(.1)' textLength='770' data-evernote-id='554' class='js-evernote-checked'%3eOpen in Colab%3c/text%3e%3c/g%3e%3c/svg%3e)](https://colab.research.google.com/github/explosion/thinc/blob/master/examples/00_intro_to_thinc.ipynb)

- ![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='_593c1d19 js-evernote-checked' width='14' height='14' style='min-width:14px' viewBox='0 0 24 24' fill='none' stroke='currentColor' stroke-width='2' stroke-linecap='round' stroke-linejoin='round' data-evernote-id='557'%3e%3cpath d='M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z' fill='none' data-evernote-id='558' class='js-evernote-checked'%3e%3c/path%3e%3cpolyline points='14 2 14 8 20 8' fill='none' data-evernote-id='559' class='js-evernote-checked'%3e%3c/polyline%3e%3cline x1='16' y1='13' x2='8' y2='13' data-evernote-id='560' class='js-evernote-checked'%3e%3c/line%3e%3cline x1='16' y1='17' x2='8' y2='17' data-evernote-id='561' class='js-evernote-checked'%3e%3c/line%3e%3cpolyline points='10 9 9 9 8 9' fill='none' data-evernote-id='562' class='js-evernote-checked'%3e%3c/polyline%3e%3c/svg%3e)  [**Training a part-of-speech tagger with transformers (BERT)**](https://github.com/explosion/thinc/blob/master/examples/02_transformers_tagger_bert.ipynb) · How to use Thinc, Transformers and PyTorch to train a part-of-speech tagger. From model definition and config to the training loop.

[![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='117' height='20' viewBox='0 0 117 20' data-evernote-id='567' class='js-evernote-checked'%3e%3cpath fill='%23555' d='M0 0h30v20H0z' data-evernote-id='568' class='js-evernote-checked'%3e%3c/path%3e%3cpath fill='%236955a1' d='M30 0h87v20H30z' data-evernote-id='569' class='js-evernote-checked'%3e%3c/path%3e%3cg fill='%23fff' text-anchor='middle' font-family='DejaVu Sans%2cVerdana%2cGeneva%2csans-serif' font-size='110' data-evernote-id='570' class='js-evernote-checked'%3e%3csvg x='4px' y='0px' width='22px' height='20px' viewBox='-2 0 28 24' style='background-color:%23fff%3bborder-radius:1px' data-evernote-id='571' class='js-evernote-checked'%3e%3cpath style='fill:%23ef9008' d='M1.977%2c16.77c-2.667-2.277-2.605-7.079%2c0-9.357C2.919%2c8.057%2c3.522%2c9.075%2c4.49%2c9.691c-1.152%2c1.6-1.146%2c3.201-0.004%2c4.803C3.522%2c15.111%2c2.918%2c16.126%2c1.977%2c16.77z' data-evernote-id='572' class='js-evernote-checked'%3e%3c/path%3e%3cpath style='fill:%23fdba18' d='M12.257%2c17.114c-1.767-1.633-2.485-3.658-2.118-6.02c0.451-2.91%2c2.139-4.893%2c4.946-5.678c2.565-0.718%2c4.964-0.217%2c6.878%2c1.819c-0.884%2c0.743-1.707%2c1.547-2.434%2c2.446C18.488%2c8.827%2c17.319%2c8.435%2c16%2c8.856c-2.404%2c0.767-3.046%2c3.241-1.494%2c5.644c-0.241%2c0.275-0.493%2c0.541-0.721%2c0.826C13.295%2c15.939%2c12.511%2c16.3%2c12.257%2c17.114z' data-evernote-id='573' class='js-evernote-checked'%3e%3c/path%3e%3cpath style='fill:%23ef9008' d='M19.529%2c9.682c0.727-0.899%2c1.55-1.703%2c2.434-2.446c2.703%2c2.783%2c2.701%2c7.031-0.005%2c9.764c-2.648%2c2.674-6.936%2c2.725-9.701%2c0.115c0.254-0.814%2c1.038-1.175%2c1.528-1.788c0.228-0.285%2c0.48-0.552%2c0.721-0.826c1.053%2c0.916%2c2.254%2c1.268%2c3.6%2c0.83C20.502%2c14.551%2c21.151%2c11.927%2c19.529%2c9.682z' data-evernote-id='574' class='js-evernote-checked'%3e%3c/path%3e%3cpath style='fill:%23fdba18' d='M4.49%2c9.691C3.522%2c9.075%2c2.919%2c8.057%2c1.977%2c7.413c2.209-2.398%2c5.721-2.942%2c8.476-1.355c0.555%2c0.32%2c0.719%2c0.606%2c0.285%2c1.128c-0.157%2c0.188-0.258%2c0.422-0.391%2c0.631c-0.299%2c0.47-0.509%2c1.067-0.929%2c1.371C8.933%2c9.539%2c8.523%2c8.847%2c8.021%2c8.746C6.673%2c8.475%2c5.509%2c8.787%2c4.49%2c9.691z' data-evernote-id='575' class='js-evernote-checked'%3e%3c/path%3e%3cpath style='fill:%23fdba18' d='M1.977%2c16.77c0.941-0.644%2c1.545-1.659%2c2.509-2.277c1.373%2c1.152%2c2.85%2c1.433%2c4.45%2c0.499c0.332-0.194%2c0.503-0.088%2c0.673%2c0.19c0.386%2c0.635%2c0.753%2c1.285%2c1.181%2c1.89c0.34%2c0.48%2c0.222%2c0.715-0.253%2c1.006C7.84%2c19.73%2c4.205%2c19.188%2c1.977%2c16.77z' data-evernote-id='576' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e%3ctext x='245' y='140' transform='scale(.1)' textLength='30' data-evernote-id='577' class='js-evernote-checked'%3e%3c/text%3e%3ctext x='725' y='140' transform='scale(.1)' textLength='770' data-evernote-id='578' class='js-evernote-checked'%3eOpen in Colab%3c/text%3e%3c/g%3e%3c/svg%3e)](https://colab.research.google.com/github/explosion/thinc/blob/master/examples/02_transformers_tagger_bert.ipynb)

- ![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='_593c1d19 js-evernote-checked' width='14' height='14' style='min-width:14px' viewBox='0 0 24 24' fill='none' stroke='currentColor' stroke-width='2' stroke-linecap='round' stroke-linejoin='round' data-evernote-id='581'%3e%3cpath d='M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z' fill='none' data-evernote-id='582' class='js-evernote-checked'%3e%3c/path%3e%3cpolyline points='14 2 14 8 20 8' fill='none' data-evernote-id='583' class='js-evernote-checked'%3e%3c/polyline%3e%3cline x1='16' y1='13' x2='8' y2='13' data-evernote-id='584' class='js-evernote-checked'%3e%3c/line%3e%3cline x1='16' y1='17' x2='8' y2='17' data-evernote-id='585' class='js-evernote-checked'%3e%3c/line%3e%3cpolyline points='10 9 9 9 8 9' fill='none' data-evernote-id='586' class='js-evernote-checked'%3e%3c/polyline%3e%3c/svg%3e)  [**Parallel training with Ray**](https://github.com/explosion/thinc/blob/master/examples/04_parallel_training_ray.ipynb) · How to set up synchronous and asynchronous parameter server training with Thinc and Ray.

[![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='117' height='20' viewBox='0 0 117 20' data-evernote-id='591' class='js-evernote-checked'%3e%3cpath fill='%23555' d='M0 0h30v20H0z' data-evernote-id='592' class='js-evernote-checked'%3e%3c/path%3e%3cpath fill='%236955a1' d='M30 0h87v20H30z' data-evernote-id='593' class='js-evernote-checked'%3e%3c/path%3e%3cg fill='%23fff' text-anchor='middle' font-family='DejaVu Sans%2cVerdana%2cGeneva%2csans-serif' font-size='110' data-evernote-id='594' class='js-evernote-checked'%3e%3csvg x='4px' y='0px' width='22px' height='20px' viewBox='-2 0 28 24' style='background-color:%23fff%3bborder-radius:1px' data-evernote-id='595' class='js-evernote-checked'%3e%3cpath style='fill:%23ef9008' d='M1.977%2c16.77c-2.667-2.277-2.605-7.079%2c0-9.357C2.919%2c8.057%2c3.522%2c9.075%2c4.49%2c9.691c-1.152%2c1.6-1.146%2c3.201-0.004%2c4.803C3.522%2c15.111%2c2.918%2c16.126%2c1.977%2c16.77z' data-evernote-id='596' class='js-evernote-checked'%3e%3c/path%3e%3cpath style='fill:%23fdba18' d='M12.257%2c17.114c-1.767-1.633-2.485-3.658-2.118-6.02c0.451-2.91%2c2.139-4.893%2c4.946-5.678c2.565-0.718%2c4.964-0.217%2c6.878%2c1.819c-0.884%2c0.743-1.707%2c1.547-2.434%2c2.446C18.488%2c8.827%2c17.319%2c8.435%2c16%2c8.856c-2.404%2c0.767-3.046%2c3.241-1.494%2c5.644c-0.241%2c0.275-0.493%2c0.541-0.721%2c0.826C13.295%2c15.939%2c12.511%2c16.3%2c12.257%2c17.114z' data-evernote-id='597' class='js-evernote-checked'%3e%3c/path%3e%3cpath style='fill:%23ef9008' d='M19.529%2c9.682c0.727-0.899%2c1.55-1.703%2c2.434-2.446c2.703%2c2.783%2c2.701%2c7.031-0.005%2c9.764c-2.648%2c2.674-6.936%2c2.725-9.701%2c0.115c0.254-0.814%2c1.038-1.175%2c1.528-1.788c0.228-0.285%2c0.48-0.552%2c0.721-0.826c1.053%2c0.916%2c2.254%2c1.268%2c3.6%2c0.83C20.502%2c14.551%2c21.151%2c11.927%2c19.529%2c9.682z' data-evernote-id='598' class='js-evernote-checked'%3e%3c/path%3e%3cpath style='fill:%23fdba18' d='M4.49%2c9.691C3.522%2c9.075%2c2.919%2c8.057%2c1.977%2c7.413c2.209-2.398%2c5.721-2.942%2c8.476-1.355c0.555%2c0.32%2c0.719%2c0.606%2c0.285%2c1.128c-0.157%2c0.188-0.258%2c0.422-0.391%2c0.631c-0.299%2c0.47-0.509%2c1.067-0.929%2c1.371C8.933%2c9.539%2c8.523%2c8.847%2c8.021%2c8.746C6.673%2c8.475%2c5.509%2c8.787%2c4.49%2c9.691z' data-evernote-id='599' class='js-evernote-checked'%3e%3c/path%3e%3cpath style='fill:%23fdba18' d='M1.977%2c16.77c0.941-0.644%2c1.545-1.659%2c2.509-2.277c1.373%2c1.152%2c2.85%2c1.433%2c4.45%2c0.499c0.332-0.194%2c0.503-0.088%2c0.673%2c0.19c0.386%2c0.635%2c0.753%2c1.285%2c1.181%2c1.89c0.34%2c0.48%2c0.222%2c0.715-0.253%2c1.006C7.84%2c19.73%2c4.205%2c19.188%2c1.977%2c16.77z' data-evernote-id='600' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e%3ctext x='245' y='140' transform='scale(.1)' textLength='30' data-evernote-id='601' class='js-evernote-checked'%3e%3c/text%3e%3ctext x='725' y='140' transform='scale(.1)' textLength='770' data-evernote-id='602' class='js-evernote-checked'%3eOpen in Colab%3c/text%3e%3c/g%3e%3c/svg%3e)](https://colab.research.google.com/github/explosion/thinc/blob/master/examples/04_parallel_training_ray.ipynb)

[Next: Concept and Design ![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='_593c1d19 _21270d89 js-evernote-checked' width='24' height='24' style='min-width:24px' viewBox='0 0 24 24' data-evernote-id='606'%3e%3cpath d='M13.293 7.293a.999.999 0 0 0 0 1.414L15.586 11H8a1 1 0 0 0 0 2h7.586l-2.293 2.293a.999.999 0 1 0 1.414 1.414L19.414 12l-4.707-4.707a.999.999 0 0 0-1.414 0z' fill='currentColor' data-evernote-id='607' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://thinc.ai/docs/concept)