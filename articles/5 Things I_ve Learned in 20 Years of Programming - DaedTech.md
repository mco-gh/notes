5 Things I've Learned in 20 Years of Programming - DaedTech

# 5 Things I’ve Learned in 20 Years of Programming

Category: [The Life of a Programmer](https://daedtech.com/category/process/)| [15 Comments](https://daedtech.com/5-things-ive-learned-in-20-years-of-programming/#comments)

This year, I’ve become increasingly acquainted with [the DEV platform](https://dev.to/).  It’s a refreshingly positive oasis in the large sea of angry Reddit commenters and “well actually” connoisseurs that is the broader software world.

One interesting facet of this community is that it seems pretty beginner-heavy.  I regularly see posts written by and for industry newbies.  And by newbies, I mean folks that are aspiring programmers, in bootcamps, looking for entry level work or in roles with [the unfortunate “junior” qualifier](http://daedtech.com/junior-developer-never-accept/).

I find this enjoyable.  Relative newbies are generally enthusiastic and excited about the industry.  And that excitement is infectious.

But it also makes me feel my industry greybeard status.

[![Lifer.jpg](../_resources/1d1f0583af49dfc4352d40e03aa70f85.jpg)](https://daedtech.com/wp-content/uploads/2013/01/Lifer.jpg)

I think of what I remember Bob Martin saying on a podcast or in a talk or something.

The demand for programmers has grown so dramatically over the last 4-5 decades that the number of programmers is always doubling every five years.  As a result, a programmer with 5 years of experienced has more industry tenure than half of the entire industry.

### Old Man Status

I’m now pushing 20 years in the industry.  I spent about 10 of those in roles where my primary function was to write code.  The other 10 have involved managing programmers, coaching them, consulting with organizations about how to manage them, running a codebase assessment practice and these days, well, actually content marketing.

But in all of these roles I’ve written code to varying degrees.

By my calculations of geometric programmer growth, this makes me more grizzled than 94% of the industry.

So we have a bit of a juxtaposition.  I’m a programming lifer hanging around with a bunch of programming newbies.

This made me wonder to myself, “if I could summarize this experience into succinct bits of advice, and assuming that anyone actually cared, what would I tell these folks?”

[![Guru.jpg](../_resources/b676e9511fbb1ad91798f1e8eb74cc11.jpg)](https://daedtech.com/wp-content/uploads/2013/01/Guru.jpg)

And that’s the premise for this post.  The following are the things I consider to be the most important lessons and takeaways from a 20 year programming career.

## 1. Duplication of Knowledge is the Worst

“Avoid copy paste programming!”

If someone hasn’t yet slapped your hand with a ruler for copying code in your application, pasting it, and adjusting the result (the “copy, paste, and adjust to taste” anti-pattern), consider it slapped now.

Stop it.  Immediately.  This is terrible and sloppy practice.

[![Spaghetti-e1574404164556.jpg](../_resources/e4b086ea695a379d209a4c07f3b1c502.jpg)](https://daedtech.com/wp-content/uploads/2016/10/Spaghetti-e1476422712269.jpg)

Imagine that you have a perfectly serviceable CalculateBill() method, but the product manager wanders over and says, “we’re onboarding new customers in Mexico, and you calculate bills a little differently there.”  So you copy the current method, paste it, rename it CalculateBillMexico() and tweak it as needed.

Here are the problems with this approach:

1. If a future change requires adjustments to the core logic, you now have to do extra labor and modify 2 methods.

2. You now have 2 chances to introduce bugs during such changes.

3. You’ve now established a ‘design pattern’ and your code is now begging for a new, redundant method as your global expansion continues.

4. Your labor is going to increase dramatically as you go.

5. It’s only a matter of time before you introduce bugs by forgetting to change things everywhere you need to.

6. Eventually, all of these methods will differ just enough that you can no longer reasonably merge them back together and fix the mess, but without differing so much that you can avoid making 20 changes each time someone updates a billing rule.

It’s a mess.  And this – copy-paste – is only the *surface level problem*.

### Copy-Pasta Is Only the Beginning

The real problem is duplication of knowledge in your system.

Duplication of knowledge in your system can occur in many ways, and ham-fisted copy-pasta is just the most obvious and obtuse.  Consider other examples of duplicate knowledge:

- A for loop and a code comment right above it explaining the start, end, and increment.
- A global variable assigned a value inline and then (maybe) re-assigned a value from a configuration file.
- A database table with columns “PretaxTotal,” “Tax,” and “Total”
- A wide-ranging ERP system that stores customers in its CRM module and then again in its billing module.

With all of this stuff, the best case scenario is that you have processes and systems in place to diligently track the duplication and ensure that you update it concurrently.

In the case of a vacuous code comment, it might just be the team’s chief nagging officer browbeating you into always checking for comments when you update code.

Or, in the case of the ERP system, it might be a sternly worded department memo telling sales and accounting that they both need to send an official email to ensure that customer information stays in sync.

[![Cartman.jpg](../_resources/cd3a5b9ab74aab9ae110ca15f43f2b98.jpg)](https://daedtech.com/wp-content/uploads/2014/06/Cartman.jpg)

And, remember, those are *best case *scenarios.

Worse scenarios occur when you start building complex logic (which you must then maintain – see the next section) to ensure synchronicity.

Maybe you implement a database trigger whenever there’s a change to the “total” column to make sure that PretaxTotal + Tax still equals Total.  Or perhaps you write some awkward state checking logic to log a warning when the default global variable value doesn’t match the assigned value in the config file.

And, worst case of all is that this data just gets out of sync.  Then you, as a programmer, probably don’t have to worry, since figuring out why you never invoiced a customer or how you’ve overcharged customers for years is probably above your paygrade.

But you can avoid all of that by ruthlessly rooting out and actively resisting duplication of knowledge anywhere in your systems.

## 2. Code is a Liability

As developers, we learn to love code.  It feels good to write code, and it’s exciting to build a thing.

Furthermore, we seek out new languages, paradigms, frameworks, stacks, tools, APIs, and libraries to learn.  We immerse ourselves and celebrate flow – the state in which we gleefully generate code.

[![DeveloperBeatsTheClock.jpg](../_resources/e09d689147c3771842e5be0fc2f00e1c.jpg)](https://daedtech.com/wp-content/uploads/2014/11/DeveloperBeatsTheClock.jpg)

And we’re not alone in this celebration.

Misguided pointy-haireds have even gone so far as to adopt lines of code generated per hour as a metric of productivity.  But even if you don’t get all the way to that point of weapons-grade stupidity, it’s easy to think that more code is better.  Code is the DNA of your killer application and business, and companies consider it valuable intellectual property.

Forget all that.

I can understand why we look at code as an asset.  But the reality is that code is a complete liability.

### Less Is More

You know what’s even better than doing in 10 lines of code what someone else did in 100?  Doing it with 0 lines of code.

Go ahead and write a line of code:
printf(“Hello World!”);
How many things do you think could go wrong?

- Will this code be run in an environment that allows console printing?
- Won’t that magic string be a problem later?
- Shouldn’t you be logging? It’s a best practice.
- Have you even thought about the security implications of this?

Let’s just conservatively call it an even 10 things that can go wrong with this line of code.  So now, let’s add line 2.

Do you think that brings the total to 20 things that can go wrong?

I’d argue that it probably brings it to more like 100.  Call me a pessimist, but I think the relationship between potential problems and lines of code is closer to combinatoric than linear.

[![ScaryComputer-e1522738137994.jpg](../_resources/19a5abbd3a9535059e1e3779b7d20fe5.jpg)](https://daedtech.com/wp-content/uploads/2014/11/ScaryComputer-e1522738137994.jpg)

I’ve actually spent a number of years as a management consultant with a very niche specialty.  I do data-driven codebase assessments and help IT leadership make strategic decisions about codebases.

So I see, analyze and gather statistics on lots and lots of codebases.

If you include codebases that I’ve robo-analyzed on top of client codebases, I’ve gathered detailed statistical info on more than 1,000 of them.  I’ve then taken that data and run regression analysis on it, looking for correlations.

Do you know what correlates more than anything else with undesirable codebase properties?  The size of the codebase.

[![ComplicatedManual.jpg](../_resources/d2692a0f825ae8f383184f43b704d111.jpg)](https://daedtech.com/wp-content/uploads/2014/11/ComplicatedManual.jpg)

Almost everything bad about codebases has a significant relationship with the size of a codebase, measured in logical lines of code.

I love code.

I love writing it, studying it, analyzing it, and building things with it.  But make no mistake – it’s a massive liability.  Always strive to do everything using as little code as humanly possible.

## 3. Senior Developers: Trust but Verify

In my first software engineering job, at age 23, I admired the senior developers there with an almost fervent reverence.  Paul, Raymond, Chris, Ken – averaging around 20 years apiece of experience – I can picture all of them vividly, and I found their facility with multiple programming languages utterly amazing.

I learned *a ton* from them.

[![Teacher-with-Classroom-of-Businessmen-e1533097850343.jpg](../_resources/8c97b4fd6a06e1c8f5a466785b8fabaa.jpg)](https://daedtech.com/wp-content/uploads/2017/01/Teacher-with-Classroom-of-Businessmen-e1533097850343.jpg)

I bring that up because I want to appropriately temper what I’m going to say next.

If you’re new to the industry, you will probably, like me, assume that every word from the senior developers in the group is a pearl of wisdom.  And, many of them will be – if you’re lucky – especially at first.

But not all senior developers are created (or promoted, as it were) equal.

In retrospect, the folks that I listed above were actually good programmers and I actually learned good things from them.  But I also learned, through my career, that I had lucked out with my initial influences.

For every shop with awesome, helpful senior developers exists a shop populated by little people with a little power, whose primary qualification isn’t technical chops, but hanging around for a long time, managing not to get fired, and backing into promotions to titles like “senior” or “principal.”

This phenomenon is so common that [a term](http://daedtech.com/how-developers-stop-learning-rise-of-the-expert-beginner/) I made up whole cloth, years ago, to describe it, now earns hundreds of Google searches per month.  When I coined the term [expert beginner](http://daedtech.com/how-developers-stop-learning-rise-of-the-expert-beginner//), it resonated so heavily with people that the original post has gone viral over and over again.

[![ExpertBeginner.jpg](../_resources/99007b0278d30208f93c0fc4a37811a7.jpg)](https://daedtech.com/wp-content/uploads/2014/05/ExpertBeginner.jpg)

Dale will tell you what’s wrong with so-called professional ORMs.

I’m not saying this to brag.  I’m saying this to warn you about how many senior developers out there superficially seem legitimate, but actually aren’t.

So when you’re new, give the seniors the benefit of the doubt and defer to them, but don’t just assume what they tell you is true or right.  Verify it on your own (preferably not right in front of them).

## 4. TDD Is Legit, and It’s a Game-Changer

When it comes to anything programming-, or even tech-related, we, as an industry, tend to go pretty nuts with choice-supportive bias.

- IDE vs lightweight editor discussion?
- Apple, Windows, or Linux?
- What do you think of PHP?
- Tabs or spaces?

Bring any of these up and watch as terminally stupid yelling matches occur between those with strong opinions.  So with all of that in mind, I recognize that I’m wading into similar territory here with “to TDD or not to TDD.”

My intention here isn’t to preach, but rather to share my own experience.

[![Erik-in-the-Woods-e1509314883713.png](../_resources/1b3cf833392f757ff4a6ff3dfc981174.png)](https://daedtech.com/wp-content/uploads/2017/10/Erik-in-the-Woods-e1509314883713.png)

About 10 years ago, I was a TDD skeptic.  I wasn’t a *unit testing* skeptic, mind you – I’d accepted that as a helpful practice pretty much from the get-go.

But TDD?  I wasn’t so sure.
I decided I’d write a blog post about why TDD wasn’t all that great.

But I didn’t want to just write a flimsy, dime-a-dozen opinion piece on the matter.  So instead I decided to do a small client project (fixed price, BTW) rigidly following TDD so that I could write a post with the premise “I spent a couple of weeks doing pure TDD and it’s not great.”

But fate had other plans.

### My Aha! Moment with TDD

It was awkward and weird for a day.  Actually, probably for multiple days.

Everything took forever and everything I did felt cumbersome and unnatural.  I was just adding note after note as evidence about why this was a terrible way to do things.

But then a funny thing happened.

I’d been so fixated on this awkward paradigm that I’d managed to spend 4-5 hours writing code one day without actually running the application to see if my changes were working.  Usually I’d run the application every 10 minutes or so as a sanity check to see if my changes were truly working.

Realizing that I was hours in, I fired up the application, sighing, and expecting to have to debug for hours.  After all, I’d procrastinated by something like 30 cycles.

But a strange thing happened.  Everything worked.

[![Twenties-Car-e1536104354609.jpg](../_resources/9be8577e1d6c4c8de4a8794dc4ada026.jpg)](https://daedtech.com/wp-content/uploads/2017/08/Twenties-Car-e1536104354609.jpg)

Everything worked perfectly, the first time, without exception.  There were absolutely no surprises.  I’d written code for hours without looking at my own GUI or validating anything at runtime, and it all just worked.

I wound up writing a much different article about TDD.  And I’ve never once looked back.

I learned the technique, mastered it, taught courses on it, consulted about it, and did developer coaching in it.  But beyond that, I examined [the effects of unit testing on codebases](https://blog.ndepend.com/unit-tests-desirable-codebase-properties/) and found those effects to be unambiguously good.

Learn yourself some TDD.  You won’t regret it.

## 5. Evidence is King

Throughout this post so far, I’ve mentioned my codebase assessment practice and talked about empirical data.  Let’s formalize that a bit with the last lesson from my career.

Evidence is everything.

Code reviews can serve as an educational, empowering activity.  Or they can [execute your soul](http://daedtech.com/how-to-use-a-code-review-to-execute-someones-soul/).

Most likely, though, they’ll fall somewhere in between teetering back and forth between enlightening experience and pointless bickering.

You’ll hear things like “that’s not a good design” or “that’s not efficient.”  You’ll also probably say those things.  And you’ll most likely hear and say them with no semblance of evidence whatsoever.

Fix that.

### The Importance of Evidence

If people are walking all over you during code reviews or any other form of collaboration within your team or organization, evidence is your friend.  If you’re trying to make any kind of case to management or leadership about anything, evidence is your friend.

Evidence will win you arguments, respect, leadership roles, and career advancement.

Do you think your team’s extensive use of global variables is killing you?  Don’t argue about it – prove it.

And by “prove,” I don’t mean finding something like [a post about the evils of global state](https://blog.ndepend.com/singleton-design-pattern-impact-quantified/) and appealing to me as an authority.  I mean go find modules in your codebase with and without global state and cross reference those against the incident rate of JIRA tickets or something.

[![Scientist.png](../_resources/925a7563c85ed3fd2ed218ed826ac7a3.png)](https://daedtech.com/wp-content/uploads/2015/04/Scientist.png)

Did someone on your team demand that you use a different library or API than the one you chose because “{hand-waving” performance?”  Does that not satisfy you?

Prove that team member wrong.  Run actual time trials.

Get yourself used to running experiments, rather than loudly expressing and doubling down on your opinions.  This has the immediate value of empirically validating your thinking.

Sometimes you’ll realize you’re right in the face of skepticism.  And, well, sometimes you’ll realize you were wrong, which is also valuable.

But beyond that, you’ll start to wage arguments in a way that others can’t contest, developing a formidable reputation for diligence and correctness.  This can help you overcome even seemingly insurmountable odds like the “I’m just a junior and he’s a senior (expert beginner)” dynamic.

And looking even a little further, this positions you well for career advancement.

The ability to write code ensures a lucrative career.  The ability to write code and use evidence to make technical and business cases for courses of actions ensures a meteoric career.

## Use These (Or Don’t) In Good Health

I was feeling philosophical as I wrote this post.  I actually wrote the entire thing on a plane ride from Chicago to Houston, glass of wine in hand and opted out of the wifi.  So I had little to do but talk to the flight attendants (I’m in the first row, so they’re hanging out here) and reminisce on my career.

I suppose you could argue with these points if you tried hard enough.

But I don’t offer these as immutable laws of programming or some kind of pro’s code of conduct.  I offer them as the lessons I’ve learned myself over the course of my career, and I offer them with a *caveat emptor* that they’re just my opinions.

But hopefully those opinions help some of you.  So take them as you will, and use in good health.