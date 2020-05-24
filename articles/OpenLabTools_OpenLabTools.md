OpenLabTools/OpenLabTools

# Using the Raspberry Pi camera module with SimpleCV

Somahtr edited this page on Jul 25, 2013 · [1 revision](https://github.com/OpenLabTools/OpenLabTools/wiki/Using-the-Raspberry-Pi-camera-module-with-SimpleCV/_history)

###    Pages 15

- **[Home](https://github.com/OpenLabTools/OpenLabTools/wiki)**

- **[3D Printing Optical Components](https://github.com/OpenLabTools/OpenLabTools/wiki/3D-Printing-Optical-Components)**

- **[Building a Microscope](https://github.com/OpenLabTools/OpenLabTools/wiki/Building-a-Microscope)**

- **[Building a Microscope: Step 1: Printing the parts](https://github.com/OpenLabTools/OpenLabTools/wiki/Building-a-Microscope:-Step-1:-Printing-the-parts)**

- **[Building a Microscope: Step 2: Assembling the Structure](https://github.com/OpenLabTools/OpenLabTools/wiki/Building-a-Microscope:-Step-2:-Assembling-the-Structure)**

- **[Illumination](https://github.com/OpenLabTools/OpenLabTools/wiki/Illumination)**

- **[Launching bash scripts at startup](https://github.com/OpenLabTools/OpenLabTools/wiki/Launching-bash-scripts-at-startup)**

- **[Library](https://github.com/OpenLabTools/OpenLabTools/wiki/Library)**

- **[Mechanics Reference](https://github.com/OpenLabTools/OpenLabTools/wiki/Mechanics-Reference)**

- **[Optical Setup](https://github.com/OpenLabTools/OpenLabTools/wiki/Optical-Setup)**

- **[Optics BOM and instructions](https://github.com/OpenLabTools/OpenLabTools/wiki/Optics-BOM-and-instructions)**

- **[SSH on Raspberry Pi with Ethernet and or WiFi](https://github.com/OpenLabTools/OpenLabTools/wiki/SSH-on-Raspberry-Pi-with-Ethernet-and-or-WiFi)**

- **[Tutorials](https://github.com/OpenLabTools/OpenLabTools/wiki/Tutorials)**

- **[Useful Links](https://github.com/OpenLabTools/OpenLabTools/wiki/Useful-Links)**

- **[Using the Raspberry Pi camera module with SimpleCV](https://github.com/OpenLabTools/OpenLabTools/wiki/Using-the-Raspberry-Pi-camera-module-with-SimpleCV)**

##### Clone this wiki locally

 [ Clone in Desktop](https://github.com/OpenLabTools/OpenLabTools/wiki/Using-the-Raspberry-Pi-camera-module-with-SimpleCVgithub-mac://openRepo/https://github.com/OpenLabTools/OpenLabTools.wiki)

### [(L)](https://github.com/OpenLabTools/OpenLabTools/wiki/Using-the-Raspberry-Pi-camera-module-with-SimpleCV#introduction)Introduction

This tutorial is designed as a first basic introduction to using the Raspberry Pi camera module. SimpleCV is a image processing library for Python which makes it very simple to perform complicated image processing tasks including image manipulation and feature recognition.

### [(L)](https://github.com/OpenLabTools/OpenLabTools/wiki/Using-the-Raspberry-Pi-camera-module-with-SimpleCV#hardware-requirements)Hardware requirements

- Raspberry Pi with internet connection
- Raspberry Pi camera module

### [(L)](https://github.com/OpenLabTools/OpenLabTools/wiki/Using-the-Raspberry-Pi-camera-module-with-SimpleCV#software-requirements)Software requirements

- SimpleCV - see below for installation intructions

### [(L)](https://github.com/OpenLabTools/OpenLabTools/wiki/Using-the-Raspberry-Pi-camera-module-with-SimpleCV#step-1---connect-the-camera-module)Step 1 - Connect the camera module

Connect the camera module to the CSI port on the Raspberry Pi. With the camera connected, enable the camera from the raspi-config menu. Detailed instructions on how to install the camera can be found at http://www.raspberrypi.org/archives/3890.

### [(L)](https://github.com/OpenLabTools/OpenLabTools/wiki/Using-the-Raspberry-Pi-camera-module-with-SimpleCV#step-2---check-that-the-camera-is-connected)Step 2 - Check that the camera is connected

In the terminal, type the following command
` raspistill -t 5000 `
This will display a preview window for 5 seconds.

### [(L)](https://github.com/OpenLabTools/OpenLabTools/wiki/Using-the-Raspberry-Pi-camera-module-with-SimpleCV#step-3---install-simplecv)Step 3 - Install SimpleCV

First install the necessary dependency packages required by SimpleCV. This can be done in the terminal with the command

` sudo apt-get install ipython python-opencv python-scipy python-numpy python-setuptools python-pip `

Next download and install SimpleCV itself
` sudo pip install https://github.com/sightmachine/SimpleCV/zipball/master `

SimpleCV should now be installed on your Raspberry Pi. SimpleCV comes with its own shell application which can be accessed from the terminal by typing ` simplecv `. From here you can carry out the full range of image processing operations availiable. However for more complex operations and for interfacing with the Raspberry Pi camera it is easier to use Python scripts.

### [(L)](https://github.com/OpenLabTools/OpenLabTools/wiki/Using-the-Raspberry-Pi-camera-module-with-SimpleCV#step-4---loading-an-image-from-the-camera-into-simplecv)Step 4 - Loading an image from the camera into SimpleCV

Everything is now in place to start using SimpleCV and the camera module. Open up a text editor and type the following:

	import subprocess
	from SimpleCV import Image
	import time

	call(“raspistill -n -t 0 -w %s -h %s -o image.bmp” % 640 480, shell=True)

	img = Image(“image.bmp”)

	img.show()
	time.sleep(5)

Save the text file as ‘camera.py’, and in the command line type ` python camera.py ` to run.

The program opens up the camera, takes a still photo, and saves it to a file called image.bmp. SimpleCV then opens the file and displays it on screen for 5 seconds. Normally in SimpleCV an image can be loaded directly from the camera, for example:

	cam = Camera()
	img = cam.getImage()

However unfortunately there is no similar method for interacting with the Raspberry Pi, which is why this rather roundabout approach of calling the command-line instruction from within Python must be used.

### [(L)](https://github.com/OpenLabTools/OpenLabTools/wiki/Using-the-Raspberry-Pi-camera-module-with-SimpleCV#step-5---image-processing)Step 5 - Image processing

With the camera image now loaded into SimpleCV, we can perform any image processing tasks we need. For example, try adding one of the following code snippets to the end of the program and running:

	img = img.edges()
	img.show()
	time.sleep(5)

	img = img.binarize()
	img.show()
	time.sleep(5)

	img = img.findBlobs()
	for blob in blobs:
	    blob.draw()
	img.show()
	time.sleep(5)