Cross-compiling TensorFlow for the Raspberry Pi

[(L)](https://petewarden.com/2017/08/20/cross-compiling-tensorflow-for-the-raspberry-pi/)

# Cross-compiling TensorFlow for the Raspberry Pi

*[August 20, 2017](https://petewarden.com/2017/08/20/cross-compiling-tensorflow-for-the-raspberry-pi/)*  *   By   [Pete Warden](https://petewarden.com/author/petewarden/)*  *in [Uncategorized](https://petewarden.com/category/uncategorized/)**[10 Comments](https://petewarden.com/2017/08/20/cross-compiling-tensorflow-for-the-raspberry-pi/#comments)*

[![raspberries](../_resources/51b400dbed0cf03b06521164c3535da8.png)*Photo by oatsy40*](https://www.flickr.com/photos/oatsy40/14411767730/in/photolist-nXw5rY-aakWLA-cBPSJo-gEyGFH-26QTk4-6U7Nts-qMtX4n-kUnpK-emPsPu-9X5tHv-7qsgz5-6M1ytr-9Srdvt-kUnsd-9YzJ9J-5CRfAt-59RMzC-7R12sc-5xF4EL-8orfBU-oikBS5-csu4Zq-6BLzzp-3ihE3-Vnb5Pv-pqaXwQ-5CVysw-oTDLmX-8fbYXt-6Mwi93-d3EJrW-haJuy-7AY7RJ-7LGq6K-bVqsqg-3QqXzu-5aFaS4-8ynrps-ozNDzL-9KuUc-261JAC-bVqsez-3PvscS-o2Kyd7-6aX47W-6GervR-8cstbt-fS6uG-4Vx5HR-cNVNy7)

I love the Raspberry Pi because it’s such a great platform for software to interact with the physical world. TensorFlow makes it possible to turn messy, chaotic sensor data from cameras and microphones into useful information, so running models on the Pi has enabled some fascinating applications, from [predicting train times](https://svds.com/tensorflow-image-recognition-raspberry-pi/), [sorting trash](https://techcrunch.com/2016/09/13/auto-trash-sorts-garbage-automatically-at-the-techcrunch-disrupt-hackathon/), [helping robots see](https://www.oreilly.com/learning/how-to-build-a-robot-that-sees-with-100-and-tensorflow), and even [avoiding traffic tickets](https://techcrunch.com/2016/09/11/not-today-satan/)!

It’s never been easy to get TensorFlow installed on a Pi though. I had created [a makefile script that let you build the C++ part from scratch](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/contrib/makefile#raspberry-pi), but it took several hours to complete and didn’t support Python. Sam Abrahams, an external contributor, did an amazing job maintaining [a Python pip wheel for major releases](https://github.com/samjabrahams/tensorflow-on-raspberry-pi), but building it required you to add swap space on a USB device for your Pi, and took even longer to compile than the makefile approach. [Snips managed to get TensorFlow cross-compiling for Rust](https://medium.com/snips-ai/how-we-made-tensorflow-run-on-a-raspberry-pi-using-rust-7478f7a31329), but it wasn’t clear how to apply this to other languages.

Plenty of people on the team are Pi enthusiasts, and happily [Eugene Brevdo](https://ebrevdo.github.io/) dived in to investigate how we could improve the situation. We knew we wanted to have something that could be run as part of [TensorFlow’s Jenkins continuous integration system](https://ci.tensorflow.org/), which meant building a completely automatic solution that would run with no user intervention. Since having a Pi plugged into a machine to run something like the makefile build would be hard to maintain, we did try using a hosted server from [Mythic Beasts](https://www.mythic-beasts.com/). Eugene got the makefile built going after a few hiccups, but the Python version required more RAM than was available, and we couldn’t plug in a USB drive remotely!

Cross compiling, building on an x86 Linux machine but targeting the Pi, looked a lot more maintainable, but also more complex. Thankfully we had the Snips example to give us some pointers, a kindly stranger had [provided a solution to a crash that blocked me last time I tried it](https://raspberrypi.stackexchange.com/questions/48225/whats-causing-these-crashes-after-cross-compiling), and Eugene managed to get an initial version working.

I was able to take [his work](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/tools/ci_build/pi/build_raspberry_pi.sh), abstract it into [a Docker container](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/tools/ci_build/Dockerfile.pi) for full reproducibility, and now we have [nightly builds](http://ci.tensorflow.org/view/Nightly/job/nightly-pi/) running as part of our main Jenkins project. If you just want to try it out for Python 2.7, run:

sudo apt-get install libblas-dev liblapack-dev python-dev \
libatlas-base-dev gfortran python-setuptools
sudo ​pip2 install \

http://ci.tensorflow.org/view/Nightly/job/nightly-pi/lastSuccessfulBuild/artifact/output-artifacts/tensorflow-1.4.0-cp27-none-any.whl

This can take quite a while to complete, largely because it looks like the SciPy compilation is extremely slow. Once it’s done, you’ll be able to run TensorFlow in Python 2. If you get an error about the .whl file not being found at that URL, the version number may have changed. To find the correct name, go to  [http://ci.tensorflow.org/view/Nightly/job/nightly-pi/lastSuccessfulBuild/artifact/output-artifacts/](http://ci.tensorflow.org/view/Nightly/job/nightly-pi/lastSuccessfulBuild/artifact/output-artifacts/http://ci.tensorflow.org/view/Nightly/job/nightly-pi/lastSuccessfulBuild/artifact/output-artifacts/) and you should see the new version listed.

For Python 3.4 support, you’ll need to use a different wheel and pip instead of pip2, like this:

sudo apt-get install libblas-dev liblapack-dev python-dev \
libatlas-base-dev gfortran python-setuptools

sudo ​pip install \ http://ci.tensorflow.org/view/Nightly/job/nightly-pi-python3/lastSuccessfulBuild/artifact/output-artifacts/tensorflow-1.4.0-cp34-none-any.whl

If you’re running Python 3.5, you can use the same wheel but with a slight change to the file name, since that encodes the version. You will see a couple of warnings every time you import tensorflow, but it should work correctly.

sudo apt-get install libblas-dev liblapack-dev python-dev \
libatlas-base-dev gfortran python-setuptools

curl -O http://ci.tensorflow.org/view/Nightly/job/nightly-pi-python3/lastSuccessfulBuild/artifact/output-artifacts/tensorflow-1.4.0-cp34-none-any.whl

mv tensorflow-1.4.0-cp34-none-any.whl tensorflow-1.4.0-cp35-none-any.whl
sudo ​pip install tensorflow-1.4.0-cp35-none-any.whl

If you have a Pi Zero or One that you want to use TensorFlow on, you’ll need to use an alternative wheel that doesn’t include NEON instructions. This is a lot slower than the one above that’s optimized for the Pi Two and above, so I don’t recommend you use it on newer devices. Here are the commands for Python 2.7:

sudo apt-get install libblas-dev liblapack-dev python-dev \
libatlas-base-dev gfortran python-setuptools
​sudo pip2 install \

http://ci.tensorflow.org/view/Nightly/job/nightly-pi-zero/lastSuccessfulBuild/artifact/output-artifacts/tensorflow-1.4.0rc1-cp27-none-any.whl

Here is the Python 3.4 version for the Pi Zero:
sudo apt-get install libblas-dev liblapack-dev python-dev \
libatlas-base-dev gfortran python-setuptools sudo ​pip install \

http://ci.tensorflow.org/view/Nightly/job/nightly-pi-zero-python3/lastSuccessfulBuild/artifact/output-artifacts/tensorflow-1.4.0-cp34-none-any.whl

And here are the Python 3.5 instructions:
sudo apt-get install libblas-dev liblapack-dev python-dev \
libatlas-base-dev gfortran python-setuptools

curl -O http://ci.tensorflow.org/view/Nightly/job/nightly-pi-zero-python3/lastSuccessfulBuild/artifact/output-artifacts/tensorflow-1.4.0-cp34-none-any.whl

mv tensorflow-1.4.0-cp34-none-any.whl tensorflow-1.4.0-cp35-none-any.whl
sudo ​pip install tensorflow-1.4.0-cp35-none-any.whl

I’ve found the scipy compilation on Pi Zeros/Ones is so slow (many hours), it is unfeasible to wait for it to complete. Instead I’ve found myself pressing Control-C to cancel when it’s in the middle of a scipy-related compile step, and then re-running with ‘–no-deps’ flag after install to skip building dependencies. This is extremely hacky, but since scipy is only needed for testing purposes you should have a workable copy of TensorFlow at the end, provided all the other dependencies completed.

If you want to build your own copy of the wheels, you can run this line from within the TensorFlow source root on a Linux machine with Docker installed to build for the Pi Two or Three with Python 2.7:

tensorflow/tools/ci_build/ci_build.sh PI tensorflow/tools/ci_build/pi/build_raspberry_pi.sh

For Python 3.4:

CI_DOCKER_EXTRA_PARAMS="-e CI_BUILD_PYTHON=python3 -e CROSSTOOL_PYTHON_INCLUDE_PATH=/usr/include/python3.4" tensorflow/tools/ci_build/ci_build.sh PI-PYTHON3 tensorflow/tools/ci_build/pi/build_raspberry_pi.sh

For Python 2.7 on the Pi Zero:

tensorflow/tools/ci_build/ci_build.sh PI tensorflow/tools/ci_build/pi/build_raspberry_pi.sh PI_ONE

For Python 3.4 on the Pi Zero:

CI_DOCKER_EXTRA_PARAMS="-e CI_BUILD_PYTHON=python3 -e CROSSTOOL_PYTHON_INCLUDE_PATH=/usr/include/python3.4" tensorflow/tools/ci_build/ci_build.sh PI-PYTHON3 tensorflow/tools/ci_build/pi/build_raspberry_pi.sh PI_ONE

This is all still experimental, so please do [file bugs](https://github.com/tensorflow/tensorflow/issues) with feedback if these don’t work for you. I’m hoping we will be able to provide official stable Pi binaries for each major release in the future, like we do for Android and iOS, so knowing how well things are working is important to me. I’m also always excited to hear about cool new applications you find for TensorFlow on the Pi, so do let me know what you build too!

### Share this:

- [Twitter](https://petewarden.com/2017/08/20/cross-compiling-tensorflow-for-the-raspberry-pi/?share=twitter&nb=1)
- [Facebook76](https://petewarden.com/2017/08/20/cross-compiling-tensorflow-for-the-raspberry-pi/?share=facebook&nb=1)
- [Google](https://petewarden.com/2017/08/20/cross-compiling-tensorflow-for-the-raspberry-pi/?share=google-plus-1&nb=1)

-
[Like](https://widgets.wp.com/likes/#)
Be the first to like this.

### *Related*

[TensorFlow for Mobile Poets](https://petewarden.com/2016/09/27/tensorflow-for-mobile-poets/)With 47 comments

[TensorFlow for Poets](https://petewarden.com/2016/02/28/tensorflow-for-poets/)With 47 comments

[Can you help me gather open speech data?](https://petewarden.com/2017/06/12/can-you-help-me-gather-open-speech-data/)With 6 comments

.