Learn X in Y Minutes: Scenic Programming Language Tours

   [Share this page](https://twitter.com/intent/tweet?url=https%3A%2F%2Flearnxinyminutes.com%2Fdocs%2Fshutit%2F&text=Learn+X+in+Y+minutes%2C+where+X%3DShutIt)

# [Learn X in Y minutes](https://learnxinyminutes.com/)

## Where X=ShutIt

Get the code: [learnshutit.html](https://learnxinyminutes.com/docs/files/learnshutit.html)

## ShutIt

ShutIt is an shell automation framework designed to be easy to use.
It is a wrapper around a python-based expect clone (pexpect).
You can look at it as ‘expect without the pain’.
It is available as a pip install.

## Hello World

Starting with the simplest example. Create a file called example.py:

import  shutitsession  =  shutit.create_session('bash')session.send('echo Hello World',  echo=True)

Running this with:
python example.py
outputs:
python example.pyecho  "Hello World"echo  "Hello World"Hello World
Ians-MacBook-Air.local:ORIGIN_ENV:RhuebR2T#

The first argument to ‘send’ is the command you want to run. The ‘echo’ argument outputs the terminal interactions. By default ShutIt is silent.

‘send’ takes care of all the messing around with prompts and ‘expects’ that you might be familiar with from expect.

## Log Into a Server

Let’s say you want to log into a server and run a command. Change example.py to:

import  shutitsession  =  shutit.create_session('bash')session.login('ssh you@example.com',  user='you',  password='mypassword')session.send('hostname',  echo=True)session.logout()

which will log you into your server (if you replace with your details) and output the hostname.

hostnamehostnameexample.comexample.com:cgoIsdVv:heDa77HB#
Obviously that’s insecure! Instead you can run:

import  shutitsession  =  shutit.create_session('bash')password  =  session.get_input('',  ispass=True)session.login('ssh you@example.com',  user='you',  password=password)session.send('hostname',  echo=True)session.logout()

which forces you to input the password:
Input  Secret:hostnamehostnameexample.comexample.com:cgoIsdVv:heDa77HB#

Again, the ‘login’ method handles the changing prompt from a login. You give ShutIt the login command, the user you expect to log in as, and a password (if needed), and ShutIt takes care of the rest.

‘logout’ handles the ending of a ‘login’, handling any changes to the prompt for you.

## Log Into Multiple Servers

Let’s say you have a server farm of two servers, and want to log onto both. Just create two sessions and run similar login and send commands:

import  shutitsession1  =  shutit.create_session('bash')session2  =  shutit.create_session('bash')password1  =  session1.get_input('Password for server1',  ispass=True)password2  =  session2.get_input('Password for server2',  ispass=True)session1.login('ssh you@one.example.com',  user='you',  password=password1)session2.login('ssh you@two.example.com',  user='you',  password=password2)session1.send('hostname',  echo=True)session2.send('hostname',  echo=True)session1.logout()session2.logout()

would output:
$ python example.py
Password for server1
Input Secret:
Password for server2
Input Secret:
hostname
hostname
one.example.com
one.example.com:Fnh2pyFj:qkrsmUNs# hostname
hostname
two.example.com
two.example.com:Gl2lldEo:D3FavQjA#

## Example: Monitor Multiple Servers

We can turn the above into a simple monitoring tool by adding some logic to examine the output of a command:

import  shutitcapacity_command="""df / | awk '{print $5}' | tail -1 | sed s/[^0-9]//"""session1  =  shutit.create_session('bash')session2  =  shutit.create_session('bash')password1  =  session.get_input('Password for server1',  ispass=True)password2  =  session.get_input('Password for server2',  ispass=True)session1.login('ssh you@one.example.com',  user='you',  password=password1)session2.login('ssh you@two.example.com',  user='you',  password=password2)capacity  =  session1.send_and_get_output(capacity_command)if  int(capacity)  <  10:  print('RUNNING OUT OF SPACE ON server1!')capacity  =  session2.send_and_get_output(capacity_command)if  int(capacity)  <  10:  print('RUNNING OUT OF SPACE ON server2!')session1.logout()session2.logout()

Here you use the ‘send*and*get_output’ method to retrieve the output of the capacity command (df).

There are much more elegant ways to do the above (eg have a dictionary of the servers to iterate over), but it’s up to you how clever you need the python to be.

## More Intricate IO - Expecting

Let’s say you have an interaction with an interactive command line application you want to automate. Here we will use telnet as a trivial example:

import  shutitsession  =  shutit.create_session('bash')session.send('telnet',  expect='elnet>',  echo=True)session.send('open google.com 80',  expect='scape character',  echo=True)session.send('GET /',  echo=True,  check_exit=False)session.logout()

Note the ‘expect’ argument. You only need to give a subset of telnet’s prompt to match and continue.

Note also the ‘check_exit’ argument in the above, which is new. We’ll come back to that. The output of the above is:

$ python example.py
telnet
telnet> open google.com 80
Trying 216.58.214.14...
Connected to google.com.
Escape character is '^]'.
GET /
HTTP/1.0 302 Found
Cache-Control: private
Content-Type: text/html;  charset=UTF-8
Referrer-Policy: no-referrer
Location: http://www.google.co.uk/?gfe_rd=cr&ei=huczWcj3GfTW8gfq0paQDA
Content-Length: 261
Date: Sun, 04 Jun 2017 10:57:10 GMT
<HTML><HEAD><meta http-equiv="content-type"  content="text/html;charset=utf-8">
<TITLE>302 Moved</TITLE></HEAD><BODY>
<H1>302 Moved</H1>
The document has moved
<A HREF="http://www.google.co.uk/?gfe_rd=cr&amp;ei=huczWcj3GfTW8gfq0paQDA">
here
</A>.
</BODY></HTML>
Connection closed by foreign host.

Now back to ‘check*exit=False’. Since the telnet command returns a failure exit code (1) and we don’t want the script to fail, you set ‘check*exit=False’ to let ShutIt know you don’t care about the exit code.

If you didn’t pass that argument in, ShutIt gives you an interactive terminal if there is a terminal to communicate with. This is called a ‘pause point’.

## Pause Points

You can trigger a ‘pause point’ at any point by calling
[...]session.pause_point('This is a pause point')[...]

within your script, and then continue with the script by hitting CTRL and ‘]’ at the same time. This is great for debugging: add a pause point, have a look around, then continue. Try this:

import  shutitsession  =  shutit.create_session('bash')session.pause_point('Have a look around!')session.send('echo "Did you enjoy your pause point?"',  echo=True)

with output like this:
$ python example.py
Have a look around!
Ians-Air.home:ORIGIN_ENV:I00LA1Mq# bash

imiell@Ians-Air:/space/git/shutit ⑂ master +  CTRL-] caught, continuing with run...

