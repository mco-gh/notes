Animating URLs with Javascript and Emojis

# Animating URLs with Javascript and Emojis

#### by [Matthew Rayfield](http://matthewrayfield.com/) on January 17th 2019

You can use emoji (and other graphical unicode characters) in URLs. And wow is it great. But no one seems to do it. Why? Perhaps emoji are too exotic for normie web platforms to handle? Or maybe they are avoided for fear of angering the SEO gods?

Whatever the reason, the overlapping portion on the Venn diagram of "It's Possible v.s. No One Is Doing It" is where my excitement usually lies. So I decided to put a little time into the possibilities of graphical characters in URLs. Specifically, with the possibility for animating these characters by way of some Javascript.

## Loopin'

First off, make sure your page's Javascript code is being labelled as UTF-8 or you're gonna have a bad time putting emoji in your code at all. This can be accomplished via an HTTP header, or page META tag. There's a good chance you don't have to worry about this. But you can find more info about this here: [Unicode in Javascript by Flavio](https://flaviocopes.com/javascript-unicode/)

To achieve our desired outcome of emoji dancing like sugar plum fairies in our address bar, we need a loop. And really, all we need is a loop. We start the loop, it loops, and we're happy. So here's our first loop, a spinning emoji moon. I think when they added this sequence of emoji they must have had this in mind right?

![moon.gif](../_resources/5da41b730f4db178fe0a835ea7fc3c3f.gif)

var f = ['', '', '', '', '', '', '', ''];
function loop() {
location.hash = f[Math.floor((Date.now()/100)%f.length)];
setTimeout(loop, 50);
}
loop();

Run Moon Code:

You can click the toggle checkbox above to see the result of this loop in your URL bar.

If you don't like the spinning moons you can swap out that array with whatever emojis you want. Like a clock:

![clock.gif](../_resources/66d209f137acc2b7140b103a9eb1871a.gif)

var f = ['','','','','','','','','','','',''];

Run Clock Code:

This is a real simple example. Too simple really. So let's upgrade our loop so that it generates a string of multiple emoji! This time we're utilizing the emoji "skin tone modifiers" characters to make some color-changing babies:

![babies2.gif](../_resources/fe3d62547575d0335ae79d210662e674.gif)

var e = ['', '', '', '', ''];
function loop() {
var s = '',
i, m;
for (i = 0; i < 10; i ++) {
m = Math.floor(e.length * ((Math.sin((Date.now()/100) + i)+1)/2));
s += '' + e[m];
}
location.hash = s;
setTimeout(loop, 50);
}
loop();

Run Babies Code:

We use a sine wave controlled by time and position to select which color we want. This gives us a nice loopy color changing effect!

Or how about we revisit our moon spinner, spread it out, and make something resembling a loading indicator? Sure, let's do it:

![moons.gif](../_resources/58e51134fbb68edeaff0c23ea0e147f2.gif)

var f = ['', '', '', '', '', '', '', ''],
d = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
m = 0;
function loop() {
var s = '', x = 0;
if (!m) {
while (d[x] == 4) {
x ++;
}
if (x >= d.length) m = 1;
else {
d[x] ++;
}
}
else {
while (d[x] == 0) {
x ++;
}
if (x >= d.length) m = 0;
else {
d[x] ++;
if (d[x] == 8) d[x] = 0;
}
}
d.forEach(function (n) {
s += f[n];
});
location.hash = s;
setTimeout(loop, 50);
}
loop();

Run Multi-Moon Code:

## Exploring Other Characters

But it's not just emoji that give us a means to pump graphics out of our URL bar. There's a whole boatload of unicode characters of interest to our goals.

Particularly interesting are the [Box-drawing Characters](https://en.wikipedia.org/wiki/Box-drawing_character):

![](../_resources/8c2802a0ee2515416fd7090eaec3ad90.png)

Many of these lend themselves better to a two dimensional output. But they're still pretty good on the single line we have to play with. For instance we can make a string of multiple height varied block characters and construct a nice little wave:

![wavy.gif](../_resources/f9c873296653c055bc950c23edb59ae9.gif)

function loop() {
var i, n, s = '';
for (i = 0; i < 10; i++) {
n = Math.floor(Math.sin((Date.now()/200) + (i/2)) * 4) + 4;
s += String.fromCharCode(0x2581 + n);
}
window.location.hash = s;
setTimeout(loop, 50);
}
loop();

Run Wavy Code:

I liked this look so much I put it up permanently at [wavyurl.com](http://wavyurl.com/).

Using the variable width characters we can even wiggle on the horizontal, creating something like a progress bar:

![progress.gif](../_resources/73673d9535120e7a2681d844b62c1330.gif)

function loop() {
var s = '',
p;
p = Math.floor(((Math.sin(Date.now()/300)+1)/2) * 100);
while (p >= 8) {
s += '█';
p -= 8;
}
s += ['⠀','▏','▎','▍','▌','▋','▊','▉'][p];
location.hash = s;
setTimeout(loop, 50);
}

Run Progress Bar Code:

A progress bar huh? That's like, almost useful. Which brings me to...

## Displaying Video Progress In The URL Bar

In an attempt to reduce the frivolity in our little experiment, I came up with the idea to show a web video's progress in the URL. I simply attach a function that renders our progress string to the "timeupdate" event for a video, and voila! A video progress indicator in the URL, complete with the time and duration!

![video-progress.gif](../_resources/dd1c496dc1423e264fd70b65097c57c6.gif)

var video;
function formatTime(seconds) {
var minutes = Math.floor(seconds/60),
seconds = Math.floor(seconds - (minutes*60));
return ('0'+minutes).substr(-2) + ':' + ('0'+seconds).substr(-2);
}
function renderProgressBar() {
var s = '',
l = 15,
p = Math.floor(video.currentTime / video.duration * (l-1)),
i;
for (i = 0; i < l; i ++) {
if (i == p) s +='◯';
else if (i < p) s += '─';
else s += '┄';
}

location.hash = '╭'+s+'╮'+formatTime(video.currentTime)+'╱'+formatTime(video.duration);

}
video = document.getElementById('video');
video.addEventListener('timeupdate', renderProgressBar);

Run Video Progress Bar Code:

With the above checkbox checked, you can use the video below to try it out.

I rather like this lines and circle progress bar, but if you fancy some moon emoji, I've got you covered:

![video-moons.gif](../_resources/81090b0aa160a243b7b0d98ad770d5de.gif)

var e = ['', '', '', '', ''],
video;
function formatTime(seconds) {
var minutes = Math.floor(seconds/60),
seconds = Math.floor(seconds - (minutes*60));
return ('0'+minutes).substr(-2) + ':' + ('0'+seconds).substr(-2);
}
function renderProgressBar() {
var s = '',
c = 0,
l = 10,
p = Math.floor(video.currentTime / video.duration * ((l*5)-1)),
i;
while (p >= 5) {
s += e[4];
c ++;
p -= 5;
}
s += e[p];
c ++;
while (c < l) {
s += e[0];
c ++;
}
location.hash = s+formatTime(video.currentTime)+'╱'+formatTime(video.duration);
}
video = document.getElementById('video');
video.addEventListener('timeupdate', renderProgressBar);

Run Video Moons Progress Bar Code:

Okay, calling this progress bar "useful" is a stretch. But if I squint, I can almost see a scenario where it would be useful to have this in a video sharing URL. Like YouTube has the option of creating a link to a video at a specific time. Might it not be cool to include a visual indication? Hmmm?

Maybe there is some more useful implementation of this "technology" that I haven't come up with. I'll keep thinking on that. And hey, maybe you can come up with something?

## One Last Thing

You may be wondering why I used "location.hash =" instead of the newer and shinier HTML5 History API. Two reasons. One solvable. The other less so. Both inconvenient.

Issue 1 is also a feature of the History API: It actually changes the whole URL path, not just the hash. So if I use the History API and change our page to "/", it'll look nicer than having tacked on a #. But it also means my web server must be able to response to "/", or the user will be out of luck if they refresh, or otherwise navigate to the modified URL. This is doable, but trickier than using "location.hash =" which doesn't require me to prepare the server in any special way.

Issue 2 is more unexpected. Turns out that in 2 out of 3 browsers I tested, the History API is throttled. If I push my wavy URL characters to the address bar at a fast rate I'll eventually get the following error in Chrome:

Throttling history state changes to prevent the browser from hanging.

Safari is nice enough to give us a bit more info:

SecurityError: Attempt to use history.pushState() more than 100 times per 30.000000 seconds

Now if I stay under that limit I'm fine. But c'mon, 3 frames a second just doesn't cut it for the ooey gooey URL animations I desire.

Good boy Firefox on the other hand doesn't seem to give a hoot how many times I push a new history or how quickly. Which is gosh darn thoughtful of it. But breaking in two major browsers, plus neccesitating the web server configuration to fix Issue 1, makes me willing to put up with a little # in the URL.

## The End ?

I'll leave it there. But I will tell ya that I've got a few ideas for making tiny games that display in the URL bar. Especially given the [Braille Characters](https://en.wikipedia.org/wiki/Braille_Patterns) that we have yet to explore. So stay tuned for that.

If you have questions, comments, or simply want to keep up with my latest tinkerings, check me out on Twitter: [@MatthewRayfield](http://twitter.com/MatthewRayfield). Or subscribe to my almost-never-bothered email list [here](https://matthewrayfield.us14.list-manage.com/subscribe?u=79fb3e3e1b6ad587be0a01fc9&id=10494371c3).

Oh and if you want the source for these URL mutilating abominations wrapped up in nice little ready-to-run HTML files, [here](http://matthewrayfield.com/articles/animating-urls-with-javascript-and-emojis/animated-urls-source-code.zip) you go ;]

Bye for now!

 [back to articles](http://matthewrayfield.com/articles)

 [back to home](http://matthewrayfield.com/)