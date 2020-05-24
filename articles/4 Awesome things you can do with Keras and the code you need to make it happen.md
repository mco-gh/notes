4 Awesome things you can do with Keras and the code you need to make it happen

# 4 Awesome things you can do with Keras and the code you need to make it happen

[![1*NXT3Mow_MRFaL68T5Cq2HA.png](../_resources/3d635a0654303c985c872e56a7f1aca4.png)](https://towardsdatascience.com/@george.seif94?source=post_page-----858f022eec85----------------------)

[George Seif](https://towardsdatascience.com/@george.seif94?source=post_page-----858f022eec85----------------------)

[Aug 26](https://towardsdatascience.com/4-awesome-things-you-can-do-with-keras-and-the-code-you-need-to-make-it-happen-858f022eec85?source=post_page-----858f022eec85----------------------) · 4 min read![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='star-15px_svg__svgIcon-use js-evernote-checked' width='15' height='15' viewBox='0 0 15 15' style='margin-top:-2px' data-evernote-id='183'%3e%3cpath d='M7.44 2.32c.03-.1.09-.1.12 0l1.2 3.53a.29.29 0 0 0 .26.2h3.88c.11 0 .13.04.04.1L9.8 8.33a.27.27 0 0 0-.1.29l1.2 3.53c.03.1-.01.13-.1.07l-3.14-2.18a.3.3 0 0 0-.32 0L4.2 12.22c-.1.06-.14.03-.1-.07l1.2-3.53a.27.27 0 0 0-.1-.3L2.06 6.16c-.1-.06-.07-.12.03-.12h3.89a.29.29 0 0 0 .26-.19l1.2-3.52z' data-evernote-id='184' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)

![1*VN6bGHQnYkd-l2eJlDA_yA.jpeg](../_resources/396538820af98460777f417d300d5d6e.jpg)
![1*VN6bGHQnYkd-l2eJlDA_yA.jpeg](../_resources/465514364235bc127eec50d65b6867cc.jpg)

Keras is one of the most widely used Deep Learning frameworks out there. It’s very easy to use and yet is still on par in terms of performance with the more complex libraries like TensorFlow, Caffe, and MXNet. Unless you’re in an application that requires some very low-level and complex code, Keras will give you the best bang for your buck!

But there’s more to Keras than meets the eye. Today we’re sharing a few lesser known yet awesome things you can do with Keras along with the code you need to make it happen. These will help you code all of your custom things directly in Keras without having to switch to those other more tedious and complex libraries.

# (1) Custom Metrics and Loss Functions

Keras comes with a number of built in metrics and loss functions which are super useful for many cases. Somewhat unfortunately though, only the most common metrics and losses are built in.

All of the metrics are basically some form of percentage accuracy; the losses do have many options but not much from the very latest state-of-the-art research. If you want something cutting edge you’ll need to implement your own.

Here’s how we can do that! All Keras losses and metrics are defined in the same way as functions with two input variables: the ground truth and the predicted value; the functions always return the value for the metric or loss. The only thing you really have to take care of is that any operations on your matrices should be compatible with *Keras or TensorFlow Tensors*, since that’s the format Keras will always expect from these custom functions. This can be accomplished by sticking to using Python math, Keras, or TensorFlow operations.

Seems easy enough! Below is an example of how to create and apply a custom loss and custom metric.

For the metric, I implemented the [PSNR](https://www.mathworks.com/help/vision/ref/psnr.html) function which is commonly used to measure image quality. For the loss function I implemented the [Charbonnier](https://arxiv.org/pdf/1701.03077.pdf) which has been shown to be more robust to outliers than L1 or L2 loss. Once the functions are written, we simply pass them to our model compilation function!

|     |     |
| --- | --- |
| 1   | import math |
| 2   | from keras import backend as K |
| 3   |     |
| 4   | # Define our custom metric |
| 5   | def  PSNR(y_true, y_pred): |
| 6   | max_pixel =  1.0 |
| 7   |  return  10.0  * math.log10((max_pixel **  2) / (K.mean(K.square(y_pred - y_true)))) |
| 8   |     |
| 9   | # Define our custom loss function |
| 10  | def  charbonnier(y_true, y_pred): |
| 11  | epsilon =  1e-3 |
| 12  | error = y_true - y_pred |
| 13  | p = K.sqrt(K.square(error) + K.square(epsilon)) |
| 14  |  return K.mean(p) |
| 15  |     |
| 16  | # Compile our model |
| 17  | adam = Adam(lr=0.0001) |
| 18  | model.compile(loss=[charbonnier], metrics=[PSNR], optimizer=adam) |

 [view raw](https://gist.github.com/GeorgeSeif/03ee25ee927f6524fbb74904d6eeb3e4/raw/4ab30c6eae88445a8a899c69b8aeef088b760248/custom_metrics.py)  [custom_metrics.py](https://gist.github.com/GeorgeSeif/03ee25ee927f6524fbb74904d6eeb3e4#file-custom_metrics-py) hosted with ❤ by [GitHub](https://github.com/)

# (2) Custom Layers

Similar to metrics and loss functions you might find yourself needing to create a custom layer if you want to use something outside of the standard convolutions, pooling, and activation functions. In such a situation you can follow the code example I’ve given below to implement it!

From the Keras documentation the two most important we’ll need to implement are:

- `call(x)`: this is where the layer's logic lives. Unless you want your layer to support masking, you only have to care about the first argument passed to `call`: the input tensor.
- `get_output_shape_for(input_shape)`: in case your layer modifies the shape of its input, you should specify here the shape transformation logic. This allows Keras to do automatic shape inference.

|     |     |
| --- | --- |
| 1   | import tensorflow as tf |
| 2   |     |
| 3   | def  tf_int_round(num): |
| 4   | return tf.cast(tf.round(num), dtype=tf.int32) |
| 5   |     |
| 6   | class  resize_layer(layers.Layer): |
| 7   |  # Initialize variables |
| 8   |  def  __init__(self, scale, **kwargs): |
| 9   |  self.scale = scale |
| 10  |  super(resize_layer, self).__init__(**kwargs) |
| 11  |     |
| 12  |  def  build(self, input_shape): |
| 13  |  super(resize_layer,self).build(input_shape) |
| 14  |     |
| 15  |  # Defining how we will call our function |
| 16  |  def  call(self, x, method="bicubic"): |
| 17  | height = tf_int_round(tf.cast(tf.shape(x)[1],dtype=tf.float32) *  self.scale) |
| 18  | width = tf_int_round(tf.cast(tf.shape(x)[2],dtype=tf.float32) *  self.scale) |
| 19  |     |
| 20  | if method ==  "bilinear": |
| 21  | return tf.image.resize_bilinear(x, size=(height, width)) |
| 22  |  elif method ==  "bicubic": |
| 23  | return tf.image.resize_bicubic(x, size=(height, width)) |
| 24  |  elif method ==  "nearest": |
| 25  | return tf.image.resize_nearest_neighbor(x, size=(height, width)) |
| 26  |     |
| 27  |  # Defining the computation of the output shape |
| 28  |  def  get_output_shape_for(self, input_shape): |
| 29  | height = tf_int_round(tf.cast(tf.shape(x)[1],dtype=tf.float32) *  self.scale) |
| 30  | width = tf_int_round(tf.cast(tf.shape(x)[2],dtype=tf.float32) *  self.scale) |
| 31  |  return (self.input_shape[0], height, width, input_shape[3]) |
| 32  |     |
| 33  | # Using our new custom layer with the Functional API |
| 34  | image_2 = resize_layer(scale=2)(image, method="bilinear") |

 [view raw](https://gist.github.com/GeorgeSeif/d3c0410f7df862ed4d9945dc2f6e7add/raw/21991980cbd503145bcac8e98a716e9d95db8668/custom_layer.py)  [custom_layer.py](https://gist.github.com/GeorgeSeif/d3c0410f7df862ed4d9945dc2f6e7add#file-custom_layer-py) hosted with ❤ by [GitHub](https://github.com/)

In my case I wanted to have a layer that could automatically resize images to any size. For this, I needed to use either blinear, bicubic, or nearest neighbour resizing.

The first input to the `call()`function is defined as `x` which is the image tensor and the second input (optional) is defined as `method` which refers to the type of resizing to be used. The resizing *scale* is defined in the initialisation function `__init__` .

Being sure to stick to TensorFlow operations (so we always use Keras or TensorFlow tensors), we resize and return the image according to our integer-rounded scale. In the `get_output_shape_for()` function, the full shape of the output tensor is calculated and returned

Now that we’ve written the code for our custom layer, assuming that our image tensor is defined as `image`, all we have to do to use it with the Functional API is call it like so:

**image_2 = resize_layer(scale=2)(image, method=”bilinear”)**

# (3) Built-in Pre-Processing

Keras comes with several [built-in models](https://keras.io/applications/) with pre-trained weights on ImageNet that you can use right out of the box. But, if you want to use those models directly, you’ll need to resize your images beforehand due to the fully connected layers at the end forcing the input size to be fixed.

For example, the Xception model was trained with image crops of 299x299, so all of your images will have to be set to the size to avoid errors. Beyond that, there may be some other kind of pre- or post- processing for the model that you want to be automatically applied whenever you pass your image to it.

Look no further!

We can use Keras’s *Lambda Layers* to have any kind of mathematical or pre-processing operation *built-in *to the model! The lambda will simply define which operation you want to apply.

The full layer *Lambda* is what allows you to have that functionality fully baked into your model. Check out the code below to see how we built in re-sizing and Xception pre-processing into the model!

|     |     |
| --- | --- |
| 1   | from keras.applications.nasnet import Xception, preprocess_input |
| 2   | from keras.models import Sequential, Model |
| 3   | from keras.layers.core import Lambda |
| 4   | from keras.backend import tf as ktf |
| 5   |     |
| 6   | # Initialize a Xception model |
| 7   | Xception_model = Xception(include_top=True, weights='imagenet', input_tensor=None, input_shape=None) |
| 8   |     |
| 9   | # Any required pre-processing should be baked into the model |
| 10  | input_tensor = Input(shape=(None, None, 3)) |
| 11  | x = Lambda(lambda  image: ktf.image.resize_images(image, (299, 299)))(input_tensor) |
| 12  | x = Lambda(lambda  image: preprocess_input(image))(x) |
| 13  | output_tensor = Xception_model(x) |
| 14  |     |
| 15  | final_Xception_model = Model(input_tensor, output_tensor) |

 [view raw](https://gist.github.com/GeorgeSeif/8262b86ee7b57dc1207f29f8b4bf4ec2/raw/fe4a755b964f2a1059f6c850d3af8ee8033926e1/preprocessing.py)  [preprocessing.py](https://gist.github.com/GeorgeSeif/8262b86ee7b57dc1207f29f8b4bf4ec2#file-preprocessing-py) hosted with ❤ by [GitHub](https://github.com/)

# (4) Functions for repeating blocks

If we want to code up a big model, say something that’s 50 or even 100 layers deep, code can get very messy. When you have to define that many layers and on top of that all of the residual or dense connections you’ll have code all over the place!

Instead, we can actually do a clever trick in the functional API of defining repeating code blocks as functions. For example, a ResNet has many repeating residual blocks that have the same base components: Batch Normalisation, Activation Function, and Convolution. So we can simply define those operations together as one block in a function, greatly simplifying our code.

Check out the code below which implements both ResNet and DenseNet blocks and shows you how to use them!

|     |     |
| --- | --- |
| 1   | def  preact_conv(inputs, k=3, filters=64): |
| 2   | outputs = BatchNormalization()(inputs) |
| 3   | outputs = Activation('relu')(outputs) |
| 4   | outputs = Conv2D(filters, kernel_size=(k, k), padding='same', |
| 5   |  kernel_initializer="glorot_normal")(outputs) |
| 6   |     |
| 7   |  return outputs |
| 8   |     |
| 9   | def  ResidualBlock(inputs, kernal_size=3, filters=64): |
| 10  | outputs = preact_conv(inputs, k=kernal_size, n_filters=filters) |
| 11  | outputs = preact_conv(outputs, k=kernal_size, n_filters=filters) |
| 12  |     |
| 13  | outputs = add([outputs, inputs]) |
| 14  |  return outputs |
| 15  |     |
| 16  | def  DenseBlock(stack, n_layers, growth_rate): |
| 17  | new_features = [] |
| 18  |  for i in  range(n_layers): |
| 19  | layer = preact_conv(stack, filters=growth_rate) |
| 20  | new_features.append(layer) |
| 21  |  # stack new layer |
| 22  | stack = concatenate([stack, layer], axis=-1) |
| 23  | new_features = concatenate(new_features, axis=-1) |
| 24  |  return new_features |
| 25  |     |
| 26  |     |
| 27  | # Applying a stack of 5 Residual Blocks for a ResNet, just 5 lines of code |
| 28  | # If we wrote this out layer by layer, this would probably take 4-5x the number of lines |
| 29  | x = ResidualBlock(x) |
| 30  | x = ResidualBlock(x) |
| 31  | x = ResidualBlock(x) |
| 32  | x = ResidualBlock(x) |
| 33  | x = ResidualBlock(x) |
| 34  |     |
| 35  | # Applying a stack of 5 Dense Blocks for a DenseNet, just 5 lines of code |
| 36  | # DenseNets are even more complex to implements than ResNets, so if we wrote |
| 37  | # this out layer by layer, this would probably take 5-10x the number of lines |
| 38  | x = DenseBlock(x, n_layers=4, growth_rate=12) |
| 39  | x = DenseBlock(x, n_layers=6, growth_rate=12) |
| 40  | x = DenseBlock(x, n_layers=8, growth_rate=12) |
| 41  | x = DenseBlock(x, n_layers=10, growth_rate=12) |
| 42  | x = DenseBlock(x, n_layers=12, growth_rate=12) |

 [view raw](https://gist.github.com/GeorgeSeif/972206ec73dfe68488f26a92a016e79c/raw/ceaff55c1c2dfc27ec627de80149bbb0b40a8ecf/repeating_blocks.py)  [repeating_blocks.py](https://gist.github.com/GeorgeSeif/972206ec73dfe68488f26a92a016e79c#file-repeating_blocks-py) hosted with ❤ by [GitHub](https://github.com/)