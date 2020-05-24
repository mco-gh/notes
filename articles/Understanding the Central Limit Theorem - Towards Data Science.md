Understanding the Central Limit Theorem - Towards Data Science

# Understanding the Central Limit Theorem

## Diving deep into one of the most important theorems in statistics

[![1*OkfOJCvE6d5AtIvEOHOP7g.jpeg](../_resources/77249e5b11c95cd61a7fb9ba6b3dafdb.jpg)](https://towardsdatascience.com/@jjw92abhi?source=post_page-----e598158cc5da----------------------)

[Abhishek Jhunjhunwala](https://towardsdatascience.com/@jjw92abhi?source=post_page-----e598158cc5da----------------------)

[Sep 8](https://towardsdatascience.com/understanding-the-central-limit-theorem-e598158cc5da?source=post_page-----e598158cc5da----------------------) · 5 min read![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='star-15px_svg__svgIcon-use js-evernote-checked' width='15' height='15' viewBox='0 0 15 15' style='margin-top:-2px' data-evernote-id='189'%3e%3cpath d='M7.44 2.32c.03-.1.09-.1.12 0l1.2 3.53a.29.29 0 0 0 .26.2h3.88c.11 0 .13.04.04.1L9.8 8.33a.27.27 0 0 0-.1.29l1.2 3.53c.03.1-.01.13-.1.07l-3.14-2.18a.3.3 0 0 0-.32 0L4.2 12.22c-.1.06-.14.03-.1-.07l1.2-3.53a.27.27 0 0 0-.1-.3L2.06 6.16c-.1-.06-.07-.12.03-.12h3.89a.29.29 0 0 0 .26-.19l1.2-3.52z' data-evernote-id='190' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)

[![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='29' height='29' class='q js-evernote-checked' data-evernote-id='195'%3e%3cpath d='M22.05 7.54a4.47 4.47 0 0 0-3.3-1.46 4.53 4.53 0 0 0-4.53 4.53c0 .35.04.7.08 1.05A12.9 12.9 0 0 1 5 6.89a5.1 5.1 0 0 0-.65 2.26c.03 1.6.83 2.99 2.02 3.79a4.3 4.3 0 0 1-2.02-.57v.08a4.55 4.55 0 0 0 3.63 4.44c-.4.08-.8.13-1.21.16l-.81-.08a4.54 4.54 0 0 0 4.2 3.15 9.56 9.56 0 0 1-5.66 1.94l-1.05-.08c2 1.27 4.38 2.02 6.94 2.02 8.3 0 12.86-6.9 12.84-12.85.02-.24 0-.43 0-.65a8.68 8.68 0 0 0 2.26-2.34c-.82.38-1.7.62-2.6.72a4.37 4.37 0 0 0 1.95-2.51c-.84.53-1.81.9-2.83 1.13z' data-evernote-id='196' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://medium.com/p/e598158cc5da/share/twitter?source=post_actions_header---------------------------)

[![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='29' height='29' class='q js-evernote-checked' data-evernote-id='199'%3e%3cpath d='M23.2 5H5.8a.8.8 0 0 0-.8.8V23.2c0 .44.35.8.8.8h9.3v-7.13h-2.38V13.9h2.38v-2.38c0-2.45 1.55-3.66 3.74-3.66 1.05 0 1.95.08 2.2.11v2.57h-1.5c-1.2 0-1.48.57-1.48 1.4v1.96h2.97l-.6 2.97h-2.37l.05 7.12h5.1a.8.8 0 0 0 .79-.8V5.8a.8.8 0 0 0-.8-.79' data-evernote-id='200' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://medium.com/p/e598158cc5da/share/facebook?source=post_actions_header---------------------------)

In this article, I want to talk about the central limit theorem and its applications in statistics. The central limit theorem states that if data is independently drawn from any distribution and the sample size is large enough, the sample mean always appears to be normally distributed. This might be a little difficult to comprehend at the moment so let’s take a look at the sample mean and its properties. Let’s try to calculate the expected value of the sample mean and sample variance which is not very difficult. Here, we assume that our data is identical and independently distributed and start with the definition of sample mean:

![1*diDGfvzh_Bjw9k-nihAbSw.png](../_resources/85612118f305b2d62ec8426b56879643.png)
![1*XmZGHTlKHpsUz5wrrW9WIg.png](../_resources/df6528eb6fecd65a4c9a02b81034b549.png)
Now we can take the constant 1/n out of the expected value:
![1*WuoeFtd86f26NHQyfsF5fw.png](../_resources/b3e980abf7ad8f9e6ab92cd174dabcbb.png)
![1*jhhTc4_9T-G0C43Gzq4NCw.png](../_resources/54b340c8c75b85e98e878fbdcb7520ba.png)
Next, we include the expected value inside the sum:
![1*Ypv5EPqg17V_-lved6T7BA.png](../_resources/6ac44b16bf8bc4aa16c2d0e78e2bbcf0.png)
![1*EunDVPVrDHCfU7ev6pK2XA.png](../_resources/ae869ac4b2cad568769d1355f7067cb7.png)
Here, the expected value of each observation is :
![1*PTE6CwVaIdRl1yeLbyzq3w.png](../_resources/50a6e4643739361fc651b25eb2d29449.png)
![1*PTE6CwVaIdRl1yeLbyzq3w.png](../_resources/85eaee0e844a6268800ab72788a2326f.png)

The term on the right side is the sum of over n times and divided by n, which gives us the expected value of the sample means as itself:

![1*EunDVPVrDHCfU7ev6pK2XA.png](../_resources/c6d544c7c1fe1bcc5089b481800a7a26.png)
![1*OsRkH-uq5WtBHEj1oBrEow.png](../_resources/71caf9ee8a2acbed66593c489de747fe.png)

Next, we try to calculate the variance of the sample mean which is a little complicated but important. We take the same assumptions about our data as before and begin with the definition of variance:

![1*jhhTc4_9T-G0C43Gzq4NCw.png](../_resources/4d6b0722ca508ec9adba3864d2922877.png)
![1*WuoeFtd86f26NHQyfsF5fw.png](../_resources/01f71012f80f8c71593164d71888b4ef.png)

We can see the sample mean in the equation and that is just wonderful because we have already calculated it above:

![1*Ica0BMkOrKuW121TcksvLw.png](../_resources/c5175c65ba642a02313e835a7d39a33d.png)
![1*diDGfvzh_Bjw9k-nihAbSw.png](../_resources/617d035c8b61427ae2eec43e7d7e29ac.png)

Now we expand the sample mean term into individual data points and combine it with :

![1*OsRkH-uq5WtBHEj1oBrEow.png](../_resources/fba2bcae1a4b152388b29f736fbc698a.png)
![1*m23Ht4nUfCO06W-CWFCCLw.png](../_resources/b408d531283a979465fcf3945f7463cc.png)
Then we separate the square term into two terms:
![1*QDdQs4g08kFyCF1D74O_lQ.png](../_resources/e56f886e499ea9a8156c66debc92fc8e.png)
![1*Ypv5EPqg17V_-lved6T7BA.png](../_resources/76d4f1a65897378c23ed892fff43c047.png)
This is same as finding the covariance between x*i* and x*j*:
![1*m23Ht4nUfCO06W-CWFCCLw.png](../_resources/3e624a9d204c994587a57e0ea91cd3e5.png)
![1*Ica0BMkOrKuW121TcksvLw.png](../_resources/fdac2eacd3ea41570085f6f51041371d.png)

Now, we know that the covariance is 0 when i is not equal to j as they are independent observations according to our initial assumption. So, we are left with only the terms where i = j and we have n of those terms which is equal to the variance of x*i*:

![1*XmZGHTlKHpsUz5wrrW9WIg.png](../_resources/3c25771901e13b875744bdd3e0dbde0e.png)
![1*qmItMfCp7G3jkPz0k2lslg.png](../_resources/05490d3e2fa4c13609dd5ba992bd1066.png)
Note that the variance of sample mean approaches 0 as n → ∞.

Now that we know the expected value of the sample mean and variance, we are in a better position to discuss the central limit theorem. But first, we should discuss a type of convergence called convergence in distribution which states that a statistic will converge to an entire distribution possessing some inherent randomness. Which means that the probability density function of a statistic should converge to the pdf of a particular distribution when we take large enough sample sizes. The central limit theorem is an application of the same which says that the sample means of any distribution should converge to a normal distribution if we take large enough samples. And once we standardise the sample means, we can approximate it to a standard normal distribution. Standardisation especially means subtracting the mean from a variable and then dividing by the standard deviation. The central limit theorem can be mathematically denoted as following:

![1*qmItMfCp7G3jkPz0k2lslg.png](../_resources/968933cfb97edf6e87e2783ef569400f.png)
![1*QDdQs4g08kFyCF1D74O_lQ.png](../_resources/ec2f7f6c2664607f8a5c78121e3a551c.png)

Here, z is the standardised form of the sample mean also known as the z statistic, is the population mean and is the population standard deviation. We get a root n term because as we had derived before, the standard deviation of the sample means is equal to the standard deviation of the population divided by n.

Now that we have an understanding of the central limit theorem, let’s test it on some data. For this, I have written a function in R using which we can take samples of different sizes from a distribution of our choice.

|     |     |
| --- | --- |
| 1   | simulate  <-  function(nsim,nvec){ |
| 2   |  simdx  <- c() |
| 3   |  for(i  in  1:length(nvec)) |
| 4   |  simdx  <- c(simdx,rep(1:nsim,each=nvec[i])+(i-1)*nsim) |
| 5   |  dt  <- data.table(sim=simdx) |
| 6   |  bigN  <- nrow(dt) |
| 7   |  dt$n  <- rep(rep(nvec,nvec),each=nsim) |
| 8   |  dt$one  <-  1 |
| 9   |  dt$simc  <-  dt[,cumsum(one),by=sim]$V1 |
| 10  |  dt$one  <-  NULL |
| 11  |  return(dt) |
| 12  | }   |
| 13  |     |
| 14  | ## Central limit theorem demo |
| 15  | dt  <- simulate(100000,c(1,2,3,5)) |
| 16  | bigN  <- nrow(dt) |
| 17  | dt$x1  <- runif(bigN,-1,1) |
| 18  | dt$x2  <- runif(bigN,-0.5,0.5) |
| 19  | dt$x3  <- runif(bigN,-2,2) |
| 20  | zstats  <-  dt[,lapply(.SD,mean),by=sim] |
| 21  | zstats  <-  zstats[,.(n,x1*sqrt(12*n)/2,x2*sqrt(12*n)/1,x3*sqrt(12*n)/4)] |
| 22  | names(zstats) <- c('n','x1','x2','x3') |
| 23  | zstats |
| 24  |     |
| 25  | ggplot(zstats[n==1],aes(x=x1)) + geom_histogram(position="identity",binwidth  =  0.01) |
| 26  | ggplot(zstats[n==2],aes(x=x1)) + geom_histogram(position="identity",binwidth  =  0.01) |
| 27  | ggplot(zstats[n==3],aes(x=x1)) + geom_histogram(position="identity",binwidth  =  0.01) |
| 28  | ggplot(zstats[n==5],aes(x=x1)) + geom_histogram(position="identity",binwidth  =  0.01) |
| 29  |     |
| 30  |     |

 [view raw](https://gist.github.com/spikar/881cc3aa73c82e61b97e0b5305e20489/raw/5de03a269ca99913dce0b813a43b3509b4adabf3/central_limit.R)  [central_limit.R](https://gist.github.com/spikar/881cc3aa73c82e61b97e0b5305e20489#file-central_limit-r) hosted with ❤ by [GitHub](https://github.com/)

The simulate function takes two inputs: *nsim*, the number of simulations and *nvec*, the number of n samples to use and returns a data.table class of the right shape for the data we generate later. Then we create a table to store 100,000 samples of sizes 1,2,3,5 each using the simulate function. Then we take the samples from a uniform distribution between 1 and -1. Then we calculate the mean of all samples and plot the pdf separately for each sample size.

![1*Sy8SBPv216kwOLw-Szlz1Q.png](../_resources/614ec08eadb359c7b766f67b1c2238f6.png)
![1*Sy8SBPv216kwOLw-Szlz1Q.png](../_resources/ec7ec5dd48fd4f0ee8f423f30d4da11c.png)
For n=1, and we see that z follows a uniform distribution just like our data.
![1*pxNk7_t5w3hJAkVQuNe9bw.png](../_resources/554cee3f2483b0bfcbbc3439ef654fa3.png)
![1*pxNk7_t5w3hJAkVQuNe9bw.png](../_resources/13b419610241f70814065755732faed8.png)
For n=2, z follows a triangular kind of shape.
![1*-eBPP6lwyrOKsRsulAnFMw.png](../_resources/ef5bfc1fad0fdd786a8096ba5cc07f8f.png)
![1*-eBPP6lwyrOKsRsulAnFMw.png](../_resources/e62618bf8868a0389b443415c6cb6a2c.png)

For n=3, things start getting interesting and z begins to look like a bell curve.

![1*9CoQurU4uUSltLcDsQQI6g.png](../_resources/7bcf3527d1d4752903c6b5c7cf2d6da6.png)
![1*9CoQurU4uUSltLcDsQQI6g.png](../_resources/4d3b997dc7143e62a4c3313612a219f9.png)

For n=5, z becomes almost completely normal. So, for sample size as small as 5, we are able to observe the central limit theorem which makes it all the more powerful with real data.

We use the central limit theorem when we don’t want to model the distribution of the data and we only need to care about the mean and the variance for our statistical analysis. This is one of the most important and useful theorems in statistics.