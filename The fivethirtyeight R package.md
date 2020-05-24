The fivethirtyeight R package

[« Because it's Friday: Code Burn](http://blog.revolutionanalytics.com/2017/01/because-its-friday-code-burn.html) |[Main](http://blog.revolutionanalytics.com/)| [Git Gud with Git and R »](http://blog.revolutionanalytics.com/2017/01/git-gud-with-git-and-r.html)

## January 16, 2017

### The fivethirtyeight R package

Andrew Flowers, data journalist and contributor to [FiveThirtyEight.com](https://fivethirtyeight.com/), announced at last weeks' [RStudio conference](https://www.rstudio.com/conference/) the availability of a new R package containing data and analyses from some of their data journalism features: [the fivethirtyeight package](https://mran.microsoft.com/package/fivethirtyeight/). (Andrew's talk isn't yet online, but you can see him discuss several of these stories in his [UseR!2016 presentation](http://blog.revolutionanalytics.com/2016/07/data-journalism-with-r-at-538.html).) While not an official product of the FiveThirtyEight editorial team, it was developed by Albert Y. Kim, Chester Ismay and Jennifer Chunn under their guidance. Their [motivation](https://mran.microsoft.com/web/packages/fivethirtyeight/vignettes/fivethirtyeight.html) for producing the package was to provide a resource for teaching data science:

> We are involved in statistics and data science education, in particular at the introductory undergraduate level. As such, we are always looking for data sets that balance being

1. **Rich enough** to answer meaningful questions with, **real enough** to ensure that there is context, and **realistic enough** to convey to students that data as it exists “in the wild” often needs processing.

2. Easily and quickly accessible to novices, so that we [minimize the prerequisites to research](https://arxiv.org/abs/1507.05346).

The package includes data sets from dozens of data journalism stories, including stories about [police killings in the USA](http://fivethirtyeight.com/features/where-police-have-killed-americans-in-2015), [plane crashes](http://fivethirtyeight.com/features/should-travelers-avoid-flying-airlines-that-have-had-crashes-in-the-past/), and [even references to presidential candidates in hip-hop lyrics](https://projects.fivethirtyeight.com/clinton-trump-hip-hop-lyrics/). There is also a complete worked analysis of [performace of movies satisfying the Bechdel Test](http://fivethirtyeight.com/features/the-dollar-and-cents-case-against-hollywoods-exclusion-of-women/), presented as an [Rmarkdown vignette](https://mran.microsoft.com/web/packages/fivethirtyeight/vignettes/bechdel.html).

The package is available for [download now on CRAN](https://mran.microsoft.com/package/fivethirtyeight/), and you can find the latest development version [on GitHub](https://github.com/rudeboybert/fivethirtyeight).

Posted by [David Smith](http://profile.typepad.com/revolutiondavid) at 13:17 in [data science](http://blog.revolutionanalytics.com/data-science/), [packages](http://blog.revolutionanalytics.com/packages/), [R](http://blog.revolutionanalytics.com/r/)    |  [Permalink](http://blog.revolutionanalytics.com/2017/01/the-fivethirtyeight-r-package.html)

### Comments

[![Feed](../_resources/9b19d1a0b20cded5a27b129f81353e07.png)](http://blog.revolutionanalytics.com/2017/01/the-fivethirtyeight-r-package/comments/atom.xml) You can follow this conversation by subscribing to the [comment feed](http://blog.revolutionanalytics.com/2017/01/the-fivethirtyeight-r-package/comments/atom.xml) for this post.

are they including obama's package on how to make healthcare cheap?

Posted by: harry balzer |[January 17, 2017 at 12:32](http://blog.revolutionanalytics.com/2017/01/the-fivethirtyeight-r-package.html?cid=6a010534b1db25970b01b7c8ca9971970b#comment-6a010534b1db25970b01b7c8ca9971970b)

i think i found the probability_to_win function that made nate silver so famous!

#odds [insert democrat here] wins
sample(75:100, 12, replace=TRUE)

Posted by: Hacker News Pitard |[January 17, 2017 at 18:34](http://blog.revolutionanalytics.com/2017/01/the-fivethirtyeight-r-package.html?cid=6a010534b1db25970b01b8d254ee39970c#comment-6a010534b1db25970b01b8d254ee39970c)

The comments to this entry are closed.