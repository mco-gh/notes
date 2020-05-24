Introducing TensorFlow Graphics: Computer Graphics Meets Deep Learning

# *Introducing TensorFlow Graphics: Computer Graphics Meets Deep Learning*

[![1*iDQvKoz7gGHc6YXqvqWWZQ.png](../_resources/e4a835d142355cf63550c631beeb96cc.png) ![](data:image/svg+xml,%3csvg viewBox='0 0 70 70' xmlns='http://www.w3.org/2000/svg' class='js-evernote-checked' data-evernote-id='123'%3e%3cpath d='M5.53538374%2c19.9430227 C11.180401%2c8.78497536 22.6271155%2c1.6 35.3571429%2c1.6 C48.0871702%2c1.6 59.5338847%2c8.78497536 65.178902%2c19.9430227 L66.2496695%2c19.401306 C60.4023065%2c7.84329843 48.5440457%2c0.4 35.3571429%2c0.4 C22.17024%2c0.4 10.3119792%2c7.84329843 4.46461626%2c19.401306 L5.53538374%2c19.9430227 Z'%3e%3c/path%3e%3cpath d='M65.178902%2c49.9077131 C59.5338847%2c61.0657604 48.0871702%2c68.2507358 35.3571429%2c68.2507358 C22.6271155%2c68.2507358 11.180401%2c61.0657604 5.53538374%2c49.9077131 L4.46461626%2c50.4494298 C10.3119792%2c62.0074373 22.17024%2c69.4507358 35.3571429%2c69.4507358 C48.5440457%2c69.4507358 60.4023065%2c62.0074373 66.2496695%2c50.4494298 L65.178902%2c49.9077131 Z'%3e%3c/path%3e%3c/svg%3e)](https://medium.com/@tensorflow?source=post_header_lockup)

[TensorFlow](https://medium.com/@tensorflow)
May 9·5 min read

*Posted by *[*Julien Valentin*](https://twitter.com/JPCValentin)* and *[*Sofien Bouaziz*](https://twitter.com/_sofien_)

![](../_resources/7a5854aeabf093b6067299f4ff9503cf.png)![1*gS7OPab2UBrXbFnsbr694Q.jpeg](../_resources/a84a7528db35bef234a39e1755f55a9d.jpg)

Github repository: [https://github.com/tensorflow/graphics](https://www.google.com/url?q=https://github.com/tensorflow/graphics&sa=D&source=hangouts&ust=1557515531193000&usg=AFQjCNHGtImz3u-RbH6QznsYM5q2EreHfQ)

The last few years have seen a rise in novel differentiable graphics layers which can be inserted in neural network architectures. From spatial transformers to differentiable graphics renderers, these new layers leverage the knowledge acquired over years of computer vision and graphics research to build new and more efficient network architectures. Explicitly modeling geometric priors and constraints into neural networks opens up the door to architectures that can be trained robustly, efficiently, and more importantly, in a self-supervised fashion.

At a high level, a computer graphics pipeline requires 3D objects and their absolute positioning in the scene, a description of the material they are made of, lights and a camera. This scene description is then interpreted by a renderer to generate a synthetic rendering.

![](../_resources/7ed62de059f32779a080f84ae3a37028.png)![0*cc_31-Ko0Pe6Rw76](../_resources/8cee172982e2e4b1c04d12847a28a096.jpg)

In comparison, a computer vision system would start from an image and try to infer the parameters of the scene. This allows the prediction of which objects are in the scene, what materials they are made of, and their three dimensional position and orientation.

![](../_resources/aaf678b47a9f28b139658078592e9381.png)![0*GQqnYSPWJRUxA4Nl](../_resources/1a5130bda3c1e646bcb7e9c7488b412c.jpg)

Training machine learning systems capable of solving these complex 3D vision tasks most often requires large quantities of data. As labelling data is a costly and complex process, it is important to have mechanisms to design machine learning models that can comprehend the three dimensional world while being trained without much supervision. Combining computer vision and computer graphics techniques provides a unique opportunity to leverage the vast amounts of readily available unlabelled data. As illustrated in the image below, this can, for instance, be achieved using analysis by synthesis where the vision system extracts the scene parameters and the graphics system renders back an image based on them. If the rendering matches the original image, the vision system has accurately extracted the scene parameters. In this setup, computer vision and computer graphics go hand-in-hand, forming a single machine learning system similar to an autoencoder, which can be trained in a self-supervised manner.

![](../_resources/b305cb7e2914d198a9154151e5aa9ee9.png)![0*75G2Q6wIygbNmsR5](../_resources/1e9884e965e1f2fa7838e23bf8949e73.jpg)

### Differentiable Graphics Layers

In the following, we will explore some of the functionalities available in TensorFlow Graphics. This tour is not exhaustive; for more information visit our [Github](https://github.com/tensorflow/graphics/) to discover the new possibilities made available by TensorFlow Graphics.

**Transformations**

Object transformations control the position of objects in space. In the illustration below, the axis-angle formalism is used to rotate a cube. The rotation axis is pointing up and the angle is positive, leading the cube to rotate counterclockwise. In this [Colab example](https://colab.sandbox.google.com/github/tensorflow/graphics/blob/master/tensorflow_graphics/notebooks/6dof_alignment.ipynb), we show how rotation formalisms can be trained in a neural network that is trained to both predict the rotation and translation of an observed object. This task is at the core of many applications, including robots that focus on interacting with their environment. In these scenarios, grasping objects (e.g. by their handle) with a robotic arm requires a precise estimation of the position of these objects with respect to the arm.

![](../_resources/1118a9b6ad8cb93fa628fe7d205c9e7d.png)![1*lyCJriyEIb9hHKVQcP8P0A.gif](../_resources/387334f39f60f811dd7fbf9c28d492e5.gif)

**Modelling cameras**

Camera models play a fundamental role in computer vision as they greatly influence the appearance of three dimensional objects projected onto the image plane. As can be observed below, the cube appears to be scaling up and down, while in reality the changes are only due to changes in focal length. Try this [Colab example](https://colab.sandbox.google.com/github/tensorflow/graphics/blob/master/tensorflow_graphics/notebooks/intrinsics_optimization.ipynb) for more details about camera models and a concrete example of how to use them in TensorFlow.

![](../_resources/36949cd09772ba7c085d2979e0be9be3.png)![1*klR2j5WgymcXhovj-mPjeg.gif](../_resources/5fe844a5489a6997247b034684ea6cef.gif)

**Materials**

Material models define how light interacts with objects to give them their unique appearance. For instance, some materials like plaster reflect light uniformly in all directions, where others like mirrors are purely specular. In this interactive [Colab notebook](https://colab.sandbox.google.com/github/tensorflow/graphics/blob/master/tensorflow_graphics/notebooks/reflectance.ipynb), you will learn how to generate the following renderings using Tensorflow Graphics. You will also have the opportunity to play with the parameters of the material and the light to develop a good sense of how they interact. Accurately predicting material properties is fundamental to many tasks. For instance, it can allow users to drop virtual furniture in their environment and have the pieces photo-realistically blend with their interior, giving users an accurate perception of how that piece of furniture would look.

![](../_resources/79197c875404d96efacfc5242ab13b0c.png)![0*vvIjTfEy9oh1Q6IG](../_resources/d1129042cc4800920261b7747b9d2dba.jpg)

**Geometry — 3D convolutions and pooling**

In recent years, sensors outputting three dimensional data in the form of point clouds or meshes are becoming part of our everyday life, from smartphone depth sensors to self driving car lidars. Due to their irregular structure, convolutions on these representations are significantly harder to implement compared to images which offer a regular grid structure. TensorFlow Graphics comes with two 3D convolution layers, and one 3D pooling layer, allowing for instance the training of networks to perform semantic part classification on meshes as illustrated below and demonstrated in this [Colab notebook](https://colab.sandbox.google.com/github/tensorflow/graphics/blob/master/tensorflow_graphics/notebooks/mesh_segmentation_demo.ipynb).

![](../_resources/95dab81ffc83dc92a0af7bf3e75feb85.png)![0*XnV_1p5S3MxQ0Yvr](../_resources/7949e56c6d3428418e7b3f710ac9cd15.png)

### TensorBoard 3d

Visual debugging is a great way to assess whether an experiment is going in the right direction. To this end, TensorFlow Graphics comes with a TensorBoard plugin to interactively visualize 3d meshes and point clouds.

![](../_resources/e459848c0d735d77310ef2c8c2211205.png)![0*y7sUnS_yx9B34HFr](../_resources/f00a0853fe8ef7bab6dc538b7f216528.gif)

### Get started

The first release of TensorFlow Graphics supports is compatible with TensorFlow 1.13.1 and above. You will find the API and instructions to install the library by visiting**  **[https://www.tensorflow.org/graphics](https://www.tensorflow.org/graphics/).

### Acknowledgments

Creating TensorFlow Graphics was a team effort. Special thanks to Cem Keskin, [Pavel Pidlypenskyi](https://twitter.com/podlipensky), [Ameesh Makadia](https://twitter.com/kiamada), and [Avneesh Sud](https://twitter.com/AvneeshSud) who all made significant contributions.