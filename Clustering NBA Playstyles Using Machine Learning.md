Clustering NBA Playstyles Using Machine Learning

# Clustering NBA Playstyles Using Machine Learning

[![2*EXTlANQ5Sxhg_QfpibqwGQ.png](../_resources/866c5aeaa98ccb2e568a66444465c1f1.png)](https://towardsdatascience.com/@jameslf?source=post_page-----8c7e8e23c90c----------------------)

[James](https://towardsdatascience.com/@jameslf?source=post_page-----8c7e8e23c90c----------------------)

[Oct 6](https://towardsdatascience.com/clustering-nba-playstyles-using-machine-learning-8c7e8e23c90c?source=post_page-----8c7e8e23c90c----------------------) · 9 min read![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='star-15px_svg__svgIcon-use js-evernote-checked' width='15' height='15' viewBox='0 0 15 15' style='margin-top:-2px' data-evernote-id='186'%3e%3cpath d='M7.44 2.32c.03-.1.09-.1.12 0l1.2 3.53a.29.29 0 0 0 .26.2h3.88c.11 0 .13.04.04.1L9.8 8.33a.27.27 0 0 0-.1.29l1.2 3.53c.03.1-.01.13-.1.07l-3.14-2.18a.3.3 0 0 0-.32 0L4.2 12.22c-.1.06-.14.03-.1-.07l1.2-3.53a.27.27 0 0 0-.1-.3L2.06 6.16c-.1-.06-.07-.12.03-.12h3.89a.29.29 0 0 0 .26-.19l1.2-3.52z' data-evernote-id='187' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)

# Intro & Motivation

I love basketball. I love playing it, watching it, or arguing scenarios with friends like who would win one on one, Kobe or Lebron. I had to combine my two passions, basketball and data science, in a machine learning project.

This past summer, two-time NBA Finals MVP Kevin Durant was traded for D’Angelo Russell. Sports analysts started speculating on his fit on the Warriors with headlines like these:

![1*7LtsQveun5uixm2qniWkNw.png](../_resources/f3ee16eaefb4afe07502afeded8d2221.png)
![1*7LtsQveun5uixm2qniWkNw.png](../_resources/9cb6df52f624479b66f4ffc3a89d6819.png)

[Image Source](https://clutchpoints.com/how-dangelo-russell-will-fit-in-with-the-warriors-splash-brothers/)

It got me wondering: how well does D’Angelo Russell fit in with the Warriors? Can we use machine learning to place NBA players into categories to predict how a player fits in on a given team?

The goal of the project is to determine the types of players and their roles based on their activity or how the space they use. Stats such as points, rebounds, assists, steals, blocks, etc. were NOT included as features as they are dependent on data like minutes played (also not included) or number of shots. Including stats like points, rebounds and assists allows for the possibility for the results to be largely based on those features, which is not the goal. The full list of features is listed in the Methodology section below.

Let’s take a look at the data.

# Data

The data was extracted from[stats.nba.com](http://stats.nba.com/) with the help of Python and the Selenium package. Majority of the features selected were based on frequency of plays. Many play type features an offense or a defense stat. For example, ‘Offense Post Up Frequency’ is how frequent that player is in post up plays on offense; ‘Defense Post Up Frequency’ is how frequent the player is playing ‘defense’ on the post up plays. For additional explanation of the features, information can be found here.[https://stats.nba.com/help/glossary/

**Data : 272 Players**

Initially there were 531 players. Players that played less than half the season and less than 1000 minutes were removed. The rationale was to remove any players that did not have consistent playing time. Here’s the full list of players:

![1*_MEvgXjC7XT8aUjEDx2iZQ.png](../_resources/c59aaa5fb16ea5e5181c7eb68eadcd98.png)
![1*_MEvgXjC7XT8aUjEDx2iZQ.png](../_resources/11ca02d762c96414b360694913d233ee.png)
Players
**Features: 41**

600+ features initially. Selected features that only described spacing or actions.

![1*8eeOvnU294Su68vMmdKB2g.png](../_resources/228a4fa582f5c7348209ac810e551a9a.png)
![1*8eeOvnU294Su68vMmdKB2g.png](../_resources/8a306f7f20f9743894eeae3a040a3daa.png)
Features

# Methodology & Model Selection

Because this was an unsupervised learning project whose results would need to be interpreted, I had two goals in mind when selecting a model and choosing the number of clusters:

**1. Distinct Differences Among Clusters. **A small number of clusters with many players would not tell us much about the differences between playstyles.

**2. Avoid Too Many Clusters. **If each NBA player was its own cluster, the results would only tell us that each individual is unique, which wouldn’t be very helpful.

**Model Options: **DBSCAN, **K-means**, Mean Shift

K-Means performed the best in achieving the goals above. The results from DBSCAN and Mean Shift had multiple one player clusters.

**Number of Clusters: **10

I decided to go with multiples of five since there are five positions in basketball. Ten was just right with the methodology goals in mind.

# **Results**

With the results, I calculated the mean of all the features within each group and ranked each group on the highest and second highest feature. Here are some defined terms:

**Primary Feature(s)**: The mean of the listed features were the highest for that group.

**Secondary Features(s):** The mean of the listed features were the second highest for that group.

In addition, a primary feature of each group was chosen to show how the feature compares to the rest of the players using a histogram plot.

# **Group 1**

![1*afddUccjz3fVG4tFCw5Efg.jpeg](../_resources/91f2d60f4a81c8eb629d856713640e3b.jpg)
![1*7TZt1u3G4YgiLAiX8SoMcA.jpeg](../_resources/870e7319f7060a46de8ac5a75524b569.jpg)
Stephen Curry

Bradley Beal, Buddy Hield, Stephen Curry, Evan Fournier, Trevor Ariza, Kyle Lowry, Joe Ingles, Otto Porter Jr., Bojan Bogdanovic, Avery Bradley, Tim Hardaway Jr., Jayson Tatum, Justise Winslow, Jeremy Lamb, E’Twaun Moore, Kevin Knox, Kevin Huerter, Bogdan Bogdanovic, Gary Harris, Bryn Forbes, Eric Gordon, Tyler Johnson, Damyean Dotson, Taurean Prince, Garrett Temple

**Primary Feature(s):** Defense Isolation Shot Frequency

**Secondary Feature(s):** Defense Handoff Frequency, Defense Off Screen Shot Frequency, Defense Offscreen Frequency, Defense Post Up Shot Frequency, Fast Break Frequency, Offense Hand Off Frequency, Offense Off Screen Shot Frequency

![0*qzitakDmLQLXIxRw](../_resources/4ef6ac2ef30628cdf0b6131a2e7e1b97.png)
![0*qzitakDmLQLXIxRw](../_resources/8cc2c154374148e1d3909590d142b5fd.png)
Defense Isolation Shot Frequency

# **Group 2**

Karl-Anthony Towns, LaMarcus Aldridge, Joel Embiid, Thaddeus Young, Blake Griffin, Anthony Davis, Nikola Jokic, Julius Randle, Nikola Vucevic, Deandre Ayton, Myles Turner, Al Horford, Marc Gasol, Marvin Bagley III, Jaren Jackson Jr., Serge Ibaka, Bobby Portis, Enes Kanter, Jonas Valanciunas, Robin Lopez, Markieff Morris, Gorgui Dieng

**Primary Feature(s):** Offense Post Up Frequency, Post Up Touches Frequency
**Secondary Feature(s):** Offense Rebounding Chance Adjusted
![0*9rOSmOUJqAdEcMKm](../_resources/7b1169475b8ad7ccc7c41c2f458afd93.png)
![0*9rOSmOUJqAdEcMKm](../_resources/06d4ec1ab79b952cafc5c4c91b8efe60.png)
Offense Post Up Frequency

# **Group 3**

PJ Tucker, Draymond Green, Marvin Williams, Jae Crowder, Brook Lopez, Dario Saric, Dewayne Dedmon, Jeff Green, Kelly Olynyk, Davis Bertans, Mike Muscala, Maxi Kleber, Jared Dudley, Mike Scott, Jonas Jerebko, Anthony Tolliver, Vince Carter

**Primary Feature(s):** Catch Shoot Frequency, Offense Spot Up Shot Frequency, Wide Open Shot Frequency, Defense Isolation Frequency, Defense Post Up Frequency

**Secondary Feature(s):** Defense Spot Up Frequency, Passes Made Over Passes Received

![0*A0BYAZZFzI3GvqNV](../_resources/6fa938a8a41344867ce110f23415487f.png)
![0*A0BYAZZFzI3GvqNV](../_resources/6d71298446abfb206f96098f1e9b9a5e.png)
Catch Shoot Frequency

# **Group 4**

Josh Richardson, CJ McCollum, Mike Conley, Jamal Murray, De’Aaron Fox, Trae Young, Cedi Osman, Elfrid Payton, Kris Dunn, Dennis Schroder, Eric Bledsoe, Malcolm Brogdon, Tomas Satoransky, Patrick Beverley, Dennis Smith Jr., Emmanuel Mudiay, Fred VanVleet, Ricky Rubio, Shai Gilgeous-Alexander, Darren Collison, Reggie Jackson, D.J. Augustin, Cory Joseph, Derrick White, Ryan Arcidiacono

**Primary Feature(s):** Defense Rebounding Distance, Defense Pick & Roll Ball Handler Frequency, Average Dribbles Per Touch, Average Speed Offense

**Secondary Feature(s):** Average Seconds Per Touch, Offense Pick & Roll Ball Handler Frequency, Offense Rebounding Distance, Pull Up Shot Frequency

![0*4x4O0y_gCT0bpEAR](../_resources/8188e941eadbb3595dc6bf84de78c29f.png)
![0*4x4O0y_gCT0bpEAR](../_resources/458c8841a9e513176b2ccc2278a5f439.png)
Defense Ball Handler Frequency

# Group 5

![1*7TZt1u3G4YgiLAiX8SoMcA.jpeg](../_resources/831766897ba2fa8e9e0536b7fa05e24c.jpg)
![1*YJJWLsHR_aD3o0oCLXK9-w.jpeg](../_resources/336b8cb2fa2cfe2c5e78d00b0ccdda3e.jpg)
LeBron James

Jrue Holiday, Paul George, Zach LaVine, Tobias Harris, Brandon Ingram, Jimmy Butler, Devin Booker, Kawhi Leonard, DeMar DeRozan, Kemba Walker, Russell Westbrook, Damian Lillard, Andrew Wiggins, Donovan Mitchell, Kyrie Irving, Kevin Durant, LeBron James, James Harden, Khris Middleton, Luka Doncic, Collin Sexton, D’Angelo Russell, Chris Paul, Rajon Rondo, Jordan Clarkson

**Primary Feature(s):** Pull Up Shot Frequency, Offense Isolation Frequency, Offense Pick & Roll Ball Handler Frequency, Average Seconds Per Touch

**Secondary Feature(s):** Average Dribbles Per Touch, Defense Pick & Roll Ball Handler Frequency, Defense Rebounding Chance Adjusted, Open Shot Frequency

![0*RaiXqpe8wIio38qt](../_resources/02a3aceb2f2d7785033c66eb94550f34.png)
![0*RaiXqpe8wIio38qt](../_resources/cf83e27af20c42896ff606efd279e1c1.png)
Average Seconds Per Touch

# **Group 6**

Nicolas Batum, Lonzo Ball, Mikal Bridges, Danny Green, Kelly Oubre Jr., Jonathan Isaac, Terrance Ferguson, Jaylen Brown, Dorian Finney-Smith, Kenrich Williams, Josh Okogie, DeMarre Carroll, DeAndre’ Bembry, Maurice Harkless, Andre Iguodala, Rodions Kurucs, James Ennis III, Shaquille Harrison, Pat Connaughton, Royce O’Neale, OG Anunoby, Torrey Craig, Justin Jackson, Bruce Brown, Frank Jackson

**Primary Feature(s):** Fast Break Frequency, Defense Post Up Shot Frequency, Defense Shot Frequency

**Secondary Feature(s):** Defense Isolation Shot Frequency, Offense Spot Up Shot Frequency, Wide Open Shot Frequency

![0*2Swoz1qr5IE42NIs](../_resources/7bc4c4dca5e0f712dd71eca59b4212f6.png)
![0*2Swoz1qr5IE42NIs](../_resources/750b6eeaaf765e811179af7636b61430.png)
Fast Break Frequency

# **Group 7**

DeAndre Jordan, Montrezl Harrell, Bam Adebayo, JaMychal Green, Mason Plumlee, Mitchell Robinson, Zach Collins

**Primary Feature(s): **Offense Playtype Misc Frequency, Offense Misc Frequency, Closely Contested Shot Frequency, Defense Pick & Roll Ball Handler Shot Frequency, Defense Spot Up Shot Frequency

**Secondary Feature(s):** Contested Shot Frequency, Defense Shot Frequency, Elbow Touches Frequency, Offense Cut Frequency, Offense Pick & Roll Roll Man Frequency, Offense Post Up Frequency, Paint Touches Frequency, Post Up Touches Frequency

![0*FOP6MHHhWVf9Yohh](../_resources/cdb7affafdca7d627b9020e72081682c.png)
![0*FOP6MHHhWVf9Yohh](../_resources/fabeeb2eca25460f1990868801e9900a.png)
Closely Contested Shot Frequency

# **Group 8**

![1*KjAtcoNUtNDjpBOR5yk1gw.png](../_resources/ea66568c37198f237e806d17990e6605.jpg)
![1*afddUccjz3fVG4tFCw5Efg.jpeg](../_resources/3d2618d14ed2ca17a4dd2813b84d77b6.jpg)
Giannis Antetokounmpo

Kyle Kuzma, Aaron Gordon, Ben Simmons, Harrison Barnes, Jerami Grant, Pascal Siakam, Giannis Antetokounmpo, Lauri Markkanen, T.J. Warren, Kyle Anderson, Danilo Gallinari, Al-Farouq Aminu, Jabari Parker, Nikola Mirotic, Marcus Morris, Rudy Gay, Paul Millsap, Noah Vonleh, Nemanja Bjelica, Wilson Chandler, Miles Bridges, Rondae Hollis-Jefferson, Mario Hezonja, James Johnson, Derrick Jones Jr.

**Primary Feature(s):** Defense Rebounding Chance Adjusted, Defense Spot Up Frequency, Defense Off Screen Shot Frequency

**Secondary Feature(s):** Defense Isolation Frequency, Defense Pick & Roll Ball Handler Shot Frequency, Defense Spot Up Shot Frequency, Offense Isolation Frequency

![0*typJiXZhrrqXyn5V](../_resources/6944a380f894a09cd3461fe6311d0fbb.png)
![0*typJiXZhrrqXyn5V](../_resources/98fbde9a9a3e357c452157413227660b.png)
Defense Rebounding Chance Adjusted

# **Group 9**

Klay Thompson, JJ Redick, Justin Holiday, Joe Harris, Reggie Bullock, Wesley Matthews, Terrence Ross, Allen Crabbe, Kentavious Caldwell-Pope, Landry Shamet, Wayne Ellington, Marco Belinelli, Darius Miller, Langston Galloway, Kyle Korver, Doug McDermott, Tony Snell

**Primary Feature(s):** Offense Hand Off Frequency, Offense Off Screen Shot Frequency, Open Shot Frequency, Offense Rebounding Distance, Defense Handoff Frequency, Defense Off Screen Frequency

**Secondary Feature(s):** Average Speed Offense, Catch Shoot Frequency, Defense Rebounding Distance

![0*q67IDkGHsZSSMB59](../_resources/3feb0ec9fa8ebf905ba3274bf5bb5cad.png)
![0*q67IDkGHsZSSMB59](../_resources/02b0662d1b43f4f2217cdda1243337a4.png)
Open Shot Frequency

# **Group 10**

Steven Adams, Clint Capela, Rudy Gobert, Andre Drummond, John Collins, Willie Cauley-Stein, Tristan Thompson, Jusuf Nurkic, Cody Zeller, Jarrett Allen, Larry Nance Jr., Wendell Carter Jr., Domantas Sabonis, Taj Gibson, Derrick Favors, Dwight Powell, JaVale McGee, Hassan Whiteside, Thomas Bryant, Alex Len, Kevon Looney, Ed Davis, Ivica Zubac, Jakob Poeltl, Ante Zizic

**Primary Feature(s): **Offense Pick & Roll Roll Man Frequency, Offense Cut Frequency, Contested Shot Frequency, Offense Rebounding Chance Adjusted, Passes Made Over Passes Received, Elbow Touches Frequency, Paint Touches Frequency

**Secondary Feature(s):** Closely Contested Shot Frequency, Defense Post Up Frequency, Offense Misc Frequency, Offense Playtype Misc Frequency

![0*5mWN6lYm1OHGmLX_](../_resources/5fd2c4b157eede880eb0622e2df9fda8.png)
![0*5mWN6lYm1OHGmLX_](../_resources/e1c111113145e5e1439a9a2a3d06b22b.png)
Paint Touches Frequency

I was very surprised by the results. Usually, when we talk about one of the best point guards in the NBA like Steph Curry, we typically put him in the same category as other star players, but the model put him into Group 1 with mostly average players. In contrast, group 5 had many star players. They can be categorized as ball dominant players and had the primary features: Pull Up Shot Frequency, Offense Isolation Frequency, Offense Pick & Roll Ball Handler Frequency, Average Seconds Per Touch.

I’d love to discuss all the groups in detail, but let’s instead move on to visualizations since this is a Data Science project.

# Visualizing the Results

Because it is very difficult to visualize 41 dimensions, principal component analysis (PCA) was applied to reduce the 41 dimensions to 3 dimensions. For those unfamiliar with PCA,

[‘*PCA finds a new set of dimensions (or a set of basis of views) such that all the dimensions are orthogonal (and hence linearly independent) and ranked according to the variance of data along them. It means more important principle*](https://medium.com/@aptrishu/understanding-principle-component-analysis-e32be0253ef0)

Taking the model results from K-means and PCA dimension reduction, here are some screenshots of the 3D clusters created in Plotly:

![1*p77NUkeMtTrBlyuv_c3ygQ.png](../_resources/6f7d2ef51b9be79745ca3a8e2a6e53fa.png)
![1*p77NUkeMtTrBlyuv_c3ygQ.png](../_resources/0d5d12d22cd192694695464cdd5cfd66.png)
3D Plot

Separation between the clusters can be clearly be seen in 3D space, and the plot gives us an idea of how K-means determined the clusters in 41 dimensions.

# **Conclusion & Last Thoughts**

Back to the original question, how well does D’Angelo Russell fit with Steph Curry? Let’s look back at Group 5.

![1*YJJWLsHR_aD3o0oCLXK9-w.jpeg](../_resources/e18567873f123bf990102e8009b5805e.png)
![1*KjAtcoNUtNDjpBOR5yk1gw.png](../_resources/6b895dea89f5529fe61b9c74454f9965.png)

The Warriors traded Kevin Durant away for D’Angelo Russell. Both are members of group 5, the ball dominant players.

Thus, my recommendation to Warriors head coach Steve Kerr is to play Curry and Russell together.[Of course, he already knows this and probably did not need a model to tell him that.](https://sports.yahoo.com/steve-kerr-envisions-starting-stephen-140046295.html) I predict Russell will handle the ball more and Curry will play more of an off ball role.

In the future, I would love to further analyze the players that make up each group and see how successful each player is at performing their primary and secondary features. With more analysis, we could improve player performance by looking at which to improve areas that have limited success or redefine the player’s role on the team.

Hope you enjoyed the read and I would love to know what you think. Thanks for reading!