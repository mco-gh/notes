10 things R can do that might surprise you · Simply Statistics

# 10 things R can do that might surprise you

##

 **  2019/03/13

Over the last few weeks I’ve had a couple of interactions with folks from the computer science world who were pretty disparaging of the R programming language. A lot of the critism focused on perceived limitations of R to statistical analysis.

It’s true, R does have a hugely comprehensive list of analysis packages on [CRAN](https://cran.r-project.org/), [Bioconductor](http://bioconductor.org/), [Neuroconductor](https://neuroconductor.org/), and [ROpenSci](https://ropensci.org/) as well as great package management. As I was having these conversations I realized that R has grown into a multi-purpose connective language for things beyond just data analysis. But that the functionality isn’t always as well known outside of the R community. So this post is about some of the ridiculously awesome features of R that may or may not be as widely known. Here are 10 things R can do you might not have known about, building on [Kara’s great tweet thread about lighthearted things to do with R](https://twitter.com/kara_woo/status/1100908125396193281).

## 1. You can write reproducible Word or Powerpoint documents from R markdown

The [rmarkdown](https://rmarkdown.rstudio.com/) package lets you [create reproducible Word documents](https://bookdown.org/yihui/rmarkdown/word-document.html) and [reproducible Powerpoint Presentations](https://bookdown.org/yihui/rmarkdown/powerpoint-presentation.html) from your R markdown code just by changing one line in the YAML!

## 2. You can build and host interactive web apps in just a few lines of code

In just a few lines of code you can create interactive web apps in R. For example, [in just 36 lines of code](https://gist.github.com/jtleek/3e1baac9a74ea81556c9e6d55743d7ea) you can create an interactive dashboard to explore your BMI in relation to the NHANES sample using the [flexdashboard](https://rmarkdown.rstudio.com/flexdashboard/) package.

## 3. You can host your web apps in one more line of R code

The other cool thing about building web apps in R is that you can get them up on the web with just another line or two of R code using the [rsconnect](https://cran.r-project.org/web/packages/rsconnect/index.html) package. You can put them up on your own server or, even easier, host them on a cloud server like [shinyapps.io](https://www.shinyapps.io/).

## 4. You can connect to almost any database under the sun and pull data with dplyr/dbplyr

It is really easy to connect to almost any database (local or remote) using the [dbplyr](https://cran.r-project.org/web/packages/dbplyr/index.html) package. This makes it possible for an R user to work independently pulling data from [almost all common database types](https://cfss.uchicago.edu/distrib001_database.html). You can also use specialized packages like [bigrquery](https://cran.r-project.org/web/packages/bigrquery/index.html) to work directly with BigQuery and other high performance data stores.

## 5. You can use the same dplyr grammar locally or on data on multiple different data stores

Once you learn how to do basic data tranforms with [dplyr](https://dplyr.tidyverse.org/), you can apply the same code to analyze data locally on your computer or remotely on any of the above databases or data stores. This simplifies and unifies data manipulation across multiple different databases and languages.

## 6. You can fit deep learning models with keras and Tensorflow

The [keras](https://keras.rstudio.com/) package allows you to fit both pre-trained and denovo deep learning models directly from R. You can also work with the direct [TensorFlow](https://tensorflow.rstudio.com/) interface to fit the same kind of models.

## 7. You can build APIs and serve them from R

The [plumbr](https://www.rplumber.io/) R package lets you convert R functions to web APIs that can be integrated into downstream applications. If you have Rstudio Connect you can also [deploy them as easily](https://blog.rstudio.com/2017/08/03/rstudio-connect-v1-5-4-plumber/) as you deploy web apps.

## 8. You can make video game interfaces with R

Not only can you deploy web apps, you can make them into awesome video games in R. The [nessy](https://github.com/ColinFay/nessy) package lets you create NES looking Shiny apps and [deploy them](https://lucy.shinyapps.io/classify/) just like you would any other Shiny app.

## 9. You can analyze data using Spark clusters right from R

Want to fit big, gnarly machine learning models on huge data sets? You can do that right from R using the [sparklyr](https://spark.rstudio.com/) package. You can use spark on your Desktop or a monster Spark cluster.

## 10. You can build and learn R interactively in R

The [swirl](https://swirlstats.com/) package is an R package that lets you build interactive tutorials for R, right inside R.

This is by no means a comprehensive list. You can also connect to AWS Polly and write [text to speech synthesis](https://github.com/seankross/ari) software or build Shiny apps that [respond to voice commands](https://yihui.shinyapps.io/voice/) or build apps that let you combine deep learning and accelerometry data to cast [Harry Potter spells](https://jhubiostatistics.shinyapps.io/cast_spells/). The point is that R has become much more than just a data analysis language (although its still good at that!) and being good at R opens the door to lots of practical and cool applications.

 [**](https://simplystatistics.org/2019/02/21/dynamite-plots-must-die/)

 [Open letter to journal editors: dynamite plots must die](https://simplystatistics.org/2019/02/21/dynamite-plots-must-die/)

- [6 comments]()
- [**Simply Statistics**](https://disqus.com/home/forums/simplystatsgithub/)
- [Marc Cohen](https://disqus.com/embed/comments/?base=default&f=simplystatsgithub&t_u=http%3A%2F%2Fsimplystatistics.org%2F2019%2F03%2F13%2F10-things-r-can-do-that-might-surprise-you%2F&t_d=10%20things%20R%20can%20do%20that%20might%20surprise%20you&t_t=10%20things%20R%20can%20do%20that%20might%20surprise%20you&s_o=default&d_m=0#)
- [](https://disqus.com/home/inbox/)
- [ Recommend  2](https://disqus.com/embed/comments/?base=default&f=simplystatsgithub&t_u=http%3A%2F%2Fsimplystatistics.org%2F2019%2F03%2F13%2F10-things-r-can-do-that-might-surprise-you%2F&t_d=10%20things%20R%20can%20do%20that%20might%20surprise%20you&t_t=10%20things%20R%20can%20do%20that%20might%20surprise%20you&s_o=default&d_m=0#)
- tTweetfShare
- [Sort by Best](https://disqus.com/embed/comments/?base=default&f=simplystatsgithub&t_u=http%3A%2F%2Fsimplystatistics.org%2F2019%2F03%2F13%2F10-things-r-can-do-that-might-surprise-you%2F&t_d=10%20things%20R%20can%20do%20that%20might%20surprise%20you&t_t=10%20things%20R%20can%20do%20that%20might%20surprise%20you&s_o=default&d_m=0#)

[![noavatar92.png](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/disqus_Q5LZbDr3pW/)

Join the discussion…

![underline.59f82f5f5bbed90fd72132ef98662fe3.png](../_resources/934680108867ffa7d395fdd4bbd0355f.png)

![spoiler.eff5de8f72591c5ceeb4fa26a117c6d1.png](../_resources/96b84d4f8860873e832b36e36e2d5731.png)

![link.5ef9a39f22ce49f926e304567b9d611b.png](../_resources/ff5312def55b6769d146cc61b15420a4.png)

![blockquote.69435f6faa8c7a193456c46bcb7fb1ed.png](../_resources/1593ac148112cfe84e726f315a476b6a.png)

![attach.03c320b14aa9c071da30c904d0a0827f.png](../_resources/b941b52a67553a95c2d82654c9c21a0a.png)

![strikethrough.ced68e63961c6bc0e072ce907906b252.png](../_resources/7b3857fd068ccbd0ee35c328563b15a0.png)

![bold.cb366e6a49396fb0e47a01df277563c8.png](../_resources/b7299ccc866f016305a105091cf0ae02.png)

![italic.a6e1da4a89899ae5e87db9ded9f84d5b.png](../_resources/8238cb2c15a34beae1c286f5a33a73a1.png)

[![code.8f558a246aa4e9c41ef343f72f012f01.png](../_resources/d02baddf90be3d2eaf06525081255899.png)](https://disqus.com/embed/comments/?base=default&f=simplystatsgithub&t_u=http%3A%2F%2Fsimplystatistics.org%2F2019%2F03%2F13%2F10-things-r-can-do-that-might-surprise-you%2F&t_d=10%20things%20R%20can%20do%20that%20might%20surprise%20you&t_t=10%20things%20R%20can%20do%20that%20might%20surprise%20you&s_o=default&d_m=0#)

![gif-picker.df38180f2d048c25fe42a2b440ff863e.png](../_resources/5f5ec942ed95355419b673488da13811.png)

-

    - [−](https://disqus.com/embed/comments/?base=default&f=simplystatsgithub&t_u=http%3A%2F%2Fsimplystatistics.org%2F2019%2F03%2F13%2F10-things-r-can-do-that-might-surprise-you%2F&t_d=10%20things%20R%20can%20do%20that%20might%20surprise%20you&t_t=10%20things%20R%20can%20do%20that%20might%20surprise%20you&s_o=default&d_m=0#)
    - [****](https://disqus.com/embed/comments/?base=default&f=simplystatsgithub&t_u=http%3A%2F%2Fsimplystatistics.org%2F2019%2F03%2F13%2F10-things-r-can-do-that-might-surprise-you%2F&t_d=10%20things%20R%20can%20do%20that%20might%20surprise%20you&t_t=10%20things%20R%20can%20do%20that%20might%20surprise%20you&s_o=default&d_m=0#)

[![avatar92.jpg](../_resources/f2ce0df4d5a5805800757453af0f12b1.jpg)](https://disqus.com/by/disqus_r6PVd3FHIp/)

 [Adrián Alejandro Rodríguez Vil](https://disqus.com/by/disqus_r6PVd3FHIp/)    •  [a day ago](https://simplystatistics.org/2019/03/13/10-things-r-can-do-that-might-surprise-you/#comment-4378892740)

In the first point there is a package to create better presentations in html5 using the xaringan package, and is interactive, for people who hate using Windows or Office Suites is a must have

-

    - [−](https://disqus.com/embed/comments/?base=default&f=simplystatsgithub&t_u=http%3A%2F%2Fsimplystatistics.org%2F2019%2F03%2F13%2F10-things-r-can-do-that-might-surprise-you%2F&t_d=10%20things%20R%20can%20do%20that%20might%20surprise%20you&t_t=10%20things%20R%20can%20do%20that%20might%20surprise%20you&s_o=default&d_m=0#)
    - [****](https://disqus.com/embed/comments/?base=default&f=simplystatsgithub&t_u=http%3A%2F%2Fsimplystatistics.org%2F2019%2F03%2F13%2F10-things-r-can-do-that-might-surprise-you%2F&t_d=10%20things%20R%20can%20do%20that%20might%20surprise%20you&t_t=10%20things%20R%20can%20do%20that%20might%20surprise%20you&s_o=default&d_m=0#)

[![avatar92.jpg](../_resources/e57825e8838bd076241d2b324ab29704.jpg)](https://disqus.com/by/folajimiaroloye/)

 [Folajimi Aroloye](https://disqus.com/by/folajimiaroloye/)    •  [a day ago](https://simplystatistics.org/2019/03/13/10-things-r-can-do-that-might-surprise-you/#comment-4378064264)

Wow, Awesome... Thanks for this eye opener

-

    - [−](https://disqus.com/embed/comments/?base=default&f=simplystatsgithub&t_u=http%3A%2F%2Fsimplystatistics.org%2F2019%2F03%2F13%2F10-things-r-can-do-that-might-surprise-you%2F&t_d=10%20things%20R%20can%20do%20that%20might%20surprise%20you&t_t=10%20things%20R%20can%20do%20that%20might%20surprise%20you&s_o=default&d_m=0#)
    - [****](https://disqus.com/embed/comments/?base=default&f=simplystatsgithub&t_u=http%3A%2F%2Fsimplystatistics.org%2F2019%2F03%2F13%2F10-things-r-can-do-that-might-surprise-you%2F&t_d=10%20things%20R%20can%20do%20that%20might%20surprise%20you&t_t=10%20things%20R%20can%20do%20that%20might%20surprise%20you&s_o=default&d_m=0#)

[![noavatar92.png](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/sdiwash/)

 [Diwash shrestha](https://disqus.com/by/sdiwash/)    •  [2 days ago](https://simplystatistics.org/2019/03/13/10-things-r-can-do-that-might-surprise-you/#comment-4377616005)

Great Article Loved it.

-

    - [−](https://disqus.com/embed/comments/?base=default&f=simplystatsgithub&t_u=http%3A%2F%2Fsimplystatistics.org%2F2019%2F03%2F13%2F10-things-r-can-do-that-might-surprise-you%2F&t_d=10%20things%20R%20can%20do%20that%20might%20surprise%20you&t_t=10%20things%20R%20can%20do%20that%20might%20surprise%20you&s_o=default&d_m=0#)
    - [****](https://disqus.com/embed/comments/?base=default&f=simplystatsgithub&t_u=http%3A%2F%2Fsimplystatistics.org%2F2019%2F03%2F13%2F10-things-r-can-do-that-might-surprise-you%2F&t_d=10%20things%20R%20can%20do%20that%20might%20surprise%20you&t_t=10%20things%20R%20can%20do%20that%20might%20surprise%20you&s_o=default&d_m=0#)

[![avatar92.jpg](../_resources/4609578e98e8a335bb676c62f1e0e7b2.jpg)](https://disqus.com/by/jongyunjung/)

 [Jongyun Jung](https://disqus.com/by/jongyunjung/)    •  [2 days ago](https://simplystatistics.org/2019/03/13/10-things-r-can-do-that-might-surprise-you/#comment-4377534276)

Thank you for summarizing the functionality of "R"

-

    - [−](https://disqus.com/embed/comments/?base=default&f=simplystatsgithub&t_u=http%3A%2F%2Fsimplystatistics.org%2F2019%2F03%2F13%2F10-things-r-can-do-that-might-surprise-you%2F&t_d=10%20things%20R%20can%20do%20that%20might%20surprise%20you&t_t=10%20things%20R%20can%20do%20that%20might%20surprise%20you&s_o=default&d_m=0#)
    - [****](https://disqus.com/embed/comments/?base=default&f=simplystatsgithub&t_u=http%3A%2F%2Fsimplystatistics.org%2F2019%2F03%2F13%2F10-things-r-can-do-that-might-surprise-you%2F&t_d=10%20things%20R%20can%20do%20that%20might%20surprise%20you&t_t=10%20things%20R%20can%20do%20that%20might%20surprise%20you&s_o=default&d_m=0#)

[![avatar92.jpg](../_resources/b897be0e3b6c1e5d33d3aa415b10ccd5.jpg)](https://disqus.com/by/danreznik/)

 [Dan Reznik](https://disqus.com/by/danreznik/)    •  [2 days ago](https://simplystatistics.org/2019/03/13/10-things-r-can-do-that-might-surprise-you/#comment-4377389527)

Great article.

## Also on **Simply Statistics**

- [

### The Tentpoles of Data Science

    - 2 comments •

    - 2 months ago

[![noavatar92.png](../_resources/675fb4b91ca717db030507f2d84bcfdf.png) Pete Fuller —  Thanks Roger, btw, the order of difficulty in climbing the tent poles:1. Narrative Stories - Effective …](http://disq.us/?url=http%3A%2F%2Fsimplystatistics.org%2F2019%2F01%2F18%2Fthe-tentpoles-of-data-science%2F&key=tUYoVQNwLowX0uucMT2MxQ)](http://disq.us/?url=http%3A%2F%2Fsimplystatistics.org%2F2019%2F01%2F18%2Fthe-tentpoles-of-data-science%2F&key=tUYoVQNwLowX0uucMT2MxQ)

- [

### How Data Scientists Think - A Mini Case Study

    - 1 comment •

    - 2 months ago

[![noavatar92.png](../_resources/675fb4b91ca717db030507f2d84bcfdf.png) Kevin Ho —  Nice write up and discussion on the podcast. I am amused that you've acknowledged that motivation and …](http://disq.us/?url=http%3A%2F%2Fsimplystatistics.org%2F2019%2F01%2F09%2Fhow-data-scientists-think-a-mini-case-study%2F&key=cnjbSeDpV8gvZfqQVRi9WA)](http://disq.us/?url=http%3A%2F%2Fsimplystatistics.org%2F2019%2F01%2F09%2Fhow-data-scientists-think-a-mini-case-study%2F&key=cnjbSeDpV8gvZfqQVRi9WA)

- [

### A first look at recently released official Puerto Rico death count data

    - 4 comments •

    - 9 months ago

[![noavatar92.png](../_resources/675fb4b91ca717db030507f2d84bcfdf.png) Rafa —  Note that this is a preliminary analysis. With more time I would have constructed a spline basis with a …](http://disq.us/?url=http%3A%2F%2Fsimplystatistics.org%2F2018%2F06%2F08%2Fa-first-look-at-recently-released-official-puerto-rico-death-count-data%2F&key=iZrTCmsjbmr3ImzTdvIqNQ)](http://disq.us/?url=http%3A%2F%2Fsimplystatistics.org%2F2018%2F06%2F08%2Fa-first-look-at-recently-released-official-puerto-rico-death-count-data%2F&key=iZrTCmsjbmr3ImzTdvIqNQ)

- [

### Interview with Stephanie Hicks

    - 1 comment •

    - 25 days ago

[![avatar92.jpg](../_resources/f301ceca54ac066fdefb43805a84aa6a.jpg) Ngọc Anh Nguyễn — Thank a lot. Awesome <3.](http://disq.us/?url=http%3A%2F%2Fsimplystatistics.org%2F2019%2F02%2F18%2Finterview-with-stephanie-hicks%2F&key=FwDM09-nVs-Uye1D5PuR3Q)](http://disq.us/?url=http%3A%2F%2Fsimplystatistics.org%2F2019%2F02%2F18%2Finterview-with-stephanie-hicks%2F&key=FwDM09-nVs-Uye1D5PuR3Q)

- [Powered by Disqus](https://disqus.com/)
- [*✉*Subscribe*✔*](https://disqus.com/embed/comments/?base=default&f=simplystatsgithub&t_u=http%3A%2F%2Fsimplystatistics.org%2F2019%2F03%2F13%2F10-things-r-can-do-that-might-surprise-you%2F&t_d=10%20things%20R%20can%20do%20that%20might%20surprise%20you&t_t=10%20things%20R%20can%20do%20that%20might%20surprise%20you&s_o=default&d_m=0#)
- [*d*Add Disqus to your site](https://publishers.disqus.com/engage?utm_source=simplystatsgithub&utm_medium=Disqus-Footer)
- [**Disqus' Privacy Policy](https://help.disqus.com/customer/portal/articles/466259-privacy-policy)