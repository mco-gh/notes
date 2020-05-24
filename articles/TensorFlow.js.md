TensorFlow.js

# Getting Started

There are two main ways to get TensorFlow.js in your JavaScript project: via [script tags](https://developer.mozilla.org/en-US/docs/Learn/HTML/Howto/Use_JavaScript_within_a_webpage)  **or** by installing it from [NPM](https://www.npmjs.com/) and using a build tool like [Parcel](https://parceljs.org/), [WebPack](https://webpack.js.org/), or [Rollup](https://rollupjs.org/guide/en).

### via Script Tag

Add the following code to an HTML file:

 	<html>

	  <head>
	    *<!-- Load TensorFlow.js -->*
	    <script src="https://cdn.jsdelivr.net/npm/@tensorflow/tfjs@0.9.0"> </script>

	    *<!-- Place your code in the script tag below. You can also use an external .js file -->*
	    <script>
	      *// Notice there is no 'import' statement. 'tf' is available on the index-page*
	      *// because of the script tag above.*

	      *// Define a model for linear regression.*
	      const model = tf.sequential();
	      model.add(tf.layers.dense({units: 1, inputShape: [1]}));

	      *// Prepare the model for training: Specify the loss and the optimizer.*
	      model.compile({loss: 'meanSquaredError', optimizer: 'sgd'});

	      *// Generate some synthetic data for training.*
	      const xs = tf.tensor2d([1, 2, 3, 4], [4, 1]);
	      const ys = tf.tensor2d([1, 3, 5, 7], [4, 1]);

	      *// Train the model using the data.*
	      model.fit(xs, ys).then(() => {
	        *// Use the model to do inference on a data point the model hasn't seen before:*
	        *// Open the browser devtools to see the output*
	        model.predict(tf.tensor2d([5], [1, 1])).print();
	      });
	    </script>
	  </head>

	  <body>
	  </body>
	</html>

Open up that html file in your browser and the code should run!

### via NPM

Add TensorFlow.js to your project using yarn **or** npm. **Note:** Because we use ES2017 syntax (such as `import`), this workflow assumes you are using a bundler/transpiler to convert your code to something the browser understands. See our [examples](https://github.com/tensorflow/tfjs-examples) to see how we use [Parcel](https://parceljs.org/) to build our code. However you are free to use any build tool that you prefer.

`yarn add @tensorflow/tfjs`

`npm install @tensorflow/tfjs`

In your main js file:

	  import * as tf from '@tensorflow/tfjs';

	  *// Define a model for linear regression.*
	  const model = tf.sequential();
	  model.add(tf.layers.dense({units: 1, inputShape: [1]}));

	  *// Prepare the model for training: Specify the loss and the optimizer.*
	  model.compile({loss: 'meanSquaredError', optimizer: 'sgd'});

	  *// Generate some synthetic data for training.*
	  const xs = tf.tensor2d([1, 2, 3, 4], [4, 1]);
	  const ys = tf.tensor2d([1, 3, 5, 7], [4, 1]);

	  *// Train the model using the data.*
	  model.fit(xs, ys).then(() => {
	    *// Use the model to do inference on a data point the model hasn't seen before:*
	    model.predict(tf.tensor2d([5], [1, 1])).print();
	  });