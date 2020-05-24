What Happens Next? COVID-19 Futures, Explained With Playable Simulations

No translations yet![Help make one?](https://github.com/ncase/covid-19#how-to-translate)

Help this guide get R > 1:

[(L)](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fncase.me%2Fcovid-19%2F)[(L)](https://twitter.com/intent/tweet?text=What%20Happens%20Next%3F%20COVID-19%20Futures%2C%20Explained%20With%20Playable%20Simulations%0A%F0%9F%94%AC%20Here%27s%20a%20real%20deep%20dive!%2030%20min%20read%2Fplay%3A%20https%3A%2F%2Fncase.me%2Fcovid-19%2F)[(L)](https://ncase.me/covid-19/mailto:?subject=What%20Happens%20Next%3F%20COVID-19%20Futures%2C%20Explained%20With%20Playable%20Simulations&body=%F0%9F%94%AC%20Here%27s%20a%20real%20deep%20dive!%2030%20min%20read%2Fplay%3A%20https%3A%2F%2Fncase.me%2Fcovid-19%2F)

What Happens Next?

COVID-19 Futures, Explained With Playable Simulations

 **30 min play/read  ·  **by [Marcel Salathé](https://scholar.google.com/citations?user=_wHMGkUAAAAJ&hl=en)(epidemiologist) & [Nicky Case](https://ncase.me/)(art/code)

"The only thing to fear is fear itself" was stupid advice.

Sure, don't hoard toilet paper – but if policymakers fear fear itself, they'll downplay real dangers to avoid "mass panic". Fear's not the problem, it's how we *channel* our fear. Fear gives us energy to deal with dangers now, and prepare for dangers later.

Honestly, we (Marcel, epidemiologist + Nicky, art/code) are worried. We bet you are, too! That's why we've channelled our fear into making these **playable simulations**, so that *you* can channel your fear into understanding:

- **The Last Few Months** (epidemiology 101, SEIR model, R & R0)
- **The Next Few Months** (lockdowns, contact tracing, masks)
- **The Next Few Years** (loss of immunity? no vaccine?)

This guide (published May 1st, 2020. click this footnote!→) is meant to give you hope *and* fear. To beat COVID-19 **in a way that also protects our mental & financial health**, we need optimism to create plans, and pessimism to create backup plans. As Gladys Bronwyn Stern once said, *“The optimist invents the airplane and the pessimist the parachute.”*

So, buckle in: we're about to experience some turbulence.

 ![curve.png](../_resources/c012557dd029a4c51f8d4e02bbccf9bf.png)
The Last Few Months

Pilots use flight simulators to learn how not to crash planes.
**Epidemiologists use epidemic simulators to learn how not to crash humanity.**

So, let's make a very, *very* simple "epidemic flight simulator"! In this simulation,  Infectious people can turn  Susceptible people into more  Infectious people:

![spread.png](../_resources/fa80b699479e73bcef020f0270cc21e5.png)

It's estimated that, *at the start* of a COVID-19 outbreak, the virus jumps from an  to an  every 4 days, *on average*. (remember, there's a lot of variation)

If we simulate "double every 4 days" *and nothing else*, on a population starting with just 0.001% , what happens?

**Click "Start" to play the simulation! You can re-play it later with different settings:** (technical caveats: )

On *average*, each ...

Infects 1  per 4 days

* * *

Simulate 0.5 years in 40 seconds

Start
![](../_resources/f2f5f5c2ffab03389f6aa31caca1e143.png)
jan 2020
feb 2020
mar 2020
apr 2020
may 2020
jun 2020
Susceptible: 99.999%
Infectious: 0.001%

This is the **exponential growth curve.** Starts small, then explodes. "Oh it's just a flu" to "Oh right, flus don't create *mass graves in rich cities*".

![exponential.png](../_resources/30f04b1d792d84f7879f6043d1f646c5.png)

But, this simulation is wrong. Exponential growth, thankfully, can't go on forever. One thing that stops a virus from spreading is if others *already* have the virus:

![susceptibles.png](../_resources/a1dc36baeba200e4a780ca64d1e2fd0d.png)

The more s there are, the faster s become s, **but the fewer s there are, the *slower*  s become s.**

How's this change the growth of an epidemic? Let's find out:

On *average*, each ...

Infects 1  per 4 days
(at the start of the epidemic)

* * *

Simulate 0.5 years in 20 seconds

Start
![](../_resources/f2f5f5c2ffab03389f6aa31caca1e143.png)
jan 2020
feb 2020
mar 2020
apr 2020
may 2020
jun 2020
Susceptible: 99.999%
Infectious: 0.001%

This is the "S-shaped" **logistic growth curve.** Starts small, explodes, then slows down again.

But, this simulation is *still* wrong. We're missing the fact that  Infectious people eventually stop being infectious, either by 1) recovering, 2) "recovering" with lung damage, or 3) dying.

For simplicity's sake, let's pretend that all  Infectious people become  Recovered. (Just remember that in reality, some are dead.) s can't be infected again, and let's pretend – *for now!* – that they stay immune for life.

With COVID-19, it's estimated you're  Infectious for 10 days, *on average*. That means some folks will recover before 10 days, some after. **Here's what that looks like, with a simulation *starting* with 100% :**

On *average*, each ...

Takes 10 days to go from  to

* * *

Simulate 0.5 years in 10 seconds

Start
![](../_resources/f2f5f5c2ffab03389f6aa31caca1e143.png)
jan 2020
feb 2020
mar 2020
apr 2020
may 2020
jun 2020
Infectious: 100.000%
Recovered: 0.000%

This is the opposite of exponential growth, the **exponential decay curve.**
Now, what happens if you simulate S-shaped logistic growth *with* recovery?
![graphs_q.png](../_resources/78670f3c7387f40e4d59daf4dca799f8.png)
Let's find out.
**Red curve** is *current* cases ,
**Gray curve** is *total* cases (current + recovered ), starts at just 0.001% :

On *average*, each ...

Infects 1  per 4 days
(at the start of the epidemic)
Takes 10 days to go from  to

* * *

Simulate 1.0 years in 10 seconds

Start
![](../_resources/f2f5f5c2ffab03389f6aa31caca1e143.png)
jan 2020
apr 2020
jul 2020
oct 2020
Susceptible: 99.999%
Infectious: 0.001%
Recovered: 0.000%

And *that's* where that famous curve comes from! It's not a bell curve, it's not even a "log-normal" curve. It has no name. But you've seen it a zillion times, and beseeched to flatten.

This is the the **SIR Model**,
(**S**usceptible **I**nfectious **R**ecovered)
the *second*-most important idea in Epidemiology 101:
![sir.png](../_resources/51bd1eddc4c480ad10a8130692d96b97.png)

**NOTE: The simulations that inform policy are way, *way* more sophisticated than this!** But the SIR Model can still explain the same general findings, even if missing the nuances.

Actually, let's add one more nuance: before an  becomes an , they first become  Exposed. This is when they have the virus but can't pass it on yet – infect*ed* but not yet infect*ious*.

![seir.png](:/1293b6f53ef3715d99a2a4c6a95e436b)

(This variant is called the **SEIR Model**, where the "E" stands for  "Exposed". Note this *isn't* the everyday meaning of "exposed", when you may or may not have the virus. In this technical definition, "Exposed" means you definitely have it. Science terminology is bad.)

For COVID-19, it's estimated that you're  infected-but-not-yet-infectious for 3 days, *on average*. What happens if we add that to the simulation?

**Red **+ Pink** curve** is *current* cases (infectious  + exposed ),
**Gray curve** is *total* cases (current + recovered ):

On *average*, each ...

Infects 1  per 4 days
(at the start of the epidemic)
Takes 3 days to go from  to
Takes 10 days to go from  to

* * *

Simulate 1.0 years in 10 seconds

Start
![](../_resources/f2f5f5c2ffab03389f6aa31caca1e143.png)
jan 2020
apr 2020
jul 2020
oct 2020
Susceptible: 99.999%
Exposed: 0.000%
Infectious: 0.001%
Recovered: 0.000%

Not much changes! How long you stay  Exposed changes the ratio of -to-, and *when* current cases peak... but the *height* of that peak, and total cases in the end, stays the same.

Why's that? Because of the *first*-most important idea in Epidemiology 101:
![r.png](../_resources/6d146d81b27de168da3b86821b1eb050.png)

Short for "Reproduction number". It's the *average* number of people an  infects *before* they recover (or die).

![r2.png](../_resources/f3ecb5d16eab4afa9bea9d27bc6b35d4.png)

**R** changes over the course of an outbreak, as we get more immunity & interventions.

**R0** (pronounced R-nought) is what R is *at the start of an outbreak, before immunity or interventions*. R0 more closely reflects the power of the virus itself, but it still changes from place to place. For example, R0 is higher in dense cities than sparse rural areas.

(Most news articles – and even some research papers! – confuse R and R0. Again, science terminology is bad)

The R0 for "the" seasonal flu is around 1.28. This means, at the *start* of a flu outbreak, each  infects 1.28 others *on average.* (If it sounds weird that this isn't a whole number, remember that the "average" mom has 2.4 children. This doesn't mean there's half-children running about.)

The R0 for COVID-19 is estimated to be around 2.2, though one *not-yet-finalized* study estimates it was 5.7(!) in Wuhan.

In our simulations – *at the start & on average* – an  infects someone every 4 days, over 10 days. "4 days" goes into "10 days" two-and-a-half times. This means – *at the start & on average* – each  infects 2.5 others. Therefore, R0 = 2.5. (caveats:)

**Play with this R0 calculator, to see how R0 depends on recovery time & new-infection time:**

On *average*, each ...

Infects 1  per 4 days
(at the start of the epidemic)
Takes 10 days to go from  to

* * *

R0 is 2.50![](../_resources/2d0cfc5860fdb6dd49d857ffc379d9dd.png)

But remember, the fewer s there are, the *slower*  s become s. The *current* reproduction number (R) depends not just on the *basic* reproduction number (R0), but *also* on how many people are no longer  Susceptible. (For example, by recovering & getting natural immunity.)

On *average*, each ...

Infects 1  per 4 days
(at the start of the epidemic)
Takes 10 days to go from  to

* * *

R0 is 2.50![](../_resources/2d0cfc5860fdb6dd49d857ffc379d9dd.png)
% of people who are *NOT*

R is now 2.50![](../_resources/2d0cfc5860fdb6dd49d857ffc379d9dd.png)

When enough people have immunity, R < 1, and the virus is contained! This is called **herd immunity**. For flus, herd immunity is achieved *with a vaccine*. Trying to achieve "natural herd immunity" by letting folks get infected is a *terrible* idea. (But not for the reason you may think! We'll explain later.)

Now, let's play the SEIR Model again, but showing R0, R over time, and the herd immunity threshold:

On *average*, each ...

Infects 1  per 4 days
(at the start of the epidemic)
Takes 3 days to go from  to
Takes 10 days to go from  to

* * *

R0 is 2.50![](../_resources/2d0cfc5860fdb6dd49d857ffc379d9dd.png)
% of people who are *NOT*

R is now 2.50![](../_resources/64daa891ec08e330004a79d2c69e046e.png)
* * *

Simulate 1.0 years in 30 seconds

Start
![](../_resources/f2f5f5c2ffab03389f6aa31caca1e143.png)
jan 2020
apr 2020
jul 2020
oct 2020
Susceptible: 99.999%
Exposed: 0.000%
Infectious: 0.001%
Recovered: 0.000%

- - - Herd Immunity

**NOTE: Total cases *does not stop* at herd immunity, but overshoots it!** And it crosses the threshold *exactly* when current cases peak. (This happens no matter how you change the settings – try it for yourself!)

This is because when there are more non-s than the herd immunity threshold, you get R < 1. And when R < 1, new cases stop growing: a peak.

**If there's only one lesson you take away from this guide, here it is** – it's an extremely complex diagram so please take time to fully absorb it:

![r3.png](../_resources/5b78426299bbc778273cdd44d54295b6.png)

**This means: we do NOT need to catch all transmissions, or even nearly all transmissions, to stop COVID-19!**

It's a paradox. COVID-19 is extremely contagious, yet to contain it, we "only" need to stop more than 60% of infections. 60%?! If that was a school grade, that's a D-. But if R0 = 2.5, cutting that by 61% gives us R = 0.975, which is R < 1, virus is contained! (exact formula:)

![r4.png](../_resources/d7ea7cf637e84dcffd5a04111bd77381.png)

(If you think R0 or the other numbers in our simulations are too low/high, that's good you're challenging our assumptions! There'll be a "Sandbox Mode" at the end of this guide, where you can plug in your *own* numbers, and simulate what happens.)

*Every* COVID-19 intervention you've heard of – handwashing, social/physical distancing, lockdowns, self-isolation, contact tracing & quarantining, face masks, even "herd immunity" – they're *all* doing the same thing:

Getting R < 1.

So now, let's use our "epidemic flight simulator" to figure this out: How can we get R < 1 in a way **that also protects our mental health *and* financial health?**

Brace yourselves for an emergency landing...

 ![curve.png](../_resources/c012557dd029a4c51f8d4e02bbccf9bf.png)
The Next Few Months

...could have been worse. Here's a parallel universe we avoided:

### Scenario 0: Do Absolutely Nothing

Around 1 in 20 people infected with COVID-19 need to go to an ICU (Intensive Care Unit). In a rich country like the USA, there's 1 ICU bed per 3400 people. Therefore, the USA can handle 20 out of 3400 people being *simultaneously* infected – or, 0.6% of the population.

Even if we *more than tripled* that capacity to 2%, here's what would've happened *if we did absolutely nothing:*

R0 is 2.50
% of people who are *NOT*

R is now 2.50
* * *

Simulate 2.0 years in 5 seconds

Start
![](../_resources/f2f5f5c2ffab03389f6aa31caca1e143.png)
2020
2021

- - - Herd Immunity––– ICU Capacity

Not good.

That's what [the March 16 Imperial College report](http://www.imperial.ac.uk/mrc-global-infectious-disease-analysis/covid-19/report-9-impact-of-npis-on-covid-19/) found: do nothing, and we run out of ICUs, with more than 80% of the population getting infected. (remember: total cases *overshoots* herd immunity)

Even if only 0.5% of infected die – a generous assumption when there's no more ICUs – in a large country like the US, with 300 million people, 0.5% of 80% of 300 million = still 1.2 million dead... *IF we did nothing.*

(Lots of news & social media reported "80% will be infected" *without* "IF WE DO NOTHING". Fear was channelled into clicks, not understanding. *Sigh.*)

### Scenario 1: Flatten The Curve / Herd Immunity

The "Flatten The Curve" plan was touted by every public health organization, while the United Kingdom's original "herd immunity" plan was universally booed. They were *the same plan.* The UK just communicated theirs poorly.

Both plans, though, had a literally fatal flaw.

First, let's look at the two main ways to "flatten the curve": handwashing & physical distancing.

Increased handwashing cuts flus & colds in high-income countries by ~25%, while the city-wide lockdown in London cut close contacts by ~70%. So, let's assume handwashing can reduce R by *up to* 25%, and distancing can reduce R by *up to* 70%:

**Play with this calculator to see how % of non-, handwashing, and distancing reduce R:** (this calculator visualizes their *relative* effects, which is why increasing one *looks* like it decreases the effect of the others.)

R0 is 2.50
% of people who are *NOT*

Increased Hygiene

Physical Distancing

R is now 2.50

Now, let's simulate what happens to a COVID-19 epidemic if, starting March 2020, we had increased handwashing but only *mild* physical distancing – so that R is lower, but still above 1:

R0 is 2.50
% of people who are *NOT*

Increased Hygiene

Physical Distancing

R is now 2.50
* * *

Simulate 2.0 years in 20 seconds

Start
![](../_resources/f2f5f5c2ffab03389f6aa31caca1e143.png)
2020
2021

- - - Herd Immunity––– ICU Capacity

This simulation has a "recorded scenario"!
Click "Start" to watch the recording *before*you change any of the numbers
Three notes:

1. This *reduces* total cases! **Even if you don't get R < 1, reducing R still saves lives, by reducing the 'overshoot' above herd immunity.** Lots of folks think "Flatten The Curve" spreads out cases without reducing the total. This is impossible in *any* Epidemiology 101 model. But because the news reported "80%+ will be infected" as inevitable, folks thought total cases will be the same no matter what. *Sigh.*

2. Due to the extra interventions, current cases peak *before* herd immunity is reached. In fact, in this simulation, total cases only overshoots *a tiny bit* above herd immunity – the UK's plan! At that point, R < 1, you can let go of all other interventions, and COVID-19 stays contained! Well, except for one problem...

3. You still run out of ICUs. For several months. (and remember, we *already* tripled ICUs for these simulations)

That was the other finding of the March 16 Imperial College report, which convinced the UK to abandon its original plan. Any attempt at **mitigation** (reduce R, but R > 1) will fail. The only way out is **suppression** (reduce R so that R < 1).

![mitigation_vs_suppression.png](../_resources/ae016d9505479551db5ed422cc1d477f.png)

That is, don't merely "flatten" the curve, *crush* the curve. For example, with a...

### Scenario 2: Months-Long Lockdown

Let's see what happens if we *crush* the curve with a 5-month lockdown, reduce  to nearly nothing, then finally – *finally* – return to normal life:

R0 is 2.50
% of people who are *NOT*

Increased Hygiene

Physical Distancing

R is now 2.50
* * *

Simulate 2.0 years in 20 seconds

Start
![](../_resources/f2f5f5c2ffab03389f6aa31caca1e143.png)
2020
2021

- - - Herd Immunity––– ICU Capacity

This simulation has a "recorded scenario"!
Click "Start" to watch the recording *before*you change any of the numbers
Oh.

This is the "second wave" everyone's talking about. As soon as we remove the lockdown, we get R > 1 again. So, a single leftover  (or imported ) can cause a spike in cases that's almost as bad as if we'd done Scenario 0: Absolutely Nothing.

**A lockdown isn't a cure, it's just a restart.**
So, what, do we just lockdown again & again?

### Scenario 3: Intermittent Lockdown

This solution was first suggested by the March 16 Imperial College report, and later again by a Harvard paper.

**Here's a simulation:** (After playing the "recorded scenario", you can try simulating your *own* lockdown schedule, by changing the sliders *while* the simulation is running! Remember you can pause & continue the sim, and change the simulation speed)

R0 is 2.50
% of people who are *NOT*

Increased Hygiene

Physical Distancing

R is now 2.50
* * *

Simulate 2.0 years in 20 seconds

Start
![](../_resources/f2f5f5c2ffab03389f6aa31caca1e143.png)
2020
2021

- - - Herd Immunity––– ICU Capacity

This simulation has a "recorded scenario"!
Click "Start" to watch the recording *before*you change any of the numbers

This *would* keep cases below ICU capacity! And it's *much* better than an 18-month lockdown until a vaccine is available. We just need to... shut down for a few months, open up for a few months, and repeat until a vaccine is available. (And if there's no vaccine, repeat until herd immunity is reached... in 2022.)

Look, it's nice to draw a line saying "ICU capacity", but there's lots of important things we *can't* simulate here. Like:

**Mental Health:** Loneliness is one of the biggest risk factors for depression, anxiety, and suicide. And it's as associated with an early death as smoking 15 cigarettes a day.

**Financial Health:** "What about the economy" sounds like you care more about dollars than lives, but "the economy" isn't just stocks: it's people's ability to provide food & shelter for their loved ones, to invest in their kids' futures, and enjoy arts, foods, videogames – the stuff that makes life worth living. And besides, poverty *itself* has horrible impacts on mental and physical health.

Not saying we *shouldn't* lock down again! We'll look at "circuit breaker" lockdowns later. Still, it's not ideal.

But wait... haven't Taiwan and South Korea *already* contained COVID-19? For 4 whole months, *without* long-term lockdowns?

How?

### Scenario 4: Test, Trace, Isolate

*"Sure, we *could've* done what Taiwan & South Korea did at the start, but it's too late now. We missed the start."*

But that's exactly it! “A lockdown isn't a cure, it's just a restart”... **and a fresh start is what we need.**

To understand how Taiwan & South Korea contained COVID-19, we need to understand the exact timeline of a typical COVID-19 infection:

![timeline1.png](../_resources/1f963a4c9a65807086212f8810f44359.png)

If cases only self-isolate when they know they're sick (that is, they feel symptoms), the virus can still spread:

![timeline2.png](../_resources/8bed302238d50e11fd4c19e59c3344cf.png)
And in fact, 44% of all transmissions are like this: *pre*-symptomatic!

But, if we find *and quarantine* a symptomatic case's recent close contacts... we stop the spread, by staying one step ahead!

![timeline3.png](../_resources/da07a6c8c9d4f372ade75bfe462658a8.png)

This is called **contact tracing**. It's an old idea, was used at an unprecedented scale to contain Ebola, and now it's core part of how Taiwan & South Korea are containing COVID-19!

(It also lets us use our limited tests more efficiently, to find pre-symptomatic s without needing to test almost everyone.)

Traditionally, contacts are found with in-person interviews, but those *alone* are too slow for COVID-19's ~48 hour window. That's why contact tracers need help, and be supported by – *NOT* replaced by – contact tracing apps.

(This idea didn't come from "techies": using an app to fight COVID-19 was first proposed by [a team of Oxford epidemiologists](https://science.sciencemag.org/content/early/2020/04/09/science.abb6936).)

Wait, apps that trace who you've been in contact with?... Does that mean giving up privacy, giving in to Big Brother?

Heck no! **[DP-3T](https://github.com/DP-3T/documents#decentralized-privacy-preserving-proximity-tracing)**, a team of epidemiologists & cryptographers (including one of us, Marcel Salathé) is *already* making a contact tracing app – with code available to the public – that reveals **no info about your identity, location, who your contacts are, or even *how many contacts* you've had.**

Here's how it works:
![dp3t.png](../_resources/8674b2247850790817673b906bd18863.png)
(& [here's the full comic](https://ncase.me/contact-tracing/))

Along with similar teams like TCN Protocol and MIT PACT, they've inspired Apple & Google to bake privacy-first contact tracing directly into Android/iOS. (Don't trust Google/Apple? Good! The beauty of this system is it doesn't *need* trust!) Soon, your local public health agency may ask you to download an app. If it's privacy-first with publicly-available code, please do!

But what about folks without smartphones? Or infections through doorknobs? Or "true" asymptomatic cases? Contact tracing apps can't catch all transmissions... *and that's okay!* We don't need to catch *all* transmissions, just 60%+ to get R < 1.

(Rant about the confusion about pre-symptomatic vs "true" asymptomatic. "True" asymptomatics are rare:)

Isolating *symptomatic* cases would reduce R by up to 40%, and quarantining their *pre/a-symptomatic* contacts would reduce R by up to 50%:

R0 is 2.50
% of people who are *NOT*

Increased Hygiene

Physical Distancing

Isolating Cases

Quarantining Contacts

R is now 1.88![](../_resources/8590dca5cbabc0bac763b73e30b404a0.png)

Thus, even without 100% contact quarantining, we can get R < 1 *without a lockdown!* Much better for our mental & financial health. (As for the cost to folks who have to self-isolate/quarantine, *governments should support them* – pay for the tests, job protection, subsidized paid leave, etc. Still way cheaper than intermittent lockdown.)

We then keep R < 1 until we have a vaccine, which turns susceptible s into immune s. Herd immunity, the *right* way:

R0 is 2.50
% of people who are *NOT*

Vaccinations

R is now 2.50

(Note: this calculator pretends the vaccines are 100% effective. Just remember that in reality, you'd have to compensate by vaccinating *more* than "herd immunity", to *actually* get herd immunity)

Okay, enough talk. Here's a simulation of:
1. A few-month lockdown, until we can...
2. Switch to "Test, Trace, Isolate" until we can...
3. Vaccinate enough people, which means...
4. We win.

R0 is 2.50
% of people who are *NOT*

Increased Hygiene

Physical Distancing

Isolating Cases

Quarantining Contacts

Vaccinations

R is now 2.50
* * *

Simulate 2.0 years in 20 seconds

Start
![](../_resources/f2f5f5c2ffab03389f6aa31caca1e143.png)
2020
2021

- - - Herd Immunity––– ICU Capacity

This simulation has a "recorded scenario"!
Click "Start" to watch the recording *before*you change any of the numbers
So that's it! That's how we make an emergency landing on this plane.
That's how we beat COVID-19.
...

But what if things *still* go wrong? Things have gone horribly wrong already. That's fear, and that's good! Fear gives us energy to create *backup plans*.

The pessimist invents the parachute.

### Scenario 4+: Masks For All, Summer, Circuit Breakers

What if R0 is way higher than we thought, and the above interventions, even with mild distancing, *still* aren't enough to get R < 1?

Remember, even if we can't get R < 1, reducing R still reduces the "overshoot" in total cases, thus saving lives. But still, R < 1 is the ideal, so here's a few other ways to reduce R:

**Masks For All:**

*"Wait,"* you might ask, *"I thought face masks don't stop you from getting sick?"*

You're right. Masks don't stop you from getting sick... they stop you from getting *others* sick.

![masks.png](../_resources/7b18f2d904937ec438e9e09aa1853fe4.png)

To put a number on it: surgical masks *on the sick person* reduce cold & flu viruses in aerosols by 70%. Reducing transmissions by 70% would be as large an impact as a lockdown!

However, we don't know for sure the impact of masks on COVID-19 *specifically*. In science, one should only publish a finding if you're 95% sure of it. (...should.) Masks, as of May 1st 2020, are less than "95% sure".

However, pandemics are like poker. **Make bets only when you're 95% sure, and you'll lose everything at stake.** As a recent article on masks in the British Medical Journal notes, we *have* to make cost/benefit analyses under uncertainty. Like so:

Cost: If homemade cloth masks (which are ~2/3 as effective as surgical masks), super cheap. If surgical masks, more expensive but still pretty cheap.

Benefit: Even if it's a 50–50 chance of surgical masks reducing transmission by 0% or 70%, the average "expected value" is still 35%, same as a half-lockdown! So let's guess-timate that surgical masks reduce R by up to 35%, discounted for our uncertainty. (Again, you can challenge our assumptions by turning the sliders up/down)

R0 is 2.50
% of people who are *NOT*

Increased Hygiene

Physical Distancing

Isolating Cases

Quarantining Contacts

Face Masks

R is now 1.10![](../_resources/dfe39ee0108db9c7f70b489c817d5001.png)
(other arguments for/against masks:)

Masks *alone* won't get R < 1. But if handwashing & "Test, Trace, Isolate" only gets us to R = 1.10, having just 1/3 of people wear masks would tip that over to R < 1, virus contained!

**Summer:**

Okay, this isn't an "intervention" we can control, but it will help! Some news outlets report that summer won't do anything to COVID-19. They're half right: summer won't get R < 1, but it *will* reduce R.

For COVID-19, every extra 1° Celsius (2.2° Fahrenheit) makes R drop by 1.2%. The summer-winter difference in New York City is 15°C (60°F), so summer will make R drop by 18%.

R0 is 2.50
% of people who are *NOT*

Summer

R is now 2.44

Summer alone won't make R < 1, but if we have limited resources, we can scale back some interventions in the summer – so we can scale them *higher* in the winter.

**A "Circuit Breaker" Lockdown:**

And if all that *still* isn't enough to get R < 1... we can do another lockdown.

But we wouldn't have to be 2-months-closed / 1-month-open over & over! Because R is reduced, we'd only need one or two more "circuit breaker" lockdowns before a vaccine is available. (Singapore had to do this recently, "despite" having controlled COVID-19 for 4 months. That's not failure: this *is* what success takes.)

Here's a simulation a "lazy case" scenario:
1. Lockdown, then

2. A moderate amount of hygiene & "Test, Trace, Isolate", with a mild amount of "Masks For All", then...

3. One more "circuit breaker" lockdown before a vaccine's found.

R0 is 2.50
% of people who are *NOT*

Increased Hygiene

Physical Distancing

Isolating Cases

Quarantining Contacts

Face Masks

Summer

Vaccinations

R is now 2.50
* * *

Simulate 2.0 years in 20 seconds

Start
![](../_resources/f2f5f5c2ffab03389f6aa31caca1e143.png)
2020
2021

- - - Herd Immunity––– ICU Capacity

This simulation has a "recorded scenario"!
Click "Start" to watch the recording *before*you change any of the numbers

Not to mention all the *other* interventions we could do, to further push R down:

- Travel restrictions/quarantines
- Temperature checks at malls & schools
- Deep-cleaning public spaces
- [Replacing hand-shaking with foot-bumping](https://twitter.com/V_actually/status/1233785527788285953)
- And all else human ingenuity shall bring

. . .
We hope these plans give you hope.

**Even under a pessimistic scenario, it *is* possible to beat COVID-19, while protecting our mental and financial health.** Use the lockdown as a "reset button", keep R < 1 with case isolation + privacy-protecting contract tracing + at *least* cloth masks for all... and life can get back to a normal-ish!

Sure, you may have dried-out hands. But you'll get to invite a date out to a comics bookstore! You'll get to go out with friends to watch the latest Hollywood cash-grab. You'll get to people-watch at a library, taking joy in people going about the simple business of *being alive.*

Even under the worst-case scenario... life perseveres.

So now, let's plan for some *worse* worst-case scenarios. Water landing, get your life jacket, and please follow the lights to the emergency exits:

 ![curve.png](../_resources/c012557dd029a4c51f8d4e02bbccf9bf.png)
The Next Few Years

You get COVID-19, and recover. Or you get the COVID-19 vaccine. Either way, you're now immune...

...*for how long?*

- COVID-19 is most closely related to SARS, which gave its survivors 2 years of immunity.
- The coronaviruses that cause "the" common cold give you 8 months of immunity.
- There's reports of folks recovering from COVID-19, then testing positive again, but it's unclear if these are false positives.
- One *not-yet-peer-reviewed* study on monkeys showed immunity to the COVID-19 coronavirus for at least 28 days.

But for COVID-19 *in humans*, as of May 1st 2020, "how long" is the big unknown.

For these simulations, let's say it's 1 year.**Here's a simulation starting with 100% **, exponentially decaying into susceptible, no-immunity s after 1 year, on *average*, with variation:

On *average*, each ...

Infects 1  per 4 days
(at the start of the epidemic)
Takes 3 days to go from  to
Takes 10 days to go from  to
Loses immunity  in 12 months

* * *

Simulate 5.0 years in 5 seconds

Start
![](../_resources/f2f5f5c2ffab03389f6aa31caca1e143.png)
2020
2021
2022
2023
2024

Return of the exponential decay!
This is the **SEIRS Model**. The final "S" stands for  Susceptible, again.
![seirs.png](../_resources/c50b433813d7e0dd269007fc9ebc21a2.png)

Now, let's simulate a COVID-19 outbreak, over 10 years, with no interventions... *if immunity only lasts a year:*

On *average*, each ...

Infects 1  per 4 days
(at the start of the epidemic)
Takes 3 days to go from  to
Takes 10 days to go from  to
Loses immunity  in 12 months

* * *

R0 is 2.50
% of people who are *NOT*

R is now 2.50
* * *

Simulate 10.0 years in 20 seconds

Start
![](../_resources/f2f5f5c2ffab03389f6aa31caca1e143.png)
2020
2021
2022
2023
2024
2025
2026
2027
2028
2029

- - - Herd Immunity––– ICU Capacity

In previous simulations, we only had *one* ICU-overwhelming spike. Now, we have several, *and*   cases come to a rest *permanently at* ICU capacity. (Which, remember, we *tripled* for these simulations)

R = 1, it's **endemic.**
Thankfully, because summer reduces R, it'll make the situation better:

On *average*, each ...

Infects 1  per 4 days
(at the start of the epidemic)
Takes 3 days to go from  to
Takes 10 days to go from  to
Loses immunity  in 12 months

* * *

R0 is 2.50
% of people who are *NOT*

Summer

R is now 2.43
* * *

Simulate 10.0 years in 20 seconds

Start
![](../_resources/f2f5f5c2ffab03389f6aa31caca1e143.png)
2020
2021
2022
2023
2024
2025
2026
2027
2028
2029

- - - Herd Immunity––– ICU Capacity

Oh.

Counterintuitively, summer makes the spikes worse *and* regular! This is because summer reduces new s, but that in turn reduces new immune s. Which means immunity plummets in the summer, *creating* large regular spikes in the winter.

Thankfully, the solution to this is pretty straightforward – just vaccinate people every fall/winter, like we do with flu shots:

**(After playing the recording, try simulating your own vaccination campaigns! Remember you can pause/continue the sim at any time)**

R0 is 2.50
% of people who are *NOT*

Summer

Vaccinations

R is now 2.43
* * *

Simulate 10.0 years in 20 seconds

Start
![](../_resources/f2f5f5c2ffab03389f6aa31caca1e143.png)
2020
2021
2022
2023
2024
2025
2026
2027
2028
2029

- - - Herd Immunity––– ICU Capacity

This simulation has a "recorded scenario"!
Click "Start" to watch the recording *before*you change any of the numbers
But here's the scarier question:
What if there's no vaccine for *years*? Or *ever?*

**To be clear: this is unlikely.** Most epidemiologists expect a vaccine in 1 to 2 years. Sure, there's never been a vaccine for any of the other coronaviruses before, but that's because SARS was eradicated quickly, and "the" common cold wasn't worth the investment.

Still, infectious disease researchers have expressed worries: What if we can't make enough? What if we rush it, and it's not safe?

Even in the nightmare "no-vaccine" scenario, we still have 3 ways out. From most to least terrible:

1) Do intermittent or loose R < 1 interventions, to reach "natural herd immunity". (Warning: this will result in many deaths & damaged lungs. *And* won't work if immunity doesn't last.)

2) Do the R < 1 interventions forever. Contact tracing & wearing masks just becomes a new norm in the post-COVID-19 world, like how STI tests & wearing condoms became a new norm in the post-HIV world.

3) Do the R < 1 interventions until we develop treatments that make COVID-19 way, way less likely to need critical care. (Which we should be doing *anyway!*) Reducing ICU use by 10x is the same as increasing our ICU capacity by 10x:

**Here's a simulation of *no* lasting immunity, *no* vaccine, and not even any interventions – just slowly increasing capacity to survive the long-term spikes:**

R0 is 2.50
% of people who are *NOT*

Summer

R is now 2.43ICU capacity at 333%

* * *

Simulate 10.0 years in 20 seconds

Start
![](../_resources/f2f5f5c2ffab03389f6aa31caca1e143.png)
2020
2021
2022
2023
2024
2025
2026
2027
2028
2029

- - - Herd Immunity––– ICU Capacity

This simulation has a "recorded scenario"!
Click "Start" to watch the recording *before*you change any of the numbers
Even under the *worst* worst-case scenario... life perseveres.
. . .

Maybe you'd like to challenge our assumptions, and try different R0's or numbers. Or try simulating your *own* combination of intervention plans!

**Here's an (optional) Sandbox Mode, with *everything* available. (scroll to see all controls) Simulate & play around to your heart's content:**

On *average*, each ...

Infects 1  per 4 days
(at the start of the epidemic)
Takes 3 days to go from  to
Takes 10 days to go from  to
Loses immunity  in 12 months

* * *

R0 is 2.50
% of people who are *NOT*

Increased Hygiene

Physical Distancing

Isolating Cases

Quarantining Contacts

Face Masks

Summer

Vaccinations

R is now 2.50ICU capacity at 333%

* * *

Simulate 5.0 years

in 10 seconds

Start

This basic "epidemic flight simulator" has taught us so much. It's let us answer questions about the past few months, next few months, and next few years.

So finally, let's return to...

 ![curve.png](../_resources/c012557dd029a4c51f8d4e02bbccf9bf.png)
The Now

Plane's sunk. We've scrambled onto the life rafts. It's time to find dry land.

Teams of epidemiologists and policymakers ([left](https://www.americanprogress.org/issues/healthcare/news/2020/04/03/482613/national-state-plan-end-coronavirus-crisis/), [right](https://www.aei.org/research-products/report/national-coronavirus-response-a-road-map-to-reopening/), and [multi-partisan](https://ethics.harvard.edu/covid-roadmap)) have come to a consensus on how to beat COVID-19, while protecting our lives *and* liberties.

Here's the rough idea, with some (less-consensus) backup plans:
![plan.png](../_resources/98356174b5f586a2017a4d6e37f4a2d2.png)
So what does this mean for YOU, right now?

**For everyone:** Respect the lockdown so we can get out of Phase I asap. Keep washing those hands. Make your own masks. Download a *privacy-protecting* contact tracing app when those are available next month. Stay healthy, physically & mentally! And write your local policymaker to get off their butt and...

**For policymakers:** Make laws to support folks who have to self-isolate/quarantine. Hire more manual contact tracers, *supported* by privacy-protecting contact tracing apps. Direct more funds into the stuff we should be building, like...

**For builders:** Build tests. Build ventilators. Build personal protective equipment for hospitals. Build tests. Build masks. Build apps. Build antivirals, prophylactics, and other treatments that aren't vaccines. Build vaccines. Build tests. Build tests. Build tests. Build hope.

Don't downplay fear to build up hope. Our fear should *team up* with our hope, like the inventors of airplanes & parachutes. Preparing for horrible futures is how we *create* a hopeful future.

The only thing to fear is the idea that the only thing to fear is fear itself.

Help this post get R > 1: [(L)](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fncase.me%2Fcovid-19%2F)[(L)](https://twitter.com/intent/tweet?text=What%20Happens%20Next%3F%20COVID-19%20Futures%2C%20Explained%20With%20Playable%20Simulations%0A%F0%9F%94%AC%20Here%27s%20a%20real%20deep%20dive!%2030%20min%20read%2Fplay%3A%20https%3A%2F%2Fncase.me%2Fcovid-19%2F)[(L)](https://ncase.me/covid-19/mailto:?subject=What%20Happens%20Next%3F%20COVID-19%20Futures%2C%20Explained%20With%20Playable%20Simulations&body=%F0%9F%94%AC%20Here%27s%20a%20real%20deep%20dive!%2030%20min%20read%2Fplay%3A%20https%3A%2F%2Fncase.me%2Fcovid-19%2F)

This guide is

![](../_resources/d561f19e6604ee5d5d3bf4b0d9fcbde6.png)**PUBLIC DOMAIN**That means you *already* have permission to re-use & remix any of the art/code/words on this page – on blogs, news sites, classrooms, anywhere![(Swipe our code on Github)](https://github.com/ncase/covid-19)

**Just remember to credit[Marcel Salathé](https://scholar.google.com/citations?user=_wHMGkUAAAAJ&hl=en)&[Nicky Case](https://ncase.me/)(May 2020)**

This free, open-source guide was made possible thanks to Nicky's supporters on Patreon. If (seriously, ONLY IF) you have some disposible income in these hard times, you can[throw coins at Nicky!](https://www.patreon.com/ncase)If not, you can share this guide or[see their other educational art/interactives](https://ncase.me/). (excellent for homeshooling if, say, schools are currently closed due to a pandemic)

Here's some of the generous Patrons who made this possible:

9_9
Aaron Steelman
Abdallah AbuHashem
Adam Zeiner
Aeryn Light
Agent Entity
Ahti Ahde
Aimee Jarboe
Akito INOUE
Aldebarb
alex
Alex Kreitzberg
Alexander Zacherl
Alexis Olson
Allison Clift-Jennings
Amy Fuchs
Amy Traylor
Andre Latchman
Andrea Chlebikova
Andrea Di Biagio
Andrew Sachs
Andy Ellis
Anton Eremin
Apollo Slater
Aria Minaei
Armelle Laine
Arvand Barghi
Aurimas
B Cavello
Ben Kraft
Benoit Doidic
Berk Gedik
Brandon Quinn
Brendan Nelligan
Brian Handy
Brian Lange
Bruce Steinberg
Caelyn McAulay
Caio Vinicius do Nascimento
Cassandra Xia
Catherine J Smith
Cathy Deng
Cedric Nering
Chad Sansing
Charlie Stigler
Chong Kee Tan
Choose A Username
Chris Hallacy
Chris Makler
Chris Ploeg
Christine Capra
Christopher Ferrie
Christopher Walker
Clive Freeman
Colin Anderson
Colin Liotta
Connie
Corey Girard
count
Cristy Stone
Curtis Frye
Cyrus Levy
D
Da LIberman
Dag Frode Solberg
Damien Bernard
Daniel Shiffman
Daniel Teitelbaum
Dante
Darius Bacon
Dave B.
Dave Tu
David E Weekly
David Mora
Denis
Dominik
Duilio Palacios
Dylan Field
Eldecrok
Eric Chisholm
Ernst Scholtz
Ethan Muller
Eugene Eric Kim
Evan Rocha
Evan Shulman
Fanboat
Fiona Nielsen
Florencia Herra Vega
FlyingRat
Gabriel Barbosa Nunes
Gargi Sharma
Gary Coulter
Gauthier Muguerza
Glen E. Ivey
Grävling
Green
Greg
Guy Chapman
Harry Brisson
HI
Hilary Fried
Hildegard von Bigass
Idahosa Ness
ikrima
IndustrialRobot
Ivar Troost
Ivo Murrell
J C
Jacob Christian Munch-Andersen
James
James Horton
Jan Kölling
Jared Cosulich
Jason Crawford
Jay Mitchell
Jay Treat
jc
Jean-Eudes Denis
Jesse Bradley
Jing Wang
Jingfeng Chen
Joe Sevits
Jonne Harja
Joost Gadellaa
Joseph Rocca
Josh 'Cheeseness' Bush
Josh Koenig
Joshua Horowitz
Joy Buolamwini
k3taminee
Kailys
Kalu
Karen Cooper
Kate Fractal
Kelly Reed
Kelvin Nishikawa
Kendra Lockman
Kevin Richardson
Kevin Simler
Kevin Zollman
KevinDeLand
Kien
Kimberly Lammi
Kwame Thomison
Kyle Buswell
Kyle Studstill
labratross
Landy Manderson
Laura
Laura Baldwin
Laurent COOPER
Lee Berman
Leopard Dan
Liyi Zhang
Lucas Garron
Lukas Peyer
Lydia Choy
M
Malte
Manuel Kueblboeck
Marc Cohen
Marc Marasco
Marguerite Dibble
Mark Guzdial
marko
Mary Bush
Mary C.
Matt Hughes
Matthew Campbell
Maura Dawes
Maxim Sidorov
Mercury Legba
Michael Donatz
Michael Handler
Michael Huff
Michael Slade
Michal Takáč
Mikayla
Mikey
Mikkel Snyder
Naomi Alderman
Nat Alison
Natalie Rothfels
Natalie Sun
Nelson Crespo
Nguyet Vuong
Nigel Kerr
Nikhil Harithas
Nikita Vasilyev
Nimrod Kimhi
Noah Richards
Orb Li
Pablo Molins
Patrick Henderson
Paul d'Aoust
Paul Sztajer
Phil Dougherty
Philip White
Pierre Thierry
Pixl Pixl
postmillenial
Przemek Piotrowski
Rachél Bazelais
Rae McIntosh
Rafael F.Font
Ralph Pantozzi
raspbeguy
Raymond Keller
Rebecca Thomas
Reed Copperstrand
Ridima Ramesh
Rob Howard
Rob McKaughan
Robert Aran
Robert Cobb
Robert Duncan
Rohit Bhat
Ruby Moore
S Smith
saianne
Sara Ness
Sasha Fenn
Scott Reynolds
Sean Riley
Sergey Dolgov
Shreeya Goel
Simon
Simon Morrow
slow.danger
Smarter Every Day
Sofia Razón
Soraya Een Hajji
Sorden
Srini Kadamati
Steve Cha
Steve Ryman
Steve Waldman
Stewart Burrows Brand
Stian Soltvedt
Stuart
Sylvain Francis
T
Tal Rotbart
Tamir Bahar
Thais Weiller
Thember
Tobias Rose-Stockwell
toby schachman
Todd Siegel
Tom Lieber
Tommy Maranges
Toph Tucker
Tyler Coleman
Victor Debrus
Vlad Dziuba
Vladimir
Wait But Why
Wesley Gardner
what's for dinner
Will Dayble
William B Everett
Wouter
Yan Naung Oak
Yohan Dash
Yu-Han Kuo
Zach Smith
Zan Armstrong
Zener
zubr kabbi
김슬

And *huge* thank you to these folks for playtesting/proofreading: Alex Kreitzberg, Amit Patel, EmilyKate McDonough, Emma Hodcroft, Evan Rocha, Gillian Tarr, Grävling, Kayle Sawyer, Michael Huff, Phil Dougherty, Philipp Wacker, Ridima Ramesh, Sofia Razón, Srini Kadamati, Vi Hart

Any errors remaining are probably Nicky's fault.

## Feetnotes:

1. These footnotes will have sources, links, or bonus commentary. Like this commentary! [↩](https://ncase.me/covid-19/#fnref1)

**This guide was published on May 1st, 2020.** Many details will become outdated, but we're confident this guide will cover 95% of possible futures, and that Epidemiology 101 will remain forever useful.

2. “The mean [serial] interval was 3.96 days (95% CI 3.53–4.39 days)”. [Du Z, Xu X, Wu Y, Wang L, Cowling BJ, Ancel Meyers L](https://wwwnc.cdc.gov/eid/article/26/6/20-0357_article) (Disclaimer: Early release articles are not considered as final versions) [↩](https://ncase.me/covid-19/#fnref2)

3. **Remember: all these simulations are super simplified, for educational purposes.** [↩](https://ncase.me/covid-19/#fnref3)

One simplification: When you tell this simulation "Infect 1 new person every X days", it's actually increasing # of infected by 1/X each day. Same for future settings in these simulations – "Recover every X days" is actually reducing # of infected by 1/X each day.

Those *aren't* exactly the same, but it's close enough, and for educational purposes it's less opaque than setting the transmission/recovery rates directly.

4. “The median communicable period [...] was 9.5 days.” [Hu, Z., Song, C., Xu, C. et al](https://link.springer.com/article/10.1007/s11427-020-1661-4) Yes, we know "median" is not the same as "average". For simplified educational purposes, close enough. [↩](https://ncase.me/covid-19/#fnref4)

5. For more technical explanations of the SIR Model, see [the Institute for Disease Modeling](https://www.idmod.org/docs/hiv/model-sir.html#) and [Wikipedia](https://en.wikipedia.org/wiki/Compartmental_models_in_epidemiology#The_SIR_model) [↩](https://ncase.me/covid-19/#fnref5)

6. For more technical explanations of the SEIR Model, see [the Institute for Disease Modeling](https://www.idmod.org/docs/hiv/model-seir.html) and [Wikipedia](https://en.wikipedia.org/wiki/Compartmental_models_in_epidemiology#The_SEIR_model) [↩](https://ncase.me/covid-19/#fnref6)

7. “Assuming an incubation period distribution of mean 5.2 days from a separate study of early COVID-19 cases, we inferred that infectiousness started from 2.3 days (95% CI, 0.8–3.0 days) before symptom onset” (translation: Assuming symptoms start at 5 days, infectiousness starts 2 days before = Infectiousness starts at 3 days) [He, X., Lau, E.H.Y., Wu, P. et al.](https://www.nature.com/articles/s41591-020-0869-5) [↩](https://ncase.me/covid-19/#fnref7)

8. “The median R value for seasonal influenza was 1.28 (IQR: 1.19–1.37)” [Biggerstaff, M., Cauchemez, S., Reed, C. et al.](https://bmcinfectdis.biomedcentral.com/articles/10.1186/1471-2334-14-480) [↩](https://ncase.me/covid-19/#fnref8)

9. “We estimated the basic reproduction number R0 of 2019-nCoV to be around 2.2 (90% high density interval: 1.4–3.8)” [Riou J, Althaus CL.](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7001239/) [↩](https://ncase.me/covid-19/#fnref9)

10. “we calculated a median R0 value of 5.7 (95% CI 3.8–8.9)” [Sanche S, Lin YT, Xu C, Romero-Severson E, Hengartner N, Ke R.](https://wwwnc.cdc.gov/eid/article/26/7/20-0282_article) [↩](https://ncase.me/covid-19/#fnref10)

11. This is pretending that you're equally infectious all throughout your "infectious period". Again, simplifications for educational purposes. [↩](https://ncase.me/covid-19/#fnref11)

12. Remember R = R0 * the ratio of transmissions still allowed. Remember also that ratio of transmissions allowed = 1 - ratio of transmissions *stopped*. [↩](https://ncase.me/covid-19/#fnref12)

Therefore, to get R < 1, you need to get R0 * TransmissionsAllowed < 1.
Therefore, TransmissionsAllowed < 1/R0
Therefore, 1 - TransmissionsStopped < 1/R0
Therefore, TransmissionsStopped > 1 - 1/R0

Therefore, you need to stop more than **1 - 1/R0** of transmissions to get R < 1 and contain the virus!

13. ["Percentage of COVID-19 cases in the United States from February 12 to March 16, 2020 that required intensive care unit (ICU) admission, by age group"](https://www.statista.com/statistics/1105420/covid-icu-admission-rates-us-by-age-group/). Between 4.9% to 11.5% of *all* COVID-19 cases required ICU. Generously picking the lower range, that's 5% or 1 in 20. Note that this total is specific to the US's age structure, and will be higher in countries with older populations, lower in countries with younger populations. [↩](https://ncase.me/covid-19/#fnref13)

14. “Number of ICU beds = 96,596”. From [the Society of Critical Care Medicine](https://sccm.org/Blog/March-2020/United-States-Resource-Availability-for-COVID-19) USA Population was 328,200,000 in 2019. 96,596 out of 328,200,000 = roughly 1 in 3400.  [↩](https://ncase.me/covid-19/#fnref14)

15. “He says that the actual goal is the same as that of other countries: flatten the curve by staggering the onset of infections. As a consequence, the nation may achieve herd immunity; it’s a side effect, not an aim. [...] The government’s actual coronavirus action plan, available online, doesn’t mention herd immunity at all.” [↩](https://ncase.me/covid-19/#fnref15)

From a [The Atlantic article by Ed Yong](https://www.theatlantic.com/health/archive/2020/03/coronavirus-pandemic-herd-immunity-uk-boris-johnson/608065/)

16. “All eight eligible studies reported that handwashing lowered risks of respiratory infection, with risk reductions ranging from 6% to 44% [pooled value 24% (95% CI 6–40%)].” We rounded up the pooled value to 25% in these simulations for simplicity. [Rabie, T. and Curtis, V.](https://onlinelibrary.wiley.com/doi/full/10.1111/j.1365-3156.2006.01568.x) Note: as this meta-analysis points out, the quality of studies for handwashing (at least in high-income countries) are awful. [↩](https://ncase.me/covid-19/#fnref16)

17. “We found a 73% reduction in the average daily number of contacts observed per participant. This would be sufficient to reduce R0 from a value from 2.6 before the lockdown to 0.62 (0.37 - 0.89) during the lockdown”. We rounded it down to 70% in these simulations for simplicity. [Jarvis and Zandvoort et al](https://cmmid.github.io/topics/covid19/comix-impact-of-physical-distance-measures-on-transmission-in-the-UK.html) [↩](https://ncase.me/covid-19/#fnref17)

18. This distortion would go away if we plotted R on a logarithmic scale... but then we'd have to explain *logarithmic scales.* [↩](https://ncase.me/covid-19/#fnref18)

19. “Absent other interventions, a key metric for the success of social distancing is whether critical care capacities are exceeded. To avoid this, prolonged or intermittent social distancing may be necessary into 2022.” [Kissler and Tedijanto et al](https://science.sciencemag.org/content/early/2020/04/14/science.abb5793) [↩](https://ncase.me/covid-19/#fnref19)

20. See [Figure 6 from Holt-Lunstad & Smith 2010](https://journals.sagepub.com/doi/abs/10.1177/1745691614568352). Of course, big disclaimer that they found a *correlation*. But unless you want to try randomly assigning people to be lonely for life, observational evidence is all you're gonna get. [↩](https://ncase.me/covid-19/#fnref20)

21. **3 days on average to infectiousness:** “Assuming an incubation period distribution of mean 5.2 days from a separate study of early COVID-19 cases, we inferred that infectiousness started from 2.3 days (95% CI, 0.8–3.0 days) before symptom onset” (translation: Assuming symptoms start at 5 days, infectiousness starts 2 days before = Infectiousness starts at 3 days) [He, X., Lau, E.H.Y., Wu, P. et al.](https://www.nature.com/articles/s41591-020-0869-5)  [↩](https://ncase.me/covid-19/#fnref21)

**4 days on average to infecting someone else:** “The mean [serial] interval was 3.96 days (95% CI 3.53–4.39 days)” [Du Z, Xu X, Wu Y, Wang L, Cowling BJ, Ancel Meyers L](https://wwwnc.cdc.gov/eid/article/26/6/20-0357_article)

**5 days on average to feeling symptoms:** “The median incubation period was estimated to be 5.1 days (95% CI, 4.5 to 5.8 days)” [Lauer SA, Grantz KH, Bi Q, et al](https://annals.org/AIM/FULLARTICLE/2762808/INCUBATION-PERIOD-CORONAVIRUS-DISEASE-2019-COVID-19-FROM-PUBLICLY-REPORTED)

22. “We estimated that 44% (95% confidence interval, 25–69%) of secondary cases were infected during the index cases’ presymptomatic stage” [He, X., Lau, E.H.Y., Wu, P. et al](https://www.nature.com/articles/s41591-020-0869-5) [↩](https://ncase.me/covid-19/#fnref22)

23. “Contact tracing was a critical intervention in Liberia and represented one of the largest contact tracing efforts during an epidemic in history.” [Swanson KC, Altare C, Wesseh CS, et al.](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6152989/) [↩](https://ncase.me/covid-19/#fnref23)

24. [Temporary Contact Numbers, a decentralized, privacy-first contact tracing protocol](https://github.com/TCNCoalition/TCN#tcn-protocol) [↩](https://ncase.me/covid-19/#fnref24)

25. [PACT: Private Automated Contact Tracing](https://pact.mit.edu/) [↩](https://ncase.me/covid-19/#fnref25)

26. [Apple and Google partner on COVID-19 contact tracing technology](https://www.apple.com/ca/newsroom/2020/04/apple-and-google-partner-on-covid-19-contact-tracing-technology/). Note they're not making the apps *themselves*, just creating the systems that will *support* those apps. [↩](https://ncase.me/covid-19/#fnref26)

27. Lots of news reports – and honestly, many research papers – did not distinguish between "cases who showed no symptoms when we tested them" (pre-symptomatic) and "cases who showed no symptoms *ever*" (true asymptomatic). The only way you could tell the difference is by following up with cases later. [↩](https://ncase.me/covid-19/#fnref27)

Which is what [this study](https://wwwnc.cdc.gov/eid/article/26/8/20-1274_article) did. (Disclaimer: "Early release articles are not considered as final versions.") In a call center in South Korea that had a COVID-19 outbreak, "only 4 (1.9%) remained asymptomatic within 14 days of quarantine, and none of their household contacts acquired secondary infections."

So that means "true asymptomatics" are rare, and catching the disease from a true asymptomatic may be even rarer!

28. From the same Oxford study that first recommended apps to fight COVID-19: [Luca Ferretti & Chris Wymant et al](https://science.sciencemag.org/content/early/2020/04/09/science.abb6936/tab-figures-data) See Figure 2. Assuming R0 = 2.0, they found that:  [↩](https://ncase.me/covid-19/#fnref28)

    - Symptomatics contribute R = 0.8 (40%)
    - Pre-symptomatics contribute R = 0.9 (45%)
    - Asymptomatics contribute R = 0.1 (5%, though their model has uncertainty and it could be much lower)
    - Environmental stuff like doorknobs contribute R = 0.2 (10%)

And add up the pre- & a-symptomatic contacts (45% + 5%) and you get 50% of R!

29. “None of these surgical masks exhibited adequate filter performance and facial fit characteristics to be considered respiratory protection devices.” [Tara Oberg & Lisa M. Brosseau](https://www.sciencedirect.com/science/article/pii/S0196655307007742) [↩](https://ncase.me/covid-19/#fnref29)

30. “The overall 3.4 fold reduction [70% reduction] in aerosol copy numbers we observed combined with a nearly complete elimination of large droplet spray demonstrated by Johnson et al. suggests that surgical masks worn by infected persons could have a clinically significant impact on transmission.” [Milton DK, Fabian MP, Cowling BJ, Grantham ML, McDevitt JJ](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3591312/) [↩](https://ncase.me/covid-19/#fnref30)

31. Any actual scientist who read that last sentence is probably laugh-crying right now. See: [p-hacking](https://en.wikipedia.org/wiki/Data_dredging), [the replication crisis](https://en.wikipedia.org/wiki/Replication_crisis)) [↩](https://ncase.me/covid-19/#fnref31)

32. “It is time to apply the precautionary principle” [Trisha Greenhalgh et al [PDF]](https://www.bmj.com/content/bmj/369/bmj.m1435.full.pdf) [↩](https://ncase.me/covid-19/#fnref32)

33. [Davies, A., Thompson, K., Giri, K., Kafatos, G., Walker, J., & Bennett, A](https://www.cambridge.org/core/journals/disaster-medicine-and-public-health-preparedness/article/testing-the-efficacy-of-homemade-masks-would-they-protect-in-an-influenza-pandemic/0921A05A69A9419C862FA2F35F819D55) See Table 1: a 100% cotton T-shirt has around 2/3 the filtration efficiency as a surgical mask, for the two bacterial aerosols they tested. [↩](https://ncase.me/covid-19/#fnref33)

34. **"We need to save supplies for hospitals."**  *Absolutely agreed.* But that's more of an argument for increasing mask production, not rationing. In the meantime, we can make cloth masks. [↩](https://ncase.me/covid-19/#fnref34)

**"They're hard to wear correctly."** It's also hard to wash your hands according to the WHO Guidelines – seriously, "Step 3) right palm over left dorsum"?! – but we still recommend handwashing, because imperfect is still better than nothing.

**"It'll make people more reckless with handwashing & social distancing."** Sure, and safety belts make people ignore stop signs, and flossing makes people eat rocks. But seriously, we'd argue the opposite: masks are a *constant physical reminder* to be careful – and in East Asia, masks are also a symbol of solidarity!

35. “One-degree Celsius increase in temperature [...] lower[s] R by 0.0225” and “The average R-value of these 100 cities is 1.83”. 0.0225 ÷ 1.83 = ~1.2%. [Wang, Jingyuan and Tang, Ke and Feng, Kai and Lv, Weifeng](https://papers.ssrn.com/sol3/Papers.cfm?abstract_id=3551767) [↩](https://ncase.me/covid-19/#fnref35)

36. “SARS-specific antibodies were maintained for an average of 2 years [...] Thus, SARS patients might be susceptible to reinfection ≥3 years after initial exposure.” [Wu LP, Wang NC, Chang YH, et al.](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2851497/) "Sadly" we'll never know how long SARS immunity would have really lasted, since we eradicated it so quickly. [↩](https://ncase.me/covid-19/#fnref36)

37. “We found no significant difference between the probability of testing positive at least once and the probability of a recurrence for the beta-coronaviruses HKU1 and OC43 at 34 weeks after enrollment/first infection.” [Marta Galanti & Jeffrey Shaman (PDF)](http://www.columbia.edu/~jls106/galanti_shaman_ms_supp.pdf) [↩](https://ncase.me/covid-19/#fnref37)

38. “Once a person fights off a virus, viral particles tend to linger for some time. These cannot cause infections, but they can trigger a positive test.” [from STAT News by Andrew Joseph](https://www.statnews.com/2020/04/20/everything-we-know-about-coronavirus-immunity-and-antibodies-and-plenty-we-still-dont/) [↩](https://ncase.me/covid-19/#fnref38)

39. From [Bao et al.](https://www.biorxiv.org/content/10.1101/2020.03.13.990226v1.abstract)  *Disclaimer: This article is a preprint and has not been certified by peer review (yet).* Also, to emphasize: they only tested re-infection 28 days later.  [↩](https://ncase.me/covid-19/#fnref39)

40. “If a coronavirus vaccine arrives, can the world make enough?” [by Roxanne Khamsi, on Nature](https://www.nature.com/articles/d41586-020-01063-8) [↩](https://ncase.me/covid-19/#fnref40)

41. “Don’t rush to deploy COVID-19 vaccines and drugs without sufficient safety guarantees” [by Shibo Jiang, on Nature](https://www.nature.com/articles/d41586-020-00751-9) [↩](https://ncase.me/covid-19/#fnref41)

42. Dry land metaphor [from Marc Lipsitch & Yonatan Grad, on STAT News](https://www.statnews.com/2020/04/01/navigating-covid-19-pandemic/) [↩](https://ncase.me/covid-19/#fnref42)

wash your hands!