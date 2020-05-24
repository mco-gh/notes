How to run Visual Studio Code in Google Cloud Shell

# How to run Visual Studio Code in Google Cloud Shell

[![1*N0OYA7HJYDyfAsr5XwDpWQ.jpeg](../_resources/dfbc36cce250e0040e550b9016cd8268.jpg)](https://medium.com/@chees?source=post_header_lockup)

[Christiaan Hees](https://medium.com/@chees)
Jul 8·2 min read

Did you know you can run Visual Studio Code in a browser? It’s so cool, it even works with extensions and all that. I’ll show you an example using [github.com/cdr/code-server](https://github.com/cdr/code-server/)

- •Go to [console.cloud.google.com](https://console.cloud.google.com/) and open Cloud Shell

![](../_resources/4ba71126147d285c4230c3ba064eb5de.png)![1*SUOU-efxQMHfZi3bfv-3Zw.png](../_resources/499f51b0bdb21fcb7136c510cb8f50a3.png)

- •Enable Boost Mode to make it faster

![](../_resources/8335c0d77ea53dbfc243a4f0527137a3.png)![1*D8J4okWRgFRnxo7MhbHGPg.png](../_resources/2f1d658be54d56dc2e814f7d0c961504.png)

- •Install code-server

export VERSION=`curl -s https://api.github.com/repos/cdr/code-server/releases/latest | grep -oP '"tag_name": "\K(.*)(?=")'`

wget https://github.com/cdr/code-server/releases/download/$VERSION/code-server$VERSION-linux-x64.tar.gz

tar -xvzf code-server$VERSION-linux-x64.tar.gz
cd code-server$VERSION-linux-x64

- •Start the server

./code-server --no-auth --port 8080

> Note that you don’t need authentication since the Google Cloud Shell proxy already handles that for you.

- •Click on Web Preview -> Preview on port 8080

![](../_resources/e24ee055c169d21159299cda6976de6c.png)![1*tcyI0xwhSF7Wn1upszdhDA.png](../_resources/3ac8d63987d718d350d7add5a9b5d5fb.png)

> If you get a 404, remove `?authuser=0`>  from the url. So for example, just

`[https://8080-dot-YOURID-dot-devshell.appspot.com/](https://8080-dot-yourid-dot-devshell.appspot.com/)`

> instead of

`[https://8080-dot-YOURID-dot-devshell.appspot.com/?authuser=0](https://8080-dot-yourid-dot-devshell.appspot.com/?authuser=0)`

#### That’s it, now you have an IDE running in your browser!

![](../_resources/cb0b3b8bf5146360f8d7d917477ee689.png)![1*BVCoNecwFAR7vcmaJ9a2gA.png](../_resources/956e02d9fbe42537e225b0b1f297d38d.png)