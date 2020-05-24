Advice for non-traditional data scientists  · Gordon Shotwell

# Advice for non-traditional data scientists

29 Aug, 2017 · by Gordon Shotwell · Read in about 9 min · (1749 Words)

I have a pretty strange background for a data scientist. In my career I’ve sold electric razors, worked on credit derivatives during the 2008 financial crash, written market reports on orthopaedic biomaterials, and practiced law. I started programming in R during law school, partly as a way to learn more about data visualization and partly to help analyze youth criminal justice data. Over time I came to enjoy programming more than law and decided to make the switch to data work about three years ago. Since then I’ve freelanced a bit, worked as a Data Scientist at Upworthy, and now am a Senior R Developer at a survey company called Crunch.io.

When I started, I honestly didn’t have any particular skills or capacity which would have made data science a good career choice. I studied philosophy in undergrad, and while I had done a bit of statistics, it wasn’t something I would have said I was comfortable with. All I really had was an interest and the capacity to learn new things. If you’re in a similar boat, here is some advice about the process:

### Emulate one or two people who know what they’re doing.

There is a huge diversity of tools and techniques for approaching data work, and if you half-learn a lot of different techniques you won’t be able to fully understand or accomplish any one technique. My recommendation is to pick one or two people who work in the field and who speak in a language you understand and try to emulate them. In my case I really focused on learning the R programming language, and picked a few R programmers to follow. I listened to all of their online talks, read their blogs and follows their activity on Github. This meant that I ended up with a deep understanding of a few small areas of the language and missed out on a lot of other areas. For instance, I learned `dplyr` really well, but didn’t learn much about object oriented programming. It’s good to try to develop depth of knowledge, rather than breadth, because when you know one thing very well you can usually apply that knowledge to other areas. A shallow understanding of many areas won’t help you tackle advanced problems in a specialized area.

### “Learning to code” and “learning statistics” are terrible goals because they have no end point.

When you are learning a new skill, it’s important to have specific criteria for success. This helps keep you on track and also helps mitigate imposter syndrome. You don’t want to move the goalposts as you develop your understanding. From this perspective, “learning to code” and “learning statistics” are terrible goals, because there’s always more to learn about these fields. It’s better to have smaller goals, like, “Learn to write a function in R,” or, “Be able to fit a linear model,” because those things can be accomplished. Goals that can be accomplished are good things because you can accomplish them, rather than being constantly reminded how far you have to go.

### Focus on trajectory

We naturally compare ourselves to others and tend to judge our own skills in terms of other people’s skills. The problem with this is that as our understanding improves, we tend to change our measures of comparison to more and more accomplished people. This is especially a problem when we compare our own general understanding of an area to that of specialists. For instance, you might have a good general understanding of neural networks, but if you compare yourself to someone who studies them full time, your understanding will obviously be pretty paltry. This kind of comparative thinking leads to always feeling insufficient, because no matter who you are or how much you know, there is always somebody who will know more.

A better approach is to focus on trajectory. Ask whether you are making progress rather than whether you are relatively successful. Think about what you knew yesterday and feel good if you learned a bit more today. Over time that approach will lead to much better understanding with much less suffering.

### Follow Kind Experts

Every field has experts, and many of those experts are assholes. Indeed in our society we frequently use lack of empathy or kindness as a sign of intelligence or accomplishment. We call these people “geniuses,” or “rockstars,” and try to forgive their personal faults by pointing to their intellectual accomplishments. I think you should ignore these people and instead try to find experts who have a genuine concern for other people. There are two reasons for this.

1. Kind experts will help you learn. This is common sense. If somebody has a genuine concern with helping other people understand an area, the resources they produce will be better at teaching other people how to do that thing. Moreover the community of learners that surrounds these people is going to be supportive, rather than combative, and so engaging with that community will be a good experience

