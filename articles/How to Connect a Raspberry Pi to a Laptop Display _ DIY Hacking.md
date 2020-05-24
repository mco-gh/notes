How to Connect a Raspberry Pi to a Laptop Display | DIY Hacking

# How to Connect a Raspberry Pi to a Laptop Display

[* *  30](https://diyhacking.com/connect-raspberry-pi-to-laptop-display/#)

[** 87](https://diyhacking.com/connect-raspberry-pi-to-laptop-display/#comments)[**](https://diyhacking.com/connect-raspberry-pi-to-laptop-display/#)

**By Sohil Patel**

[![Connect raspberry pi to laptop display DIY Hacking](../_resources/8c802270fe905c5c08857efb541a8249.jpg)](https://301o583r8shhildde3s0vcnh-wpengine.netdna-ssl.com/wp-content/uploads/2015/02/Cover1.jpg)

I came up with this tutorial was because one day, my friend Suvigya and I were struggling to work on the Raspberry Pi because we did not have any HDdisplays. Hence, I came up with this tutorial so others in the same situation as ours would be able to use their laptop display as a monitor for their Raspberry Pi.

As we know Raspberry Pi is known as the “Pocket Size PC”, but for debugging and project purposes it’s cumbersome to carry an additional display for it. Also, many of us don’t have access to an HDMI display. So, we figured out a way to easily connect a Raspberry Pi to a laptop display. So sit back and enjoy this simple tutorial!

[![Connect raspberry pi to laptop display DIY Hacking](../_resources/010d2a57e4a8473fe8de0189d1b8991e.jpg)](https://301o583r8shhildde3s0vcnh-wpengine.netdna-ssl.com/wp-content/uploads/2015/02/compon-compressed1.jpg)

### **Required Materials**

1. [Raspberry Pi.](https://www.allaboutcircuits.com/electronic-components/?p=BCM2836+Raspberry+Pi+2+Model+B)

2. Ethernet Cable.
3. Laptop.
4. SD Card with Raspbian.
5. Micro USB Cable.
(Optional) Components required for setting it up the first time:
1. HDMI/ AV Display.
2. Keyboard and Mouse.

### **How Does it Work?**

To connect a Raspberry Pi to a laptop display, you can simply use an ethernet cable. The Raspberry Pi’s desktop GUI (Graphical User Interface) can be viewed through the laptop display using a 100Mbps ethernet connection between the two. There are many software programs available that can establish connection between a Raspberry Pi and your laptop. We used VNC server software to Connect the Pi to our laptop.

Installing the VNC server on your Pi allows you to see the Raspberry Pi’s desktop remotely, using the mouse and keyboard as if you were sitting right in front of your Pi. It also means that you can put your Pi anywhere else in your home and still control it. Also, the internet can be shared from laptop’s WiFi over Ethernet. This also lets you access internet on the Pi and connect it to your laptop display.

### ****Setting up your Raspberry Pi****

Before moving to connect your Raspberry Pi to laptop display, you need an SD card with the OS preinstalled. You will find lots of blogs and tutorials on preparing an SD card for the Raspberry Pi. If you are a beginner, you can simply download this free beginner’s guide eBook on the Pi: [Raspberry Pi guide](http://diyhacking.com/). This will show how to install the OS for the Raspberry Pi. You can also buy SD cards with the Raspian and NOOBs operating systems preinstalled.

After setting up your SD Card, insert it into the Raspberry Pi. Next, connect your micro USB cable to the Raspberry Pi to power it. Also connect your Raspberry Pi to the laptop via an ethernet cable and connect a keyboard and mouse to it. Now, connect the HDMI display (the HDMI is only required to run the Pi for the first time) and power on your Pi. Follow the next steps to connect your Raspberry Pi to a laptop display.

### ****Sharing Internet Over Ethernet****

This step explains how you can share your laptop internet with the Raspberry pi via Ethernet cable.

In Windows: To share internet with multiple users over Ethernet, go to Network and Sharing Center. Then click on the WiFi network:

[![Connect raspberry pi to laptop display DIY Hacking](../_resources/2232ed52ca55013c9b6f2c7f826592db.jpg)](https://301o583r8shhildde3s0vcnh-wpengine.netdna-ssl.com/wp-content/uploads/2015/02/win1-e14337880655451.jpg)

Click on Properties (shown below), then go to Sharing and click on “Allow other network users to connect”. Make sure that networking connection is changed to “Local Area Connection”:[![Connect raspberry pi to laptop display DIY Hacking](../_resources/a040cddec83604a0c2ef957471aa663e.jpg)](https://301o583r8shhildde3s0vcnh-wpengine.netdna-ssl.com/wp-content/uploads/2015/02/win2-e14337886851901.jpg)

[![Connect raspberry pi to laptop display DIY Hacking](../_resources/11abce75f81616ddd961e4587e8071db.jpg)](https://301o583r8shhildde3s0vcnh-wpengine.netdna-ssl.com/wp-content/uploads/2015/02/win3-e14337889657973.jpg)

Note: Doing this will provide a dynamic IP to the Ethernet port on your laptop and other devices connected to your laptop. Now, to check the IP assigned to your laptop, click on the new local area connection link created:

[(L)](https://301o583r8shhildde3s0vcnh-wpengine.netdna-ssl.com/wp-content/uploads/2015/02/win4-e1424932354447.jpg)[![Connect raspberry pi to laptop display DIY Hacking](../_resources/40f576c799876fc3ed125f2eb19cd634.jpg)](https://301o583r8shhildde3s0vcnh-wpengine.netdna-ssl.com/wp-content/uploads/2015/02/win411.jpg)

[![Connect raspberry pi to laptop display DIY Hacking](../_resources/823312709f5a1a9ea3c92823a1193ccb.jpg)](https://301o583r8shhildde3s0vcnh-wpengine.netdna-ssl.com/wp-content/uploads/2015/02/win511.jpg)

As shown above, the IP assigned to my laptop is 192.168.137.1. To check the IP assigned to the connected ethernet device, do the following. Considering that the IP assigned to your Laptop is 192.168.137.1 and subnet mask is 255.255.255.0 :

- Open command prompt.
- Ping the broadcast address of your IP. (Type) Eg: ping 192.168.137.255
- Stop the ping after 5 seconds.
- Check the reply from device: arp –a

### **Setting up the VNC Server to Connect Your Raspberry Pi to a Laptop Display**

**If you have an HDMI display:** Using the connected HDMI display on your Pi, you should install VNC server on your Raspberry Pi. Open the LX-Terminal and type the following commands to install VNC:

$ sudo apt-get update
$ sudo apt-get install tightvncserver

**If you don’t have an HDMI display:** If you do not have a display even for one-time setup, then no need to worry. Install [Putty](http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html) as per your Windows configuration and via SSH you can connect with your Raspberry Pi. As you get access to your pi terminal, run the same commands as above to install VNC.

**Starting VNC Server on Pi:**
To start VNC, enter the following command in the SSH terminal:
$ vncserver :1

You will be prompted to enter and confirm a password. This will be asked only once, during first time setup. Enter an 8 digit password. Note that this is the password you will need to use to connect to your Raspberry Pi remotely. You will also be asked if you want to create a separate “read-only” password – say no (n).

Yippeee!….The VNC server is now running on your Pi and we can now attempt to connect to it. First, we must switch to the laptop, from which we want to control the Pi. Then set up a VNC client to connect to the Pi.

### **Setting Up the Client Side (Laptop)**

Download VNC client from [here](https://www.realvnc.com/download/vnc/) and install it. When you first run VNC viewer, you will see following:

[![Connect raspberry pi to laptop display DIY Hacking](../_resources/17ce42778530fbd2910d2349c5352507.jpg)](https://301o583r8shhildde3s0vcnh-wpengine.netdna-ssl.com/wp-content/uploads/2015/02/vnc111.jpg)

Enter the IP address of your Raspberry Pi given dynamically by your laptop (you got the address from the earlier step) and append with :1 (denoting port number) and press connect. You will get a warning message, press ‘Continue’:

[![Connect raspberry pi to laptop display DIY Hacking](../_resources/c86b4f5eb2f9389491dd3aa4ac65bd09.jpg)](https://301o583r8shhildde3s0vcnh-wpengine.netdna-ssl.com/wp-content/uploads/2015/02/vnc211.jpg)

Enter the 8 digit password which was entered in the VNC server installation on your Raspberry Pi:

[![Connect raspberry pi to laptop display DIY Hacking](../_resources/1ed0023bb2e31e1fe1cc29fcfa86758a.jpg)](https://301o583r8shhildde3s0vcnh-wpengine.netdna-ssl.com/wp-content/uploads/2015/02/vnc311.jpg)

Finally, the Raspberry Pi desktop should appear as a VNC window. You will be able to access the GUI and do everything as if you were using the Pi’s keyboard, mouse, and monitor directly. As with SSH, since this is working over your network, your Pi can be situated anywhere as long as it is connected to your network.

[![Connect raspberry pi to laptop display DIY Hacking](../_resources/a00283994f377018f811b9894c00f743.jpg)](https://301o583r8shhildde3s0vcnh-wpengine.netdna-ssl.com/wp-content/uploads/2015/02/rpi.jpg)

Raspberry pi desktop on your laptop display

### **Running VNC Server During Startup in the Raspberry Pi GUI**

Connecting to your Raspberry Pi remotely with VNC is fine as long as your Pi does not reboot. If it does, then you either have to connect with SSH and restart the VNC Server or arrange for the VNC Server to run automatically after the Raspberry Pi reboots. To ensure that the VNC starts automatically each time when booting up, run the following commands in the terminal:

Open “.config” folder from the Pi’s: user folder (it is a hidden folder).
$ cd /home/pi
$ cd .config

Create a folder called “autostart” in it. Also, create a file called “tightvnc.desktop” in that folder. You can use any known text editor to create the files. I used gnome-text-editor for this:

$ mkdir autostart
$ cd autostart
$ gnome tightvnc.desktop
Edit the contents of the file with the following text and save the file:
[Desktop Entry]
Type=Application
Name=TightVNC
Exec=vncserver :1
StartupNotify=false

Now next time you reboot your Pi, vncserver will start automatically and will seamlessly connect your Raspberry Pi to a laptop display. Good job!

Whenever you want to do something with your Pi, just connect it with an ethernet cable to your laptop and power it. Then open VNCViewer, mention the IP address of your Pi, and you can use your laptop’s display as the Raspberry Pi’s monitor.

Tags: [connect raspberry pi laptop display](https://diyhacking.com/tag/connect-raspberry-pi-laptop-display/), [laptop display](https://diyhacking.com/tag/laptop-display/), [laptop screen](https://diyhacking.com/tag/laptop-screen/), [Raspberry pi](https://diyhacking.com/tag/raspberry-pi/), [raspberry pi monitor](https://diyhacking.com/tag/raspberry-pi-monitor/)

Recommended Posts

- [![How to Make a Raspberry Pi Web Server](../_resources/41208b6cb359667cc2ac3e95c0074e6d.jpg)](https://diyhacking.com/raspberry-pi-web-server/)[How to Make a Raspberry Pi Web Server](https://diyhacking.com/raspberry-pi-web-server/)
- [![How to Get Started With IoT Using Raspberry Pi and PuTTY – Part 1](../_resources/1ae6d0c767708364e9e0b287af544544.jpg)](https://diyhacking.com/best-raspberry-pi-iot-project/)[How to Get Started With IoT Using Raspberry Pi and PuTTY – Part 1](https://diyhacking.com/best-raspberry-pi-iot-project/)
- [![How to Get Started With IoT Using Raspberry Pi and PuTTY – Part 2](../_resources/a6f4a68470efa37a7388b59bcd88e546.jpg)](https://diyhacking.com/best-raspberry-pi-iot-android/)[How to Get Started With IoT Using Raspberry Pi and PuTTY – Part 2](https://diyhacking.com/best-raspberry-pi-iot-android/)
- [![IoT Based Raspberry Pi Home Automation Using IBM Bluemix](../_resources/acc1647704fb074d85d326fedc9ea1d2.jpg)](https://diyhacking.com/raspberry-pi-home-automation-ibm-bluemix/)[IoT Based Raspberry Pi Home Automation Using IBM Bluemix](https://diyhacking.com/raspberry-pi-home-automation-ibm-bluemix/)

Showing 87 comments

- ![6b16b99c5db6b1c544ed7dc10ca7db23.jpg](../_resources/c0ab18e56c9ef1f05b6ffe3d3521270c.jpg)

RobertMarch 8, 2017

[Reply](https://diyhacking.com/connect-raspberry-pi-to-laptop-display/?replytocom=5018#respond)

I can get VNC up and working but not the austostart, I have loaded raspberry PI three times and made sure to the programming.

Still dose not work.

- ![975738812e5e45d1e4c798bced6f7aac.jpg](../_resources/ca117b85796679a59cbaa46335964101.jpg)

zoroastraFebruary 22, 2017

[Reply](https://diyhacking.com/connect-raspberry-pi-to-laptop-display/?replytocom=4899#respond)

http://mercadolikes.com/

Hi thеrе, I discovered youг website ƅy way of Google еven as lookіng for ɑ comparable matter,

your website ǥot here uρ, it seems to be goߋⅾ.
Ⅰ have bookmarked іt іn my google bookmarks.

Ηеllo thᥱre, ϳust was aware оf your blog via Google, and located tһat it’s truly

informative. І am going to be careful foг brussels.
Ι’ll aρpreciate ѕhould уou proceed tҺis iin future.
Numerous people ѕhall be benefited fгom yοur writing.
Cheers!

- ![6b16b99c5db6b1c544ed7dc10ca7db23.jpg](../_resources/c0ab18e56c9ef1f05b6ffe3d3521270c.jpg)

sri divyaFebruary 13, 2017

[Reply](https://diyhacking.com/connect-raspberry-pi-to-laptop-display/?replytocom=4825#respond)

god

- ![6b16b99c5db6b1c544ed7dc10ca7db23.jpg](../_resources/c0ab18e56c9ef1f05b6ffe3d3521270c.jpg)

JephDecember 27, 2016

[Reply](https://diyhacking.com/connect-raspberry-pi-to-laptop-display/?replytocom=4529#respond)

thanks for the help… but have issue making it autostart.

especially how do i know the name for the text editor … like gnome tightvnc.desktop

    - ![975738812e5e45d1e4c798bced6f7aac.jpg](../_resources/ca117b85796679a59cbaa46335964101.jpg)

MyNameJeffJanuary 13, 2017

[Reply](https://diyhacking.com/connect-raspberry-pi-to-laptop-display/?replytocom=4638#respond)

type ‘nano tightvnc.desktop’ if you don’t have the gnome text editor.

- ![6b16b99c5db6b1c544ed7dc10ca7db23.jpg](../_resources/c0ab18e56c9ef1f05b6ffe3d3521270c.jpg)

sharathDecember 4, 2016

[Reply](https://diyhacking.com/connect-raspberry-pi-to-laptop-display/?replytocom=4367#respond)

each and every restart ip of raspberry is changing

    - ![6b16b99c5db6b1c544ed7dc10ca7db23.jpg](../_resources/c0ab18e56c9ef1f05b6ffe3d3521270c.jpg)

fakenameJanuary 13, 2017

[Reply](https://diyhacking.com/connect-raspberry-pi-to-laptop-display/?replytocom=4639#respond)

Use ‘raspberrypi.mshome.net’ as the ip, works for me.

- ![6b16b99c5db6b1c544ed7dc10ca7db23.jpg](../_resources/c0ab18e56c9ef1f05b6ffe3d3521270c.jpg)

WesleyNovember 3, 2016

[Reply](https://diyhacking.com/connect-raspberry-pi-to-laptop-display/?replytocom=4138#respond)

Hi, I would like to ask how do you configure the microphone? It does not record anything and shows No Translation. And how do you edit the command file? I faces Permission denied problem. By the way, I am using Raspberry Pi 3 model b+ and Logitech Webcam C170. Thank you.

- ![6b16b99c5db6b1c544ed7dc10ca7db23.jpg](../_resources/c0ab18e56c9ef1f05b6ffe3d3521270c.jpg)

Walt WilliamsOctober 28, 2016

[Reply](https://diyhacking.com/connect-raspberry-pi-to-laptop-display/?replytocom=4095#respond)

What if your running Debian on your laptop?

- ![6b16b99c5db6b1c544ed7dc10ca7db23.jpg](../_resources/c0ab18e56c9ef1f05b6ffe3d3521270c.jpg)

Veera RagavOctober 26, 2016

[Reply](https://diyhacking.com/connect-raspberry-pi-to-laptop-display/?replytocom=4078#respond)

Hi… My pi got connected. The desktop is opened in the vnc viewer. But the desktop is empty(fully grey). Right click works which shows some options like terminal emulator, web browser, restart, exit etc., Why cant i see my desktop wallpaper and the icons on it…??

- ![6b16b99c5db6b1c544ed7dc10ca7db23.jpg](../_resources/c0ab18e56c9ef1f05b6ffe3d3521270c.jpg)

DuarteOctober 2, 2016

[Reply](https://diyhacking.com/connect-raspberry-pi-to-laptop-display/?replytocom=3902#respond)

Beautiful, it worked for me! Just one thing: do not connect the ethernet cable while the RPI is restaring (otherwise it just keeps on restarting). At least that is what happened to me. Thanks a lot!

    - ![6b16b99c5db6b1c544ed7dc10ca7db23.jpg](../_resources/c0ab18e56c9ef1f05b6ffe3d3521270c.jpg)

TayyabOctober 21, 2016

[Reply](https://diyhacking.com/connect-raspberry-pi-to-laptop-display/?replytocom=4041#respond)

So i have a question, i have already configured my pi, summing up all the steps above, if i connect my pi to an Ethernet connection and give that ip address to the VNC server software on my laptop, it should display the raspbian screen right? It worked with putty, just wondering if it will work this way. I did this at my university so i am assuming that my laptop was connected to a wifi and the pi to an ethernet cable and by just giving the ip address of the pi to my the VNC software on my laptop should yield an instant access to the raspbian?

- ![6b16b99c5db6b1c544ed7dc10ca7db23.jpg](../_resources/c0ab18e56c9ef1f05b6ffe3d3521270c.jpg)

suSeptember 29, 2016

[Reply](https://diyhacking.com/connect-raspberry-pi-to-laptop-display/?replytocom=3882#respond)

whenever i connect to my respberry pi, the screen is duplicating and cannot do anything. how can i solve that?

- ![6b16b99c5db6b1c544ed7dc10ca7db23.jpg](../_resources/c0ab18e56c9ef1f05b6ffe3d3521270c.jpg)

ammySeptember 25, 2016

[Reply](https://diyhacking.com/connect-raspberry-pi-to-laptop-display/?replytocom=3849#respond)

great post wanna see [more](https://www.laboneinside.com/)

- ![975738812e5e45d1e4c798bced6f7aac.jpg](../_resources/ca117b85796679a59cbaa46335964101.jpg)

GAURAV TYAGISeptember 2, 2016

[Reply](https://diyhacking.com/connect-raspberry-pi-to-laptop-display/?replytocom=3741#respond)

Hi Friends,

I a beginner , starting to use raspberry PI Model B. Connected it to the laptop via HDMI port. Setup Putty, commands worked and everything done. Downloaded VNC. Assigned password for VNC viewer but when I click connect it opens it an array of hundred’s of windows. Please help.

    - ![6b16b99c5db6b1c544ed7dc10ca7db23.jpg](../_resources/c0ab18e56c9ef1f05b6ffe3d3521270c.jpg)

Afif Widiyanto MusthofaSeptember 30, 2016

[Reply](https://diyhacking.com/connect-raspberry-pi-to-laptop-display/?replytocom=3886#respond)

You don’t need the HDMI cables. In fact, it won’t work if you connect those two ports as both are Output ports. We only need the Ethernet connection.

- ![e16cf8050105e7ae84c22a5363bcf13d.jpg](../_resources/0cd43c7866be9a7c0dc104361a927d53.jpg)

DanielleJuly 28, 2016

[Reply](https://diyhacking.com/connect-raspberry-pi-to-laptop-display/?replytocom=3537#respond)

Seriously amazing :) thank you so much for a clear tutorial that Just Works!

- ![6b16b99c5db6b1c544ed7dc10ca7db23.jpg](../_resources/c0ab18e56c9ef1f05b6ffe3d3521270c.jpg)

EM FarihJuly 25, 2016

[Reply](https://diyhacking.com/connect-raspberry-pi-to-laptop-display/?replytocom=3522#respond)

Thanks…
You’re so amazing… :D

- ![6b16b99c5db6b1c544ed7dc10ca7db23.jpg](../_resources/c0ab18e56c9ef1f05b6ffe3d3521270c.jpg)

OnurJuly 14, 2016

[Reply](https://diyhacking.com/connect-raspberry-pi-to-laptop-display/?replytocom=3455#respond)

Can i use it for orange pi pc too?I think that would work for it too.

- ![6b16b99c5db6b1c544ed7dc10ca7db23.jpg](../_resources/c0ab18e56c9ef1f05b6ffe3d3521270c.jpg)

G.NishanthanJuly 2, 2016

[Reply](https://diyhacking.com/connect-raspberry-pi-to-laptop-display/?replytocom=3398#respond)

You are so amazing man.. Worked perfectly….

- ![975738812e5e45d1e4c798bced6f7aac.jpg](../_resources/ca117b85796679a59cbaa46335964101.jpg)

el soonfyJune 21, 2016

[Reply](https://diyhacking.com/connect-raspberry-pi-to-laptop-display/?replytocom=3340#respond)

hi . Dude please help me , i want you to buy me the latest Raspberry Pi with all the connectors needed to power up pi. And tell me how much it cost you. Then i pay you via paypal or western union. Byd way u wil send it to my country.. You have my email. Just tel me if you can do it..pls i wil be waiting. THANKX

- ![6b16b99c5db6b1c544ed7dc10ca7db23.jpg](../_resources/c0ab18e56c9ef1f05b6ffe3d3521270c.jpg)

bobMay 14, 2016

[Reply](https://diyhacking.com/connect-raspberry-pi-to-laptop-display/?replytocom=3105#respond)

Well, My laptop doesn’t have an ethernet port.
What would I do?

    - ![6b16b99c5db6b1c544ed7dc10ca7db23.jpg](../_resources/c0ab18e56c9ef1f05b6ffe3d3521270c.jpg)

bobMay 15, 2016

[Reply](https://diyhacking.com/connect-raspberry-pi-to-laptop-display/?replytocom=3108#respond)

never mind, My laptop does have one

        - ![6b16b99c5db6b1c544ed7dc10ca7db23.jpg](../_resources/c0ab18e56c9ef1f05b6ffe3d3521270c.jpg)

Leo EdwardsJune 8, 2016

[Reply](https://diyhacking.com/connect-raspberry-pi-to-laptop-display/?replytocom=3264#respond)

It took you a whole day to figure that out? More coffee my man

- ![6b16b99c5db6b1c544ed7dc10ca7db23.jpg](../_resources/c0ab18e56c9ef1f05b6ffe3d3521270c.jpg)

RatnakarApril 8, 2016

[Reply](https://diyhacking.com/connect-raspberry-pi-to-laptop-display/?replytocom=2878#respond)

Hi, Need help for setting up Raspberry Pi Model B without HDMI port on laptop. I could do step 2 but in step 3 I am not able to connect to board through Putty. Can somebody help me in this.I seeing the below result for command prompt on laptop :

C:\Users\User>ping 192.168.137.1
Pinging 192.168.137.1 with 32 bytes of data:
Reply from 192.168.137.1: bytes=32 time<1ms TTL=128
Reply from 192.168.137.1: bytes=32 time<1ms TTL=128
Reply from 192.168.137.1: bytes=32 time<1ms TTL=128
Reply from 192.168.137.1: bytes=32 timearp -a
Interface: 192.168.1.103 — 0xb
Internet Address Physical Address Type
192.168.1.1 94-fb-b2-b8-db-d0 dynamic
192.168.1.255 ff-ff-ff-ff-ff-ff static
224.0.0.22 01-00-5e-00-00-16 static
224.0.0.252 01-00-5e-00-00-fc static
239.255.255.250 01-00-5e-7f-ff-fa static
255.255.255.255 ff-ff-ff-ff-ff-ff static
Interface: 192.168.137.1 — 0xc
Internet Address Physical Address Type
192.168.137.92 b8-27-eb-e7-d8-87 dynamic
192.168.137.255 ff-ff-ff-ff-ff-ff static
224.0.0.22 01-00-5e-00-00-16 static
224.0.0.252 01-00-5e-00-00-fc static
239.255.255.250 01-00-5e-7f-ff-fa static
255.255.255.255 ff-ff-ff-ff-ff-ff static

    - ![6b16b99c5db6b1c544ed7dc10ca7db23.jpg](../_resources/c0ab18e56c9ef1f05b6ffe3d3521270c.jpg)

Afif Widiyanto MusthofaSeptember 30, 2016

[Reply](https://diyhacking.com/connect-raspberry-pi-to-laptop-display/?replytocom=3885#respond)

Your Raspberry Pi’s address is 192.168.137.92

- ![6b16b99c5db6b1c544ed7dc10ca7db23.jpg](../_resources/c0ab18e56c9ef1f05b6ffe3d3521270c.jpg)

chirag patelApril 6, 2016

[Reply](https://diyhacking.com/connect-raspberry-pi-to-laptop-display/?replytocom=2858#respond)

Hello Brother,

i want to interface ATian 3.5 Inch TFT LCD Monitor. i want some steps required for it.

- ![975738812e5e45d1e4c798bced6f7aac.jpg](../_resources/ca117b85796679a59cbaa46335964101.jpg)

BhavanaMarch 29, 2016

[Reply](https://diyhacking.com/connect-raspberry-pi-to-laptop-display/?replytocom=2788#respond)

Hello,

After going to the network and sharing centre –> properties –> sharing i’m not getting that drop down list for networking connection to change it to local area connection. Please help.

- ![6b16b99c5db6b1c544ed7dc10ca7db23.jpg](../_resources/c0ab18e56c9ef1f05b6ffe3d3521270c.jpg)

Mahesh PrasathMarch 17, 2016

[Reply](https://diyhacking.com/connect-raspberry-pi-to-laptop-display/?replytocom=2704#respond)

My raspberry pi IP 169.254.249.206 got it through (ifconfig) when I try connecting I get error “host computer refused connection”

- ![975738812e5e45d1e4c798bced6f7aac.jpg](../_resources/ca117b85796679a59cbaa46335964101.jpg)

Zainab HusainMarch 16, 2016

[Reply](https://diyhacking.com/connect-raspberry-pi-to-laptop-display/?replytocom=2696#respond)

I’m trying to set up my Raspberry Pi A+ for the first time using this method.

However, the A+ model doesn’t come with an Ethernet port so I’m using a USB to ethernet port to connect the Pi to the laptop. However, the ethernet dongle doesn’t light up like it usually does on making a connection.

So when I ping, I don’t get any replies.
Can anyone suggest anything?
PS. I’m working without a HDMI cable/monitor.

- ![6b16b99c5db6b1c544ed7dc10ca7db23.jpg](../_resources/c0ab18e56c9ef1f05b6ffe3d3521270c.jpg)

VinayFebruary 26, 2016

[Reply](https://diyhacking.com/connect-raspberry-pi-to-laptop-display/?replytocom=2543#respond)

Everything just worked fine but I’am not getting Rpi background instead blank grey screen, where if you right I get pop up menu with terminal, browser options. Is there any method to bring that proper gui?

- ![6b16b99c5db6b1c544ed7dc10ca7db23.jpg](../_resources/c0ab18e56c9ef1f05b6ffe3d3521270c.jpg)

KarthickFebruary 20, 2016

[Reply](https://diyhacking.com/connect-raspberry-pi-to-laptop-display/?replytocom=2498#respond)

hi bro…I need to display contents on display connected to Raspberry Pi..(like laptop)..the contents are coming from a link…

Like home automation Project…In that only ON/OFF commands only there…But in my idea,Any contents entered in HTML page..Need to be displayed in DISPlay..So please Guide me..How to Do it..

Thanks in Advance..

- ![6b16b99c5db6b1c544ed7dc10ca7db23.jpg](../_resources/c0ab18e56c9ef1f05b6ffe3d3521270c.jpg)

Oshan FernandoFebruary 7, 2016

[Reply](https://diyhacking.com/connect-raspberry-pi-to-laptop-display/?replytocom=2402#respond)

Great job..! It is working. Thank you.

- ![6b16b99c5db6b1c544ed7dc10ca7db23.jpg](../_resources/c0ab18e56c9ef1f05b6ffe3d3521270c.jpg)

Kaustubh AgarwalFebruary 4, 2016

[Reply](https://diyhacking.com/connect-raspberry-pi-to-laptop-display/?replytocom=2381#respond)

Whenever i try to connect my pi to putty, it says connection refused. Can you tell me how to solve this problem? I am using pi 2

    - ![975738812e5e45d1e4c798bced6f7aac.jpg](../_resources/ca117b85796679a59cbaa46335964101.jpg)

JFebruary 5, 2016

[Reply](https://diyhacking.com/connect-raspberry-pi-to-laptop-display/?replytocom=2386#respond)

This method worked really well until the IP address assigned to my laptop was no longer visible and it chose automatically choose IP address. Any ideas how to get round that?

        - ![6b16b99c5db6b1c544ed7dc10ca7db23.jpg](../_resources/c0ab18e56c9ef1f05b6ffe3d3521270c.jpg)

AbrarFebruary 21, 2016

[Reply](https://diyhacking.com/connect-raspberry-pi-to-laptop-display/?replytocom=2512#respond)

When i’m sharing my internet over LAN, It gives me error..
“An error occured while Internet connection was being enables. (null)”
What to do ? Please help.

    - ![6b16b99c5db6b1c544ed7dc10ca7db23.jpg](../_resources/c0ab18e56c9ef1f05b6ffe3d3521270c.jpg)

dalkyMarch 16, 2016

[Reply](https://diyhacking.com/connect-raspberry-pi-to-laptop-display/?replytocom=2691#respond)

I’m a bit late, but SSH is disabled by default in many raspberry pi distros. Unfortunately, this means you actually will need a monitor/keyboard to set up the pi with, which kind of defeats the purpose of that section of this tutorial (there’s no actual way to setup completely “headless”, ie, using only a laptop and no peripherals). You can find more information here:

https://www.raspberrypi.org/forums/viewtopic.php?t=5167&f=5

- ![6b16b99c5db6b1c544ed7dc10ca7db23.jpg](../_resources/c0ab18e56c9ef1f05b6ffe3d3521270c.jpg)

gautamJanuary 28, 2016

[Reply](https://diyhacking.com/connect-raspberry-pi-to-laptop-display/?replytocom=2327#respond)

in the getting the IP address of pi portion how do i stop the ping after 5 seconds.can anybody please elaborate on that part of the essay.

- ![975738812e5e45d1e4c798bced6f7aac.jpg](../_resources/ca117b85796679a59cbaa46335964101.jpg)

frankoJanuary 24, 2016

[Reply](https://diyhacking.com/connect-raspberry-pi-to-laptop-display/?replytocom=2296#respond)

I’m using the default buildroot configuration for the raspberry … I have used an ethernet cable and AngryIpScanner but couldn’t find the pi adress …. I don’t know now how to set up the adress for the pi

please help

    - ![6b16b99c5db6b1c544ed7dc10ca7db23.jpg](../_resources/c0ab18e56c9ef1f05b6ffe3d3521270c.jpg)

JoeJanuary 24, 2016

[Reply](https://diyhacking.com/connect-raspberry-pi-to-laptop-display/?replytocom=2297#respond)

To do this I plugged my pi into my hun via Ethernet and turned it on.. Then I did a network scan and it came up with it? It didn’t change when I plugged into my laptop so that might work? Or plug it into the hub then SSH it and follow some Internet instructions so it is a static ip? Then it won’t change!

- ![6b16b99c5db6b1c544ed7dc10ca7db23.jpg](../_resources/c0ab18e56c9ef1f05b6ffe3d3521270c.jpg)

saurabhJanuary 21, 2016

[Reply](https://diyhacking.com/connect-raspberry-pi-to-laptop-display/?replytocom=2263#respond)

mu web browser is not working at all what to do

- ![6b16b99c5db6b1c544ed7dc10ca7db23.jpg](../_resources/c0ab18e56c9ef1f05b6ffe3d3521270c.jpg)

hariprasadJanuary 16, 2016

[Reply](https://diyhacking.com/connect-raspberry-pi-to-laptop-display/?replytocom=2229#respond)

HI ,

Its working, but I tried to configure for “autostart”, made the directory and all but once I enter the command “gnome tightvnc.desktop” its showed “Bash: Command not found”

How can I able to make autostart of VNC server while connecting Rasbi?

- ![975738812e5e45d1e4c798bced6f7aac.jpg](../_resources/ca117b85796679a59cbaa46335964101.jpg)

AbhayaJanuary 15, 2016

[Reply](https://diyhacking.com/connect-raspberry-pi-to-laptop-display/?replytocom=2215#respond)

As i am learning Raspberry Pi, i found that we need to enable SSH in the advanced setting in raspberry pi before. I didnt found nowhere in this tutorial that SSH is enabled; as by default it is disabled in raspberry pi setting. If it isn’t enabled, can we setup the connection between putty and raspberry pi. Please make this edit, otherwise cool tutorial(Might be i am wrong). Grt job, thx Arvind.

- ![6b16b99c5db6b1c544ed7dc10ca7db23.jpg](../_resources/c0ab18e56c9ef1f05b6ffe3d3521270c.jpg)

RahulJanuary 7, 2016

[Reply](https://diyhacking.com/connect-raspberry-pi-to-laptop-display/?replytocom=2162#respond)

Hi, there i tried the all above steps as specefied in the above, i was successful complete up to step3(server side), but at the client (my laptop) when i try to connect through the vnc it is giving an error as “server refused the connection”.

Pleas some one help…
Thank you.

- ![6b16b99c5db6b1c544ed7dc10ca7db23.jpg](../_resources/c0ab18e56c9ef1f05b6ffe3d3521270c.jpg)

RajJanuary 2, 2016

[Reply](https://diyhacking.com/connect-raspberry-pi-to-laptop-display/?replytocom=2121#respond)

Hi,

Great summary. It works fine for me. One more question. How can i get Audio thru the VNC connection?

- ![6b16b99c5db6b1c544ed7dc10ca7db23.jpg](../_resources/c0ab18e56c9ef1f05b6ffe3d3521270c.jpg)

benjotitusJanuary 1, 2016

[Reply](https://diyhacking.com/connect-raspberry-pi-to-laptop-display/?replytocom=2114#respond)

could i use xming

- ![6b16b99c5db6b1c544ed7dc10ca7db23.jpg](../_resources/c0ab18e56c9ef1f05b6ffe3d3521270c.jpg)

benjotitusJanuary 1, 2016

[Reply](https://diyhacking.com/connect-raspberry-pi-to-laptop-display/?replytocom=2113#respond)

unable to connect
showing network error in putty

- ![6b16b99c5db6b1c544ed7dc10ca7db23.jpg](../_resources/c0ab18e56c9ef1f05b6ffe3d3521270c.jpg)

Jose CuevaDecember 31, 2015

[Reply](https://diyhacking.com/connect-raspberry-pi-to-laptop-display/?replytocom=2108#respond)

Hi
Your method works fine for me,

I was using Xming a time ago, it was getting slower and with screen resolution problems, i did not get a solution for this.

Using VNC seems a good and better alternative,
Actually i am using a wifi module with my raspberry.
Thank you

- ![6b16b99c5db6b1c544ed7dc10ca7db23.jpg](../_resources/c0ab18e56c9ef1f05b6ffe3d3521270c.jpg)

Rio CruzDecember 26, 2015

[Reply](https://diyhacking.com/connect-raspberry-pi-to-laptop-display/?replytocom=2071#respond)

Hi! I got the rpi 2 and installed ubuntu mate. I was able to view my pi using this tutorial, however I recently found out that each time i connect my rpi2 to my laptop ethernet the IP address changes. how will I know the pi’s IP address so I can connect via putty? Is there any way I can set-up a static ip address? It would be nice to share both internet and display to the rpi2. please help.

- ![6b16b99c5db6b1c544ed7dc10ca7db23.jpg](../_resources/c0ab18e56c9ef1f05b6ffe3d3521270c.jpg)

SultanAugust 4, 2015

[Reply](https://diyhacking.com/connect-raspberry-pi-to-laptop-display/?replytocom=1430#respond)

PUTTY shows network error: connection refused

- ![6b16b99c5db6b1c544ed7dc10ca7db23.jpg](../_resources/c0ab18e56c9ef1f05b6ffe3d3521270c.jpg)

SultanAugust 4, 2015

[Reply](https://diyhacking.com/connect-raspberry-pi-to-laptop-display/?replytocom=1429#respond)

In step 2 in Wireless network properties window there is no such field as sharing only for LAN.

How can i fix it?

- ![6b16b99c5db6b1c544ed7dc10ca7db23.jpg](../_resources/c0ab18e56c9ef1f05b6ffe3d3521270c.jpg)

priyankJuly 7, 2015

[Reply](https://diyhacking.com/connect-raspberry-pi-to-laptop-display/?replytocom=1399#respond)

Thank you dear.it helps a lot.

- ![6b16b99c5db6b1c544ed7dc10ca7db23.jpg](../_resources/c0ab18e56c9ef1f05b6ffe3d3521270c.jpg)

AJuly 4, 2015

[Reply](https://diyhacking.com/connect-raspberry-pi-to-laptop-display/?replytocom=1393#respond)

No HDMI cable any way to set it up for the first time?

- ![c261efed9dc3b2661a88de4e9e6478db.jpg](../_resources/2696c08a6598eaedab294603b0977b17.jpg)

AbhiramJune 13, 2015

[Reply](https://diyhacking.com/connect-raspberry-pi-to-laptop-display/?replytocom=1367#respond)

I have a Raspberry Pi Model B that I’m trying to connect with my Windows 7 laptop using the above steps.

I made it to Step 3 and was able to connect to the Pi through Putty.

After logging in, I tried to install tightvncserver using the following commands-

sudo apt-get update
sudo apt-get install tightvncserver

However, I got error messages for both commands. Screenshot of error messages – https://drive.google.com/file/d/0B-J9rdwFEFl_WHkyMndhNElaNkU/view?usp=sharing

    - ![6b16b99c5db6b1c544ed7dc10ca7db23.jpg](../_resources/c0ab18e56c9ef1f05b6ffe3d3521270c.jpg)

PremJune 20, 2015

[Reply](https://diyhacking.com/connect-raspberry-pi-to-laptop-display/?replytocom=1378#respond)

Hi, the error means your Pi is not getting internet connection. It is getting failed to ping the server of Raspberry Pi. Check the internet connection. How you have connected the Pi to internet?

- ![6b16b99c5db6b1c544ed7dc10ca7db23.jpg](../_resources/c0ab18e56c9ef1f05b6ffe3d3521270c.jpg)

A.SJune 7, 2015

[Reply](https://diyhacking.com/connect-raspberry-pi-to-laptop-display/?replytocom=1346#respond)

Hi

I have a raspberry pi model B,and i installed rasbian using NOOBS , hooked it to my TV and it showed the rasberry pi desktop successfully. But when i hook it to my laptop it wont show anything,are there any setting i should do? or any support software i should download?

Please help!!!!
Thnakyou.

- ![975738812e5e45d1e4c798bced6f7aac.jpg](../_resources/ca117b85796679a59cbaa46335964101.jpg)

samiApril 30, 2015

[Reply](https://diyhacking.com/connect-raspberry-pi-to-laptop-display/?replytocom=1206#respond)

Hi,

Will you be able to use the laptop normally when you unplug the raspberry or after you have plunged it in you can only use it for the raspberry???????

    - ![3eba72d6437805760c3c9c2c70e10adb.jpg](../_resources/c1212a78cda067af6b1ab47b545638c0.jpg)

Arvind SanjeevMay 2, 2015

[Reply](https://diyhacking.com/connect-raspberry-pi-to-laptop-display/?replytocom=1207#respond)

Yes, you can use the raspberry pi and the laptop simultaneously. On the laptop, there will be a window through which we access the raspberry pi.

- ![6b16b99c5db6b1c544ed7dc10ca7db23.jpg](../_resources/c0ab18e56c9ef1f05b6ffe3d3521270c.jpg)

ShivamApril 25, 2015

[Reply](https://diyhacking.com/connect-raspberry-pi-to-laptop-display/?replytocom=1204#respond)

Thanks a lot Sohil! Seamless tutorial and worked on the first try.

- ![6b16b99c5db6b1c544ed7dc10ca7db23.jpg](../_resources/c0ab18e56c9ef1f05b6ffe3d3521270c.jpg)

keerthana pApril 23, 2015

[Reply](https://diyhacking.com/connect-raspberry-pi-to-laptop-display/?replytocom=1203#respond)

can i use a idea net setter as an Ethernet cable?

    - ![3eba72d6437805760c3c9c2c70e10adb.jpg](../_resources/c1212a78cda067af6b1ab47b545638c0.jpg)

Arvind SanjeevApril 26, 2015

[Reply](https://diyhacking.com/connect-raspberry-pi-to-laptop-display/?replytocom=1205#respond)

This should help you: https://shkspr.mobi/blog/2012/07/3g-internet-on-raspberry-pi-success/

- ![6b16b99c5db6b1c544ed7dc10ca7db23.jpg](../_resources/c0ab18e56c9ef1f05b6ffe3d3521270c.jpg)

WoodlandApril 22, 2015

[Reply](https://diyhacking.com/connect-raspberry-pi-to-laptop-display/?replytocom=1201#respond)

Well written blog, Nice layout and interesting to read. Good luck.
My question:

Your blog says “Keyboard and mouse” are optional, and step 1 says “connect the Keyboard and Mouse”.

How do I go about – “without” using keyboard and a mouse to begin with. I am a beginner.

    - ![3eba72d6437805760c3c9c2c70e10adb.jpg](../_resources/c1212a78cda067af6b1ab47b545638c0.jpg)

Arvind SanjeevApril 22, 2015

[Reply](https://diyhacking.com/connect-raspberry-pi-to-laptop-display/?replytocom=1202#respond)

Initial setup would require using the keyboard and mouse.

- ![6b16b99c5db6b1c544ed7dc10ca7db23.jpg](../_resources/c0ab18e56c9ef1f05b6ffe3d3521270c.jpg)

gouriApril 11, 2015

[Reply](https://diyhacking.com/connect-raspberry-pi-to-laptop-display/?replytocom=1196#respond)

how can i share my laps wifi to pi with putty and xming …. i used this to connect to my pi and lap…bt not able to share internet

    - ![3eba72d6437805760c3c9c2c70e10adb.jpg](../_resources/c1212a78cda067af6b1ab47b545638c0.jpg)

Arvind SanjeevApril 19, 2015

[Reply](https://diyhacking.com/connect-raspberry-pi-to-laptop-display/?replytocom=1199#respond)

Hi Gouri,

If your lap has wifi, then this method would definitely share internet with the pi too.

- ![6b16b99c5db6b1c544ed7dc10ca7db23.jpg](../_resources/c0ab18e56c9ef1f05b6ffe3d3521270c.jpg)

OBHApril 2, 2015

[Reply](https://diyhacking.com/connect-raspberry-pi-to-laptop-display/?replytocom=1193#respond)

I could not find the raspberry pi IP address, I had to found out from the raspberry using the display by typing : hostname -I on the LX Terminal.

    - ![3eba72d6437805760c3c9c2c70e10adb.jpg](../_resources/c1212a78cda067af6b1ab47b545638c0.jpg)

Arvind SanjeevApril 4, 2015

[Reply](https://diyhacking.com/connect-raspberry-pi-to-laptop-display/?replytocom=1194#respond)

Use the command: ifconfig

    - ![6b16b99c5db6b1c544ed7dc10ca7db23.jpg](../_resources/c0ab18e56c9ef1f05b6ffe3d3521270c.jpg)

hariFebruary 4, 2016

[Reply](https://diyhacking.com/connect-raspberry-pi-to-laptop-display/?replytocom=2378#respond)

use command “ipconfig”

- ![975738812e5e45d1e4c798bced6f7aac.jpg](../_resources/ca117b85796679a59cbaa46335964101.jpg)

lethaianMarch 17, 2015

[Reply](https://diyhacking.com/connect-raspberry-pi-to-laptop-display/?replytocom=1191#respond)

I have stuck in the step 4 but finally i got a solution. You just have simply type “ifconfig” in raspberry to see its IP and then type it to the VNC. It should work ! (sorry for my bad English)

- ![6b16b99c5db6b1c544ed7dc10ca7db23.jpg](../_resources/c0ab18e56c9ef1f05b6ffe3d3521270c.jpg)

rashiMarch 14, 2015

[Reply](https://diyhacking.com/connect-raspberry-pi-to-laptop-display/?replytocom=1190#respond)

Open command prompt.
Ping on broadcast address of your IP. (Type) Eg: ping 192.168.137.255

when i ping 192.168.137.1, it works fine; but any other address such as 192.168.137.255 do not work and say “request timed out”.

- ![975738812e5e45d1e4c798bced6f7aac.jpg](../_resources/ca117b85796679a59cbaa46335964101.jpg)

deependraFebruary 26, 2015

[Reply](https://diyhacking.com/connect-raspberry-pi-to-laptop-display/?replytocom=1189#respond)

How to change network connection to LAN .Tried lot of YouTube. Tutorials but still have a

problem

- ![163ef6fccbc5ecef165334784b9394f3.jpg](../_resources/74f32735e9be7de76e7b8d369e797383.jpg)

Tushar ThakurFebruary 26, 2015

[Reply](https://diyhacking.com/connect-raspberry-pi-to-laptop-display/?replytocom=1188#respond)

Why don’t you use simple Remote Desktop client? Windows inbuilt and also having Android app. Very handy. No need of that VNC client.

    - ![6b16b99c5db6b1c544ed7dc10ca7db23.jpg](../_resources/c0ab18e56c9ef1f05b6ffe3d3521270c.jpg)

JeffMarch 22, 2015

[Reply](https://diyhacking.com/connect-raspberry-pi-to-laptop-display/?replytocom=1192#respond)

Agreed.
simple to install and much easier to use:
`sudo apt-get install xrdp`

        - ![542517e5cb2bbd7ac2ebdadb04e83d2f.png](../_resources/1a5efab002d6e7cd0d44f12d6ae9739b.png)

Robert SchleyApril 11, 2015

[Reply](https://diyhacking.com/connect-raspberry-pi-to-laptop-display/?replytocom=1197#respond)

Awesome. Thanks! I was able to set this up using the xrdp. It looks like the xrdp uses the tightvnc libraries anyway but is simpler.

To add to this, I was able to not have to find the the ip address by just putting the name of the device ‘raspberrypi’ into the rdp connection detail window from my windows laptop.

Even if you do need to find the IP, I recommend “angry IP scanner”.
thanks again.

            - ![3eba72d6437805760c3c9c2c70e10adb.jpg](../_resources/c1212a78cda067af6b1ab47b545638c0.jpg)

Arvind SanjeevApril 19, 2015

[Reply](https://diyhacking.com/connect-raspberry-pi-to-laptop-display/?replytocom=1200#respond)

Thanks for the cool feedback Robert :)

                - ![6b16b99c5db6b1c544ed7dc10ca7db23.jpg](../_resources/c0ab18e56c9ef1f05b6ffe3d3521270c.jpg)

AbhijeetDecember 19, 2015

[Reply](https://diyhacking.com/connect-raspberry-pi-to-laptop-display/?replytocom=2019#respond)

Thanks Robert.I was going through the blog, things were not working for me, I came across this comment so I downloaded ‘Angry IP Scanner’ connected r-pi to my lapi found its IP and directly copied it to ‘Putty.exe’ and it worked!! No vcu or any initialization required as mentioned. Thanks People!!!

- ![6b16b99c5db6b1c544ed7dc10ca7db23.jpg](../_resources/c0ab18e56c9ef1f05b6ffe3d3521270c.jpg)

Anand KrishnanFebruary 26, 2015

[Reply](https://diyhacking.com/connect-raspberry-pi-to-laptop-display/?replytocom=1187#respond)

When i tried to connect internet via ethernet cable to Pi.The browser showed couldn’t locate host.The orange and green indication is on in LAN port of pi.When i tried same connection in Laptop it worked fine.But host error is showing in Pi.What is the problem ?

pingbacks / trackbacks

- **[PI display on PC](https://allaharsha.wordpress.com/2017/02/08/pi-display-on-pc/)**

[…] Laptop to PI using network: Raspberry PI to laptop using Ethernet cable […]
February 8th, 2017 07:28 AM

- **[How To Connect Pocket Pc To Laptop | Information](http://davai27.trustourworld.info/2017/02/03/how-to-connect-pocket-pc-to-laptop/)**

[…] The Best way to Connect Raspberry Pi to Laptop display – Before moving to connect raspberry pi to laptop display, you need an SD card having the OS preinstalled. You will find lots of blogs and tutorials about preparing an … […]

February 3rd, 2017 10:56 AM

- **[How To Connect A Desktop To A Laptop Via Usb | Information](http://davai27.trustourworld.info/2017/01/30/how-to-connect-a-desktop-to-a-laptop-via-usb/)**

[…] The Best way to Connect Raspberry Pi to Laptop display – To connect raspberry pi to laptop display, you can simply use an ethernet cable. The desktop GUI (Graphical User Interface) of the raspberry pi can be viewed through … […]

January 31st, 2017 04:49 AM

- **[Boot Your Raspberry Pi | DIY SPACE](http://diyspacepk.com/2016/07/04/boot-your-raspberry-pi/)**

[…] will work. Use an HDMI video cable to connect an LCD with your Raspberry pi, or you can use the network cable method as well. Connect keyboard and mouse on the USB ports available on the Raspberry pi and you are […]

December 24th, 2016 02:19 AM

- **[Setting up of pi | Jyotendra's Blog](http://jyotendrasharma.in/?p=304)**

[…] Wifi connectivity came then. I also wanted to work on Raspberry pi using my own laptop. I was following this Guide. […]

September 5th, 2016 05:37 PM

- **[BUILD RASPBERRY PI ROBOTS: BEST TUTORIAL FOR BEGINNERS – RaspBerry Pi, Arduino, Internet Of Think (IOT)](http://yoursmart.mobi/raspberry/build-raspberry-pi-robots-best-tutorial-for-beginners)**

[…] it. You can either extend the display of your laptop via VNC server and a LAN cable by using this tutorial. Or use SSH to connect remotely to your pi from the terminal wirelessly using this tutorial. And […]

May 19th, 2016 01:34 AM

- **[Setting up of pi | My Projects](https://jyotendrasharmaprojects.wordpress.com/2016/03/16/setting-up-of-pi/)**

[…] Wifi connectivity came then. I also wanted to work on Raspberry pi using my own laptop. I was following this Guide. […]

March 29th, 2016 03:34 PM

- **[Running Raspberry Pi For The First Time – Using Laptop’s Display, Keyboard & Touchpad (no HDMI cable requird) | mypynotes](https://mypynotes.wordpress.com/2015/07/04/running-raspberry-pi-for-the-first-time-using-laptop-dsiplay-keyboard-touchpad-no-hdmi-cable/)**

[…] for running Rpi’s GUI on laptop see this tutorial from step 3: http://diyhacking.com/connect-raspberry-pi-to-laptop-display/ (many thanks to the author) . This tutorial tells about windows but after if you followed my […]

January 2nd, 2016 11:01 PM

- **[Raspberry Pi GPIO control: Best tutorial for beginners](http://diyhacking.com/raspberry-pi-gpio-control/)**

[…] extend the display of your laptop to the raspberry pi via VNC server and a LAN cable by using this tutorial. You can see this sensor in action, in the video […]

April 12th, 2015 05:03 AM

- **[Raspberry Pi robots for Beginners: Best Tutorial](http://diyhacking.com/raspberry-pi-obstacle-avoiding-robot/)**

[…] it. You can either extend the display of your laptop via VNC server and a LAN cable by using this tutorial. Or use SSH to connect remotely to your pi from the terminal wirelessly using this tutorial. And […]

April 10th, 2015 02:58 PM

###

Leave a Comment

Math Captcha
24 + = 25