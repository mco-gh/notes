Visual Studio Code editing GCE files – Daz Wilkin – Medium

# Visual Studio Code editing GCE files

Like many, I’m mostly completely converted to [Visual Studio Code](https://code.visualstudio.com/) and [Google Cloud Platform](https://cloud.google.com/) (full disclosure: Googler). Until today, I suffered through nano (very occasionally vi) when editing files on Google Compute Engine (GCE) instances.

#### rmate

Another editor — Textmate — has a feature called ‘rmate’ that enables remote editing by leveraging an ssh tunnel to the remote machine. Rafael Maiolla developed an [extension](https://marketplace.visualstudio.com/items?itemName=rafaelmaiolla.remote-vscode) that brings this experience to Visual Studio Code. Thanks, Rafael!

This post explains how to use this extension to remotely edit files on GCE instances.

#### Local machine

You will need Visual Studio Code, ruby, rmate and Rafael’s [remote-vscode](https://marketplace.visualstudio.com/items?itemName=rafaelmaiolla.remote-vscode) extension. I’m running a Linux (Ubuntu) workstation, ymmv. Restart Visual Studio Code. Open “settings” (CTRL-,) and search for “remote.”. I left the settings at their defaults:

![1*bxWMKYvUM4aAZw74HC-Iow.png](../_resources/89977a95fc9f47b04b07f89339424baf.png)
![1*bxWMKYvUM4aAZw74HC-Iow.png](../_resources/7b13c3c82a7b02b7e8e7e986ca203c18.png)
Visual Studio Code settings: “Remove VSCode configuration”

Then press “F1” to open Visual Studio Code’s Command Palette and find “Remote: Start Server”, click it. You should see (briefly) “starting server” (perhaps “restarting server”) in the bottom left hand corner of Visual Studio Code’s screen. Code is ready.

![1*KJFa-yUeDgNh8Exh5fX-8g.png](../_resources/16a42c21ee77b604f9ba04fe7a0547fc.png)
![1*KJFa-yUeDgNh8Exh5fX-8g.png](../_resources/8f5e629b88c8745d42bed958c8fefdd7.png)

We’ll now set up a secure reverse (remote machine is the client) tunnel between your local machine and a remote GCE instance. To do this, you will, of course, need to have a remote GCE instance. I’ll assume you’ve done that and you have a machine called ‘my-gce-instance’.

You should replace the $VARIABLES in the following command but use something similar to:

INSTANCE="my-gce-instance"
gcloud compute ssh $INSTANCE \
--ssh-flag="-R 52698:localhost:52698" \
--project=$PROJECT \
--zone=$ZONE

#### Remote (GCE) machine

All being well, you should find yourself logged in to a secure session on ‘my-gce-instance’.

You must install rmate on the GCE instance before you can use it. I’m running Ubuntu on the GCE instance and the commands I used are:

sudo apt update && \
sudo apt -y install ruby \
&& sudo gem install rmate

When you wish to use Visual Studio Code (on your local machine) to edit a file (on the GCE instance), run this command on the GCE instance:

rmate /path/to/my-file
For example, to edit index.html in /www, you would type:
rmate /www/index.html
Don’t be disappointed when it appears nothing has happened…
Something useful has happened!

**NB**: You must maintain the ssh session while you are editing. You may issue multiple ‘rmate’ commands, one for each file you wish to edit.

#### Local machine

Return to Visual Studio Code and you should see that the remote file has been opened!

![1*J77UYzzMzilgDqV223ADsw.png](../_resources/4f77a605f62e711138253847dd463347.png)
![1*J77UYzzMzilgDqV223ADsw.png](../_resources/a5d7eb660c8b9f5efd0faec768c242a6.png)
Visual Studio Code remotely editing GCE-hosted files

When you close each file, the associated (remote) rmate process will be terminated. When you’re done editing, you should exit the ssh session.