2. Kind people know more than unkind people. This is less intuitive, but just as important. Experts who are genuinely concerned with other people tend to create environments where other people help them. A good example of this is Hadley Wickham’s Twitter feed. What you notice following him is that he is for the most part very kind in how he communicates with other people. The result of this is that he has developed a powerful network of people who answer his questions, test and provide feedback on his software projects, and grow into kind experts themselves. Most of the really productive developers I have interacted with have these same kinds of networks, and the reason they have them is that they spend a lot of time and energy supporting people, rather than belittling them. No matter how brilliant a brilliant jerk is, they will always always lose out to a group of people working together on a problem.

### Try to Ignore Boundary Setting Behaviour

Boundary setting behaviour is when people who are part of a group attempt to draw the lines around that group to include themselves and exclude you. For instance, programmers sometimes say things like, “Real programmers use the command line,” or, “You really need to learn Scala if you want to be a programmer.” The motivation for this is not to accurate express the boundaries of the discipline, but instead to make themselves feel better about their own skills. Often, out of insecurity, people will express the importance of their own skills and try to minimize the importance of skills they lack. About half of the stuff you read is written to address that insecurity rather than to help you learn. If possible, you should try to avoid this kind of advice.

But you will definitely encounter it. You will get rejected from jobs, or made to feel like an idiot, because of this kind of behaviour, and there’s nothing you can really do about that. Applying for data science jobs from a non-traditional background, I frequently encountered people who believe all of the following:

1. Data manipulation, visualization, and communication are the most common data science tasks;

2. We should focus on building teams with distinct capacities rather than trying to find one person who knows how to do everything;

3. Most of the time you want a simple linear model, not a complex machine learning algorithm;

4. There is a labour shortage for data science roles and we should expand the applicant pool; and

5. It is absolutely essential that you have an advanced degree in statistics to apply for a job at my company

Now, there’s a way that all of these things can be true at the same time, but more likely than not #1-4 describe a lot of the actual job requirements, and #5 is boundary setting. But when you apply for and get rejected from the job you can’t really ignore that behaviour; you have to deal with it emotionally.

One of the key ways you can recognize boundary setting behaviour is when people start to equate being a member of a profession with being a particularly good member of that profession. For instance someone might tell you that you be a real data scientist you need to have a PHD in statistics, and have mastered R, Python, and big-data query languages, and be an exceptional written and verbal communicator. Having these skills probably makes you an extremely skilled data scientist, but are they really hard boundaries around the profession? I’m not so sure. In most cases we talk about jobs based on the job title, rather than the job requirements. If you’re a baseball player who stands near first base we call you a first baseman, if you write for a living we call you a writer. These things are true even if you write trashy science fiction novels or are a terrible fielder. The boundaries of the profession are set by the market, not by your skills, and so you can be a good or bad example of the profession without having that change your membership in that profession. I think the same thing should be true of programming. Can you get a job writing computer programs? Then you’re a programmer. Do you work with data for a living? You can probably call yourself a data scientist.

### Learn to Bounce Back

The main currency in learning a new skill is enthusiasm. Each time you have some success, you bank a bit of enthusiasm, and each time you experience challenges you lose a little bit of it. It is important to try to understand what helps you gain energy and enthusiasm, and what helps you lose it. Whenever you notice that you’re going into the red in the enthusiasm department, either take a break, or do something that helps you feel a bit better. Here are some of the things I do when I feel bleak about my abilities:

- Take a walk
- Take a nap
- Exercise for five minutes
- Answer easy stack overflow questions
- If I’m frustrated by a computer problem I copy and paste the examples and run them
- Meditate

I think the key to this is not so much what particular things you do to bounce back, but that you recognize when you are losing energy for a task, and take a break from learning.. Stress basically obliterates our ability to learn new things and so simply stopping for a bit is a powerful way to maintain our capacity for new skills.

 [ Previous](http://blog.shotwell.ca/2017/05/03/why-you-should-work-remotely-even-if-youre-not-remote/)  [Next](http://blog.shotwell.ca/2017/08/29/advice-for-non-traditional-data-scientists/)

## Comments