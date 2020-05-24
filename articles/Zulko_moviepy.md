Zulko/moviepy

# MoviePy

MoviePy (full [documentation](http://zulko.github.io/moviepy/)) is a Python library for video editing: cutting, concatenations, title insertions, video compositing (a.k.a. non-linear editing), video processing, and creation of custom effects. See the [gallery](http://zulko.github.io/moviepy/gallery.html) for some examples of use.

MoviePy can read and write all the most common audio and video formats, including GIF, and runs on Windows/Mac/Linux, with Python 2.7+ and 3. Here it is in action in an IPython notebook:

[(L)](https://raw.githubusercontent.com/Zulko/moviepy/master/docs/demo_preview.jpeg)

[![[logo\]](../_resources/bf08298e0edd7a6e05ce03e19f805eb4.jpg)](https://raw.githubusercontent.com/Zulko/moviepy/master/docs/demo_preview.jpeg)

## Example

In this example we open a video file, select the subclip between t=50s and t=60s, add a title at the center of the screen, and write the result to a new file:

from moviepy.editor import *
video = VideoFileClip("myHolidays.mp4").subclip(50,60)

# Make the text. Many more options are available.

txt_clip = ( TextClip("My Holidays 2013",fontsize=70,color='white')
.set_position('center')
.set_duration(10) )
result = CompositeVideoClip([video, txt_clip]) # Overlay text on video
result.write_videofile("myHolidays_edited.webm",fps=25) # Many options...

## Installation

MoviePy depends on the Python modules [Numpy](http://www.scipy.org/install.html), [imageio](http://imageio.github.io/), [Decorator](https://pypi.python.org/pypi/decorator), and [tqdm](https://github.com/noamraph/tqdm), which will be automatically installed during MoviePy's installation. The software FFMPEG should be automatically downloaded/installed (by imageio) during your first use of MoviePy (installation will take a few seconds). If you want to use a specific version of FFMPEG, follow the instructions in `config_defaults.py`. In case of trouble, provide feedback.

**Installation by hand:** download the sources, either from [PyPI](https://pypi.python.org/pypi/moviepy) or, if you want the development version, from [GitHub](https://github.com/Zulko/moviepy), unzip everything into one folder, open a terminal and type:

$ (sudo) python setup.py install

**Installation with pip:** if you have `pip` installed, just type this in a terminal:

$ (sudo) pip install moviepy

If you have neither `setuptools` nor `ez_setup` installed, the command above will fail. In this case type this before installing:

$ (sudo) pip install ez_setup

### Optional but useful dependencies

You can install `moviepy` with all dependencies via:
> $ (sudo) pip install moviepy[optional]

[ImageMagick](http://www.imagemagick.org/script/index.php) is not strictly required, but needed if you want to incorporate texts. It can also be used as a backend for GIFs, though you can also create GIFs with MoviePy without ImageMagick.

Once you have installed ImageMagick, it will be automatically detected by MoviePy, **except on Windows!** Windows users, before installing MoviePy by hand, need to edit `moviepy/config_defaults.py` to provide the path to the ImageMagick binary, which is called convert. It should look like this

IMAGEMAGICK_BINARY = "C:\\Program Files\\ImageMagick_VERSION\\convert.exe"

[PyGame](http://www.pygame.org/download.shtml) is needed for video and sound previews (not relevant if you intend to work with MoviePy on a server but essential for advanced video editing by hand).

For advanced image processing, you will need one or several of the following packages:

- The Python Imaging Library (PIL) or, even better, its branch [Pillow](http://pillow.readthedocs.org/en/latest/).
- [Scipy](http://www.scipy.org/) (for tracking, segmenting, etc.) can be used to resize video clips if PIL and OpenCV are not installed.
- [Scikit Image](http://scikit-image.org/download.html) may be needed for some advanced image manipulation.
- [OpenCV 2.4.6](http://sourceforge.net/projects/opencvlibrary/files/) or a more recent version (one that provides the package `cv2`) may be needed for some advanced image manipulation.
- [Matplotlib](https://matplotlib.org/)

Once you have installed it, ImageMagick will be automatically detected by MoviePy, (except for windows users and Ubuntu 16.04LTS users).

For Windows users, before installing MoviePy by hand, go into the `moviepy/config_defaults.py` file and provide the path to the ImageMagick binary called `magick`. It should look like this

IMAGEMAGICK_BINARY = "C:\\Program Files\\ImageMagick_VERSION\\magick.exe"

If you are using an older version of ImageMagick, keep in mind the name of the executable is not `magick.exe` but `convert.exe`. In that case, the IMAGEMAGICK_BINARY property should be `C:\\Program Files\\ImageMagick_VERSION\\convert.exe`

For Ubuntu 16.04LTS users, after installing MoviePy on the terminal, IMAGEMAGICK will not be detected by moviepy. This bug can be fixed. Modify the file in this directory: /etc/ImageMagick-6/policy.xml, comment out the statement <!-- <policy domain="path" rights="none" pattern="@*" /> -->.

[PyGame](http://www.pygame.org/download.shtml) is needed for video and sound previews (useless if you intend to work with MoviePy on a server but really essential for advanced video editing *by hand*).

For instance, using the method `clip.resize` requires that at least one of Scipy, PIL, Pillow or OpenCV is installed.

## Documentation

Running build_docs has additional dependencies that require installation.
> $ (sudo) pip install moviepy[docs]
The documentation can be generated and viewed via:
> $ python setup.py build_docs

You can pass additional arguments to the documentation build, such as clean build:

> $ python setup.py build_docs -E

More information is available from the [Sphinx](http://www.sphinx-doc.org/en/master/setuptools.html) documentation.

## Running Tests

The testing suite can be executed via:
> $ python setup.py test

Running the test suite in this manner will install the testing dependencies. If you opt to run the test suite manually, you can install the dependencies via:

> $ (sudo) pip install moviepy[test]

## Contribute

MoviePy is open-source software originally written by [Zulko](https://github.com/Zulko) and released under the MIT licence. The project is hosted on [GitHub](https://github.com/Zulko/moviepy), where everyone is welcome to contribute, ask for help or simply give feedback.

You can also discuss the project on [Reddit](http://www.reddit.com/r/moviepy/) (preferred over GitHub issues for usage/examples), [Gitter](https://gitter.im/movie-py/Lobby) or the mailing list [moviepy@librelist.com](https://github.com/Zulko/moviepymailto:moviepy@librelist.com).

## Maintainers