2017-06-05 15:12:33,577 INFO: Sending: exit2017-06-05 15:12:33,633 INFO: Output (squashed): exitexitIans-Air.home:ORIGIN_ENV:I00LA1Mq# [...]echo  "Did you enjoy your pause point?"echo  "Did you enjoy your pause point?"Did you enjoy your pause point?

Ians-Air.home:ORIGIN_ENV:I00LA1Mq#

## More Intricate IO - Backgrounding

Returning to our ‘monitoring multiple servers’ example, let’s imagine we have a long-running task that we want to run on each server. By default, ShutIt works serially which would take a long time. But we can run tasks in the background to speed things up.

Here you can try an example with the trivial command: ‘sleep 60’.

import  shutitimport  timelong_command="""sleep 60"""session1  =  shutit.create_session('bash')session2  =  shutit.create_session('bash')password1  =  session1.get_input('Password for server1',  ispass=True)password2  =  session2.get_input('Password for server2',  ispass=True)session1.login('ssh you@one.example.com',  user='you',  password=password1)session2.login('ssh you@two.example.com',  user='you',  password=password2)start  =  time.time()session1.send(long_command,  background=True)session2.send(long_command,  background=True)print('That took: '  +  str(time.time()  -  start)  +  ' seconds to fire')session1.wait()session2.wait()print('That took: '  +  str(time.time()  -  start)  +  ' seconds to complete')

My laptop says it took 0.5 seconds to run fire those two commands, and then just over a minute to complete (using the ‘wait’ method).

Again, this is trivial, but imagine you have hundreds of servers to manage like this and you can see the power it can bring in a few lines of code and one python import.

## Learn More

There’s a lot more that can be done with ShutIt.
To learn more, see:

[ShutIt](https://ianmiell.github.io/shutit/)[GitHub](https://github.com/ianmiell/shutit/blob/master/README.md)

It’s a broader automation framework, and the above is its ‘standalone mode’.

Feedback, feature requests, ‘how do I?’s highly appreciated! Reach me at[@ianmiell](https://twitter.com/ianmiell)

* * *

Got a suggestion? A correction, perhaps? [Open an Issue](https://github.com/adambard/learnxinyminutes-docs/issues/new) on the Github Repo, or make a pull request yourself!

Originally contributed by Ian Miell, and updated by [1 contributor(s)](https://github.com/adambard/learnxinyminutes-docs/blame/master/shutit.html.markdown).

 [![Creative Commons License](../_resources/2780aefe6b14e22f37855df2a05bb47b.png)](https://creativecommons.org/licenses/by-sa/3.0/deed.en_US)

© 2017 [Ian Miell](http://ian.meirionconsulting.tk/)