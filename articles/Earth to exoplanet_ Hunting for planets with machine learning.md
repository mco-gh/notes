Earth to exoplanet: Hunting for planets with machine learning

# Earth to exoplanet: Hunting for planets with machine learning

Chris Shallue

Google AI

Andrew Vanderburg

UT Austin

 Published Dec 14, 2017

For thousands of years, people have looked up at the stars, recorded observations, and noticed patterns. Some of the first objects early astronomers identified were planets, which the Greeks called “planētai,” or “wanderers,” for their seemingly irregular movement through the night sky. Centuries of study helped people understand that the Earth and other planets in our solar system orbit the sun—a star like many others.

Today, with the help of technologies like telescope optics, space flight, digital cameras, and computers, it’s possible for us to extend our understanding beyond our own sun and detect planets around other stars. Studying these planets—called exoplanets—helps us explore some of our deepest human inquiries about the universe. What else is out there? Are there other planets and solar systems like our own?

Though technology has aided the hunt, finding exoplanets isn’t easy. Compared to their host stars, exoplanets are cold, small and dark—about as tricky to spot as a firefly flying next to a searchlight … from thousands of miles away. But with the help of machine learning, we’ve recently made some progress.

One of the main ways astrophysicists search for exoplanets is by analyzing large amounts of data from NASA’s [Kepler mission](https://www.nasa.gov/mission_pages/kepler/overview/index.html) with both automated software and manual analysis. Kepler observed about 200,000 stars for four years, taking a picture every 30 minutes, creating about 14 billion data points. Those 14 billion data points translate to about 2 quadrillion possible planet orbits! It’s a huge amount of information for even the most powerful computers to analyze, creating a laborious, time-intensive process. To make this process faster and more effective, we turned to machine learning.

![NASA_PlanetsPart1_v03_1000px.gif](../_resources/3efa3afe13d6a1f95eba6b707be8d5fa.gif)

The measured brightness of a star decreases ever so slightly when an orbiting planet blocks some of the light. The Kepler space telescope observed the brightness of 200,000 stars for 4 years to hunt for these characteristic signals caused by transiting planets.

Machine learning is a way of teaching computers to recognize patterns, and it’s particularly useful in making sense of large amounts of data. The key idea is to let a computer learn by example instead of programming it with specific rules.

I'm a Google AI researcher with an interest in space, and started this work as a 20 percent project (an opportunity at Google to work on something that interests you for 20 percent of your time). In the process, I reached out to Andrew, an astrophysicist from UT Austin, to collaborate. Together, we took this technique to the skies and taught a machine learning system how to identify planets around faraway stars.

Using a dataset of more than 15,000 labeled Kepler signals, we created a [TensorFlow](https://www.tensorflow.org/) model to distinguish planets from non-planets. To do this, it had to recognize patterns caused by actual planets, versus patterns caused by other objects like [starspots](https://en.wikipedia.org/wiki/Starspot) and [binary stars](https://en.wikipedia.org/wiki/Binary_star). When we tested our model on signals it had never seen before, it correctly identified which signals were planets and which signals were not planets 96 percent of the time. So we knew it worked!

 "Kepler 90i is the eighth planet discovered orbiting the Kepler 90 star, making it the first known 8-planet system outside of our own."

Armed with our working model, we shot for the stars, using it to hunt for new planets in Kepler data. To narrow the search, we looked at the 670 stars that were already known to host two or more exoplanets. In doing so, we discovered two new planets: Kepler 80g and Kepler 90i. Significantly, Kepler 90i is the eighth planet discovered orbiting the Kepler 90 star, making it the first known 8-planet system outside of our own.

![NASA_PlanetsPart2_v05_750px.gif](../_resources/3bd3d0e1274af306ec57bfef3274aebc.gif)

We used 15,000 labeled Kepler signals to train our machine learning model to identify planet signals. We used this model to hunt for new planets in data from 670 stars, and discovered two planets missed in previous searches.

Some fun facts about our newly discovered planet: it’s 30 percent larger than Earth, and with a surface temperature of approximately 800°F—not ideal for your next vacation. It also orbits its star every 14 days, meaning you’d have a birthday there just about every two weeks.

![sol-&-kepler-2.gif](../_resources/c8f6782fcac385d4c75da3ee910efe5e.gif)

Kepler 90 is the first known 8-planet system outside of our own. In this system, planets orbit closer to their star, and Kepler 90i orbits once every 14 days. (Note that planet sizes and distances from stars are not to scale.)

The sky is the limit (so to speak) when it comes to the possibilities of this technology. So far, we’ve only used our model to search 670 stars out of 200,000. There may be many exoplanets still unfound in Kepler data, and new ideas and techniques like machine learning will help fuel celestial discoveries for many years to come. To infinity, and beyond!

Posted in:

- [Machine Learning](https://www.blog.google/topics/machine-learning/)