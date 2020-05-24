Data Science on a Chromebook · Simply Statistics

# Data Science on a Chromebook

##

 **  Jeff Leek  **  2017/08/29

 **  [chromebook](https://simplystatistics.org/tags/chromebook)

About nine months ago [I announced](https://simplystatistics.org/2016/11/08/chromebook-part2/) that I was attempting a Chromebook experiment for the 2nd time. At first I thought it was going to be a short term experiment just to see if it was possible to function with only a Chromebook. But in an interesting twist I got used to it and have been working exclusively on a Chromebook for the last few months since the experiment started.

I set myself the following requirements:
1. I could only use Chrome OS - no installing/booting to Linux
2. I couldn’t use another computer for any task

3. I had to be “fully cloudy” in the sense that I didn’t run any additional hardware

One of the reasons I did this was I wanted to see if it was possible to be a functioning/day to day data scientist without using an expensive laptop. This is part of a broader experiment I’m just beginning on how to [democratize data science education](https://peerj.com/preprints/3195/).

I’m not going to go into extreme detail on how I set everything up here (more on that in a second) but I thought I’d describe my Chromebook set up that I’ve been using for the last couple of months.

I have been using two [Samsung Chromebook Plus](https://www.amazon.com/dp/B01LZ6XKS6) computers, one of which I keep at home and one which I keep at work. One of the best parts about the fully cloudy/Chrome OS requirement is this means that from the user perspective everything is always in sync. I log off the computer at home, come to work, log on and its like I’m on the same computer.

I thought I’d just go through at a high level the software I’m using to keep everything running.

- **Google Slides for presentations** - *(Cost:free)* For the most part this has been really easy and is a smooth transition from Powerpoint. One thing I’ve found really useful is the laser pointer mode of the Chromebook plus for highlighting things on screen when presenting. I have also found that since they are using USB-C adapters I can participate in [dongle communism](https://simplystatistics.org/2011/09/23/dongle-communism/) with Apple users. I had to figure out the display mirroring menus in Chrome OS but after that this was easy.
- **Google Docs/Paperpile for writing** - *(Cost:free)* This works great and has been my work flow as I describe [in my book](https://leanpub.com/modernscientist) since before the Chromebook experiment started.
- **DocHub for signing things** - *(Cost:$4.99/month/billed yearly)* Often I have to “sign” a document by adding my electronic signature. I used the note feature to create a jpeg of my signature. I can then upload the file to Docub
- **Overleaf for writing latex** - *(Cost:free or $10/month/billed yearly)* This is not necessary for all data scientists, but it has some nice features, including when I could [live write a grant](https://twitter.com/jtleek/status/856297030582497281) and people could watch.
- **Gmail for email** - *(Cost:free)* this one is pretty obvious.
- **Google Sheets for data** - *(Cost:free)* this is again a choice I had been making frequently before I moved to Chromebooks. The [googlesheets](https://github.com/jennybc/googlesheets) R package lets you do [all sorts of cool things](https://simplystatistics.org/2016/08/26/googlesheets/) with google sheets.
- **Digital Ocean for Rstudio** - _(Cost: $20/mo)__ I set up an Rstudio server and run it remotely on Digital Ocean. I currently use the $20/month option but sometimes scale it up or down as needed. One great thing about the dockerized version of the software is that I can pause the instance, scale up the compute infrastructre, restart and everything is just as I left it but with more computational horsepower. I can then use that for a few hours as needed and scale back down. I use the terminal in Rstudio for most of my management of code/etc. on Github.
- **Google Hangouts for video conferencing** - *(Cost:free)* this is the default but honestly I wish I had a better option. I often find it complicated and laggy to work with, but still mostly better than Skype. Would be open to suggestions on that front.
- **Slack for communication**  *(Cost: $6.67/month)* a variety of different teams here at JHU and around the country use Slack for group communication. I use it through the web browser, although the Chromebook Plus allows you to install Android apps.
- **Google Music for listening to music/podcasts**  *(Cost:$10/month)* This is an unnecesary expense but I like having something to listen to while I work.
- **Tweetdeck for twitter** - *(Cost:free)* I have a couple of accounts I manage and I do this through the web browser. For the most part this works great.

So my total monthly cost comes to something like $35 a month for various cloud services. At first doing this was sort of like writing a Haiku. I could still write, but the constraints made me think hard about how I did things. But after a while I have gotten so used to the form that it feels natural and I don’t miss my (really expensive) Apple products anymore.

The biggest headaches have been:

- **Wifi connectivity issues** - this isn’t as big as I thought it would be, most places have wifi where I work and it is mostly ok. When I have trouble I stream from my phone.
- **Wifi blocking my DO server** - this one has been a headache. I think if I just got a custom domain for the webserver and didn’t just use the IP address I could avoid it. When I have trouble I stream from my phone.
- **httr and Rstudio on a server** - when I need to authenticate for websites I have run into trouble, but if I set `httr_oob_default==TRUE` ([documentation here](https://support.rstudio.com/hc/en-us/articles/217952868-Generating-OAuth-tokens-from-a-server)) then the Oauth process generates a code I can paste into my server.

Beyond that it has actually been pretty straightforward to do almost anything I need. Stay tuned because this experiment has inspired a broader effort we are doing with Chromebooks here at the [JHU Data Science Lab](http://jhudatascience.org/). If you want to hear about this effort as it gets underway, sign up for [our weekly newsletter](http://jhudatascience.us16.list-manage.com/subscribe?u=5ea551600fcdf84334e5aa6b0&id=26c0b7221a) and you’ll be the first to hear new announcements.

 [**](https://simplystatistics.org/2017/08/28/simple-queue-package-for-r/)

 [Simple Queue Package for R](https://simplystatistics.org/2017/08/28/simple-queue-package-for-r/)

 [Deep Dive - Y. Ogata's Residual Analysis for Point Processes](https://simplystatistics.org/2017/09/04/deep-dive-ogata/)

 [**](https://simplystatistics.org/2017/09/04/deep-dive-ogata/)

- [14 comments]()
- [**Simply Statistics**](https://disqus.com/home/forums/simplystatsgithub/)
- [(L)](https://disqus.com/embed/comments/?base=default&f=simplystatsgithub&t_u=http%3A%2F%2Fsimplystatistics.org%2F2017%2F08%2F29%2Fdata-science-on-a-chromebook%2F&t_d=Data%20Science%20on%20a%20Chromebook%20%C2%B7%20Simply%20Statistics&t_t=Data%20Science%20on%20a%20Chromebook%20%C2%B7%20Simply%20Statistics&s_o=default#)
- [](https://disqus.com/home/inbox/)
- [ Recommend  1](https://disqus.com/embed/comments/?base=default&f=simplystatsgithub&t_u=http%3A%2F%2Fsimplystatistics.org%2F2017%2F08%2F29%2Fdata-science-on-a-chromebook%2F&t_d=Data%20Science%20on%20a%20Chromebook%20%C2%B7%20Simply%20Statistics&t_t=Data%20Science%20on%20a%20Chromebook%20%C2%B7%20Simply%20Statistics&s_o=default#)
- [⤤  Share](https://disqus.com/embed/comments/?base=default&f=simplystatsgithub&t_u=http%3A%2F%2Fsimplystatistics.org%2F2017%2F08%2F29%2Fdata-science-on-a-chromebook%2F&t_d=Data%20Science%20on%20a%20Chromebook%20%C2%B7%20Simply%20Statistics&t_t=Data%20Science%20on%20a%20Chromebook%20%C2%B7%20Simply%20Statistics&s_o=default#)
- [Sort by Best](https://disqus.com/embed/comments/?base=default&f=simplystatsgithub&t_u=http%3A%2F%2Fsimplystatistics.org%2F2017%2F08%2F29%2Fdata-science-on-a-chromebook%2F&t_d=Data%20Science%20on%20a%20Chromebook%20%C2%B7%20Simply%20Statistics&t_t=Data%20Science%20on%20a%20Chromebook%20%C2%B7%20Simply%20Statistics&s_o=default#)

[![Avatar](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/disqus_Q5LZbDr3pW/)

Join the discussion…

- [Attach](https://disqus.com/embed/comments/?base=default&f=simplystatsgithub&t_u=http%3A%2F%2Fsimplystatistics.org%2F2017%2F08%2F29%2Fdata-science-on-a-chromebook%2F&t_d=Data%20Science%20on%20a%20Chromebook%20%C2%B7%20Simply%20Statistics&t_t=Data%20Science%20on%20a%20Chromebook%20%C2%B7%20Simply%20Statistics&s_o=default#)

-

[![Avatar](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/billraynor/)

 [Bill Raynor](https://disqus.com/by/billraynor/)    •  [2 months ago](https://simplystatistics.org/2017/08/29/data-science-on-a-chromebook/#comment-3492754138)

I've been trying Data Science on the iPad, with minimal external support (e.g. Dropbox or iTunes for import/export). I use a combination of

- AnalyseR - a iPad app with embedded R, Python, and SQLite engines,
- Textastic for an external code editor, and
- Editorial, TeX Writer, and Pages/Numbers for reporting.

on an iPadPro. Apple's restrictions on dynamically linked libraries make it somewhat tricky to add new packages, although it is possible to convert some packages to "pure R" or "pure Python". This is all inexpensive (beyond the iPadPro), mobile, and can work nicely off-line. I still use a laptop for staging data and code.

    - [−](https://disqus.com/embed/comments/?base=default&f=simplystatsgithub&t_u=http%3A%2F%2Fsimplystatistics.org%2F2017%2F08%2F29%2Fdata-science-on-a-chromebook%2F&t_d=Data%20Science%20on%20a%20Chromebook%20%C2%B7%20Simply%20Statistics&t_t=Data%20Science%20on%20a%20Chromebook%20%C2%B7%20Simply%20Statistics&s_o=default#)
    - [****](https://disqus.com/embed/comments/?base=default&f=simplystatsgithub&t_u=http%3A%2F%2Fsimplystatistics.org%2F2017%2F08%2F29%2Fdata-science-on-a-chromebook%2F&t_d=Data%20Science%20on%20a%20Chromebook%20%C2%B7%20Simply%20Statistics&t_t=Data%20Science%20on%20a%20Chromebook%20%C2%B7%20Simply%20Statistics&s_o=default#)

-

[![Avatar](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/disqus_R6k9rkm9UW/)

 [Ben](https://disqus.com/by/disqus_R6k9rkm9UW/)    •  [2 months ago](https://simplystatistics.org/2017/08/29/data-science-on-a-chromebook/#comment-3494254624)

Just curious on if there was a specific reason you chose Digital Ocean over other services since in the first post you mentioned you were planning on using Amazon AMI.

    - [−](https://disqus.com/embed/comments/?base=default&f=simplystatsgithub&t_u=http%3A%2F%2Fsimplystatistics.org%2F2017%2F08%2F29%2Fdata-science-on-a-chromebook%2F&t_d=Data%20Science%20on%20a%20Chromebook%20%C2%B7%20Simply%20Statistics&t_t=Data%20Science%20on%20a%20Chromebook%20%C2%B7%20Simply%20Statistics&s_o=default#)
    - [****](https://disqus.com/embed/comments/?base=default&f=simplystatsgithub&t_u=http%3A%2F%2Fsimplystatistics.org%2F2017%2F08%2F29%2Fdata-science-on-a-chromebook%2F&t_d=Data%20Science%20on%20a%20Chromebook%20%C2%B7%20Simply%20Statistics&t_t=Data%20Science%20on%20a%20Chromebook%20%C2%B7%20Simply%20Statistics&s_o=default#)

-

[![Avatar](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/aaroncharlton/)

 [Aaron Charlton](https://disqus.com/by/aaroncharlton/)    •  [2 months ago](https://simplystatistics.org/2017/08/29/data-science-on-a-chromebook/#comment-3492691914)

I use paperpile and google docs together too, and I love it. I run into problems with math formulas though. Do you have a good way to get them into your manuscript?

    - [−](https://disqus.com/embed/comments/?base=default&f=simplystatsgithub&t_u=http%3A%2F%2Fsimplystatistics.org%2F2017%2F08%2F29%2Fdata-science-on-a-chromebook%2F&t_d=Data%20Science%20on%20a%20Chromebook%20%C2%B7%20Simply%20Statistics&t_t=Data%20Science%20on%20a%20Chromebook%20%C2%B7%20Simply%20Statistics&s_o=default#)
    - [****](https://disqus.com/embed/comments/?base=default&f=simplystatsgithub&t_u=http%3A%2F%2Fsimplystatistics.org%2F2017%2F08%2F29%2Fdata-science-on-a-chromebook%2F&t_d=Data%20Science%20on%20a%20Chromebook%20%C2%B7%20Simply%20Statistics&t_t=Data%20Science%20on%20a%20Chromebook%20%C2%B7%20Simply%20Statistics&s_o=default#)

-

[![Avatar](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/disqus_pyK1du9ktZ/)

 [Scott C.](https://disqus.com/by/disqus_pyK1du9ktZ/)    •  [2 months ago](https://simplystatistics.org/2017/08/29/data-science-on-a-chromebook/#comment-3492548401)

Try Zoom for video conferencing. I've used Skype, Hangouts, Webex, other misc. corporate-provided options... Zoom beat them all for 1:1 and team calls.

    - [−](https://disqus.com/embed/comments/?base=default&f=simplystatsgithub&t_u=http%3A%2F%2Fsimplystatistics.org%2F2017%2F08%2F29%2Fdata-science-on-a-chromebook%2F&t_d=Data%20Science%20on%20a%20Chromebook%20%C2%B7%20Simply%20Statistics&t_t=Data%20Science%20on%20a%20Chromebook%20%C2%B7%20Simply%20Statistics&s_o=default#)
    - [****](https://disqus.com/embed/comments/?base=default&f=simplystatsgithub&t_u=http%3A%2F%2Fsimplystatistics.org%2F2017%2F08%2F29%2Fdata-science-on-a-chromebook%2F&t_d=Data%20Science%20on%20a%20Chromebook%20%C2%B7%20Simply%20Statistics&t_t=Data%20Science%20on%20a%20Chromebook%20%C2%B7%20Simply%20Statistics&s_o=default#)

    -

[![Avatar](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/untangle/)

 [Bob Walters](https://disqus.com/by/untangle/)    [*>* Scott C.](https://simplystatistics.org/2017/08/29/data-science-on-a-chromebook/#comment-3492548401)  •  [2 months ago](https://simplystatistics.org/2017/08/29/data-science-on-a-chromebook/#comment-3492874304)

Or [appear.in](http://disq.us/url?url=http%3A%2F%2Fappear.in%3AiaQi0ubhdjFSUA72YH1auOh2y8g&cuid=4023757)

        - [−](https://disqus.com/embed/comments/?base=default&f=simplystatsgithub&t_u=http%3A%2F%2Fsimplystatistics.org%2F2017%2F08%2F29%2Fdata-science-on-a-chromebook%2F&t_d=Data%20Science%20on%20a%20Chromebook%20%C2%B7%20Simply%20Statistics&t_t=Data%20Science%20on%20a%20Chromebook%20%C2%B7%20Simply%20Statistics&s_o=default#)
        - [****](https://disqus.com/embed/comments/?base=default&f=simplystatsgithub&t_u=http%3A%2F%2Fsimplystatistics.org%2F2017%2F08%2F29%2Fdata-science-on-a-chromebook%2F&t_d=Data%20Science%20on%20a%20Chromebook%20%C2%B7%20Simply%20Statistics&t_t=Data%20Science%20on%20a%20Chromebook%20%C2%B7%20Simply%20Statistics&s_o=default#)

    -

[![Avatar](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/disqus_4LOdLCfSqj/)

 [Austin](https://disqus.com/by/disqus_4LOdLCfSqj/)    [*>* Scott C.](https://simplystatistics.org/2017/08/29/data-science-on-a-chromebook/#comment-3492548401)  •  [2 months ago](https://simplystatistics.org/2017/08/29/data-science-on-a-chromebook/#comment-3492586879)

I agree with Scott. Zoom is nice, though I haven't used it on Chrome OS ([https://support.zoom.us/hc/...](https://disq.us/url?url=https%3A%2F%2Fsupport.zoom.us%2Fhc%2Fen-us%2Farticles%2F213298746-Getting-Started-On-Chrome-OS%29%3AADsBTI0dA7LIArblCdpChtOGRp8&cuid=4023757)

How does Google Meet compare to Google Hangouts?

        - [−](https://disqus.com/embed/comments/?base=default&f=simplystatsgithub&t_u=http%3A%2F%2Fsimplystatistics.org%2F2017%2F08%2F29%2Fdata-science-on-a-chromebook%2F&t_d=Data%20Science%20on%20a%20Chromebook%20%C2%B7%20Simply%20Statistics&t_t=Data%20Science%20on%20a%20Chromebook%20%C2%B7%20Simply%20Statistics&s_o=default#)
        - [****](https://disqus.com/embed/comments/?base=default&f=simplystatsgithub&t_u=http%3A%2F%2Fsimplystatistics.org%2F2017%2F08%2F29%2Fdata-science-on-a-chromebook%2F&t_d=Data%20Science%20on%20a%20Chromebook%20%C2%B7%20Simply%20Statistics&t_t=Data%20Science%20on%20a%20Chromebook%20%C2%B7%20Simply%20Statistics&s_o=default#)

-

[![Avatar](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/jeffhollister/)

 [Jeff Hollister](https://disqus.com/by/jeffhollister/)    •  [2 months ago](https://simplystatistics.org/2017/08/29/data-science-on-a-chromebook/#comment-3492729190)

Thanks for sharing. To add another data point, I have been using my Asus Chromebook, although only as my remote option, for my R work for about 5 months and absolutely love it. Unlike you, I wanted to go the linux route. I've done that with crouton and the xiwi extension. Allows me to boot solely into Chrome OS and fire up a new window for RStudio. It can be a little fiddly, but 90% of the time it works great. Other 10% was mostly me getting stuff figured out. I am curious why you didn't want to go this route? Seems to a better option for democratizing data science since you don't incur the monthly cost of a DO server.

Also, as an alternative to hangouts, I have used [https://appear.in](https://disq.us/url?url=https%3A%2F%2Fappear.in%3AXBjsYWsSeP3mT4Thz9PQkEStTS8&cuid=4023757). It works pretty well and is more straightforward to get going than hangouts, IMO.

    - [−](https://disqus.com/embed/comments/?base=default&f=simplystatsgithub&t_u=http%3A%2F%2Fsimplystatistics.org%2F2017%2F08%2F29%2Fdata-science-on-a-chromebook%2F&t_d=Data%20Science%20on%20a%20Chromebook%20%C2%B7%20Simply%20Statistics&t_t=Data%20Science%20on%20a%20Chromebook%20%C2%B7%20Simply%20Statistics&s_o=default#)
    - [****](https://disqus.com/embed/comments/?base=default&f=simplystatsgithub&t_u=http%3A%2F%2Fsimplystatistics.org%2F2017%2F08%2F29%2Fdata-science-on-a-chromebook%2F&t_d=Data%20Science%20on%20a%20Chromebook%20%C2%B7%20Simply%20Statistics&t_t=Data%20Science%20on%20a%20Chromebook%20%C2%B7%20Simply%20Statistics&s_o=default#)

-

[![Avatar](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/blazewon22/)

 [blazewon22](https://disqus.com/by/blazewon22/)    •  [11 days ago](https://simplystatistics.org/2017/08/29/data-science-on-a-chromebook/#comment-3568272670)

Just came across your blog as I am pondering getting the new PixelBook. So would there be any savings on the $35/mo cost($420 year) if you were using a Mac or Windows 10 device?

    - [−](https://disqus.com/embed/comments/?base=default&f=simplystatsgithub&t_u=http%3A%2F%2Fsimplystatistics.org%2F2017%2F08%2F29%2Fdata-science-on-a-chromebook%2F&t_d=Data%20Science%20on%20a%20Chromebook%20%C2%B7%20Simply%20Statistics&t_t=Data%20Science%20on%20a%20Chromebook%20%C2%B7%20Simply%20Statistics&s_o=default#)
    - [****](https://disqus.com/embed/comments/?base=default&f=simplystatsgithub&t_u=http%3A%2F%2Fsimplystatistics.org%2F2017%2F08%2F29%2Fdata-science-on-a-chromebook%2F&t_d=Data%20Science%20on%20a%20Chromebook%20%C2%B7%20Simply%20Statistics&t_t=Data%20Science%20on%20a%20Chromebook%20%C2%B7%20Simply%20Statistics&s_o=default#)

-

[![Avatar](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/disqus_4mVbYXlveY/)

 [Syed Khan](https://disqus.com/by/disqus_4mVbYXlveY/)    •  [a month ago](https://simplystatistics.org/2017/08/29/data-science-on-a-chromebook/#comment-3515554038)

How do you include non or semi-structured data for data analytics?

    - [−](https://disqus.com/embed/comments/?base=default&f=simplystatsgithub&t_u=http%3A%2F%2Fsimplystatistics.org%2F2017%2F08%2F29%2Fdata-science-on-a-chromebook%2F&t_d=Data%20Science%20on%20a%20Chromebook%20%C2%B7%20Simply%20Statistics&t_t=Data%20Science%20on%20a%20Chromebook%20%C2%B7%20Simply%20Statistics&s_o=default#)
    - [****](https://disqus.com/embed/comments/?base=default&f=simplystatsgithub&t_u=http%3A%2F%2Fsimplystatistics.org%2F2017%2F08%2F29%2Fdata-science-on-a-chromebook%2F&t_d=Data%20Science%20on%20a%20Chromebook%20%C2%B7%20Simply%20Statistics&t_t=Data%20Science%20on%20a%20Chromebook%20%C2%B7%20Simply%20Statistics&s_o=default#)

-

[![Avatar](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/petrsimecek/)

 [Petr Simecek](https://disqus.com/by/petrsimecek/)    •  [2 months ago](https://simplystatistics.org/2017/08/29/data-science-on-a-chromebook/#comment-3506034322)

I believe you can save additional 10-15$/month if you switch from Digital Ocean to Amazon EC2 or Google Cloud. Digital Ocean is easy to use but unfortunately it charges you for stopped machines. For other services you pay only if the machine is running (+ a few pennies for storage). This is my post how to set up AWS with Jupyter Notebook that way [http://simecek.xyz/blog/201...](http://disq.us/url?url=http%3A%2F%2Fsimecek.xyz%2Fblog%2F2017%2F02%2F17%2Fdata-science-amazon-vm-with-start%2Fstop-functionality%2F%3Az7_Ki3EA2LSIOn0cattBKAawsr0&cuid=4023757) Setting up VM with RStudio or Shiny Server is analogical. You can even SSH to your linux machine using Secure Shell extension of Chrome.

    - [−](https://disqus.com/embed/comments/?base=default&f=simplystatsgithub&t_u=http%3A%2F%2Fsimplystatistics.org%2F2017%2F08%2F29%2Fdata-science-on-a-chromebook%2F&t_d=Data%20Science%20on%20a%20Chromebook%20%C2%B7%20Simply%20Statistics&t_t=Data%20Science%20on%20a%20Chromebook%20%C2%B7%20Simply%20Statistics&s_o=default#)
    - [****](https://disqus.com/embed/comments/?base=default&f=simplystatsgithub&t_u=http%3A%2F%2Fsimplystatistics.org%2F2017%2F08%2F29%2Fdata-science-on-a-chromebook%2F&t_d=Data%20Science%20on%20a%20Chromebook%20%C2%B7%20Simply%20Statistics&t_t=Data%20Science%20on%20a%20Chromebook%20%C2%B7%20Simply%20Statistics&s_o=default#)

-

[![Avatar](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/evangelostzimopoulos/)

 [Evangelos Tzimopoulos](https://disqus.com/by/evangelostzimopoulos/)    •  [2 months ago](https://simplystatistics.org/2017/08/29/data-science-on-a-chromebook/#comment-3505361492)

Has anyone tried Rkward ([https://www.rollapp.com/app...](https://disq.us/url?url=https%3A%2F%2Fwww.rollapp.com%2Fapp%2Frkward%29%3AEW6pfjIXipuIr0RMF_-Nkfo6eaY&cuid=4023757), I was trying to find something light to run on a browser for my Chromebook and seems to have everything including a GUI for beginners with all the backend support of the full command prompt of R for more advanced users? WIth basic free subscription seems to be ok with option to upgrade for $6/month.

    - [−](https://disqus.com/embed/comments/?base=default&f=simplystatsgithub&t_u=http%3A%2F%2Fsimplystatistics.org%2F2017%2F08%2F29%2Fdata-science-on-a-chromebook%2F&t_d=Data%20Science%20on%20a%20Chromebook%20%C2%B7%20Simply%20Statistics&t_t=Data%20Science%20on%20a%20Chromebook%20%C2%B7%20Simply%20Statistics&s_o=default#)
    - [****](https://disqus.com/embed/comments/?base=default&f=simplystatsgithub&t_u=http%3A%2F%2Fsimplystatistics.org%2F2017%2F08%2F29%2Fdata-science-on-a-chromebook%2F&t_d=Data%20Science%20on%20a%20Chromebook%20%C2%B7%20Simply%20Statistics&t_t=Data%20Science%20on%20a%20Chromebook%20%C2%B7%20Simply%20Statistics&s_o=default#)

-

[![Avatar](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/chrismihale/)

 [Chris Mihale](https://disqus.com/by/chrismihale/)    •  [2 months ago](https://simplystatistics.org/2017/08/29/data-science-on-a-chromebook/#comment-3501566114)

Thank you for starting this discussion. Have been wondering for a while if I could use my Chromebook (primary day-to-day usage) in a Data Science role.

    - [−](https://disqus.com/embed/comments/?base=default&f=simplystatsgithub&t_u=http%3A%2F%2Fsimplystatistics.org%2F2017%2F08%2F29%2Fdata-science-on-a-chromebook%2F&t_d=Data%20Science%20on%20a%20Chromebook%20%C2%B7%20Simply%20Statistics&t_t=Data%20Science%20on%20a%20Chromebook%20%C2%B7%20Simply%20Statistics&s_o=default#)
    - [****](https://disqus.com/embed/comments/?base=default&f=simplystatsgithub&t_u=http%3A%2F%2Fsimplystatistics.org%2F2017%2F08%2F29%2Fdata-science-on-a-chromebook%2F&t_d=Data%20Science%20on%20a%20Chromebook%20%C2%B7%20Simply%20Statistics&t_t=Data%20Science%20on%20a%20Chromebook%20%C2%B7%20Simply%20Statistics&s_o=default#)

-

[![Avatar](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/dr_franklund/)

 [Dr_Franklund](https://disqus.com/by/dr_franklund/)    •  [2 months ago](https://simplystatistics.org/2017/08/29/data-science-on-a-chromebook/#comment-3495698445)

I believe that Paperpile is not free (after 30 days). However, your costs of ~$45 per month are appealing. I might have to try a Chromebook again. I've also been exploring what sorts of data science can be done with just a Raspberry Pi.

    - [−](https://disqus.com/embed/comments/?base=default&f=simplystatsgithub&t_u=http%3A%2F%2Fsimplystatistics.org%2F2017%2F08%2F29%2Fdata-science-on-a-chromebook%2F&t_d=Data%20Science%20on%20a%20Chromebook%20%C2%B7%20Simply%20Statistics&t_t=Data%20Science%20on%20a%20Chromebook%20%C2%B7%20Simply%20Statistics&s_o=default#)
    - [****](https://disqus.com/embed/comments/?base=default&f=simplystatsgithub&t_u=http%3A%2F%2Fsimplystatistics.org%2F2017%2F08%2F29%2Fdata-science-on-a-chromebook%2F&t_d=Data%20Science%20on%20a%20Chromebook%20%C2%B7%20Simply%20Statistics&t_t=Data%20Science%20on%20a%20Chromebook%20%C2%B7%20Simply%20Statistics&s_o=default#)

-

[![Avatar](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/lightweight/)

 [lightweight](https://disqus.com/by/lightweight/)    •  [2 months ago](https://simplystatistics.org/2017/08/29/data-science-on-a-chromebook/#comment-3495159293)

I recommend Jitsi Meet to replace Google Hangouts. It's WebRTC-based, but end-to-end encrypted, and a 100% open source stack. Free to use the reference instance of the service too (or you could set up your own JitsiMeet server, e.g. on a DO host) - just go to [https://meet.jit.si/](https://disq.us/url?url=https%3A%2F%2Fmeet.jit.si%2F%3A038XIg7PH2ZtIoaJMeqxnKIzHME&cuid=4023757)[nameofyourdesiredroom] - just give that URL to anyone else you want to meet with. Works great.

Also, I prefer open source messaging software to Slack, where, to communicate with you, others have to sign their Ts and Cs... I use Rocket.Chat (but many other good open source options exist). I've written up how to set up Rocket.Chat - [https://tech.oeru.org/docke...](https://disq.us/url?url=https%3A%2F%2Ftech.oeru.org%2Fdocker-compose-better-way-deploy-rocketchat-wekan-and-mongodb%3A7nsRKE3v2c2hpYujROMg-xXCUW8&cuid=4023757) (you'll find other open source platform how-tos on the same site. Note: it's all non-profit, open source, and CC-licensed)

Actually, you could use NextCloud ([https://nextcloud.org](https://disq.us/url?url=https%3A%2F%2Fnextcloud.org%3An6g_6s_X6eTCQ1nS3fIgmwObFoU&cuid=4023757)) to replace Document Hub, and you could probably replace Google Docs with Collabora Office Online (integrated with NextCloud) - Collabora provides a browser-based collaborative editing front-end for LibreOffice, which is far more full-featured than Google Docs. I'll write up another how-to on how to set that all up.

    - [−](https://disqus.com/embed/comments/?base=default&f=simplystatsgithub&t_u=http%3A%2F%2Fsimplystatistics.org%2F2017%2F08%2F29%2Fdata-science-on-a-chromebook%2F&t_d=Data%20Science%20on%20a%20Chromebook%20%C2%B7%20Simply%20Statistics&t_t=Data%20Science%20on%20a%20Chromebook%20%C2%B7%20Simply%20Statistics&s_o=default#)
    - [****](https://disqus.com/embed/comments/?base=default&f=simplystatsgithub&t_u=http%3A%2F%2Fsimplystatistics.org%2F2017%2F08%2F29%2Fdata-science-on-a-chromebook%2F&t_d=Data%20Science%20on%20a%20Chromebook%20%C2%B7%20Simply%20Statistics&t_t=Data%20Science%20on%20a%20Chromebook%20%C2%B7%20Simply%20Statistics&s_o=default#)

## Also on **Simply Statistics**

- [

### Specialization and Communication in Data Science

    - 5 comments •

    - 2 months ago

[Neelanshi— Those are some amazing analogies, sir. Like the separation between the owners and managers of the company there is a proper need to …](http://disq.us/?url=http%3A%2F%2Fsimplystatistics.org%2F2017%2F09%2F11%2Fspecialization-and-communication-in-data-science%2F&key=uKcu2Nl82M_AGrp5FwyHFw)](http://disq.us/?url=http%3A%2F%2Fsimplystatistics.org%2F2017%2F09%2F11%2Fspecialization-and-communication-in-data-science%2F&key=uKcu2Nl82M_AGrp5FwyHFw)

- [

### Deep Dive - Y. Ogata's Residual Analysis for Point Processes

    - 3 comments •

    - 2 months ago

[channelclemente—I wonder if some interesting way such a method might not be useful in analyzing hitting in baseball analysis?](http://disq.us/?url=http%3A%2F%2Fsimplystatistics.org%2F2017%2F09%2F04%2Fdeep-dive-ogata%2F&key=6EHQXBnbuwCBXBJ4CWZeDg)](http://disq.us/?url=http%3A%2F%2Fsimplystatistics.org%2F2017%2F09%2F04%2Fdeep-dive-ogata%2F&key=6EHQXBnbuwCBXBJ4CWZeDg)

- [

### Moon Shots Cost More Than You Think

    - 1 comment •

    - 2 months ago

[deathisastar—The metaphor itself if problematic. Sending astronauts to the moon is an engineering challenge. Cancer is far more complicated.](http://disq.us/?url=http%3A%2F%2Fsimplystatistics.org%2F2017%2F09%2F07%2Fmoon-shots-cost-more-than-you-think%2F&key=QxVkB0MlzYcu6T15G6IAQw)](http://disq.us/?url=http%3A%2F%2Fsimplystatistics.org%2F2017%2F09%2F07%2Fmoon-shots-cost-more-than-you-think%2F&key=QxVkB0MlzYcu6T15G6IAQw)

- [

### Don't use deep learning your data isn't that big

    - 19 comments •

    - 5 months ago

[Andrew Beam—I wrote up my thoughts and analysis on this if anyone is interested: http://beamandrew.github.io...](http://disq.us/?url=http%3A%2F%2Fsimplystatistics.org%2F2017%2F05%2F31%2Fdeeplearning-vs-leekasso%2F&key=nX4SPuYpi59xRr-_lPOPMQ)](http://disq.us/?url=http%3A%2F%2Fsimplystatistics.org%2F2017%2F05%2F31%2Fdeeplearning-vs-leekasso%2F&key=nX4SPuYpi59xRr-_lPOPMQ)

- [Powered by Disqus](https://disqus.com/)
- [*✉*Subscribe*✔*](https://disqus.com/embed/comments/?base=default&f=simplystatsgithub&t_u=http%3A%2F%2Fsimplystatistics.org%2F2017%2F08%2F29%2Fdata-science-on-a-chromebook%2F&t_d=Data%20Science%20on%20a%20Chromebook%20%C2%B7%20Simply%20Statistics&t_t=Data%20Science%20on%20a%20Chromebook%20%C2%B7%20Simply%20Statistics&s_o=default#)
- [*d*Add Disqus to your site](https://publishers.disqus.com/engage?utm_source=simplystatsgithub&utm_medium=Disqus-Footer)
- [*🔒*Privacy](https://help.disqus.com/customer/portal/articles/466259-privacy-policy)