My First Year as a Data Scientist

### My First Year as a Data Scientist

[March 28, 2020](https://codebuildrepeat.blogspot.com/2020/03/my-first-year-as-data-scientist.html)

I was very fortunate to be given the opportunity by my employer to change role from a full-stack software developer to data scientist with the in-house Data Team. I've now spent over a year in this new data science role and thoroughly enjoy the different challenges it brings over software development. I wanted to write this blog post to firstly help me reflect on what I've been doing over the past year: what changes I had to undergo, what I did well, what I could improve on. And, secondly to help others in a similar situation to me - either thinking about transitioning or already transitioning by writing about some of the pitfalls and challenges I've had.

Before I start, to elaborate on my background a little bit more: I haven't always been a software developer. I have completed both a Masters and PhD in Computer Science. So I didn't go into the move completely blind, I did have some previous experience of tools, models and methodologies to rely on. But I have also been a developer for almost 8 years. So things have changed quite a bit since my thesis.

This post is split into two parts. The things that went well (The Good) and the things that didn't go so well (The Bad). For those just interested in the outcomes please see the summary at the end.

## The Good

### Python and R

At the very beginning of my role change, I was undecided about whether to use Python and/or R in my project work. So initially I investigated using both, learning the two languages and using a combination of the two in my project pipeline.

R very much reminds me of Matlab, which I used exclusively for my Masters thesis and partially for my PhD thesis, in both the interface you use to write and execute code (I tried out both R Studio and the R plugin for Visual Studio) and the way you have to think about program construction and data manipulation. Comparing R to other programming languages I've used (I've used C# a lot for software development over the years), you have to think about things differently. Everything is a lot more data-centric and you don't interact with data in the same sort of way. In R there are: lists, matrices, vectors, arrays and data frames. All of which have a different purpose and you need to learn which ones to use when. There's also a marked difference in R's syntax when compared to, for example, C# which didn't help me initially. I'm not saying that R is bad, just that it's been nearly 10 years since I was neck-deep in using Matlab and that inbetween time spent as a developer has conditioned by brain to work in a different way and I now naturally think about things a bit differently.  Because of these differences, I found R much harder to pick up and use in a meaningful way early on in my data science role.

Having been a developer using C# for 8 years, I found Python a lot easier to pickup and use "out of the box" than R. Again, this is probably just because of the way my brain has been trained to work now after 8 years of being of developer using C# daily. The syntax is much more similar to C# than R and so I just picked it up a lot quicker than R.

Whilst using both, I also couldn't find much discernible difference between the two, especially with all the libraries that are available for both. I found with the work that I was doing they pretty much had the same capability, being able to produce the same results even if through the use of imported libraries. Also, including both got a little confusing for me whilst I was still trying to figure out what my "pipeline" was. Just the way my brain works now after being a developer for so long means Python was easier to use.

Given the above, I quickly abandoned learning and using R and just focused on Python. This helped me to generate results more quickly as I had to spend less time reading up on a new syntax and made my pipeline easier to follow - keeping things simple (which I'm always an advocate for). This also helped because there were lots of other changes in the role too that I had to cope with. So, doing this I minimised the changes. I'm sure that there are numerous opinions on this. About which one of these to use and when. But for me, making the transition from developer to data scientist I've found Python a lot easier to pick up and get going with. Especially in the early days of my new role where I wanted to get going quickly and producing results. So, my time spent as a developer meant that I was able to get up and running with Python quicker than with R and I couldn't really find any discernible difference between them in terms of what they can output. I've put this down as something that went well, because I made this decision pretty early on in the job swap and I'm still yet to find a use case in my work that indicates it was an incorrect choice and the time saving I've made not having to learn all the intricacies of R meant I could get on with my job quicker.

### Documentation

Document everything. I mean everything: from model hyper-parameters to where and how you got training data to rationale for making choices throughout a project. Also, write the documentation in a ordered, logical way. A good tip to achieve this is, if you are just writing it for yourself (as in my case being the sole data scientist), is to pretend that you are writing it for someone else to read.

Further, be strict with yourself when documenting. Don't wait to write something down and don't take shortcuts. If you do, by the time you get round to writing down (if you ever do) you may have forgotten some of the detail that you need to include. So, just document something when you do it, don't delay. I don't consider a ticket of work done (I work in an agile way, completing tickets of work within a sprint) until the documentation has been completed.

I took this approach to documentation from the beginning and it's been a life saver.

One of the things that I've found is that, even in a medium sized business, it can take a while for knowledge of a project you've done to be disseminated - interested parties will have other work on and may come back to my work later. I've been asked questions about a project months after I've finished it and haven't been able to answer them off the top of my head. But I've been able to reference my documentation and provide a detailed answer pretty much instantly. For example, months after finishing a project, off the back of a conversation with another manager I was showing them some work I'd done and they asked what was the training set size was and what date range had I used to get my data. I didn't know off the top of my head. But I did know that I had written it down and where. So I was able to load the documentation and show them there and then.

Another situation I've found myself in is that business priorities will change, so you could find yourself in a situation where you end up switching between unfinished projects. And when you get back to a previously started project, having complete documentation helps you to pick up where you left off a lot easier.

## The Bad

### Data Storage

Reflecting on the previous year, one of the things that didn't go so well was the way that I worked with data (pretty critical for a data scientist). I essentially reverted to the way I worked with data during my PhD, when I didn't have any experience using databases. That is, I started using flat files (specifically CSVs). I would store initial data extracted from production databases, intermediate cleansed data, features calculated from cleansed data, experimental results, analysis of the experimental results (and more) all in CSVs. And every step of my pipeline would read in the file created by the previous step and output to a new file using a Python script to load, transform and save the data.

By storing everything in these files all over my hard drive and interacting with the data via Python scripts, several problems reared their heads:

- Sometimes, amongst the sea of files, it was hard to find the exact file I was looking for. Even with documenting the contents and location of files, it was difficult sometimes to find the exact one that I wanted just because there ended up being so many.
- I always seemed to be writing lines of Python that would read data from file, or write data to file. In fact, every script was starting to have one (and often more) sets of these read/write lines. Basically I was spending my life writing this file access code over and over again, ending up with lots of (effectively) duplicated code that didn't really do anything towards the task I was currently working on.
- Just wanting to quickly pull together some stats from data seemed laborious: read the data in, aggregate some stats, write the stats out, look at the stats in the file.
- Some files were huge in size and so very difficult to work with (opening a 10GB+ file in notepad doesn't work very well, or at all, even more annoying if you just want to see the top 10 lines).

It actually took me a (very) long time over this first year to spot the (now obvious) answer to the dense jungle of files on my disk ... SQL.

I had used SQL before in my pre-data scientist life as a developer. But it took a while to dawn on me that this was the solution to my problem. Once I figured out this was the solution I spent a significant amount of time learning more about SQL as I had only really touched upon SQL in my developer life. Specifically, I learnt about querying data (especially the more advanced parts I had never used before) and the basics of setting up and maintaining databases. I even managed to pass two Microsoft SQL exams. I am now an advocate for doing everything possible in SQL. I store all project data in a SQL database and do as much of the querying and data manipulation that I can without having to leave the confines of SQL. I use the rule: if I can do it in SQL, I do it in SQL. For everything I can't do in SQL I use Python (for example actual model training and execution). Which does a raise a side point: you will need to learn how to use Python libraries like [SQLAlchemy](https://www.sqlalchemy.org/) to read and write data from SQL in Python.

My post-SQL epiphany life is now much easier:

- All project data is stored in one, easy to find place.
- There's no more duplicated code for reading and writing to files.
- I can query data quickly and generate stats from the data with ease.
- I can very easily look at large amounts of data (especially the top X of something).
- Bonus benefits include: it's now much easier to relate different data together - it's already in a **relational** database.
- Also security is now improved: storing data locally on disk is potentially catastrophic. Now it's tucked away safely on a server somewhere.

So, I would highly recommend learning some flavour of SQL and using it.

### Presentations

Another thing that didn't go so well was some of the presentations I gave. One change moving from developer to data scientist I've encountered is an increase in presentations I've delivered. These presentations have varied from technical demos to devs, to project reports to business stakeholders, to discussing project work with other departments inside the business and even presenting work to third parties outside of the business.

Want didn't go so well about these presentations is that I didn't always target the presentations appropriately to the audience. It wasn't all bad. The tech demos given to fellow devs were positioned correctly. I found these a lot easier to position as we share a common technical background and can speak more or less the same language. The other types of presentations were harder to position, which (unfortunately) I only tended to figure out during the presentations when I realised I had "lost" my audience.

To help explain this better, in my situation, audiences can be divided up into the four categories already mentioned, and I can arrange them in the following order of increasing difficultly to present to, starting at the easiest (left) and ending with the hardest (right):

- devs, stakeholders, other departments and external.

Interestingly, I can also label those audiences towards the left as being most technical and those audiences at the right as being more "salesy", with there being a transition between these two as you move from left to right. I naturally find audiences towards the left easiest to prepare for and to present to - they have the most understanding of either the tech I'm using or the business domain I'm working in. But I naturally find the audiences towards the right the hardest to prepare for and present to, as they tend to have the least knowledge. And what I've done in the past with these "right hand" audiences is to jump straight into the technical detail of the work, as I would when presenting to the "left hand" audiences. However, this worked out badly because they hadn't necessarily had any experience of any data science or machine learning previously, which meant a lot of the concepts I was talking about didn't make much sense. They had little to no context. So they weren't entirely sure what I was talking about. It would have been a lot better if, for these audiences, I spent the time introducing a lot more of the background to the work I was doing. And even some audiences, it would have been beneficial to introduce to them the concept of machine learning, why we would want to use it and why it's cool. Sometimes it would have even been a good idea for me to not go into the technical detail as much - just giving them the broad brush strokes of the technical work.

After reflecting on this, I now, when preparing a presentation, think about the audience that I'm delivering to a lot more. Specifically, I think about what the audience may or may not already know and what I need to present to them to help frame the work I'm discussing and to what level of detail I should to go into. So that they can understand the work I'm talking about and take something away from the presentation. To this end, some useful questions I've developed to ask myself when preparing a presentation are:

- What does the audience know about the domain of data science?
- What does the audience know about the problem I'm trying to solve/the question I'm trying to answer?
- What does the audience know about the techniques I'm using?
- Is the audience interested in the technical detail of my approach and/or the results?

### Planning

Planning you're work as a data scientist is going to be difficult, compared to when you were planning your work as a dev. As a dev, work is pretty straightforward to plan and estimate. You generally know what you are trying to achieve and how you are going to achieve it. For context, when I was a dev I was sprinting using agile ceremonies. So tickets of work would be estimated, planned and lined up ready to go. Using these techniques, if work didn't make sense or you are unclear how to proceed with it, it doesn't make it into your sprint and you don't work on it. Because you can't estimate it, because there are unknowns, you wait until all the questions have been answered before you commit to the work.

With data science work, the work isn't as straightforward as this. You will not always know ahead of time what will work for a given problem. You will not always know what type of model will be the most accurate. These points and similar are counter to the point just made that when you are a dev you only accept work into a sprint once you have all the questions about it have been answered. You can't always do this as a data scientist because your work **is** answering the questions. Also, the problem you are tackling may change as you work on a project and explore the data. So X weeks of plans you have already made for your work may be thrown out of the window.

In terms of planning, I like to think of dev work as a straight line - you know what you are doing and how to get there and I like to think of data science work as a branching tree, with different avenues that you may need to follow and dead ends that you may hit.

Generally, it will be easy to plan your data science work in the short term. This will be things like current models you are training and testing - the next week or twos worth of work. However, planning in the long term is a lot harder. It's not always possible to know what will work and what won't ahead of time. That's why we run experiments and test things, without having to do that a lot of the job of data science wouldn't exist.

On a final point about this: be prepared to spend time on work that won't be fruitful, it's not the end of the world if something doesn't work.

### Answering the Right Question

Over the year (and this has tripped me up a bit) I've figured out that a key part of data science work is about answering questions, but more importantly answering the **right **question. As I said, this has tripped me up a few times, where I was answering a question. But not answering the question the stakeholder actually wanted answering. This happened because of different terminology between the business language used by the stakeholder and the technical language I was using, where we meant different things by the same the words.

The way that I've gone about fixing this is to do a phase before I do the actual work of the project (what I now call the 'pre-project' work) where I take initial requirements and information gathered from the stakeholder, do some initial analysis of the potential data that will be used for the project and then feedback this analysis with the stakeholder. I work in an agile way, so I try to have a deliverable for each sprint that I work in and share this deliverable with the stakeholder. That way I can build up a feedback loop with the stakeholder, of me showing them something (and asking them questions if required) and this builds up a dialogue that helps refine what the actual question is that needs to be answered for the project. This helps for all stages of the project, not just the initial stage. As you show the stakeholder results of what you are working on that can spark different ideas from them as well as different input that they may have not considered before. And helps you get to the right question to answer.

So a key skill I've had to develop over the year is this interaction with a stakeholder, digging down into what it is that they really want.

## Summary (tl;dr)

- Python was easier to pick up than R, because of it's similarity to other programming languages encountered as a developer.
- Write everything down, when you do it.
- Learn how to use relational databases (e.g. SQL) to query, manipulate and store data, don't use flat files.
- You are going to be doing a lot more presentations, not only reporting your findings to stakeholders of the projects you are working on but also to other members of the company and others, even outside your company. You'll need to improve you're presentation skills and work on delivery to a range of audiences - technical and/or business-minded.
- Planning work isn't straightforward because you don't always know what is going to work and what isn't - be prepared to spend time on things that don't work.
- Spend time figuring out what it is you are actually trying to do in a project, don't just jump straight in. Building a feedback loop with the stakeholder is valuable for this.

## The End

[Data Science](https://codebuildrepeat.blogspot.com/search/label/Data%20Science)[Developer to Data Scientist](https://codebuildrepeat.blogspot.com/search/label/Developer%20to%20Data%20Scientist)[First Year](https://codebuildrepeat.blogspot.com/search/label/First%20Year)