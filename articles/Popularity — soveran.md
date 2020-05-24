Popularity — soveran

# Popularity

Donald Knuth once said: "If I find too many people adopting a certain idea I'd probably think it's wrong".

Good tools can be popular, but that doesn't imply *all good tools are popular*, or *all popular tools are good*. We can reflect on whether the same logic applies to something other than tools: for example, are the best singer and the most popular singer the same person? Is the most sold beverage also the best one? It's tempting to distance ourselves from the problem and discuss what "best" means, but I think we could agree that, at least in those examples, we would be talking about two different singers and two different beverages. And yet, what if most people think otherwise? If most people think otherwise we would think they are wrong, just as Donald Knuth said.

In software development, a lot of people pick the most popular tool that can solve a given problem. Popularity is measurable: you can check the number of downloads, the number of stars, the questions and answers all over the web. Quality, on the other hand, is hard to measure: you have to read the code and prove its correctness, evaluate several metrics and heuristics. It's hard work compared to counting stars. Then, as a lot of people pick the most popular tool that can solve a given problem, the popular tool gets more downloads, more stars, and more people ask questions about it. Popularity is the best trait for becoming more popular.

If I find too many people adopting a certain software tool, I'd probably think it's bad. It would require an in depth analysis to convince me otherwise, because the mechanics at work are well established.

A bit over a year ago, somebody pointed me to [a conversation](http://tinyurl.com/ov6hbgd) in a forum regarding a tool I've been using for the past five years. I will reproduce the ideas here.

It all started when the co-founder and CTO of a tech company asked for help to decide whether or not using [Cuba](http://cuba.is/) would be a good fit for his project. Here's the original post:

> My company hired a team of developers to build an MVP of a web app. We've talked exclusively of using Rails, but now that they've started development, they're using a microframework called Cuba.

> Is anyone familiar with Cuba? I've been vetting it all day and I'm not sure about it.

> The main benefit is that it's tiny (<300 LOC) and faster than Rails, because it's essentially just a router for a Rack app. I'm slightly worried that the team is simply sticking to what they've been using for years rather than what is the best solution... the Cuba gem hasn't been updated since mid 2012. I'm concerned that this microframework isn't as future-proof as we need, and that it may be harder to migrate development to our own team once the MVP is done.

> If anyone has any thoughts, please share them.

Many replies followed, some of them stating the fact that using Cuba would be fine, especially if the team was comfortable with it. Others replied that, as they had never heard of Cuba, it was better to use Rails or Sinatra.

A few days later, the original poster sent this message:
> Thanks for all the valuable feedback everyone!

> I agree that I would prefer a framework with a larger community, but we're going to go with Cuba for a few reasons:

> 1. The team is very comfortable and efficient with it.

> 2. It's essentially the same as Sinatra at its core, but claims to be smaller and faster.

> 3. Cuba itself is extremely easy to work with because it barely does anything. You can read the entire source in 5 minutes and understand it completely. I'm confident future teams could pick it up.

> 4. Even though there's little to no community, Cuba is very well tested, and simple enough that I'm not worried about deprecation.

> I thank you all again for taking the time to share your thoughts.

At that point the CTO was convinced the technology was sound. The fact that there was little code to read probably helped. One person argued that strict discipline with the project structure would be required, someone else expressed concerns that in the end, the team would have to "rebuild Rails" in order to match its functionality. The original poster then replied.

About structure:

> Thanks for the concern. I've been working with the team and overseeing the repo on GitHub since the very beginning of development. I was very vocal about my concerns, which were very similar to yours. It turns out the team is very experienced in building large scale production quality apps in Cuba, and are very organized, which is a relief!

About rebuilding Rails:

> I was worried that the team would have to "> rebuild Rails"> as well, but the thing is, many parts of Rails aren't required by most apps, and they've done this before, so their toolbox is already full of handpicked solutions for common problems that a web app would face. If I was doing the development, I would absolutely choose Rails because I'm not comfortable enough with the microframeworks to be able to achieve any sort of efficient result, but so far we've been in development almost a week and I'm quite pleased.

He posted the original message because he had the same concerns other people expressed in their replies, yet after only one week of development those concerns were addressed and he was happy with the decision. That didn't prevent further criticism, and many comments followed recommending Rails and Sinatra as alternatives based on familiarity and popularity.

Finally, an extremist suggested to fire the team:

> If you have an agreement that they use Rails—get them to use Rails. Simple as that. They just can't decide to use something else without discussing that with you. Since they are not keeping to the agreement, don't pay them. Even the Sr. Engineer can't make such a decision without discussing it with the customer. I think their behavior is very very unprofessional.

If you care about your tools and recommend what you think is best, somebody may still think you are unprofessional and you deserve no pay.

Rails, Sinatra and Cuba are tools with different traits, and it's expected that people will recommend whatever works for them. But we should be extremely cautious about taking what is popular for what is good, and conversely we should not disregard something just because it didn't gather enough stars. I'm not claiming here that one of those tools is better than the others: even if I have a strong preference, the question should be open and the code should be analyzed by the potential users.

When Rails was created, Ruby wasn't mainstream. When Twitter launched, Rails had been out for just four months. Adopting Ruby and Rails were bold moves made by people that didn't care about popularity. They were forced to assess the quality despite the lack of stars.

Technical analysis is hard work. Following the crowd is easy, but it's often a shortcut to the wrong place.

⊙ 2015-04-09