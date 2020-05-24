FIGLAB/ubicoustics: Accompanying repository for Ubicoustics: Plug-and-Play Acoustic Activity Recognition

# [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='166'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1151' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/FIGLAB/ubicoustics#research-code-for-ubicoustics)Research Code for Ubicoustics

This is the research repository for Ubicoustics: Plug-and-Play Acoustic Activity Recognition (UIST 2018). It contains the base toolchain and demo for Ubicoustics. [More information about the research can be found here](http://www.gierad.com/projects/ubicoustics).

[![ubicoustics_a.gif](../_resources/89f3ad304dc0a248dc1b81940e302ea4.gif)](https://github.com/FIGLAB/ubicoustics/blob/master/media/ubicoustics_a.gif?raw=true)[![ubicoustics_b.gif](../_resources/bd103518931cf4e78bfec954cc4e3d18.gif)](https://github.com/FIGLAB/ubicoustics/blob/master/media/ubicoustics_b.gif?raw=true)

# [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='167'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1154' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/FIGLAB/ubicoustics#system-requirements)System Requirements

The deep learning system is written in `python3`, specifically `tensorflow` and `keras`.

To begin, we recommend using `virtualenv` to run a self-contained setup:
$ virtualenv ./ubicoustics -p python3.6
$ source ubicoustics/bin/activate
Once `virtualenv` is activated, install the following dependencies via `pip`:
(ubicoustics)$ git clone https://github.com/FIGLAB/ubicoustics.git
(ubicoustics)$ pip install numpy==1.14.1 tensorflow==1.5.0 keras==2.1.6 wget
Finally, install `pyaudio` for microphone access:

(ubicoustics)$ pip install --global-option='build_ext' --global-option='-I/opt/local/include' --global-option='-L/opt/local/lib' pyaudio

Keep in mind that `pyaudio` will require `portaudio` and `libasound` as non-python dependencies. You'll have to install those separately for your OS.

`IMPORTANT:` When you install `pyaudio` via pip, you need to manually specify the `lib` and `include` directories via the `--global-option` flag. The example above assumes `portaudio` is installed under `/opt/local/include` and `/opt/local/lib`.

# [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='168'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1164' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/FIGLAB/ubicoustics#example-demos)Example Demos

Once the dependencies above are installed, try these four demos. It requires our pre-trained model that is not part of this repo (due to filesize restrictions), but we provide a downloader script to simplify this process.

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='169'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1167' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/FIGLAB/ubicoustics#example-0-file-prediction-simple)Example #0: File Prediction (Simple)

This simple demo reads an audio file, extracts features, and feeds them into the ML model for offline prediction. Once you've installed all dependencies, run `example_fileprediction_simple.py`:

(ubicoustics)$ python example_fileprediction_simple.py

The script will automatically download a model file called `example_model.hdf5` into the `/models` directory (if it doesn't exist). It's an 865.8MB file, so the download might take a while depending on your Internet connection. The script above will perform audio event detection on `example.wav`.

=====
Checking model...
=====
Downloading example_model.hdf5 [867MB]:
100% [.......................................]
Prediction: Coughing (1.00)
Prediction: Coughing (1.00)
Prediction: Coughing (1.00)
Prediction: Coughing (1.00)
Prediction: Coughing (1.00)
Prediction: Toilet Flushing (1.00)
Prediction: Toilet Flushing (1.00)
Prediction: Toilet Flushing (1.00)
Prediction: Water Running (1.00)
Prediction: Water Running (1.00)
Prediction: Water Running (1.00)
Prediction: Water Running (1.00)
Prediction: Water Running (1.00)
Prediction: Water Running (1.00)
Prediction: Water Running (1.00)
Prediction: Water Running (1.00)
Prediction: Knocking (1.00)
Prediction: Knocking (0.99)
Prediction: Knocking (0.91)

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='170'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1173' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/FIGLAB/ubicoustics#example-1-file-prediction-playback)Example #1: File Prediction (Playback)

Next, you can run the demo that plays back an audio file via `example_fileprediction_playback.py`:

(ubicoustics)$ python example_fileprediction_playback.py

It's similar to the previous example, but it uses `pyaudio`'s non-blocking mechanism to process audio buffers at a given sample length. We insert `ubicoustics` predictions within that block:

# Audio FORMATFORMAT  = pyaudio.paInt16CHANNELS  =  1RATE  =  16000CHUNK  =  RATE# Input fileswf = wave.open('example.wav', 'rb')# Callbackdef  audio_samples(input, frame_count, time_info, status_flags):

in_data = wf.readframes(frame_count) # Audio Processing Code here  # ...  return (in_data, pyaudio.paContinue)# Non-Blocking Callp = pyaudio.PyAudio()

stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, output=True, frames_per_buffer=CHUNK, stream_callback=audio_samples)

The script will use your computer's speakers to playback the audio file while displaying its predictions. If everything runs correctly, you should get the following output:

=====
Checking model...
=====
Beginning prediction for example.wav (use speakers for playback):
Prediction: Coughing (1.00)
Prediction: Coughing (1.00)
Prediction: Coughing (1.00)
Prediction: Coughing (1.00)
Prediction: Coughing (0.06)
Prediction: Toilet Flushing (1.00)
Prediction: Toilet Flushing (1.00)
Prediction: Toilet Flushing (1.00)
Prediction: Water Running (1.00)
Prediction: Water Running (1.00)
Prediction: Water Running (1.00)
Prediction: Water Running (1.00)
Prediction: Water Running (1.00)
Prediction: Water Running (1.00)
Prediction: Water Running (1.00)
Prediction: Chopping (0.96)
Prediction: Knocking (1.00)
Prediction: Knocking (1.00)
Prediction: Knocking (0.99)

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='171'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1181' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/FIGLAB/ubicoustics#example-2-live-prediction-simple)Example #2: Live Prediction (Simple)

This next example will use your system microphone to perform live audio event predictions.

(ubicoustics)$ python example_liveprediction_simple.py

It will check your system for a list of available microphones, and it will prompt you to choose one.

	=====
	1 / 2: Checking Microphones...
	=====
	=== Available Microphones: ===
	# 0 - Built-in Microphone
	# 1 - Gierad's Apple AirPods
	======================================
	Select microphone [0]: 0

You can also use the `--mic <mic-id>` flag to specify which local microphone to use.

	(ubicoustics)$ python example_liveprediction_simple.py --mic 0

The system will then perform audio event predictions using the chosen microphone. Your output should look something like this:

	Using mic: # 0 - Built-in Microphone
	=====
	2 / 2: Checking model...
	=====
	# Live Prediction Using Microphone: # 0 - Built-in Microphone
	Prediction: Typing (0.97)
	Prediction: Typing (0.97)
	Prediction: Typing (1.00)
	Prediction: Knocking (1.00)
	Prediction: Knocking (0.46)
	Prediction: Door In-Use (0.15)
	Prediction: Door In-Use (0.12)
	Prediction: Door In-Use (0.12)
	Prediction: Phone Ringing (0.46)
	Prediction: Phone Ringing (0.86)

This script makes predictions every second. This script should run on most platforms, including a `Raspberry Pi B+` (1GB of memory, 16GB disk space, with 4GB set as SWAP). If you need help setting up your RPi, send an email to Gierad ([gierad.laput@cs.cmu.edu](https://github.com/FIGLAB/ubicousticsmailto:gierad.laput@cs.cmu.edu)).

To manually grab a list of microphones for your system, just run `microphones.py`:

(ubicoustics)$ python microphones.py

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='172'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1191' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/FIGLAB/ubicoustics#example-3-live-prediction-detail-view)Example #3: Live Prediction (Detail View)

To form a better intuition on the system's behavior, this final example shows all the knobs you can turn, including the system's confidence values, along with audio levels and some parameters that you can tweak (e.g., thresholds) for real-time prediction.

	(ubicoustics)$ python example_liveprediction_detail.py

Here's an example screenshot:

[![example_liveprediction_detail.gif](../_resources/a1276a6cdcdbd4736e1b550cbc12a0ad.gif)](https://github.com/FIGLAB/ubicoustics/blob/master/media/example_liveprediction_detail.gif?raw=true)

Prediction confidence values will be shown in real time. The system checks whether the highest confidence value exceeds a given threshold AND wether the audio levels are significant enough to warrant an event trigger (e.g., > -40dB). These parameters can be adjusted using the `PREDICTION_THRES` and `DBLEVEL_THRES` parameters:

PREDICTION_THRES  =  0.8  # confidenceDBLEVEL_THRES  =  -40  # dB

# [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='173'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1197' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/FIGLAB/ubicoustics#reference)Reference

Gierad Laput, Karan Ahuja, Mayank Goel, Chris Harrison. 2018. Ubicoustics: Plug-and-Play Acoustic Activity Recognition. In Proceedings of the 31st Annual Symposium on User Interface Software and Technology (UIST '18). ACM, New York, NY, USA.

[Download the paper here](http://www.gierad.com/assets/ubicoustics/ubicoustics.pdf).

BibTex Reference:

	@inproceedings {ubicoustics,
	  author={Laput, G. and Ahuja, K. and Goel, M. and Harrison, C},
	  title={Ubicoustics: Plug-and-Play Acoustic Activity Recognition},
	  booktitle={Proceedings of the 31st Annual Symposium on User Interface Software and Technology},
	  series={USIT '18},
	  year={2018},
	  location={Berlin, Germany},
	  numpages={10},
	  publisher={ACM},
	  address={New York, NY, USA}
	}

# [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='174'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1201' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/FIGLAB/ubicoustics#license)License

Due to licensing restrictions, audio `wav` files and training code are only available by request (for now), and can only be used for research i.e., non-commercial purposes. Otherwise, Ubicoustics is freely available for non-commercial use, and may be redistributed under these conditions. Please see the license file for further details. For a commercial license, please contact Gierad Laput, Chris Harrison, and the CMU Technology Transfer Office ([innovation@cmu.edu](https://github.com/FIGLAB/ubicousticsmailto:innovation@cmu.edu)).

# [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='175'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1203' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/FIGLAB/ubicoustics#appendix-a-raspberry-pi)Appendix A: Raspberry Pi

We've received several requests to document how we made Ubicoustics run on a Raspberry Pi. Be forewarned that we're pushing the limits of what an RPi can do, but that's part of the fun. If you're all for it, here's what you'll need:

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='176'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1206' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/FIGLAB/ubicoustics#hardware)Hardware

1. [Raspberry Pi 3 Model B+ - CortexA53 with 1GB](https://www.adafruit.com/product/3775)

[![](https://camo.githubusercontent.com/ea9ce065790dce4c7c8bc8797852338283ce8d76/68747470733a2f2f63646e2d73686f702e61646166727569742e636f6d2f393730783732382f333737352d30342e6a7067)](https://camo.githubusercontent.com/ea9ce065790dce4c7c8bc8797852338283ce8d76/68747470733a2f2f63646e2d73686f702e61646166727569742e636f6d2f393730783732382f333737352d30342e6a7067)

1. [ReSpeaker 2-Mics Pi HAT (or better)](https://m.seeedstudio.com/productDetail/2874)

[![68747470733a2f2f73746174696373332e736565656473747564696f2e636f6d2f73656565642f696d672f323031372d30362f4877496b4366757a525a354561754c375134786d616a33442e6a7067](../_resources/ff4e7b916feda80827324dbd1f00133d.jpg)](https://camo.githubusercontent.com/0147f54898bab30529b6070f116795746400f36e/68747470733a2f2f73746174696373332e736565656473747564696f2e636f6d2f73656565642f696d672f323031372d30362f4877496b4366757a525a354561754c375134786d616a33442e6a7067)

1. [16GB Micro SD Card (Class 10)](https://www.amazon.com/SanDisk-COMINU024966-16GB-microSD-Card/dp/B004KSMXVM)

[![68747470733a2f2f69736162656c612e697765622e636f2e756b2f726573697a652f5a5430784d6a41354e6a41774a6d67394e5441774a6e45394e7a556d6444317664585269623356755a435a31636d77396148523063484d6c4d30456c4d6b596c4d6b5a7a6447463061574d7562586c745a573176636e6b75593238756457736c4d6b5a745a57527059535579526d4e68644746736232636c4d6b5a77636d396b64574e304a544a4755795579526d456c4d6b5a545957354561584e724c544d304e6a51304e454975616e426e4a6e63394e5441772f](../_resources/4878ce29b0ff7f3c73f479cb005d8e39.jpg)](https://camo.githubusercontent.com/a470e5552d4e72fcbd4c076ddae7516af7a76b79/68747470733a2f2f69736162656c612e697765622e636f2e756b2f726573697a652f5a5430784d6a41354e6a41774a6d67394e5441774a6e45394e7a556d6444317664585269623356755a435a31636d77396148523063484d6c4d30456c4d6b596c4d6b5a7a6447463061574d7562586c745a573176636e6b75593238756457736c4d6b5a745a57527059535579526d4e68644746736232636c4d6b5a77636d396b64574e304a544a4755795579526d456c4d6b5a545957354561584e724c544d304e6a51304e454975616e426e4a6e63394e5441772f)

1. [5V 2.5A Switching Power Supply (Highly Recommended)](https://www.adafruit.com/product/1995)

[![68747470733a2f2f63646e2d73686f702e61646166727569742e636f6d2f393730783732382f313939352d30322e6a7067](../_resources/1d46d76e64da31d8e9e35fee03d1e47e.jpg)](https://camo.githubusercontent.com/547482e81df8da3802ddf439d37b646ad1338602/68747470733a2f2f63646e2d73686f702e61646166727569742e636f6d2f393730783732382f313939352d30322e6a7067)

1. Alternative: Google AIY Kit

You can also use Google's AIY Voice Kit as a starting point. It uses roughly the same configuration as above, except you'll need a 16GB Mini SD Card (the AIY Kit comes with an 8GB card). It is markedly slower than an RPi B+.

You can buy the Google AIY Voice Kit from [Target](https://www.target.com/p/-/A-53416295).

[![68747470733a2f2f61697970726f6a656374732e77697468676f6f676c652e636f6d2f7374617469632f696d616765732f766f6963652d76322f67756964652f766f6963652d3030302e6a7067](../_resources/872ec11f2888ff7000b2b50adb916fe6.jpg)](https://camo.githubusercontent.com/5edfd295ffb0812bced1208f6050a1517e560ec6/68747470733a2f2f61697970726f6a656374732e77697468676f6f676c652e636f6d2f7374617469632f696d616765732f766f6963652d76322f67756964652f766f6963652d3030302e6a7067)

The Google AIY Kit is the absolute bare-bones configuration that we've tested. Again, it is significantly slower than an RPi B+ (but it has built-in Google integrations that you might find useful for other apps).

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='177'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1226' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/FIGLAB/ubicoustics#software-and-configuration)Software and Configuration

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='178'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1228' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/FIGLAB/ubicoustics#install-raspbian-os)Install Raspbian OS

We recommend using Raspbian Lite as the operating system, but other flavors will do. There's an entire process that documents [how to flash your SD card with the latest Raspbian OS](https://www.raspberrypi.org/documentation/installation/installing-images/). If you're running macOS, we recommend [going through this documentation](https://www.raspberrypi.org/documentation/installation/installing-images/mac.md).

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='179'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1231' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/FIGLAB/ubicoustics#install-microphone-drivers)Install Microphone Drivers

Next, install the audio drivers for the ReSpeaker 2-Mics Pi HAT. Detailed documentation about the process [can be found here](http://wiki.seeedstudio.com/ReSpeaker_2_Mics_Pi_HAT/).

$ git clone https://github.com/respeaker/seeed-voicecard.git
$ cd seeed-voicecard
$ sudo ./install.sh
$ reboot

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='180'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1235' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/FIGLAB/ubicoustics#configure-swap-space)Configure SWAP Space

Once flashed, change your RPi configuration so that it uses extra memory SWAP space. You can do this by editing `/etc/dphys-swapfile`:

	$ sudo nano /etc/dphys-swapfile

Uncomment the `CONF_SWAPSIZE` and `CONF_MAXSWAP` parameters, and set them to a value that is roughly above 1G. In our case, we've set it to `4096`.

	CONF_SWAPSIZE=4096
	CONF_MAXSWAP=4096

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='181'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1239' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/FIGLAB/ubicoustics#install-virtualenv)Install `virtualenv`

Once you've configured your SWAP space, we recommend creating a `virtualenv` environment. You can do this via:

$ sudo pip3 install virtualenv
$ virtualenv ./ubicoustics -p python3
$ source ubicoustics/bin/activate

Once `virtualenv` is installed, clone the repo and follow the instructions above to run Ubicoustics.

(ubicoustics)$ git clone https://github.com/FIGLAB/ubicoustics.git
(ubicoustics)$ cd ubicoustics
(ubicoustics)$ python example_fileprediction_simple.py

Once running, you'll get warning messages, specifically about exceeding memory. Don't worry— RPi will keep chugging along until `tensorflow` completes loading the model. Once done, your output should look something like this:

	Downloading example_model.hdf5 [867MB]:
	100% [......................................................................] 865808944 / 865808944
	Using deep learning model: models/example_model.hdf5
	2018-12-17 15:09:08.039745: W tensorflow/core/framework/allocator.cc:113] Allocation of 1024 exceeds 10% of system memory.
	2018-12-17 15:09:08.040125: W tensorflow/core/framework/allocator.cc:113] Allocation of 1024 exceeds 10% of system memory.
	2018-12-17 15:09:08.040456: W tensorflow/core/framework/allocator.cc:113] Allocation of 2048 exceeds 10% of system memory.
	2018-12-17 15:09:08.040689: W tensorflow/core/framework/allocator.cc:113] Allocation of 2048 exceeds 10% of system memory.
	2018-12-17 15:09:08.040904: W tensorflow/core/framework/allocator.cc:113] Allocation of 16384 exceeds 10% of system memory.
	Prediction: Coughing (1.00)
	Prediction: Coughing (1.00)
	Prediction: Coughing (1.00)
	Prediction: Coughing (1.00)
	Prediction: Coughing (1.00)
	Prediction: Toilet Flushing (1.00)
	Prediction: Toilet Flushing (1.00)
	Prediction: Toilet Flushing (1.00)
	Prediction: Water Running (1.00)
	Prediction: Water Running (1.00)
	Prediction: Water Running (1.00)
	Prediction: Water Running (1.00)
	Prediction: Water Running (1.00)
	Prediction: Water Running (1.00)
	Prediction: Water Running (1.00)
	Prediction: Water Running (1.00)
	Prediction: Knocking (1.00)
	Prediction: Knocking (0.99)
	Prediction: Knocking (0.91)

Feel free to try the other examples. It takes a while for RPi to run the script, but once loaded, you'll have a prediction framerate of about 1Hz. If you've made it this far, congratulations! :)

(ubicoustics)$ python example_liveprediction_simple.py

That's it! For help, questions, and general feedback, contact Gierad Laput ([gierad.laput@cs.cmu.edu](https://github.com/FIGLAB/ubicousticsmailto:gierad.laput@cs.cmu.edu)).

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='182'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1249' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/FIGLAB/ubicoustics#disclaimer)Disclaimer

	THE PROGRAM IS DISTRIBUTED IN THE HOPE THAT IT WILL BE USEFUL, BUT WITHOUT ANY WARRANTY. IT IS PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE. THE ENTIRE RISK AS TO THE QUALITY AND PERFORMANCE OF THE PROGRAM IS WITH YOU. SHOULD THE PROGRAM PROVE DEFECTIVE, YOU ASSUME THE COST OF ALL NECESSARY SERVICING, REPAIR OR CORRECTION.

	IN NO EVENT UNLESS REQUIRED BY APPLICABLE LAW THE AUTHOR WILL BE LIABLE TO YOU FOR DAMAGES, INCLUDING ANY GENERAL, SPECIAL, INCIDENTAL OR CONSEQUENTIAL DAMAGES ARISING OUT OF THE USE OR INABILITY TO USE THE PROGRAM (INCLUDING BUT NOT LIMITED TO LOSS OF DATA OR DATA BEING RENDERED INACCURATE OR LOSSES SUSTAINED BY YOU OR THIRD PARTIES OR A FAILURE OF THE PROGRAM TO OPERATE WITH ANY OTHER PROGRAMS), EVEN IF THE AUTHOR HAS BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGES.