We analyzed thousands of technical interviews on everything from language to code style. Here’s what we found.

# We analyzed thousands of technical interviews on everything from language to code style. Here’s what we found.

Postedby[![user](../_resources/3badc68909727c56be06a9929bc30fb0.jpg)Aline Lerner](https://twitter.com/alinelernerLLC)on ** June 13th, 2017.

*Note: Though I wrote most of the words in this post, the legendary [Dave Holtz](https://twitter.com/daveholtz) did the heavy lifting on the data side. See more of his work on [his blog](http://daveholtz.net/).*

If you’re reading this post, there’s a decent chance that you’re about to re-enter the crazy and scary world of technical interviewing. Maybe you’re a college student or fresh grad who is going through the interviewing process for the first time. Maybe you’re an experienced software engineer who hasn’t even thought about interviews for a few years. Either way, the first step in the interviewing process is usually to read a bunch of online interview guides (especially if they’re written by companies you’re interested in) and to chat with friends about their experiences with the interviewing process (both as an interviewer and interviewee). More likely than not, what you read and learn in this first, “exploratory” phase of the interview process will inform how you choose to prepare moving forward.

There are a few issues with this typical approach to interview preparation:

- Most interview guides are written from the perspective of one company. While Company A may really value efficient code, Company B may place more of an emphasis on high-level problem-solving skills. Unless your heart is set on Company A, you probably don’t want to give too much weight to what they value.
- People lie sometimes, even if they don’t mean to. In writing, companies may say they’re language agnostic, or that it’s worthwhile to explain your thought process, even if the answer isn’t quite right. However, it’s not clear if this is actually how they act! We’re not saying that tech companies are nefarious liars who are trying to mislead their applicant pool. We’re just saying that sometimes implicit biases sneak in and people aren’t even aware of them.
- A lot of the “folk knowledge” that you hear from friends and acquaintances may not be based in fact at all. A lot of people assume that short interviews spell doom. Similarly, everyone can recall one long interview after which they’ve thought to themselves, “I really hit it off with that interviewer, I’ll definitely get passed onto the next stage.” In the past, [we’ve seen that people are really bad at gauging how they did in interviews](http://blog.interviewing.io/people-are-still-bad-at-gauging-their-own-interview-performance-heres-the-data/). This time, we wanted to look directly at indicators like interview length and see if those actually matter.

**Here at interviewing.io, we are uniquely positioned to approach technical interviews and their outcomes in a data-driven way. This time, we’ve opted for a quick (if not dirty) and quantitative analysis. In other words, rather than digging deep into individual interviews, we focused on easily measurable attributes that many interviews share, like duration and language choice.** In upcoming posts, we’ll be delving deeper into the interview content itself. If you’re new to our blog and want to get some context about how interviewing.io works and what interview data we collect, please take a look at the section called “The setup” below. Otherwise, please skip over that and head straight for the results!

The setup

[interviewing.io](http://www.interviewing.io/) is a platform where people can practice technical interviewing anonymously, and if things go well, unlock the ability to interview anonymously, whenever they’d like, with top companies like Uber, Lyft, and Twitch. The cool thing is that both practice interviews and real interviews with companies take place within the interviewing.io ecosystem. As a result, we’re able to collect quite a bit of interview data and analyze it to better understand technical interviews, the signal they carry, what works and what doesn’t, and which aspects of an interview might actually matter for the outcome.

Each interview, whether it’s practice or real, starts with the interviewer and interviewee meeting in a collaborative coding environment with voice, text chat, and a whiteboard, at which point they jump right into a technical question. Interview questions tend to fall into the category of what you’d encounter in a phone screen for a back-end software engineering role. **During these interviews, we collect everything that happens, including audio transcripts, data and metadata describing the code that the interviewee wrote and tried to run, and detailed feedback from both the interviewer and interviewee about how they think the interview went and what they thought of each other.**

If you’re curious, you can see what the feedback forms for interviewers and interviewees look like below — in addition to one direct yes/no question, we also ask about a few different aspects of interview performance using a 1-4 scale. We also ask interviewees some extra questions that we don’t share with their interviewers, and one of the things we ask is whether an interviewee has previously seen the question they just worked on.

[![Feedback form for interviewers](../_resources/46ac2193ce4777af4a871d52c1598824.png)](http://blog.interviewing.io/wp-content/uploads/2016/05/new-interviewer-feedback.png)

Feedback form for interviewers

[![Feedback form for interviewees](../_resources/e94c21197f23e48dea6375a8f6afbe83.png)](http://blog.interviewing.io/what-really-matters-in-technical-interviews-we-analyzed-thousands-of-interviews-on-everything-from-language-to-code-style-heres-what-we-found/hhttp://blog.interviewing.io/wp-content/uploads/2017/06/new-interviewee-feedback.png)

Feedback form for interviewees
The results

Before getting into the thick of it, it’s worth noting that the conclusions below are based on observational data, which means we can’t make strong causal claims… but we can still share surprising relationships we’ve observed and explain what we found so you can draw your own conclusions.

Having seen the interview question before
*“We’re talking about practice!”* -Allen Iverson

First thing’s first. It doesn’t take a rocket scientist to suggest that one of the best ways to do better in interviews is to… practice interviewing. There are a number of resources out there to help you practice, ours among them. One of the main benefits of working through practice problems is that you reduce the likelihood of being asked to solve something you’ve never seen before. Balancing that binary search tree will be much less intimidating if you’ve already done it once or twice.

We looked at a sample of ~3000 interviews and compared the outcome to whether the interviewee had seen the interview question before. You can see the results in the plot below.

FalseTrue0%10%20%30%40%50%60%70%

The effect of having already seen an interview questionInterviewee Has Seen QuestionSuccess Rate

[Download plot as a png]()
[Zoom]()[Pan]()
[Zoom in]()[Zoom out]()[Autoscale]()[Reset axes]()
[Toggle Spike Lines]()[Show closest data on hover]()[Compare data on hover]()
[Produced with Plotly](https://plot.ly/)

 [Edit chart](https://plot.ly/create/?fid=aline_interviewingio:942)

**Unsurprisingly, interviewees who had seen the question were 16.6% more likely to be considered hirable by their interviewer.** This difference is statistically significant (p < 0.001).[1](http://blog.interviewing.io/what-really-matters-in-technical-interviews-we-analyzed-thousands-of-interviews-on-everything-from-language-to-code-style-heres-what-we-found/#guide-fn1)

Does it matter what language you code in?

*“Whoever does not love the language of his birth is lower than a beast and a foul smelling fish.”* -Jose Rizal

You might imagine that different languages lead to better interviews. For instance, maybe the readability of Python gives you a leg up in interviews. Or perhaps the fact that certain languages handle data structures in a particularly clean way makes common interview questions easier. We wanted to see whether or not there were statistically significant differences in interview performance across different interview languages.

To investigate, we grouped interviews on our platform by interview language and filtered out any languages that were used in fewer than 5 interviews (this only threw out a handful of interviews). After doing this, we were able to look at interview outcome and how it varied as a function of interview language.

The results of that analysis are in the chart below. Any non-overlapping confidence intervals represent a statistically significant difference in how likely an interviewee is to ‘pass’ an interview, as a function of interview language. Although we don’t do a pairwise comparison for every possible pair of languages, the data below suggest that generally speaking, **there aren’t statistically significant differences between the success rate when interviews are conducted in different languages**.[2](http://blog.interviewing.io/what-really-matters-in-technical-interviews-we-analyzed-thousands-of-interviews-on-everything-from-language-to-code-style-heres-what-we-found/#guide-fn2)

CC++C#GoJavaJavascriptPythonRuby0%10%20%30%40%50%60%70%

How interview success ratevaries with interview languageLanguageSuccess Rate
[Download plot as a png]()
[Zoom]()[Pan]()
[Zoom in]()[Zoom out]()[Autoscale]()[Reset axes]()
[Toggle Spike Lines]()[Show closest data on hover]()[Compare data on hover]()
[Produced with Plotly](https://plot.ly/)

 [Edit chart](https://plot.ly/create/?fid=aline_interviewingio:944)

That said, one of the most common mistakes we’ve observed qualitatively is people choosing languages they’re not comfortable in and then messing up basic stuff like array length lookup, iterating over an array, instantiating a hash table, and so on. This is especially mortifying when interviewees purposely pick a fancy-sounding language to impress their interviewer. Trust us, wielding your language of choice comfortably beats out showing off in a fancy-sounding language you don’t know well, every time.

Even if language doesn’t matter… is it advantageous to code in the company’s language of choice?

*“God help me, I’ve gone native.”* -Margaret Blaine

It’s all well and good that, in general, interview language doesn’t seem particularly correlated with performance. However, you might imagine that there could be an effect depending on the language that a given company uses. You could imagine a Ruby shop saying “we only hire Ruby developers, if you interview in Python we’re less likely to hire you.” On the flip side, you could imagine that a company that writes all of their code in Python is going to be much more critical of an interviewee in Python – they know the ins and outs of the language, and might judge the candidate for doing all sorts of “non-pythonic” things during their interview.

The chart below is similar to the chart which showed differences in interview success rate (as measured by interviewers being willing to hire the interviewee) for C++, Java, and Python. However, this chart also breaks out performance by whether or not the interview language is in the company’s stack. We restrict this analysis to C++, Java and Python because these are the three languages where we had a good mixture of interviews where the company did and did not use that language. **The results here are mixed. When the interview language is Python or C++, there’s no statistically significant difference between the success rates for interviews where the interview language is or is not a language in the company’s stack. However, interviewers who interviewed in Java were more likely to succeed when interviewing with a Java shop (p=0.037).**

So, why is it that coding in the company’s language seems to be helpful when it’s Java, but *not* when it’s Python or C++? One possible explanation is that the communities that exist around certain programming languages (such as Java) place a higher premium on previous experience with the language. Along these lines, it’s also possible that interviewers from companies that use Java are more likely to ask questions that favor those with a pre-existing knowledge of Java’s idiosyncrasies.

C++JavaPython0102030405060708090

How success rate varieswith interview languageCompany uses languageCompany does not use languageLanguageSuccess Rate

[Download plot as a png]()
[Zoom]()[Pan]()
[Zoom in]()[Zoom out]()[Autoscale]()[Reset axes]()
[Toggle Spike Lines]()[Show closest data on hover]()[Compare data on hover]()
[Produced with Plotly](https://plot.ly/)

 [Edit chart](https://plot.ly/create/?fid=aline_interviewingio:950)

What about the relationship between what language you program in and how good of a communicator you’re perceived to be?

*“To handle a language skillfully is to practice a kind of evocative sorcery.”* -Charles Baudelaire

Even if language choice doesn’t matter that much for overall performance (Java-wielding companies notwithstanding), we were curious whether different language choices led to different outcomes in other interview dimensions. For instance, an extremely readable language, like Python, may lead to interview candidates who are assessed to have communicated better. On the other hand, a low-level language like C++ might lead to higher scores for technical ability. Furthermore, very readable or low-level languages might lead to correlations between these two scores (for instance, maybe they’re a C++ interview candidate who can’t explain at all what he or she is doing but who writes very efficient code). The chart below suggests that there isn’t really any observable difference between how candidates’ technical and communication abilities are perceived, across a variety of programming languages.

![](../_resources/8da88f8a4ecfb365a93f82a2868e288d.jpg)

**Furthermore, no matter what, poor technical ability seems highly correlated with poor communication ability – regardless of language, it’s relatively rare for candidates to perform well technically but not effectively communicate what they’re doing (or vice versa)**, largely (and fortunately) debunking the myth of the incoherent, fast-talking, awkward engineer.[3](http://blog.interviewing.io/what-really-matters-in-technical-interviews-we-analyzed-thousands-of-interviews-on-everything-from-language-to-code-style-heres-what-we-found/#guide-fn3)

Interview duration

*“It’s fine when you careen off disasters and terrifyingly bad reviews and rejection and all that stuff when you’re young; your resilience is just terrific.”* -Harold Prince

We’ve all had the experience of leaving an interview and just feeling like it went poorly. Often, that feeling of certain underperformance is motivated by rules of thumb that we’ve either come up with ourselves or heard repeated over and over again. You might find yourself thinking, “the interview didn’t last long? That’s probably a bad sign… ” or “I barely wrote anything in that interview! I’m definitely not going to pass.” Using our data, we wanted to see whether these rules of thumb for evaluating your interview performance had any merit.

First, we looked at the length of the interview. Does a shorter interviewer mean you were such a trainwreck that the interviewer just had to stop the interview early? Or was it maybe the case that the interviewer had less time than normal, or had seen in just a short amount of time that you were an awesome candidate? The plot below shows the distributions of interview length (measured in minutes) for both successful and unsuccessful candidates. **A quick look at this chart suggests that there is no difference in the distribution of interview lengths between interviews that go well and interviews that don’t — the average length of interviews where the interviewer wanted to hire the candidate was 51.00 minutes, whereas the average length of interviews where the interviewer did not was 49.95 minutes. This difference is not statistically significant.**[4](http://blog.interviewing.io/what-really-matters-in-technical-interviews-we-analyzed-thousands-of-interviews-on-everything-from-language-to-code-style-heres-what-we-found/#guide-fn4)

![interview_duration_plot](../_resources/491c73f6e1e127b305b7c8fed944aa83.png)

Amount of code written
*“Brevity is the soul of wit.”* -William Shakespeare

You may have experienced an interview where you were totally stumped. The interviewer asks you a question you barely understand, you repeat back to him or her “binary search what?”, and you basically write no code during your interview. You might hope that you could still pass an interview like this through sheer wit, charm, and high-level problem-solving skills. In order to assess whether or not this was true, we looked at the final character length of code written by the interviewee. The plot below shows the distributions of character length for both successful and unsuccessful. A quick look at this chart suggests that there is a difference between the two — interviews that don’t go well tend to have less code. There are two phenomena that may contribute to this. First, unsuccessful interviewers may write less code to begin with. Additionally, they may be more prone to delete large swathes of code they’ve written that either don’t run or don’t return the expected result.

02000400060008000

Is the amount of code written  correlated with interview outcome?Interviewer would hireInterviewer would not hireFinal interview submission length (characters)Number of interviews

[Download plot as a png]()
[Zoom]()[Pan]()
[Zoom in]()[Zoom out]()[Autoscale]()[Reset axes]()
[Toggle Spike Lines]()[Show closest data on hover]()[Compare data on hover]()
[Produced with Plotly](https://plot.ly/)

 [Edit chart](https://plot.ly/create/?fid=aline_interviewingio:954)

**On average, successful interviews had final interview code that was on average 2045 characters long, whereas unsuccessful ones were, on average, 1760 characters long.** That’s a big difference! This finding is statistically significant and probably not very surprising.

Code modularity

*“The mark of a mature programmer is willingness to throw out code you spent time on when you realize it’s pointless.”* -Bram Cohen

In addition to just look at *how much* code you write, we can also think about the type of code you write. Conventional wisdom suggests that good programmers don’t recycle code – they write modular code that can be reused over and over again. We wanted to know if that type of behavior was actually rewarded during the interview process. In order to do so, we looked at interviews conducted in Python[5](http://blog.interviewing.io/what-really-matters-in-technical-interviews-we-analyzed-thousands-of-interviews-on-everything-from-language-to-code-style-heres-what-we-found/#guide-fn5) and counted how many function definitions appeared in the final version of the interview. We wanted to know if successful interviewees defined more functions — while having more function handlers is not the definition of modularity, in our experience, it’s a pretty strong signal of it. As always, it’s impossible to make strong causal claims about this – it might be the case that certain interviewers (who are more or less lenient) ask interview questions that lend themselves to more or fewer functions. Nonetheless, it is an interesting trend to investigate!

The plot below shows the distribution of the number of Python functions defined for both candidates who the interviewer said they would hire and candidates who the interviewer said they would not hire. A quick look at this chart suggests that there *is* a difference in the distribution of function definitions between interviews that go well and interviews that don’t. Successful interviewees seem to define *more* functions.

05100%5%10%15%20%25%30%

Do successful intervieweeswrite more modular code?Interviewer would hireInterviewer would not hireNumber of functions definedPercentage of interviews

[Download plot as a png]()
[Zoom]()[Pan]()
[Zoom in]()[Zoom out]()[Autoscale]()[Reset axes]()
[Toggle Spike Lines]()[Show closest data on hover]()[Compare data on hover]()
[Produced with Plotly](https://plot.ly/)

 [Edit chart](https://plot.ly/create/?fid=aline_interviewingio:958)

**On average, successful candidates interviewing in Python define 3.29 functions, whereas unsuccessful candidates define 2.71 functions. This finding is statistically significant. The upshot here is that interviewers really do reward the kind of code they say they want you to write.**

Does it matter if your code runs?

*“Move fast and break things. Unless you are breaking stuff, you are not moving fast enough.”* -Mark Zuckerberg

*“The most effective debugging tool is still careful thought, coupled with judiciously placed print statements.”* -Brian Kernighan

A common refrain in technical interviews is that interviewers don’t actually care if your code runs – what they care about is problem-solving skills. Since we collect data on the code interviewees run and whether or not that code compiles, we wanted to see if there was evidence for this in our data. Is there any difference between the percentage of code that compiles error-free in successful interviews versus unsuccessful interviews? Furthermore, can interviewees actually still get hired, even if they make tons of syntax errors?

In order to get at this question, we looked at the data. We restricted our dataset to interviews longer than 10 minutes with more than 5 unique instances of code being executed. This helped filter out interviews where interviewers didn’t actually want the interviewee to run code, or where the interview was cut short for some reason. We then measured the percent of code runs that resulted in errors.[5](http://blog.interviewing.io/what-really-matters-in-technical-interviews-we-analyzed-thousands-of-interviews-on-everything-from-language-to-code-style-heres-what-we-found/#guide-fn5) Of course, there are some limitations to this approach – for instance, candidates could execute code that does compile but gives a slightly incorrect answer. They could also get the right answer and write it to stderr! Nonetheless, this should give us a directional sense of whether or not there’s a difference.

The chart below gives a summary of this data. The x-axis shows the percentage of code executions that were error-free in a given interview. So an interview with 3 code executions and 1 error message would count towards the “30%-40%” bucket. The y-axis indicates the percentage of all interviews that fall in that bucket, for both successful and unsuccessful interviews. Just eyeballing the chart below, one gets the sense that on average, successful candidates run more code that goes off without an error. But is this difference statistically significant?

0%-10%10%-20%20%-30%30%-40%40%-50%50%-60%60%-70%70%-80%80%-90%90%-100%100%0%5%10%15%

Do successful interviews have fewer code execution errors?Interviewer would hireInterviewer would not hirePercentage of Code that Runs Without ErrorPercentage of Interviews

[Download plot as a png]()
[Zoom]()[Pan]()
[Zoom in]()[Zoom out]()[Autoscale]()[Reset axes]()
[Toggle Spike Lines]()[Show closest data on hover]()[Compare data on hover]()
[Produced with Plotly](https://plot.ly/)

 [Edit chart](https://plot.ly/create/?fid=aline_interviewingio:984)

On average, successful candidates’ code ran successfully (didn’t result in errors) 64% of the time, whereas unsuccessful candidates’ attempts to compile code ran successfully 60% of the time, and this difference was indeed significant. **Again, while we can’t make any causal claims, the main takeaway is that successful candidates do usually write code that runs better, despite what interviewers may tell you at the outset of an interview.**

Should you wait and gather your thoughts before writing code?

*“Never forget the power of silence, that massively disconcerting pause which goes on and on and may at last induce an opponent to babble and backtrack nervously.”* -Lance Morrow

We were also curious whether or not successful interviewees tended to take their time in the interview. Interview questions are often complex! After being presented with a question, there might be some benefit to taking a step back and coming up with a plan, rather than jumping right into things. In order to get a sense of whether or not this was true, we measured how far into a given interview candidates first executed code. Below is a histogram showing how far into interviews both successful and unsuccessful interviewees first ran code. Looking quickly at the histogram, you can tell that successful candidates do in fact wait a bit longer to start running code, although the magnitude of the effect isn’t huge.

0%25%50%75%100%

Do successful candidatesrun code sooner?Interviewer would hireInterviewer would not hireHow far into the interview the candidate first runs codeNumber of interviews

[Download plot as a png]()
[Zoom]()[Pan]()
[Zoom in]()[Zoom out]()[Autoscale]()[Reset axes]()
[Toggle Spike Lines]()[Show closest data on hover]()[Compare data on hover]()
[Produced with Plotly](https://plot.ly/)

 [Edit chart](https://plot.ly/create/?fid=aline_interviewingio:963)

More specifically, **on average, candidates with successful interviews first run code 27% of the way through the interview, whereas candidates with unsuccessful interviews first run code 23.9% of the way into the interview, and this difference is significant**. Of course, there are alternate explanations for what’s happening here. For instance, perhaps successful candidates are better at taking the time to sweet-talk their interviewer. Furthermore, the usual caveat that we can’t make causal claims applies – if you just sit in an interview for an extra 5 minutes in complete silence, it won’t help your chances. Nonetheless, there does seem to be a difference between the two cohorts.

Conclusions

All in all, this post was our first attempt to understand what does and does not typically lead to an interviewer saying “you know what, I’d really like to hire this person.” Because all of our data are observational, its hard to make causal claims about what we see. While successful interviewees may exhibit certain behaviors, adopting those behaviors doesn’t guarantee success. Nonetheless, it does allow us to support (or call bullshit on) a lot of the advice you’ll read on the internet about how to be a successful interviewee.

That said, there is much still to be done. This was a first, quantitative pass over our data (which is, in many ways, a treasure trove of interview secrets), but we’re excited to do a deeper, qualitative dive and actually start to categorize different questions to see which carry the most signal as well as really get our head around 2nd order behaviors that you can’t measure easily by running a regex over a code sample or measuring how long an interview took. If you want to help us with this and are excited to listen to a bunch of technical interviews, drop me a line (at aline@interviewing.io)!

1All error bars in this post represent a 95% confidence interval.[[↩](../_resources/0a1b64d0eb2783edb6ef2bcca2b158e8.bin)](http://blog.interviewing.io/what-really-matters-in-technical-interviews-we-analyzed-thousands-of-interviews-on-everything-from-language-to-code-style-heres-what-we-found/#guide-ref1)

2There were more languages than these on our platform, but the more obscure the language, the less data points we have. For instance, all interviews in [Brainfuck](https://en.wikipedia.org/wiki/Brainfuck) were clearly successful. Kidding.[(L)](http://blog.interviewing.io/what-really-matters-in-technical-interviews-we-analyzed-thousands-of-interviews-on-everything-from-language-to-code-style-heres-what-we-found/#guide-ref2)

3The best engineers I’ve met have also been legendarily good at breaking down complex concepts and explaining them to laypeople. Why the infuriating myth of the socially awkward, incoherent tech nerd continues to exist, I have absolutely no idea.[(L)](http://blog.interviewing.io/what-really-matters-in-technical-interviews-we-analyzed-thousands-of-interviews-on-everything-from-language-to-code-style-heres-what-we-found/#guide-ref3)

4For every comparison of distributions in this post, we use both a Fisher-Pitman permutation test to compare the difference in the means of the distributions.[(L)](http://blog.interviewing.io/what-really-matters-in-technical-interviews-we-analyzed-thousands-of-interviews-on-everything-from-language-to-code-style-heres-what-we-found/#guide-ref4)

5We limit this analysis to interviews in Python because it lends itself particularly well to the identification of function definitions with a simple parsing script.[(L)](http://blog.interviewing.io/what-really-matters-in-technical-interviews-we-analyzed-thousands-of-interviews-on-everything-from-language-to-code-style-heres-what-we-found/#guide-ref5)

6We calculate this by looking at what percentage of the time the interviewee executed code that resulted in either an error or non-error output contained the term “error” or “traceback.”[(L)](http://blog.interviewing.io/what-really-matters-in-technical-interviews-we-analyzed-thousands-of-interviews-on-everything-from-language-to-code-style-heres-what-we-found/#guide-ref6)

### Share this:

-

[(L)](https://www.facebook.com/sharer/sharer.php?app_id=249643311490&kid_directed_site=0&sdk=joey&u=http%3A%2F%2Fblog.interviewing.io%2Fwhat-really-matters-in-technical-interviews-we-analyzed-thousands-of-interviews-on-everything-from-language-to-code-style-heres-what-we-found%2F&display=popup&ref=plugin&src=share_button)

- [**Tweet](https://twitter.com/intent/tweet?original_referer=http%3A%2F%2Fblog.interviewing.io%2Fwhat-really-matters-in-technical-interviews-we-analyzed-thousands-of-interviews-on-everything-from-language-to-code-style-heres-what-we-found%2F&ref_src=twsrc%5Etfw&text=We%20analyzed%20thousands%20of%20technical%20interviews%20on%20everything%20from%20language%20to%20code%20style.%20Here%27s%20what%20we%20found.&tw_p=tweetbutton&url=http%3A%2F%2Fblog.interviewing.io%2Fwhat-really-matters-in-technical-interviews-we-analyzed-thousands-of-interviews-on-everything-from-language-to-code-style-heres-what-we-found%2F&via=interviewingio)
- [inShare.](#)639

-
.

[**View Comments (14) ...](#)