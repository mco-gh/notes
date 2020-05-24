Opinion Spam Detection: Detect Fake Reviews and Reviewers

#

Opinion Spam Detection: Detecting Fake Reviews and Reviewers

###

Many names: Spam Review, Fake Review, Bogus Review, Deceptive review
Opinion Spammer, Review Spammer, Fake Reviewer, Shill (Stooge or Plant),

(See this [The New York Times](http://www.nytimes.com/2012/01/27/technology/for-2-a-star-a-retailer-gets-5-star-reviews.html?_r=2&ref=business) front page article, Jan. 26, 2012)

(Bloomberg [BusinessWeek](http://www.businessweek.com/magazine/a-lie-detector-test-for-online-reviewers-09292011.html), Sept. 29, 2011 and [more ...](http://www.cs.uic.edu/~liub/FBS/media-coverage.html))

###   *New Book*: ![new.gif](../_resources/31b9c50c0f2cc3fbeb8ba8164264f466.gif)  [Sentiment Analysis: mining opinions, sentiments, and emotions](http://www.cambridge.org/us/academic/subjects/computer-science/knowledge-management-databases-and-data-mining/sentiment-analysis-mining-opinions-sentiments-and-emotions). Cambridge University Press, available from March 2015.

###  Book: [**Sentiment Analysis and Opinion Mining**](http://www.cs.uic.edu/~liub/FBS/SentimentAnalysis-and-OpinionMining.html)  (Introduction and Survey), Morgan & Claypool, May 2012.

### *Fake news detection* can be done in similar ways to fake review detection as the behaviors of fraudsters in both cases are similar.

## Introduction

It has become a common practice for people to read online opinions/reviews for different purposes. For example, if one wants to buy a product, one typically goes to a review site (e.g., amazon.com) to read some reviews of the product. If most reviews are positive, one is likely to buy the product. If most reviews are negative, one will almost certainly not buy it. Positive opinions can result in significant financial gains and/or fames for busineses, organizations and individuals. This, unfortunately, gives strong incentives for opinion spamming.

 **Can you figure out**** which of these [three reviews](https://www.cs.uic.edu/~liub/FBS/fake-reviews.html#reviews) are fake?**

**Opinion Spamming**: It refers to "illegal" activities (e.g., *writing fake reviews*, also called *shilling*) that try to mislead readers or automated [opinion mining and sentiment analysis](http://www.cs.uic.edu/~liub/FBS/sentiment-analysis.html) systems by giving undeserving positive opinions to some target entities in order to promote the entities and/or by giving false negative opinions to some other entities in order to damage their reputations. Opinion spam has many forms, e.g., *fake reviews* (also called *bogus reviews*), *fake comments*, *fake blogs*, *fake social network postings*, *deceptions*, and *deceptive messages*.

We believe that as opinions on the Web are increasingly used in practice by consumers, organizations, and businesses for their decision making, opinion spamming will get worse and also more sophisticated. Detecting spam reviews or opinions will become more and more critical. The situation is already quite bad.

To the best of our knowledge, my group is the first to conduct research on detecting fake reviews and reviewers (or shills). Our first paper was published in 2007, and subsequent papers were published in 2008, 2010, and 2012. Both my books [**Web Data Mining**](http://www.cs.uic.edu/~liub/WebMiningBook.html) and [**Sentiment Analysis and Opinion Mining**](http://www.cs.uic.edu/~liub/FBS/SentimentAnalysis-and-OpinionMining.pdf) discuss the issue.

 **NOTE**: This is closely related to **Astroturfing**: "Astroturfing refers to political, advertising, or public relations campaigns that are designed to mask the sponsors of the message to give the appearance of coming from a disinterested, grassroots participant. Astroturfing is intended to give the statements the credibility of an independent entity by withholding information about the source's financial connection. The term is a derivation of AstroTurf, a brand of synthetic carpeting designed to look like natural grass." Quoted from the [Wikipedia](http://en.wikipedia.org/wiki/Astroturfing) page.

###  Acknowledgement: This project has been partially funded by *National Science Foundation, Microsoft, and Google*

### Fake Review Detection

We have used supervised learning, pattern discovery, graph-based methods, and relational modeling to solve the problem. Below are some main signals that we have used:

1.  Review content:

    1. **Lexical features** such as word n-grams, part-of-speech n-grams, and other lexical attributes.

    2. **Content and style similarity** of reviews from different reviewers.

    3. **Semantic inconsistency** (we have never used this kind of features). For example, a reviewer wrote "My wife and I bought this car ..." in one review and then in another review he/she wrote "My husband really love ..." (I heard this example from a friend in a company which actively detects fake reviews).

2.  Reviewer abnormal behaviors:

    1.   **Public data available from Web sites**, e.g., reviewer id, time of posting, frequency of posting, first reviewers of products, and many more. For example, do you see anything wrong with the reviews from this user, [Big John](http://www.amazon.com/gp/pdp/profile/A3URRTIZEE8R7W)? What about after you see the reviews of these two users, [Cletus](http://www.amazon.com/gp/pdp/profile/A254LYRIZUYXZG) and [Jake](http://www.amazon.com/gp/cdp/member-reviews/A1O70AIHNS4EIY)? In fact, if you browse the reviews of their reviewed products, you will find another suspicious user/reviewer. This is just one example of atypical behaviors that our algorithms are able to discover.

    2.   **Web site private/internal data **(we have not used such data, but they are extremely useful), e.g., IP and MAC addresses, time taking to post a review, physical location of the reviewer, etc (a lot of them).

3.  Product related features: E.g., product decription, sales volume, and sales rank

4.  Relationships: Complex relationships among reviewers, reviews, and entities (e.g., products and stores).

### Some Fake Review Cases in the News

- **Must Read:**  [Samsung probed in Taiwan over 'fake web reviews'](http://www.bbc.co.uk/news/technology-22166606), April 16, 2013 [BBC News].
- **Must Read:**  [Woman Paid To Post Five-Star Google Feedback](http://www.thedenverchannel.com/news/woman-paid-to-post-five-star-google-feedback), September 15, 2012 [ABC7 News] (our algorithm in [WWW-2012](http://www.cs.uic.edu/~liub/publications/WWW-2012-group-spam-camera-final.pdf) paper can catch them).
- **Must Read:**  [Are You Buying Reviews For Google Places?](http://www.localgoldmine.com/blog/reputation-management/are-you-buying-reviews-for-google-places/), Local Internet Marketing, January 27, 2012. (our algorithm in [WWW-2012](http://www.cs.uic.edu/~liub/publications/WWW-2012-group-spam-camera-final.pdf) paper can catch them).
- **Must Read:**  [The Best Book Reviews Money Can Buy](http://www.nytimes.com/2012/08/26/business/book-reviewers-for-hire-meet-a-demand-for-online-raves.html?pagewanted=1&_r=2&partner=rss&emc=rss), August 25, 2012 [The New York Times].
- **Must Read:**  [For $2 a Star, an Online Retailer Gets 5-Star Product Reviews](http://www.nytimes.com/2012/01/27/technology/for-2-a-star-a-retailer-gets-5-star-reviews.html?_r=2&ref=business), Jan 26, 2012 [The New York Times].
- **Must Read:**  [Amazon Glitch Unmasks War Of Reviewers](http://www.nytimes.com/2004/02/14/us/amazon-glitch-unmasks-war-of-reviewers.html), February 14, 2004 [The New York Times].
- [Charges Settled Over Fake Reviews on iTunes](http://www.nytimes.com/2010/08/27/technology/27ftc.html), August 26, 2010 [The New York Times].
- [Company Settles Case of Reviews It Faked](http://www.nytimes.com/2009/07/15/technology/internet/15lift.html), July 14, 2009 [The New York Times].
- [TripAdvisor warns consumers about fake reviews](http://travel.usatoday.com/hotels/post/2009/07/tripadvisor-warns-consumers-about-fake-reviews-week-long-hotel-sales-ethics-rules-reduce-trips-taken-by-congress/68494570/1), July 16, 2009 [USA Today].
- [Belkin's Development Rep is Hiring People to Write Fake Positive Amazon Reviews](http://thedailybackground.com/2009/01/16/exclusive-belkins-development-rep-is-hiring-people-to-write-fake-positive-amazon-reviews/), January 16, 2009 [The Daily Background].
- [A Fake Amazon Reviewer Confesses](http://blogs.wsj.com/wallet/2009/07/09/delonghis-strange-brew-tracking-down-fake-amazon-raves/), July 9, 2009 [The Wall Street Journal].

###  Professional Fake Review Writing Services (some *Reputation Management* companies)

- [Post positive reviews](http://postingpositivereviews.blogspot.com/) (this site's content and even URL keep changing)
- [Sponsored reviews](http://www.sponsoredreviews.com/) (a site where advertisers and bloggers get in touch to write paid reviews)
- [Pay per post](https://payperpost.com/) (also a site where advertisers and bloggers get in touch to write paid reviews)
- [Need someone to write positive reviews about our company](http://www.freelancer.com/projects/Forum-Posting-Reviews/Need-someone-write-post-positive.html) (budget: $250-$750 USD)
- [Fake review writer](http://www.freelancer.com/projects/by-tag/fake-review-writer.html)
- [Product review writer for hire](http://www.productreviewwriter.com/)
- [Hire a content writer](http://www.hire-a-content-writer.com/)
- [Fake Amazon book reviews (hiring book reviewers)](http://www.blog-relations.com/2006/12/19/fake-amazon-book-reviews/)
- [People are just having fun (not serious)](http://www.amazon.com/Wheelmate-Laptop-Steering-Wheel-Desk/dp/B000IZGIA8/ref=cm_cr_pr_product_top)

###  How to Spot Fake Reviews Manually

- [30 Ways You Can Spot Fake Online Reviews](http://consumerist.com/2010/04/how-you-spot-fake-online-reviews.html) -- [Test Your Ability!](https://www.cs.uic.edu/~liub/FBS/fake-reviews.html#reviews)
- [3 Tips for Spotting Fake Product Reviews - From Someone Who Wrote Them](http://www.moneytalksnews.com/2011/07/25/3-tips-for-spotting-fake-product-reviews-%E2%80%93-from-someone-who-wrote-them/)
- [Hone Your Eye for Fake Online Reviews](http://lifehacker.com/5511726/hone-your-eye-for-fake-online-reviews)
- [How to spot fake user reviews](http://www.consumersearch.com/blog/how-to-spot-fake-user-reviews)

I am doubtful that people can really spot fake reviews reliably (especially those well written ones). I have done experiments with 30+ students to show otherwise. One of the fallacies is that people usually think others would write like them or should write in certain ways.

### Manipulating Social Media (sock puppets - fake identities - fake personas)

- [Revealed: US spy operation that manipulates social media](http://www.guardian.co.uk/technology/2011/mar/17/us-spy-operation-social-networks), Guardian.co.uk, Thursday 17 March 2011.
- [America's absurd stab at systematising sock puppetry](http://www.guardian.co.uk/commentisfree/cifamerica/2011/mar/17/us-internet-morals-clumsy-spammer), Guardian.co.uk, Thursday 17 March 2011.

### China's Internet "Water Army" (Shuijun) - Opinion Spammers

- You can hire people to write and post fake reviews or comments, and even bribe staff at review, forum and microblog sites to delete posts that you do not like.
- ['Water Army' Whistleblower Threatened](http://english.peopledaily.com.cn/90001/90776/90882/7253359.html), January 7, 2011, People's Daily.
- [The Chinese Online "Water Army"](http://www.wired.com/beyond_the_beyond/2010/06/the-chinese-online-water-army/), June 25, 2010, Wired.com.
- If you read Chinese, see [this description](http://baike.baidu.com/view/3098178.htm) from Baidu Baike at baidu.com.

## Data Sets

- [Amazon Product Review Data (Huge)](http://liu.cs.uic.edu/download/data/) used in (Jindal and Liu, WWW-2007; WSDM-2008; Lim et al, CIKM-2010; Jindal, Liu and Lim, CIKM-2010; Mukherjee et al. WWW-2011; Mukherjee, Liu and Glance, WWW-2012) for review spam (fake review) detection. It has information about reviewers, review text, ratings, product info, etc. Due to the large file size, you may need to use *Download Accelerator Plus* (DAP) to download. If you use this data, please cite (Jindal and Liu, WSDM-2008).

## Publications

1. Huayi Li, Geli Fei, Shuai Wang, Bing Liu, Weixiang Shao, Arjun Mukherjee and Jidong Shao. Bimodal Distribution and Co-Bursting in Review Spam Detection. To appear in *Proceedings of International World Wide Web Conference (WWW-2017)*, April 3-7, 2017, Perth, Australia.

2.  Jing Wang, Clement. T. Yu, Philip S. Yu, Bing Liu, Weiyi Meng. “Diversionary comments under blog posts." Accepted. *ACM Transactions on the Web (TWEB)*, 2015.

3.  Huayi Li, Zhiyuan Chen, Arjun Mukherjee, Bing Liu and Jidong Shao. "Analyzing and Detecting Opinion Spam on a Large-scale Dataset via Temporal and Spatial Patterns." Short paper at *ICWSM-2015*, 2015.

4. Huayi Li, Arjun Mukherjee, Bing Liu, Rachel Kornfieldz and Sherry Emery. [Detecting Campaign Promoters on Twitter using Markov Random Fields](http://www.cs.uic.edu/~liub/publications/twitter-promoters-paper531.pdf). to appear in *Proceedings of IEEE International Conference on Data Mining (ICDM-2014)*, December 14-17, 2014.

5. Huayi Li, Zhiyuan Chen, Bing Liu, Xiaokai Wei and Jidong Shao. [Spotting Fake Reviews via Collective Positive-Unlabeled Learning](http://www.cs.uic.edu/~liub/publications/fake-PU-learning-paper274.pdf). to appear in *Proceedings of IEEE International Conference on Data Mining (ICDM-2014, short paper)*, December 14-17, 2014.

6.  Tieyun Qian, Bing Liu. [Identifying Multiple Userids of the Same Author](http://www.cs.uic.edu/~liub/publications/EMNLP-2013-Qian-Liu.pdf). To appear in *Proceedings of Conference on Empirical Methods in Natural Language Processing (EMNLP-2013)*, October 18-21, 2013, Seattle, USA.

7.  Arjun Mukherjee, Abhinav Kumar, Bing Liu, Junhui Wang, Meichun Hsu, Malu Castellanos, and Riddhiman Ghosh. [Spotting Opinion Spammers using Behavioral Footprints](http://www.cs.uic.edu/~liub/publications/KDD-2013-Arjun-spam.pdf). *To appear in Proceedings of SIGKDD International Conference on Knowledge Discovery and Data Mining (KDD-2013)*, August 11-14 2013 in Chicago, USA.

8.  Arjun Mukherjee, Vivek Venkataraman, Bing Liu, and Natalie Glance. [What Yelp Fake Review Filter Might Be Doing](http://www.cs.uic.edu/~liub/publications/ICWSM-2013-Arjun-Spam.pdf). *Proceedings of The International AAAI Conference on Weblogs and Social Media (ICWSM-2013)*, July 8-10, 2013, Boston, USA.

9.  Geli Fei, Arjun Mukherjee, Bing Liu, Meichun Hsu, Malu Castellanos, and Riddhiman Ghosh. [Exploiting Burstiness in Reviews for Review Spammer Detection](http://www.cs.uic.edu/~liub/publications/ICWSM-2013-Geli-burst.pdf). *Proceedings of The International AAAI Conference on Weblogs and Social Media (ICWSM-2013)*, July 8-10, 2013, Boston, USA.

10.  Arjun Mukherjee, Bing Liu, and Natalie Glance. [Spotting Fake Reviewer Groups in Consumer Reviews](http://www.cs.uic.edu/~liub/publications/WWW-2012-group-spam-camera-final.pdf). *International World Wide Web Conference (WWW-2012)*, Lyon, France, April 16-20, 2012. (See *[media coverage](http://www.cs.uic.edu/~liub/FBS/media-coverage.html)* of this work from April 16, 2012)

11.  Guan Wang, Sihong Xie, Bing Liu, Philip S. Yu. [Identify Online Store Review Spammers via Social Review Graph](http://www.cs.uic.edu/~liub/publications/TIST-final.pdf). *ACM Transactions on Intelligent Systems and Technology*, accepted for publication, 2011.

12.  Guan Wang, Sihong Xie, Bing Liu, Philip S. Yu. [Review Graph based Online Store Review Spammer Detection](http://www.cs.uic.edu/~liub/publications/ICDM-2011-final.pdf). *ICDM-2011*, 2011.

13.  Arjun Mukherjee, Bing Liu, Junhui Wang, Natalie Glance, Nitin Jindal. [Detecting Group Review Spam](http://www.cs.uic.edu/~liub/publications/WWW-2011-group-review-spam.pdf). *WWW-2011 poster paper*, 2011.

14.  Nitin Jindal, Bing Liu and Ee-Peng Lim. ["Finding Unusual Review Patterns Using Unexpected Rules"](http://www.cs.uic.edu/~liub/publications/CIKM-final-unexpected.pdf)  *Proceedings of the 19th ACM International Conference on Information and Knowledge Management (CIKM-2010, short paper)*, Toronto, Canada, Oct 26 - 30, 2010.

15.  Ee-Peng Lim, Viet-An Nguyen, Nitin Jindal, Bing Liu and Hady Lauw. ["Detecting Product Review Spammers using Rating Behaviors."](http://www.cs.uic.edu/~liub/publications/cikm-2010-final-spam.pdf)  *Proceedings of the 19th ACM International Conference on Information and Knowledge Management (CIKM-2010, full paper)*, Toronto, Canada, Oct 26 - 30, 2010.

16. Nitin Jindal and Bing Liu. ["Opinion Spam and Analysis."](http://www.cs.uic.edu/~liub/FBS/opinion-spam-WSDM-08.pdf)  *Proceedings of First ACM International Conference on Web Search and Data Mining (WSDM-2008)*, Feb 11-12, 2008, Stanford University, Stanford, California, USA.

17. Nitin Jindal and Bing Liu. ["Review Spam Detection."](http://www.cs.uic.edu/~liub/publications/reviewSpam-2007.pdf) Proceedings of *WWW-2007* (poster paper), May 8-12, Banff, Canada.

##  Three Reviews - Can you figure out which ones are fake?

1.  I want to make this review in order to comment on the excellent service that my mother and I received on the Serenade of the Seas, a cruise line for Royal Caribbean. There was a lot of things to do in the morning and afternoon portion for the 7 days that we were on the ship. We went to 6 different islands and saw some amazing sites! It was definitely worth the effort of planning beforehand. The dinner service was 5 star for sure. One of our main waiters, Muhammad was one of the nicest people I have ever met. However, I am not one for clubbing, drinking, or gambling, so the nights were pretty slow for me because there was not much else to do. Either than that, I recommend the Serenade to anyone who is looking for excellent service, excellent food, and a week full of amazing day-activities!

2.  This movie starring big names - Tom Hanks, Sandra Bullock, Viola Davis, and John Goodman - is one of the most emotionally endearing films of 2012. While some might argue that this film was "too Hollywood" and others might see the film solely because of the cast, it is Thomas Horn's performance as young Oskar that is deserving of awards. The story is about a 9-year-old boy on a journey to make sense of his father's tragic death in the 9/11 attacks on the World Trade Center. Oskar is a bright and nervous adventurer calmed only by the rattle of a tambourine in his ear. "I got tested once to see if I had Asperger's disease," the boy offers in explain of his odd behavior. "The tests weren't definitive." One year after the tragedy, Oskar finds a key in his father's closest and thus begins a quest to find the missing lock. Oskar's battle to control his emotional anxiety and form and mend relationships proves difficult, even with his mother. "If the sun were to explode, you wouldn't even know about it for eight minutes," Oskar narrates. "For eight minutes, the world would still be bright and it would still feel warm." Those fleeting eight minutes Oskar has left of his father make for two hours and nine minutes of Extremely Emotional and Incredibly Inspiring film. Leaving the theatre, emotionally drained, it is a wonder where a movie like this has been. We saw Fahrenheit 9/11 and United 93, but finally here is the story of a New York family's struggle to understand why on "the worst day" innocent people would die. I highly recommend this movie as a must see.

3.  High Points: Guacamole burger was quite tall; clam chowder was tasty. The decor was pretty good, but not worth the downsides. Low Points: Noisy, noisy, noisy. The appetizers weren't very good at all. And the service kind of lagged. A cross between Las Vegas and Disney world, but on the cheesy side. This Cafe is a place where you eat inside a plastic rain forest. The walls are lined with fake trees, plants, and wildlife, including animatronic animals. A flowing waterfall makes sure that you won't hear the conversations of your neighbors without yelling. I could see it being fun for a child's birthday party (there were several that occurred during our meal), but not a place to go if you're looking for a good meal.

4.   **The answer is at the bottom of my homepage. If you get them right, please let me know your clues. ** You can click my name below to get to my homepage.

Created by [Bing Liu,](http://www.cs.uic.edu/~liub) 2008.
[(L)](https://www.cs.uic.edu/~liub/FBS/fake-reviews.html#)Window size:  x
Viewport size:  x