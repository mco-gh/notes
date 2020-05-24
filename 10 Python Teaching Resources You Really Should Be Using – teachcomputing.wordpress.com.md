10 Python Teaching Resources You Really Should Be Using – teachcomputing.wordpress.com

Since I first started teaching text-based programming with Python in 2011, I’ve discovered some resources that I make use of regularly. I still use these extensively with the teachers that I support as part of my work with [Exa Education](http://exa.education/). I’m sure that others reading this post may like to suggest other tools, and I would encourage you to add them as a comment on this post.

When I made my first tentative steps into the world of Python I was pleasantly surprised how welcoming, supportive and accommodating I found the Python community to be. The vast abundance of high quality, free teaching and learning resources are testament to this. Though you might equate the word ‘resource’ to describe something more akin to a textbook or webpage, without the assiduous efforts of the Python community the resources listed below would simply not exist.

### 1. Invent Your Own Computer Games With Python

You may already have your own favourite book for learning Python – this title, written by Al Sweigart is my personal favourite. I spent months searching for the most suitable text-based programming language for teaching before I found this book, it may just have saved me from a fate worse than Java! The book and associated resources have helped me enormously so many times. You can either choose to purchase the book, download for free as a .PDF or view each chapter as .HTML in your browser. I particularly love how each chapter is set out in the same structure starting with the learning objectives, demonstrating sample programs accompanied with step-by-step explanations. Not content with writing one great book, Al has gone on to write three more titles. http://inventwithpython.com/

Report this ad
![screenshot-2016-03-20-11-42-41.png](../_resources/b1f3c75a8e3479c8ac89c215f8da60ad.png)

### 2. Skulpt

Occasionally I’ve worked in schools where for one reason or another Python is not available, occasionally because an overzealous network manager worries about the damage that it may do in the wrong hands. Skulpt executes Python script in a browser and includes some examples which work straight away. Example number 1 uses **a logo-based Turtle module** to draw geometric shapes on screen. I use this example often to test learner’s previous knowledge and experience as well as their ability to predict the outcomes. [http://skulpt.org](http://skulpt.org/)

### 3. Guess The Number

In Al Sweigart’s first book, Chapter 4 includes a text-based number guessing game. I’m particularly fond of this as a teaching tool since it contains many of the basic concepts of text-based programming that I was required to teach including **data types, sequence, conditionals and iteration**. When I’ve taught with this example, I’ve asked learners to create their own different versions of the game (forking), for example, more difficult and ridiculously easy versions. http://inventwithpython.com/chapter4.html

### 4. Teach Python

After introducing Python to my classes in 2011, a non-computing colleague asked me to write some plans that would enable her to introduce Python to her classes. I wrote these down as a series of 5 lesson plans and shared them on the **Computing At School** community site. They’ve proved to be extremely popular and many teachers have gone on to modify them and adapt them to suit their own settings. http://community.computingatschool.org.uk/resources/221

**

> “Its a really straightforward, interesting way to introduce a language. To others who use it, follow the advice given and check out the videos yourself first.” – Paula Clay, Teacher

> “Have been using this with my Year 9 classes and they have enjoyed it. I like how it has been put into context with the chat bots.” – Dean Whittle, Teacher

**

### 5. Minecraft API on Raspberry Pi

Minecraft is more than just a game, it has proven to be an extremely popular sandbox environment in which learners can collaborate and create together. While Minecraft is widely available in many different flavours for a variety of platforms, the Raspberry Pi edition has some super cool power features. Using the Minecraft API, it’s possible to use python to control interactions between the physical world and the Minecraft world, as well as move players and blocks in response to conditions in both the Minecraft and real world.

- **Get started with Minecraft on Pi**: https://www.raspberrypi.org/learning/getting-started-with-minecraft-pi/
- **Whac-a-block:**  https://www.raspberrypi.org/learning/minecraft-whac-a-block-game/
- **David Whale & Martin O’Hanlon’s fabulous ‘Adventures in Minecraft’ book:**  https://www.ebooks-it.net/ebook/adventures-in-minecraft
- **Craig Richardson’s excellent ‘Learn To Program With Minecraft’ book**: https://www.nostarch.com/programwithminecraft

![16582331172_d0625c4c37_z.jpg](../_resources/dc5844c221dffd32a43fadec0fc55a73.jpg)

[(L)](https://teachcomputing.wordpress.com/2016/03/20/10-python-teaching-resources-you-really-should-be-using/#)[(L)](https://teachcomputing.wordpress.com/2016/03/20/10-python-teaching-resources-you-really-should-be-using/#)[(L)](https://teachcomputing.wordpress.com/2016/03/20/10-python-teaching-resources-you-really-should-be-using/#)

### 6. Squirrel Eat Squirrel

The Pygame library extends the potential of Python to include a graphical user interface (GUI) for games development. Al Sweigart’s Pygame book is accompanied by an excellent library of pygame examples. After asking my class to first master playing the game and predict the effects of small changes to the script, I then ask them to make more significant changes to the squirrel game. Daniel Pope’s **Pygame Zero**, goes a long way to making Pygame more accessible to learners by minimising use of ‘boilerplate’: https://pygame-zero.readthedocs.org/en/latest/   **Squirrel Eat Squirrel**: [http://inventwithpython.com/pygame/chapter8.html

![16581695682_d13117dbf8_z.jpg](../_resources/753e5f25d1dcde4ddeb01fc9775c7fb5.jpg)

[(L)](https://teachcomputing.wordpress.com/2016/03/20/10-python-teaching-resources-you-really-should-be-using/#)[(L)](https://teachcomputing.wordpress.com/2016/03/20/10-python-teaching-resources-you-really-should-be-using/#)[(L)](https://teachcomputing.wordpress.com/2016/03/20/10-python-teaching-resources-you-really-should-be-using/#)

### 7. Coding Dojo

It took me a long time to develop my teaching style and method into one where pupils were more engaged in problem solving. Visiting Coding Dojos (monthly meet-ups for software developers) where I observed developers collaborating to solve problems and sharing their solutions inspired me to introduce this style into my own Computing lessons. I have found that once we have started, the learners become highly absorbed and make few demands on me. Don’t judge the success after your first dojo, this is something to work into your practice over time. I wrote about it here: https://teachcomputing.wordpress.com/2016/02/28/the-best-way-to-teach-text-based-programming/

### 8. Random

Python has some really useful built-in functions, eg. print and input. The random module on the other hand –  is one of many modules that needs to be imported from the python library before it can be used. We have become used to computers being exactly predictable, but the random module allows pupils to add some elements of chance, unpredictability and risk into their projects.

import random
coin = [‘heads’,’tails’]
flip = random.choice(coin)
print(flip)

### 9. Anti Gravity

I don’t use python’s anti gravity module as widely as the other python modules. On the odd occasion that I do use it in my teaching, I ask learners to predict what might happen after they **import antigravity**. This typically generates a wide range of responses from the group, some pupils have suggested that furniture in the room will start to float weightlessly – they clearly have an accurate grasp of just how powerful python can be! Now, rather than demonstrate this to your class, leave them to find out for themselves and after that discuss eggs with them.

**
> > >>> import antigravity
**

### 10. Sabotage

The biggest challenge I faced as a Computing teacher was dealing with the syntax errors that pupils had in their coded solutions. In the early days, as I became more efficient at fixing their bugs, the more inclined learners were to ask for my help. Before I burned out completely from exhaustion and exasperation, I conceived ‘sabotage’ – a teaching strategy that turns debugging into a fun game. Pupils deliberately hide bugs in their own scripts and then challenge others to find them. https://teachcomputing.wordpress.com/2013/11/23/sabotage-teach-debugging-by-stealth/

### 10 + 1  – Micro Python and Micro:bit – The Future

The 10 resources listed above are those I have used regularly in the last 5 years. At the time of writing this list, I’ve only just started using **Micro Python on the Micro:bit**, but I expect that it will soon appear at the top of this list. It’s a really flexible python application that allows me to interact with my BBC Micro:bit. The ten resources I’ve listed above only allow you to control software (virtual environments), since Micro Python allows you to control actions in the physical world it doesn’t take a huge leap to see how much of a motivator this could be to inspire the minds of young computer scientists. My first Micro Python creation was to build a tool that can test to see if you’re “Dead or Alive”, the source code makes use of 9 lines: https://github.com/teknoteacher/micropython/blob/master/dead_or_alive.py

### CAS TV Python – The Bathroom Interview

I was recently interviewed by Miles Berry for a CAS TV episode. This was recorded in a tiny office at the London headquarters of the BCS, and not as the sound quality might suggest in somebody’s bathroom. Miles asked me a series of questions about teaching text-based programming with Python.

Report this ad

Advertisements

Report this ad
Advertisements

 ![1572516627-600x600_c1.jpg](../_resources/cd2bc604112cf35fed4b78f91fe8a11d.jpg)

20% SALE

Create a custom photo project with 20% for a limited time only

Report this ad

### Share this:

- [Twitter](https://teachcomputing.wordpress.com/2016/03/20/10-python-teaching-resources-you-really-should-be-using/?share=twitter&nb=1)
- [Facebook](https://teachcomputing.wordpress.com/2016/03/20/10-python-teaching-resources-you-really-should-be-using/?share=facebook&nb=1)

-

[Like](https://widgets.wp.com/likes/index.html?ver=20190321#)

- [![d9f3eacd9b5f87225d8745e2e1bc6111](../_resources/b297e31307ef6a40c056340c79d853db.jpg)](https://en.gravatar.com/lenandlar)
- [![0d84de56d86a715680c212c08f253466](../_resources/547e777bf0fabef078b0c9d2843e4ec9.png)](https://en.gravatar.com/daveb64)
- [![51dbaad5ca578bef4042d4c37ad0e961](../_resources/1cb7054b6df1766c5a18da148ff7cf3a.png)](https://en.gravatar.com/kokhuatan)
- [![720b851f3c7dbde2689dfb851f0ff83e](../_resources/1bbe04b3f971bde91863ccbd178ead16.png)](https://en.gravatar.com/oxfordtutoringblog)
- [![b9d3de9766b3b7aaaf64a7a00d5ef8a3](../_resources/d91701b92e960e198eb0da36e1428622.png)](https://en.gravatar.com/babesyoga)
- [![a00680d31fcd5c5d71fbf7f202050f30](../_resources/c893632e50fd14e611c8b4cfd637f307.png)](https://en.gravatar.com/breannahubbard)
- [![0ffc37b8dad55e21e120bad65f0fb260](../_resources/ac21d4fb39df256c1032354459db009b.png)](https://en.gravatar.com/samuelnixons)

[7 bloggers](https://widgets.wp.com/likes/index.html?ver=20190321#) like this.

### *Related*

[Teach Computing 18.06.2012](https://teachcomputing.wordpress.com/2012/06/19/teach-computing-18-06-2012/)In "Computing"

["How do we teach programming in schools?"](https://teachcomputing.wordpress.com/2014/02/21/how-do-we-teach-programming-in-schools/)In "Classroom"

[Proposal for a GCSE Computing MOOC](https://teachcomputing.wordpress.com/2016/05/30/proposal-for-a-gcse-computing-mooc/)In "Computing"