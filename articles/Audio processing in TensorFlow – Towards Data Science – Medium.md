Audio processing in TensorFlow – Towards Data Science – Medium

# Audio processing in TensorFlow

![](../_resources/3dd65a5a82655330223828dec6ddf1f7.png)![1*YsFMNUMSZv4Axbp-ouOLiA.png](../_resources/8a17844b9f02ee02e77708de9383b2bf.png)

### An implementation of the Short Time Fourier Transform

#### **We found audio processing in TensorFlow hard, here is our fix**

There are countless ways to perform audio processing. The usual flow for running experiments with Artificial Neural Networks in TensorFlow with audio inputs is to first preprocess the audio, then feed it to the Neural Net.

What happens though when one wants to perform audio processing somewhere in the middle of the computation graph?

TensorFlow comes with an implementation of the [Fast Fourier Transform](https://www.tensorflow.org/api_docs/python/tf/fft), but it is not enough.

In this post we will explain how we implemented it and provide the code so that the Short Time Fourier Transform can be used anywhere in the computation graph.

#### Audio preprocessing: the usual approach

When developing a Speech Recognition engine using Deep Neural Networks we need to feed the audio to our Neural Network, but… what is the right way to preprocess this input?

There are 2 common ways to represent sound:

- •*Time domain: *each sample represents the variation in air pressure.
- •*Frequency domain*: at each time stamp we indicate the amplitude for each frequency.

Despite the fact that Deep Neural Networks are extremely good at learning features automagically, it is always a good idea to rely on known features that carry the information needed for the task that we are trying to solve.

For most application, a Speech Recognition Engine included, the features we are interested in are encoded in the frequency domain representation of the sound.

#### The spectrogram and the Short Time Fourier Transform

A [spectrogram](https://en.wikipedia.org/wiki/Spectrogram) shows how the frequency content of a signal changes over time and can be calculated from the time domain signal.

The operation, or transformation, used to do that is known as the [Short Time Fourier Transform](https://en.wikipedia.org/wiki/Short-time_Fourier_transform).

We could let the Neural Network figure out how to learn this operation, but it turns out to be quite complex to learn with 1 hidden layer. (refer to the [Universal approximation theorem](https://en.wikipedia.org/wiki/Universal_approximation_theorem))

We could add more layers, but we want to keep the complexity of the Neural Networks as small as possible and learn features only where it is most needed.

We have used the example of developing an Automatic Speech Recognition engine, but the use of the spectrogram as input to Deep Neural Nets is common also for similar tasks involving non-speech audio like noise reduction, music genre classification, whale call detection, etc.

A particular project that we want to mention is [Magenta](https://magenta.tensorflow.org/welcome-to-magenta), from the [Google Brain team](https://research.google.com/teams/brain/), who’s aim is to advance the state of the art in machine intelligence for music and art generation.

#### **Why TensorFlow?**

We mainly use TensorFlow when implementing Artificial Neural Networks and, because we haven’t found an implementation of the Short Time Fourier Transform in TF, we decided to implement our own.

There can also be multiple reasons why a deep learning practitioner might want to include the Short Time Fourier Transform (STFT for my friends) in the computation graph, and not just as a separate preprocessing step.

Keep in mind that we haven’t focused on making this efficient. It should (and will) be improved before being used in production.

#### **What we need to know**

In order to understand how the STFT is calculated, we need to understand how to compute the Discrete Fourier Transform.

#### **Discrete Fourier Transform — DFT**

This part can appear quite technical for those who are not familiar with these concepts, but we think it is important to go through some maths in order give a complete understanding of the code.

**Theory

**Fourier analysis is fundamentally a method for expressing a function as a sum of periodic components, and for recovering the function from those components. When both the function and its Fourier transform are replaced with discretized counterparts, it is called the discrete Fourier transform (DFT).

Given a vector ***x*** of *n* input amplitudes such as:
{x[0], x[1], x[2], x[3], …, x[N-1]}
the Discrete Fourier Transform yields a set of *n* frequency magnitudes.
The DFT is defined by this equation:

![](../_resources/9f7625ba64e9e4c269d7ea164696f5fd.png)![1*PKevkPcpgv2kWU84QT17XQ.png](../_resources/9f384e94aaf72eae0e10239b91860033.png)

DFT equation

- •k is used to denote the frequency domain ordinal
- •n is used to represent the time-domain ordinal
- •N is the length of the sequence to be transformed.

**Fast Fourier Transform

**The [Fast Fourier Transform](https://en.wikipedia.org/wiki/Fast_Fourier_transform) is an efficient implementation of the DFT equation. The signal must be restricted to be of size of a power of 2.

This explains why we want N (the size of the signal in input to the DFT function) to be power of 2 and why it must be zero-padded otherwise.

We can detect whether x is a power of 2 very simply in python:

![](../_resources/1d8c3268b48ab0ce32f6e4e8e95aff6a.png)

|     |     |
| --- | --- |
| 1   | def  is_power2(x): |
| 2   |  return x >  0  and ((x & (x -  1)) ==  0) |

 [view raw](https://gist.github.com/dariocazzani/9faadf0223cdf30a581bb23e267f9fb6/raw/05ddd2ae4c70e5aa7ae2039ecd035696560dba3f/ispower2.py)  [ispower2.py](https://gist.github.com/dariocazzani/9faadf0223cdf30a581bb23e267f9fb6#file-ispower2-py) hosted with ❤ by [GitHub](https://github.com/)

**We only need half of it

**Real sine waves can be expressed as the sum of complex sine waves using [Euler’s identity](https://en.wikipedia.org/wiki/Euler%27s_formula)

![](../_resources/2b77459a5679ec6d8b1d65acff9d2d03.png)![1*eU5F-WZZGiFX9Ov26E3iVw.png](../_resources/a3952028ac36dbd662154d71a2e1df43.png)

Because the DFT is a linear function, the DFT of a sum of sine waves is the sum of the DFT of each sine wave. So for our spectral case, we get 2 DFTs, one for the positive frequencies and one for the negative frequencies, which are symmetric.

This symmetry occurs for real signals that can be viewed as an infinite (or finite in our case) sum of sine waves.

**Windowing

**Truncating a signal in the time domain will lead to ripples appearing in the frequency domain.

This can be understood if we think of truncating the signal as if we applied a rectangular window. Applying a window in the time domain results in a convolution in the frequency domain.

The ripples are caused when we convolve the 2 frequency domain representations together.

Find out more about [spectral_leakage](https://mil.ufl.edu/nechyba/www/__eel3135.s2003/lectures/lecture19/spectral_leakage.pdf) if you’re interested.

Here is an example of an implementation of windowing in Python:

![](../_resources/1d8c3268b48ab0ce32f6e4e8e95aff6a.png)

|     |     |
| --- | --- |
| 1   | from scipy.signal import hanning |
| 2   | import tensorflow as tf |
| 3   | import numpy as np |
| 4   |     |
| 5   | N =  256  # FFT size |
| 6   | audio = np.random.rand(N, 1) *  2  -  1 |
| 7   | w = hanning(N) |
| 8   |     |
| 9   | input  = tf.placeholder(tf.float32, shape=(N, 1)) |
| 10  | window = tf.placeholder(tf.float32, shape=(N)) |
| 11  | window_norm = tf.div(window, tf.reduce_sum(window)) |
| 12  | windowed_input = tf.multiply(input, window_norm) |
| 13  |     |
| 14  | with tf.Session() as sess: |
| 15  | tf.global_variables_initializer().run() |
| 16  | windowed_input_val = sess.run(windowed_input, { |
| 17  | window: w, |
| 18  |  input: audio |
| 19  | })  |

 [view raw](https://gist.github.com/dariocazzani/8e19fc38991602346eb116daca3f055c/raw/c89b5c6ecf830a952d2e752c7f6542cda5350115/windowing.py)  [windowing.py](https://gist.github.com/dariocazzani/8e19fc38991602346eb116daca3f055c#file-windowing-py) hosted with ❤ by [GitHub](https://github.com/)

**Zero-phase padding**

In order to use the FFT, we need to have the input signal to have a power of 2 length. If the input signal does not have the right length, we have to append zeros to the signal itself both at the beginning and at the end.

Because the zero sample is originally at the center of the input signal, we have to split the padded signal through the middle and swap the order of these 2 parts.

The next code snippet shows how to do this in TensorFlow for a batch of inputs:

![](../_resources/1d8c3268b48ab0ce32f6e4e8e95aff6a.png)

|     |     |
| --- | --- |
| 1   | N =  512  # FFT size |
| 2   | input_length =  int(input.get_shape()[1]) |
| 3   |     |
| 4   | zeros_left = tf.zeros([int(input.get_shape()[0]), int((N - input_length+1) /  2)]) |
| 5   | zeros_right = tf.zeros([int(input.get_shape()[0]), int((N - input_length) /  2)]) |
| 6   | input_padded = tf.concat([zeros_left, input, zeros_right], axis=1) |
| 7   |     |
| 8   | fftbuffer_left = tf.slice(windowed_input, [0, int(N/2)], [-1, -1]) |
| 9   | fftbuffer_right = tf.slice(windowed_input, [0, 0], [-1, int(N/2)]) |
| 10  | fftbuffer = tf.concat([fftbuffer_left, fftbuffer_right], axis=1) |

 [view raw](https://gist.github.com/dariocazzani/a1d31c1c0a73031e54a5371ffa6c63b8/raw/84cad5190c8a8f3d1411c173048c77620e1cb540/zero-phase.py)  [zero-phase.py](https://gist.github.com/dariocazzani/a1d31c1c0a73031e54a5371ffa6c63b8#file-zero-phase-py) hosted with ❤ by [GitHub](https://github.com/)

**FFT, Magnitude and Phase

**We now have everything we need to calculate the magnitude of the spectrogram in decibels and the phase of the signal:

![](../_resources/1d8c3268b48ab0ce32f6e4e8e95aff6a.png)

|     |     |
| --- | --- |
| 1   | fft = tf.fft(tf.cast(fftbuffer, tf.complex64)) |
| 2   |     |
| 3   | # compute absolute value of positive side |
| 4   | sliced_fft = tf.slice(fft, [0, 0], [-1, positive_spectrum_size]) |
| 5   | abs_fft = tf.abs(sliced_fft) |
| 6   |     |
| 7   | # magnitude spectrum of positive frequencies in dB |
| 8   | magnitude =  20  * log10(tf.maximum(abs_fft, 1E-06)) |
| 9   |     |
| 10  | # phase of positive frequencies |
| 11  | phase = angle(sliced_fft) |

 [view raw](https://gist.github.com/dariocazzani/b9930791a27b3791f42adc32e74ee226/raw/c822c5a0fb54b67cf36e18f72ae4f939b9baa8c1/fft.py)  [fft.py](https://gist.github.com/dariocazzani/b9930791a27b3791f42adc32e74ee226#file-fft-py) hosted with ❤ by [GitHub](https://github.com/)

#### **Short Time Fourier Transform**

We now know how to compute the DFT to evaluate the frequency content of a signal.

The STFT is used to analyze the frequency content of signals when that frequency content varies with time.

We can do this by:
1. 1Taking segments of the signal.

2. 2Windowing those out from the rest of the signal, and applying a DFT to each segment.

3. 3Sliding this window along each segment.
We get DFT coefficients as a function of both time and frequency.
The complete code is divided in 2 parts: *helpers.py* and* stft.py*.

![](../_resources/1d8c3268b48ab0ce32f6e4e8e95aff6a.png)

#### Conclusion

The possibility of doing the STFT in TensorFlow allows Machine Learning practitioners to perform the transformation of a signal, from time-domain to frequency domain, anywhere in the computation graph.

New tools always bring new ideas and we hope this post will be the source of new ideas for developing new Deep Learning solutions.

### About Cisco Emerge

At Cisco Emerge, we are using the latest machine learning technologies to advance the future of work.

Find out more on [our website](http://emerge.cisco.com/?utm_source=medium&utm_medium=text_link&utm_content=text_link).