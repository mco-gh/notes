Jupyter + TensorFlow with Google Cloud… in 90 seconds!

# Jupyter + TensorFlow with Google Cloud… in 90 seconds!

## Is it possible for data science beginners to get up and running in under 2 minutes?

[ ![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='57' height='57' viewBox='0 0 57 57' data-evernote-id='183' class='js-evernote-checked'%3e%3cpath fill-rule='evenodd' clip-rule='evenodd' d='M28.5 1.2A27.45 27.45 0 0 0 4.06 15.82L3 15.27A28.65 28.65 0 0 1 28.5 0C39.64 0 49.29 6.2 54 15.27l-1.06.55A27.45 27.45 0 0 0 28.5 1.2zM4.06 41.18A27.45 27.45 0 0 0 28.5 55.8a27.45 27.45 0 0 0 24.44-14.62l1.06.55A28.65 28.65 0 0 1 28.5 57 28.65 28.65 0 0 1 3 41.73l1.06-.55z' data-evernote-id='184' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e) ![1*IL0mnvzNcpG2ZD0JBqo7zQ.jpeg](../_resources/bdd198bb8510e1e6545d3079c7910a2b.jpg)](https://towardsdatascience.com/@kozyrkov?source=post_page-----93038bcac996----------------------)

[Cassie Kozyrkov](https://towardsdatascience.com/@kozyrkov?source=post_page-----93038bcac996----------------------)

[Apr 29](https://towardsdatascience.com/90-second-setup-challenge-jupyter-tensorflow-in-google-cloud-93038bcac996?source=post_page-----93038bcac996----------------------) · 5 min read![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='star-15px_svg__svgIcon-use js-evernote-checked' width='15' height='15' viewBox='0 0 15 15' style='margin-top:-2px' data-evernote-id='200'%3e%3cpath d='M7.44 2.32c.03-.1.09-.1.12 0l1.2 3.53a.29.29 0 0 0 .26.2h3.88c.11 0 .13.04.04.1L9.8 8.33a.27.27 0 0 0-.1.29l1.2 3.53c.03.1-.01.13-.1.07l-3.14-2.18a.3.3 0 0 0-.32 0L4.2 12.22c-.1.06-.14.03-.1-.07l1.2-3.53a.27.27 0 0 0-.1-.3L2.06 6.16c-.1-.06-.07-.12.03-.12h3.89a.29.29 0 0 0 .26-.19l1.2-3.52z' data-evernote-id='201' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)

[![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='29' height='29' class='q js-evernote-checked' data-evernote-id='206'%3e%3cpath d='M22.05 7.54a4.47 4.47 0 0 0-3.3-1.46 4.53 4.53 0 0 0-4.53 4.53c0 .35.04.7.08 1.05A12.9 12.9 0 0 1 5 6.89a5.1 5.1 0 0 0-.65 2.26c.03 1.6.83 2.99 2.02 3.79a4.3 4.3 0 0 1-2.02-.57v.08a4.55 4.55 0 0 0 3.63 4.44c-.4.08-.8.13-1.21.16l-.81-.08a4.54 4.54 0 0 0 4.2 3.15 9.56 9.56 0 0 1-5.66 1.94l-1.05-.08c2 1.27 4.38 2.02 6.94 2.02 8.3 0 12.86-6.9 12.84-12.85.02-.24 0-.43 0-.65a8.68 8.68 0 0 0 2.26-2.34c-.82.38-1.7.62-2.6.72a4.37 4.37 0 0 0 1.95-2.51c-.84.53-1.81.9-2.83 1.13z' data-evernote-id='207' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://medium.com/p/93038bcac996/share/twitter?source=post_actions_header---------------------------)

[![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='29' height='29' class='q js-evernote-checked' data-evernote-id='215'%3e%3cpath d='M23.2 5H5.8a.8.8 0 0 0-.8.8V23.2c0 .44.35.8.8.8h9.3v-7.13h-2.38V13.9h2.38v-2.38c0-2.45 1.55-3.66 3.74-3.66 1.05 0 1.95.08 2.2.11v2.57h-1.5c-1.2 0-1.48.57-1.48 1.4v1.96h2.97l-.6 2.97h-2.37l.05 7.12h5.1a.8.8 0 0 0 .79-.8V5.8a.8.8 0 0 0-.8-.79' data-evernote-id='216' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://medium.com/p/93038bcac996/share/facebook?source=post_actions_header---------------------------)

Data science enthusiasts, how fast can you go from zero to Google Cloud Jupyter notebook? Let’s find out!

![1*6a4Qu3xVUrO4visFqIiPtw.png](../_resources/44fae7a4fb69c0b0d928ee39349a0639.png)
![1*6a4Qu3xVUrO4visFqIiPtw.png](../_resources/e472c198c6d60a33fe49c03f8646c30d.png)

Image: [SOURCE](https://pixabay.com/photos/blue-sunglasses-woman-swimming-pool-2705642/).

# To customize or not to customize?

If you’re in the mood to ultra-customize your setup, [Google Cloud](http://bit.ly/gcp-hello) gives you dizzying granularity. That’s a fabulous thing for teams starting an enterprise-scale project, which scales up the consequences of every corner you cut.

> Do beginners have to trudge through a forest of options to get started?

But what if you’re a beginner who just wants to play around with a [data science](http://bit.ly/quaesita_datascim) notebook? Do you have to trudge through that forest of options to get started? Great news: you don’t. You can get up and running in under 90 seconds! (Feel free to skip to the walk-through below.)

> You can get up and running in under 2 minutes! (Walk-through below.)

If this is your first time, I bet you’re probably especially keen to get to `hello world` as quickly as possible. You’ll want to skip the control panel and use someone else’s setup solution. If so, you’ll love the Google Cloud [Marketplace](https://bit.ly/gcpmarketplace)!

# What is the Marketplace?

Welcome to a collection of prebaked [machine images](http://bit.ly/quaesita_mimag) that you can use as a springboard for your own work. And yes, you can customize these third party templates later if you need to (learn more [here](http://bit.ly/quaesita_mimag)).

> A collection of prebaked templates.

# The 90 second challenge

Enough preamble! Let’s see if it is possible to go from zero to hero in under 2 minutes. I’ll break down the steps below — this is just the proof that it can be done. Here’s we go:

![1*Ghms-lXqfhnIobdALcWGnA.gif](../_resources/6dc4d33948a68e5ce15b102c86199d27.jpg)
![1*Ghms-lXqfhnIobdALcWGnA.gif](../_resources/027f62fd32149d592e367d5ca69fc177.gif)

This recording of my screen shows you that it’s possible to get going under 90 sec, but your sore eyes might prefer the step-by-step screenshot guide below.

# What did we just watch?

First, what *didn’t* we watch? Steps 0.1–0.3.

## Step 0.1: Create Google account

You’ll need a [Google account](https://bit.ly/myaccountgoogl) to use Google Cloud. I’ve had mine for a while, so that’s not shown.

## Step 0.2: Open Google Cloud Console

My video starts on the Google Cloud Dashboard screen, which you’ll get to by clicking [console.cloud.google.com](https://bit.ly/consolecloudgoogle). First-time users will be prompted through a few housekeeping items.

## Step 0.3: Create a new project

I’m using a project I made called *ItsTimeForDemos*. To make a new project, I clicked on this part of the dashboard:

![1*IYTPSWffQolcxgxcNIVHcQ.png](../_resources/2ab44fd0a84374627468f2617888e424.png)
![1*2EVripv_Idhh50sBn6m3uQ.png](../_resources/52391f7a9ee5641f5f21c43cd40363c3.png)
Now that we’re ready, let’s examine what we saw on my screen.

## Step 1: Head to the Marketplace!

To skip reinventing your own wheel, you’ll head to Google Cloud [Marketplace](https://bit.ly/gcpmarketplace).

![1*4LxprxomT4dNhVeiJ_d40Q.png](../_resources/d176cc0d7d80eb85540182c13aa5f749.png)
![1*4LxprxomT4dNhVeiJ_d40Q.png](../_resources/1d38394fa4512d3f764df9e77db37694.png)

## Step 2: Search for the solution you need

![1*tBZPg4nvRlYPdvN18tm3sA.png](../_resources/beb4b9e6f11884d22c3a1fc2f21d020f.png)
![1*tBZPg4nvRlYPdvN18tm3sA.png](../_resources/b234fc534a6eb4588fead52711cb8218.png)
In the search bar, I’ll enter the keywords “*ai cpu.*”

*Why *[*AI*](http://bit.ly/quaesita_ai)*? *I felt like doing this demo with an AI-geared notebook. If you’re looking for something else, simply ask the search bar. There are almost 2000 solutions here.

*Why CPU? *It’s the vanilla option. More powerful hardware — like GPUs — is more powerful… which usually also means it’s more expensive and will burn through your [$300 free credits](https://bit.ly/free300gcp) faster. Unless you already know why you need the beast option, it’s probably a good idea to start with its lightweight cousin.

## Step 3: Choose your winner

Among the solutions, I picked the TensorFlow Jupyter notebook. You pick whatever you like.

![1*rlPPDs6ouTe_lj3m-jTgow.png](../_resources/534e14f3f24a8a434485d71de154241c.png)
![1*rlPPDs6ouTe_lj3m-jTgow.png](../_resources/342986a580971a5a50aabba7d07aa7fe.png)

*Why notebook? *[Data scientists](http://bit.ly/quaesita_universe) like notebooks because they combine the best of interactive data analysis with pretty report-making.

*Why *[*Jupyter*](http://bit.ly/jupyter_try)*? *It’s the notebook solution you’re most likely to have heard of.

*Why *[*TensorFlow*](http://bit.ly/quaesita_tf)*? *It’s a powerful [deep-learning](http://bit.ly/quaesita_emperor) framework; get more info [here](http://bit.ly/quaesita_tf2).

## Step 4: Launch and deploy

Hit the big blue button. Repeat.
![1*OkGN2eTk9ENlsaxCTeKNsg.png](../_resources/500d7c7a8dc001fb2db3695240980b7b.png)
![1*OkGN2eTk9ENlsaxCTeKNsg.png](../_resources/4e4291baab4934807cbdfbb8f6d8fcf3.png)
![1*vWEdpbcpfPSnUFXapfJNtA.png](../_resources/eb85c8636bab2ada410df6c8b6fd108b.png)
![1*vWEdpbcpfPSnUFXapfJNtA.png](../_resources/33bb138e0a0b2738d0bb8deb4abaf038.png)

## Step 5: Copy the provided password and open the notebook

A randomly-generated password will be created for you. Copy its text while you wait patiently for a few seconds, then open the Jupyter notebook when that option becomes available.

![1*ZbiH7V95GdT_jJKMz5LWSg.png](../_resources/a931fc7bac05ca6cf35158d862b00260.png)
![1*ZbiH7V95GdT_jJKMz5LWSg.png](../_resources/b34b9fff215d3b4aab8cd40c9018c949.png)

## Step 6: Hello world!

![1*2EVripv_Idhh50sBn6m3uQ.png](../_resources/67bed905c791ba4a251d7fa9945d1d5c.png)
![1*-GFd3VWtUH0nzX4k1h3lGw.png](../_resources/6118ab0a84c717b7b5919c0daae0aae1.png)
Paste in your copied password to open Jupyter, then create a new notebook.
![1*n3Z3lGrn5Q_gYnzwWjszAA.png](../_resources/2f178cb214089a7adcc29f5cb30d4f2b.png)
![1*n3Z3lGrn5Q_gYnzwWjszAA.png](../_resources/dd855561434ab6b62401ed9844677723.png)

Once you’re in, you’ll see that TensorFlow is installed and you’re ready to start exploring.

![1*-GFd3VWtUH0nzX4k1h3lGw.png](../_resources/11aaa4c9e5ff6c08f96327ac4b7f5fdc.png)
![1*IYTPSWffQolcxgxcNIVHcQ.png](../_resources/971c0f35c753c687d116e581f9e38c6b.png)
Getting up and running took less than 90 seconds!

# Game on!

Is this the best data science environment you can have? No, because creating the *perfect* solution for you means [customizing](http://bit.ly/quaesita_mimag) everything to *your* personal needs. One day, that’s probably what you’ll choose to do. But in the meantime, this was the shortest path to getting up and running that I’ve found. My goal with this blog post was simply to show you that there are super-quick options out there.

> Can you do it faster than me?

Can you do it faster than me? Maybe! Consider it a challenge and [let me know](https://twitter.com/quaesita/status/1255625073924472833) how many seconds it takes you.

# Don’t forget

To avoid charges, don’t forget to turn out the lights when you’re done; use the search bar to find the *Deployment Manager* page where you can delete/stop whatever you don’t need anymore.

![1*e5WggDgz3Nr-erHv1WjPHA.png](../_resources/781628b50a512388f63a3e23d5bde075.png)
![1*e5WggDgz3Nr-erHv1WjPHA.png](../_resources/1ae1e9120cf7e7e7627ab65d7f148e41.png)

# Disclaimer

*This blog post was written in April 2020, so if you’re from The Future, things might look different in your world.*