Hiring Great Data Scientists

# Hiring Great Data Scientists

by [Michael Brundage](http://michaelbrundage.com/)  Created: 10 May 2014  Updated: 10 May 2014

In this note, I share my thoughts about the role of ‘Data Scientist’, how to hire great ones, and some practical matters of tools and version control.

Although I consider myself primarily a software engineer, for most of 2011, I filled the role of Data Scientist for my team. I helped John Rauser create the Data Scientist role and career path at Amazon, and hired many Data Scientists.

Software engineers have many specialties: network engineers, database engineers, compiler engineers, game developers, … Could ‘Data Scientist’ be just a specialized software engineer? Or is ‘Data Scientist’ just ‘Statistician’ in another form? There are [some who believe believe Data Science is a “sabotage of meaning” and is just “Statistics 2.0”](http://insideanalysis.com/2013/08/a-data-science-rant/).

Whether Data Science is a unique discipline (alongside Physics, Chemistry, and Mathematics) is somewhat unimportant to me. My focus here is on the Data Scientist role inside a company, the kinds of work that a person in that role does, and the skills they require to do that work well.

## The Role ‘Data Scientist’

[John Rauser](https://www.linkedin.com/in/jrauser) was a Principal Engineer at Amazon ([now at Pinterest](http://mashable.com/2013/06/03/pinterest-dream-job/)), but I think of John as Amazon’s first and greatest Data Scientist, before that title even existed. John and I discussed ‘What is a Data Scientist?’ before he outlined his ideas in [this 2011 Forbes article](http://www.forbes.com/sites/danwoods/2011/10/07/amazons-john-rauser-on-what-is-a-data-scientist/), discussions that led to the creation of the Data Scientist role and career path at Amazon.

John and I believed strongly that Data Science **is** a separate discipline from Software Development, Statistics, and Program Management, although it overlaps some skills with each of those. Here are some of the reasons why.

I argued that one of the most important skills a Data Scientist must possess is **curiosity**. Curiosity is of course great to have in most roles, but for a Data Scientist it is not just a ‘nice to have’ but a requirement. Data Scientists must dig deeper to understand observed phenomena. I’ve seen this happen again and again in interpreting A/B test results and other data analyses, that asking and answering ‘why?’ makes all the difference in the result and often leads to new hypotheses and results.

John argued that an equally or even more important quality Data Scientists must possess is **skepticism**, of both positive and negative outcomes. “Only the paranoid survive.” ([Andrew Grove](http://en.wikipedia.org/wiki/Andrew_Grove)) You don’t want to present a result to your CEO and then have to retract your findings later because your whole approach was flawed. Look at recent cases of how stock prices are supposedly correlated with [Twitter mood](http://sellthenews.tumblr.com/post/21067996377/noitdoesnot) or [Google searches](http://sellthenews.tumblr.com/post/55147868376/overfitting-on-google-trends) for examples where data scientists needed to be more skeptical. “Extraordinary claims require extraordinary proof.” ([Marcello Truzzi](http://en.wikipedia.org/wiki/Marcello_Truzzi))

Both curiosity and skepticism are really just facets of [the scientific method](http://en.wikipedia.org/wiki/Scientific_method), which gets us into the “science” part of Data Science:

>  Scientific researchers propose hypotheses as explanations of phenomena and design experimental studies to test these hypotheses via predictions which can be derived from them. These steps must be repeatable to guard against mistake or confusion in any particular experimenter.

Proposing hypotheses and designing experiments are both responsibilities of the Data Scientist role. But, and I think this is critical, where successful scientists may devise theories with no immediate practical applications and may couch their results in dense technical prose and mathematics, the successful Data Scientist must be both practical and understood. Hands-on engineering and excellent communication are critical skills for Data Scientists.

Hands-on engineering is important because Data Scientists must often write code to perform analyses and create data visualizations. In theory, this code doesn’t have to be “production-ready” (robust, scalable, performant, well-tested, commented), however… if you don’t test the code you wrote to perform a data analysis, how can you have confidence that its results are correct? If you don’t comment or document your work, how can you or others hope to understand it in a few months or years? If your code breaks all the time or takes forever to run, how can you be effective in getting your job done? We sometimes fool ourselves into thinking that just because a task needs only a small piece of software (hours or days for one person to complete), that it doesn’t require the same discipline and attention to detail as larger multi-month team efforts.

And finally, communication skills are really important: reading, writing, listening, and speaking. A Data Scientist must be able to consume dense research papers, apply the knowledge gained to new analyses and code, and then turn around and present methods and results to co-workers and executives. The best Data Scientists create beautful and functional data visualizations that effectively communicate the message. For some excellent examples of Data Scientist communication, watch one of John’s public talks:

- **[Investigating Anomalies](https://www.youtube.com/watch?v=-3dw09N5_Aw)**, Velocity, 2012.

- **[What is a Career in Big Data?](https://www.youtube.com/watch?v=0tuEEnL61HM)**, Strata, 2011.

- **[Look at Your Data](https://www.youtube.com/watch?v=coNDCIMH8bk)**, Velocity, 2011.

- **[TCP and the Lower Bound of Web Performance](http://www.stevesouders.com/blog/2010/07/13/velocity-tcp-and-the-lower-bound-of-web-performance/)**, ([slides](http://assets.en.oreilly.com/1/event/44/TCP%20and%20the%20Lower%20Bound%20of%20Web%20Performance%20Presentation.pdf)), Velocity, 2010.

I liken the emergence of Data Science to the emergence of Computer Science back in the day. There were many who believed Computer Science was just another branch of Electrical Engineering, or Mathematics – even today many universities still teach EECS or EEMCS courses. In the beginning, all Computer Science professionals were trained in other fields. Hopefully, we can all agree that Software Engineering and Computer Scientist are real roles now, distinct from Mathematician and Electrical Engineer.

Similarly, Data Scientists are not software engineers — their focus is not developing and launching production code — yet, they do need to write quality code. They are not program managers — their focus is not designing products or coordinating projects – yet, they do need to design experiments and communicate cross-group, and sometimes drive empirical change. They are not statisticians or (purely) scientists – their focus is not the development and application of statistical methods, indeed, one can practice data science in some cases without using any statistics – yet, they may develop new analytical methods and the role usually involves quite a bit of mathematics.

## Hiring Great Data Scientists

I interviewed dozens of Data Scientists and Research Scientists at Amazon and hired many, including [Rahul Bhagat](http://www.linkedin.com/pub/rahul-bhagat/1/273/626), [Minmin Chen](http://www.linkedin.com/pub/minmin-chen/11/113/884), [Austin Frank](http://www.linkedin.com/in/aufrank), [Tianran Li](http://www.linkedin.com/pub/tianran-li/3/569/500), [Xiaofeng Ren](http://www.linkedin.com/pub/xiaofeng-ren/90/9ab/693), [Luis Sarmento](http://www.linkedin.com/pub/luis-sarmento/4/4a4/853), [Kang Tu](http://www.linkedin.com/pub/kang-tu-phd/17/a3b/150), and [Chang Yuan](http://www.linkedin.com/in/cyuan) (some of whom have since moved on to other companies).

Here is some hard-earned advice for attracting, interviewing, and on-boarding data scientists:

#### Attracting Data Scientists

Most Data Scientists are specialized now, just like software engineers, except that the specialties are less well-defined or understood because it’s all still fairly new and changing.

A Data Scientist may have experience with any of: neural networks, linear regressions, clustering, classification (in general or specific kinds of classifiers), modeling, forecasting, ensemble methods such as random forests, boosting, wavelets, collaborative filtering, text analytics, classical natural language processing, statistical natural language processing, various computer vision methods, anomaly detection, and many more. Some of these are large areas with many sub-specialties. For example, a computer vision expert may know all about object detection but little about face detection, or may have lots of experience doing low-level image processing but none with dimensionality reduction methods, or vice-versa.

You need to understand which skills are most relevant to the work you need done now and in the future, and list those skills in the job description. Just as you wouldn’t usually hire a software engineer who specializes in distributed computing to create a mobile game, you shouldn’t hire a Data Scientist who specializes in text analytics to do financial modeling. Of course, there are always exceptions; sometimes a person wants a new role precisely because they have a little experience in the required skills and want to build up more experience. All of these skills can be acquired on the job, especially when you have a real-world problem to which to apply them.

Separately from the generic skills, there is domain experience in fields such as biology, finance, astronomy, statistics, economics, computer vision, information retrieval (including search), robotics, security, fraud detection, etc. Often a technical skill translates easily across all domains, but communicating effectively requires domain knowledge. If you need someone to come in and present to the CEO next month, you likely need a domain expert. Again, domain expertise can be acquired on the job.

Large companies need a role definition and career ladder laid out for Data Scientists, just as you have for other functional roles. It should be clear to any employee with the title ‘Data Scientist’ or ‘Research Scientist’ what they need to do to be considered for promotion to the next level.

You also need to think about how you set up your Data Scientist(s) to publish research papers, give conference presentations, and generally participate in the wider community. This is similar to engineers participating in Open Source projects, except that it’s even more important for Data Scientists to practice the art of communicating in these forums and to learn from (and contribute to) the community at large, because the field is so new and so rapidly evolving. Data Scientists will often expect this, so it’s good to proactively mention these opportunities in the job description or the informationals.

#### Interviewing Data Scientists

Structure the interview loop somewhat like you would structure the loop for software engineers, in terms of length and mix of interviewers probing soft skills and technical skills. If feasible, it’s a great idea to have Data Scientist candidates give a presentation to the team at the beginning of the day; this serves as both a practical demonstration of some of their communication skills and provides conversation topics for the interviewers. They may not be able to do this if all of their prior work has been proprietary.

Like software engineers, Data Scientists exhibit a range of code skill levels from “script kiddie” to Principal Engineer. Probe this, but ask fewer coding questions than you would of a software engineer, and typically no questions about software design and operations. Instead, ask about experimental design and probe math skills — basic probability as well as techniques like linear algebra or calculus, as applicable to the role. If the job entails machine learning, ask many questions about that, especially cross-validation and overfitting, bias and variance, when you need more data vs. more features vs. better algorithms, and specific algorithms from the candidate’s past.

If you have no staff capable of assessing a prospective Data Scientist’s technical and/or mathematical skills, you’re in a tough spot. You can still learn a lot about experienced candidates via [behavioral interviewing](http://www.udel.edu/CSC/pdf/behav_interview.pdf). Hilary Mason has some great [interview questions to ask Data Scientists](http://www.hilarymason.com/blog/interview-questions-for-data-scientists/), but be aware many candidates already may have read this article.

Ask questions designed to elicit the qualties previously noted – curiosity, skepticism, and communication — that are so critical to the Data Scientist role. Ask about experiments the candidate has invented/created in the past, the results of those experiments, and how the results were communicated to partners/customers/peers/management.

If your candidate pool isn’t producing candidates who meet all your requirements, consider splitting the role. Instead of one Data Scientist, you could hire one software engineer with mathematical experience and one statistician with software experience and get close to the desired results. Or, just be patient. One Data Scientist position I was [Bar Raiser](http://online.wsj.com/news/articles/SB10001424052702304753504579285133045398344) for interviewed candidates for nearly a year before finding the right person.

#### On-boarding Data Scientists

Most Data Scientists, like most software engineers, want to have large impact and grow their skills. Make sure you have projects of sufficient scope for the job level planned for the next few months and list those in the job description or describe them during the interview process.

The Data Scientist’s work needs to be appropriate for the role. I saw one hiring manager try to give a recently graduated machine learning Ph.D. the task of generating large datasets of images, including writing code to synthesize new images from 3D models. Although there are always exceptions, generally writing code to do 3D graphics and image processing is not a task a Data Scientist will excel at or enjoy and assigning work like this to a new hire is a great way to cause that employee to leave your company. I saw another Data Scientist come into an ill-prepared team and get done in only a few months the work the team had thought would occupy the entire first year. Both of these hires left after a year or less. Don’t make mistakes like these.

Set up new Data Scientist employees with a mentor (ideally another Data Scientist, if you have one). Mentors are so important for many reasons, including retention and personal growth. Think about all the people you want to be part of the new hire’s launch plan, especially points of contact for various topics.

Data Scientists need data. Make sure the launch plan includes meeting with people who generate all the telemetry and other data your Data Scientist will need to use. Design initial tasks to help them become proficient with using those systems and that data. Just as you might start off a software engineer with simple bug fixes, start off a Data Scientist with relatively simple (but still useful and interesting) data analyses so they can learn the systems.

If you hire a Data Scientist with strong coding skills, they may be able to build systems such as metrics dashboards. If not, then you should plan on partnering them with software engineers whenever you need systems built.

## Data Science Tools and Version Control

Engineers use a variety of tools (editors, compilers, debuggers, performance analyzers, etc.) and store their code under version control. Data Scientists also use a variety of tools and need to store their code and analyses (and datasets!!) under version control, for the same reasons and also to assist with reproducibility and repeatability of results.

Most version control software does not handle large datasets well. There are tools like [git-media](https://github.com/schacon/git-media), but you may need to figure out your own solutions.

Naming conventions help a lot here. There are many [computer vision datasets](http://www.cvpapers.com/datasets.html) publicly available, but naming conventions among them are chaotic and mostly non-existent. Think hard about the attributes that differentiate your datasets, and include those attribute names in the dataset names.

Also, consider that datasets change over time, and so you likely want to include the date in the dataset name as well, or be able to reconstruct historical datasets via version control to compare future algorithms with past results. If your datasets share instances (e.g., you have a million audio recordings your datasets are subsets of those million) then I recommend you store the originals once and have each dataset simply refer back into the larger set to reduce storage requirements.

The tools being used in this space are rapidly evolving. Unlike software projects, where you typically have teams of engineers working from a single codebase and the code is actively developed over many years and personnel changes, data science projects are often the work of solo contributors and are actively maintained only during the current analysis effort. You still need to preserve the code and results for the future and may return to them or apply them to a new project, but it’s not under active team development the same way a normal product codebase would be. Consequently, it’s less important that all your Data Scientists conform to some common tool set. If some want to use R and some use Python and some use Matlab and some use Weka, that’s probably just fine.

That said, I do really like [the iPython Notebook](http://ipython.org/notebook.html) approach to Data Science. Recording your code, mathematics, results and visualizations in a single living document is a very powerful way to do to Data Science. There is a similar project for [R Notebooks](https://github.com/ramnathv/rNotebook).

## Conclusion

Data Science is different from engineering and statistics in skills required, interview process, and career path. The role of Data Scientist deserves careful design and planning. I hope the ideas presented here will help you to more effectively recruit and retain Data Scientists!

Share this page:

 [](https://www.twitter.com/intent/tweet?via=michaelbrundage&text=Hiring+Great+Data+Scientists&url=http%3A%2F%2Fmichaelbrundage.com%2Fnote%2F2014%2F05%2F10%2Fhiring-great-data-scientists%2F)  [](https://www.facebook.com/sharer.php?u=http://michaelbrundage.com/note/2014/05/10/hiring-great-data-scientists/&t=Hiring+Great+Data+Scientists&i=http%3A%2F%2Fmichaelbrundage.com%2Fthumbnote%2Fhiring-great-data-scientists.png)  [](https://www.linkedin.com/shareArticle?mini=true&url=http%3A%2F%2Fmichaelbrundage.com%2Fnote%2F2014%2F05%2F10%2Fhiring-great-data-scientists%2F&title=Hiring+Great+Data+Scientists&Michael+Brundage&summary=Thoughts+about+the+role+of+%27Data+Scientist%27%2C+how+to+hire+great+ones%2C+and+some+practical+matters+of+tools+and+version+control.)  [](https://plus.google.com/share?url=http%3A%2F%2Fmichaelbrundage.com%2Fnote%2F2014%2F05%2F10%2Fhiring-great-data-scientists%2F)

### You may also like…

#### [Counting is Hard](http://michaelbrundage.com/note/2014/05/11/counting-is-hard/)

 [![](../_resources/082e158fca2035aa9b7977108b66ec86.png)](http://michaelbrundage.com//note/2014/05/11/counting-is-hard/)

#### [MIT Media Lab Visit](http://michaelbrundage.com/note/2013/01/24/mit-media-lab/)

 [![](../_resources/b9d148a3f20110e4257a349975b4444c.png)](http://michaelbrundage.com//note/2013/01/24/mit-media-lab/)