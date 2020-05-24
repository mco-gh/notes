fresh block - Bl.ock Builder

[(L)](http://blockbuilder.org/)
[(L)](http://blockbuilder.org/about)
[(L)](http://blockbuilder.org/search)

[login]()
New
Save

start coding

# Bl.ock Builder

Quickly create, edit and fork d3.js examples

Are you learning d3 or trying out new ideas? Bl.ock Builder is an in-browser code editor built for creating and sharing d3.js examples. Check out this short video for an overview of how it works!

## Create and Edit

If you login with GitHub, all of your examples will save to GitHub gists associated with your account. Everything is powered by URL, so when you create a new block in Bl.ock Builder your URL will change to something like

[http://blockbuilder.org/enjalot/64dbd9b7b740ba44462f](http://blockbuilder.org/enjalot/64dbd9b7b740ba44462f)

Which means your code is saved here:

[http://gist.github.com/enjalot/64dbd9b7b740ba44462f](http://gist.github.com/enjalot/64dbd9b7b740ba44462f)

And you can view the example on bl.ocks.org like

[http://bl.ocks.org/enjalot/64dbd9b7b740ba44462f](http://bl.ocks.org/enjalot/64dbd9b7b740ba44462f)

This means you can quickly come back and edit code you wrote earlier. All you need is the URL of one of your blocks!

## Fork

There is no need to start from a blank slate, find a block you like [here](http://bl.ocks.org/enjalot/raw/211bd42857358a60a936/):

[![](../_resources/4636b4e8e421f15639a8165a3ec60bdd.jpg)](http://bl.ocks.org/enjalot/raw/211bd42857358a60a936/)

Just change the URL of your favorite block from bl.ocks.org to blockbuilder.org and start hacking!

### Bookmarklet

It can get annoying to edit the URL all the time. If you drag this link: [Bl.ock Builder](#) into your bookmark bar and click it while on a gist or block it will take you to blockbuilder.org!

### How it works

Read more here about [how Bl.ock Builder works](https://github.com/enjalot/blockbuilder/wiki/How-it-works). It is [open source software](https://github.com/enjalot/blockbuilder), so checkout the [issues](https://github.com/enjalot/blockbuilder/issues) or catch us in [our chat room](https://gitter.im/enjalot/blockbuilder).

### Try it out

Some things are best experienced, so go ahead:get started!

[index.html]()
[README.md]()
[➕]()
[⋯ (1)]()

​x

1
<!DOCTYPE html>
2
<head>
3
 <meta  charset=*"utf-8"*>
4
 <script  src=*"https://d3js.org/d3.v4.min.js"*></script>
5
 <style>
6
  body { margin:0;position:fixed;top:0;right:0;bottom:0;left:0; }
7
 </style>
8
</head>
9
​
10
<body>
11
 <script>
12
  // Feel free to change or delete any of the code you see in this editor!
13
  var  svg  =  d3.select(*"body"*).append(*"svg"*)
14
    .attr(*"width"*, 960)
15
    .attr(*"height"*, 500)
16
​
17
  svg.append(*"text"*)
18
    .text(*"Edit the code below to change me!"*)
19
    .attr(*"y"*, 200)
20
    .attr(*"x"*, 120)
21
    .attr(*"font-size"*, 36)
22
    .attr(*"font-family"*, *"monospace"*)
23
​
24
 </script>
25
</body>
26
​

![close_icon.png](../_resources/84fc025b2e6ece6f37cfbf5a8c7b496d.png)[9 min to Spreed]()