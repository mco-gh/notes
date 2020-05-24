We Analysed the 527,350 Facebook Ads placed by the US Presidential Candidates. Here Are The Results.

![1*idvPKjhQ5K1iDQFQGNVIdw.png](../_resources/786dcb8b05502160299fea2813d0c25e.png)
![1*idvPKjhQ5K1iDQFQGNVIdw.png](../_resources/9feb7cc2874ca817bf09151a0e735888.png)

# We Analysed the 527,350 Facebook Ads placed by the US Presidential Candidates. Here Are The Results.

## Using the Facebook Ad Library API to reveal how each candidate is using social media to attract voters.

[![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='52' height='58' viewBox='0 0 52 58' class='ha gm lg lh li lj dl js-evernote-checked' data-evernote-id='138'%3e%3cpath d='M1.49 16.25A27.53 27.53 0 0 1 26 1.55V.45A28.63 28.63 0 0 0 .51 15.75l.98.5zM26 1.55a27.53 27.53 0 0 1 24.51 14.7l.98-.5A28.63 28.63 0 0 0 26 .45v1.1zm24.51 40.2A27.53 27.53 0 0 1 26 56.45v1.1a28.63 28.63 0 0 0 25.49-15.3l-.98-.5zM26 56.45a27.53 27.53 0 0 1-24.51-14.7l-.98.5A28.63 28.63 0 0 0 26 57.55v-1.1z' data-evernote-id='139' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)![1*QqMD1rth7ahcS7Gc415R9w.jpeg](../_resources/c6f1ddde0c3f38fb76ad1e908573d9c6.jpg)](https://medium.com/@dtfoster?source=post_page-----2dcc32fe2c02----------------------)

[David Foster](https://medium.com/@dtfoster?source=post_page-----2dcc32fe2c02----------------------)

[Aug 10](https://medium.com/applied-data-science/56-070-165-facebook-ad-spend-of-us-presidential-candidates-broken-down-by-age-and-gender-2dcc32fe2c02?source=post_page-----2dcc32fe2c02----------------------) · 6 min read![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='star-15px_svg__svgIcon-use js-evernote-checked' width='15' height='15' viewBox='0 0 15 15' style='margin-top:-2px' data-evernote-id='155'%3e%3cpath d='M7.44 2.32c.03-.1.09-.1.12 0l1.2 3.53a.29.29 0 0 0 .26.2h3.88c.11 0 .13.04.04.1L9.8 8.33a.27.27 0 0 0-.1.29l1.2 3.53c.03.1-.01.13-.1.07l-3.14-2.18a.3.3 0 0 0-.32 0L4.2 12.22c-.1.06-.14.03-.1-.07l1.2-3.53a.27.27 0 0 0-.1-.3L2.06 6.16c-.1-.06-.07-.12.03-.12h3.89a.29.29 0 0 0 .26-.19l1.2-3.52z' data-evernote-id='156' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)

In [March 2019](https://newsroom.fb.com/news/2019/03/a-better-way-to-learn-about-ads/), Facebook launched the [Ad Library](https://www.facebook.com/ads/library/) — a direct response to the [Cambridge Analytica scandal](https://en.wikipedia.org/wiki/Facebook%E2%80%93Cambridge_Analytica_data_scandal) that hit the platform in early 2018.

The Ad Library is a place where anyone can see ads placed by any Facebook page. Currently this is available for ads relating to social, political, or electoral issues.

The data can be accessed programmatically through the Ad Library API. At [Applied Data Science](https://adsp.ai/), we use this open data to generate insight and shine light on how advertisers are using Facebook to influence voters. If you’re interested in receiving this analysis on a regular basis, please do [get in touch](https://adsp.ai/contact).

One area of particular relevance and interest is the US 2020 Presidential campaign. In this post, we shall explore the spend of each candidate.

* * *

*...*

# Overall spend

First, let’s take a look at the total spend of each Democrat candidate and the current president, between May 2018 and July 2019 inclusive:

![1*v8mtSEbFRWqe2zhKc_9R8A.png](../_resources/1dc58bb80847baa11dff5fd10a350c07.png)
![1*HhaIaEmpjV3yE9QNaZqKcg.png](../_resources/2cd1a32d688a306e69561638a22bddb8.png)
Spend by candidate

The overall spend totals $56,070,195 — across 527,350 ads, with Trump accounting for 30% of the total. For clarity, in this article we shall focus primarily on the 13 candidates who have spent more than $1m across this timeframe.

The following chart shows that the $8.9m spent by O’Rourke (orange) was mostly during the 2018 Senate election campaign in Texas, which he narrowly lost to Ted Cruz.

![1*bnyQNo2ofIyAf5aAnDyHLw.png](../_resources/0f93cbb790c94edc9c82073faa1a0ed8.png)
![1*UMh-U2rra06VIhkVcBi8HQ.png](../_resources/b315b122246618504b76e34d9715c684.png)

Before we break this spend down by demographic, we’ll quickly run through how targeted advertising work on Facebook.

# How targeted ads work on Facebook

![1*UMh-U2rra06VIhkVcBi8HQ.png](../_resources/c38d00a11ddb45412dbc35507369364a.png)
![1*B3Pok50IOaclBMhY1ppwUg.png](../_resources/a4fb91cbd448f70039d5f3dbeb42b0d6.png)
Creating a Facebook Ad

Facebook allows you to select the location, age range, gender and ‘interests’ of your audience.

Only people that fall into your target audience will see the sponsored ad.

Specifying ‘interests’ indirectly affects the distribution of age, gender and location.

![0*8D6Z_DYar9LddczD.png](../_resources/bb04e63bb3e1b56d040ce63ad0000c05.png)
![1*cB2FtUKZHPCQrLXToHQuGw.png](../_resources/731f6563d813fca0652c69c33503c9ad.png)

In the Ad Library, you can see the actual demographic distribution of people who were shown the ad.

In this particular example, both males and females aged 35+ were shown the advert, but there is a heavy bias toward the older demographic, due to the selection of certain interests.

The Ad Library does not allow you to see which interests were chosen for a particular ad — only the resulting distribution.

The same information is also available through the API. By assigning the spend of the advert proportionally across this distribution and summing, we can calculate how much each candidate is spending on each demographic aggregated across all ads.

# Spend by demographic

Now let’s break each candidate’s spend down by demographic — starting with gender.

![1*sqgD4Pz38lG1Z5gNVuBANg.png](../_resources/5ca11aeeeb0f577ec9f2886da1d42843.png)
![1*v8mtSEbFRWqe2zhKc_9R8A.png](../_resources/c1ef1892101bdb6fc3fc6f6c9d1134a0.png)
Percentage spend by gender for each candidate

First, we can see that the majority of candidates are leaning towards targeting a female audience. The average split across all candidates aggregated is 57% / 43%, in favour of a female audience.

We can also perform the same analysis by age.
![1*wLm2vUx2PYbP8VQTu5vMqA.png](../_resources/8aaba963a11d2056e81233665cbe30ae.png)
![1*wLm2vUx2PYbP8VQTu5vMqA.png](../_resources/d47458be1f699b62a919384b0f4bb88c.png)
Percentage spend by age bracket, for each candidate

Biden targets the oldest audience, with 84% of his Facebook advertising being shown to over 45s. Yang targets a younger audience — 81% of his ads are shown to under 45s.

We can also view age and gender on the same graph, by plotting the average age targeted against the percentage female spend, for each candidate.

![1*i-w2jRcSteQeG3JOACK8Pw.png](../_resources/495ca55eabfea5a518a4b59d2554a65a.png)
![1*sqgD4Pz38lG1Z5gNVuBANg.png](../_resources/aebc4bbc8be640fd9efffc9195fafa3f.png)
Percentage spend on female audience against average age of audience

What’s interesting here is the strong relationship between female spend and average age, amongst Democrat candidates.

The four Democrat candidates with the smallest % female ad spend (Yang, Sanders, O’Rourke, Buttigieg) are also the four with the youngest audience. At the other end of the spectrum, candidates who target a more female audience (Castro, Booker, Gillibrand etc.), also target an older audience.

This means there is a clear gap in the top left section of the chart — representing older men. Trump’s average just about falls in this segment, but no Democrat candidate comes close.

To dig a little deeper into this, let’s check out the overall split of ad spend across the 13 candidates in total, by age and gender.

![1*HhaIaEmpjV3yE9QNaZqKcg.png](../_resources/935d90c3161d469e79b571216f0016bb.png)
![1*PL7LYIijPyTVcdy8z8LJag.png](../_resources/3f6be4626e61244f8872f06e77f83fec.png)
Percentage of spend by age and gender across the 13 candidates
What if we now coloured this chart by candidate?
![1*xa_Wi5fv-arJqvKH4_VMjA.png](../_resources/5881d0f1841a56e6750a9c1486f4b2a8.png)
![1*xa_Wi5fv-arJqvKH4_VMjA.png](../_resources/d120db1c29570d0aa1574b370111e05e.png)
Percentage of spend by age and gender, coloured by candidate

It’s clear that whilst Trump’s advertising spend is split approximately evenly between men and women, he is able to take a greater share of the market for older men, because there is less competition for this demographic from Democrat candidates.

This is even clearer if we show the proportion of spend for each age group and gender separately, so that each column totals 100%.

![1*PL7LYIijPyTVcdy8z8LJag.png](../_resources/df5a6fd239e6eb5af34e5e7b3411b495.png)
![1*bnyQNo2ofIyAf5aAnDyHLw.png](../_resources/be206ff25f707de5f3206c44f24aec89.png)

Percentage of ‘market share’ (amongst the 13 candidates) for each age group and gender bracket.

So even though Trump spends roughly the same amount of advertising money on 45–64 men as 45–64 women, he is able to achieve 46% of the market share for the male group compared to 30% for the female group, as the Democrat representation is stronger in the female demographic.

A similar idea can be seen for the 18–24 male demographic — Yang takes 11% of this market, even though his total spend is much smaller than say, the spend of Seyer to capture the 11% share of the 45–54 female bracket.

# Summary

In this article we have shown how the Facebook Ad Library API can be used to produce detailed, transparent summaries of advertising spend on the platform.

We also produce similar real-time analysis of social and political advertising spend across a range of countries, including the UK and across Europe.

If you would like additional information on any of the above, or further detail on region, impressions or CPM metrics do [get in touch](https://adsp.ai./contact).

* * *

*...*
![1*cB2FtUKZHPCQrLXToHQuGw.png](../_resources/31d706e559473c07e21be19e0b014195.png)
![0*8D6Z_DYar9LddczD.png](../_resources/335dbaf9d02299a0e867366d32741c9a.png)

This is the blog of Applied Data Science, a consultancy that develops innovative data science solutions for businesses. To learn more, feel free to get in touch through our [website](https://adsp.ai/).

# Additional information

Below is the split of advertising spend by age and gender for each of the 13 candidates analysed in this article individually.

![1*B3Pok50IOaclBMhY1ppwUg.png](../_resources/a1b878dd5c105cab479c452bd84b3eb0.png)
![1*i-w2jRcSteQeG3JOACK8Pw.png](../_resources/669752bd6f69b8d2b8c580dff7508b09.png)
Breakdown of spend by age and gender for each candidate