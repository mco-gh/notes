An Amazon Programmer's Perspective (http://pastebin.com/BjD84BQ3)

An Amazon Programmer's Perspective (http://pastebin.com/BjD84BQ3)

 [Raw](https://gist.github.com/bricker/cb811b3b86d767124801/raw/d5e29f99e4f46be506fc842336daa5da95ec299c/amznymous.md)

   ![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-gist js-evernote-checked' viewBox='0 0 12 16' version='1.1' width='12' height='16' aria-hidden='true' data-evernote-id='20'%3e%3cpath fill-rule='evenodd' d='M7.5 5L10 7.5 7.5 10l-.75-.75L8.5 7.5 6.75 5.75 7.5 5zm-3 0L2 7.5 4.5 10l.75-.75L3.5 7.5l1.75-1.75L4.5 5zM0 13V2c0-.55.45-1 1-1h10c.55 0 1 .45 1 1v11c0 .55-.45 1-1 1H1c-.55 0-1-.45-1-1zm1 0h10V2H1v11z' data-evernote-id='875' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)    [**amznymous.md**](https://gist.github.com/bricker/cb811b3b86d767124801#file-amznymous-md)

*Originally posted at http://pastebin.com/BjD84BQ3*
Trigger warning: mention of suicidal ideation

**tl;dr: I burned out as a developer at Amazon at the end of my second year. I’ve since found a healthy and sustainable work-life balance and enjoy work again. I write this to A) raise awareness, especially for new-hires and their families, and B) help give hope and advice to people going through the same at Amazon or other companies.**

#### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='21'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='882' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://gist.github.com/bricker/cb811b3b86d767124801#hello-world)Hello, world

There’s been no shortage of anecdotes, opinions, and rebuttals regarding Amazon’s corporate culture as of late. I write this not to capitalize on the latest news-feed fad, but to share what I had already written and promptly deleted. I didn’t think anyone would want to hear my story, but it’s apparent people are going through a similar experience and don’t have a voice.

I’m a Software Development Engineer II at Amazon; SDE II basically means a software developer with at least 2–3 years of industry experience. I started at Amazon as an SDE I.

To work at one of the Big 5 is no uncommon dream for most devs, but it was one that I shared. After passing a timed online coding quiz, I was flown to Seattle for an interview. Within a week of flying back, I got a call to congratulate me as well as discuss the usual (compensation, and benefits), as well as the exceptional (moving bonus, signing bonus, and vesting stock options). Remember those “exceptional” bits, as they matter later.

For the first few months, things were fairly standard: typical corporate mottos (this time called “Principles”) and “your work is more than just work” speeches. I see through it now but at the time phrases like “World’s Most Customer-Centric Company” are candy to a wide-eyed new-hire.

#### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='22'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='888' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://gist.github.com/bricker/cb811b3b86d767124801#first-comes-the-pager)First Comes the Pager

After being on the team for a couple of months, I was put on the on-call rotation. Here’s what being on-call means:

- You are on-call for 1 week every X weeks, where X is the number of members on your team
- While on-call, your other projects take up at most half your time during the workday
- The rest of the workday is focused on operational issues (keeping the lights on)
- You are on 24/7 pager duty during your on-call

Here’s what pager duty means:

- You are paged if a “thing” your team owns goes “into alarm.” This is intentionally vague because it means different things for different teams.
- If paged, you have 15 minutes to get online and respond to the page
- If you don’t, your manager is paged. You do NOT want this to happen

On-call wasn’t (and isn’t) too terrible for my team. At first we averaged 1 page every 2 weeks; now we’re up to about 1 a week. Other teams have it much, much worse. It is a social damper though. If you have to be able to “bail out” at a second’s notice, you can’t really make plans to go out anywhere.

I mention on-call duty because it is “peculiar” in that the only other profession requiring this kind of responsiveness is doctors, literal lifesavers. When you go on-call for the first time, it’s terrifying and tells you “holy crap, this is serious.”

During the hiring process, on-call is not mentioned in any way other than the usual salaried catch-all "are you willing to work nights and/or weekends."

#### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='23'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='904' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://gist.github.com/bricker/cb811b3b86d767124801#then-come-loaners)Then Come Loaners

Occasionally in order to complete a large project, some other team may need to make code changes. That other team, naturally, may not be able to spare the developers required, so you get loaned out. Until the project is done, you're between teams and serving two managers.

In some cases, that other team thought they could spare the dev-hours and complete the code changes. When they don’t, at some point they fall behind, so you get loaned out.

Anyone who's read "The Mythical Man-Month" has their ears perking up. For those who haven't read it, here's the gist, via Wikipedia: "adding manpower to a late software project makes it later".

My worst days at Amazon have been when I was loaned out; in fact, the worst days of my life were when I was loaned out.

Near the end of my second year at Amazon, I was pulled into "Project X" (obviously renamed). It had all the underpinnings of a project with a bad future:

- changing requirements from different teams, in different countries
- high stakes and visibility (practically up to Bezos himself)

I won't give a day-by-day account, but to cut to the chase: things got intense.

As the project fell behind, the pressure and scrutiny from above grew. The project managers wanted to pass down the urgency in the most productive way possible, to moderate success.

Long weekdays turned into working over the weekend. I felt largely responsible for how behind things were. As of now, I have no idea how true that is. Whatever the cause, whether through the need to prove my worth or out of fear of failure, the result was the same: I worked non-stop. Every waking hour was put into write code and fixing bugs.

At first I still had some self-awareness. I knew objectively that working more only makes one less productive, but It Had To Be Done.

Exhaustion eventually took over. My code got worse and worse. I thought I could outrace my bug-count with lines of code. The Inner Loop of the Death Spiral had begun to spin.

Eventually the stress changed my personality in ways that became visible to others. I was rude, when I’m normally out-going and understanding. I was humorless when I’m usually the one who makes jokes. My co-workers starting noticing it, despite the guise I tried to put on. I started choosing work over being with my friends. At first they understood. Some amount of "sorry I need to work" is understandable. Eventually they started to worry too. Again, in a misguided attempt to not burden them, I began to isolate myself => The Second Loop of the Death Spiral.

#### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='24'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='920' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://gist.github.com/bricker/cb811b3b86d767124801#lock-in)Lock-in

We haven't yet reached the outermost loop, but first, a short aside.

Remember when I mentioned Amazon's moving and signing bonus? Little caveat on that, if you leave or are fired within 2 years, you have to pay it back.

Still fresh out of college, my savings were significantly less than how much I would've owed. So if I were to quit Amazon, I wouldn't just be out of a job, I would be in the hole more than three months' income.

So now I cannot "just leave." With that realization came paralyzing hopelessness. If I failed and got fired, then I may not be able to find another job for quite a while. Un/Underemployment among Millennials is kind of A Thing. Now I have the stress of staying employed on top of everything => The Third Loop.

#### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='25'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='926' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://gist.github.com/bricker/cb811b3b86d767124801#cascading-failure)Cascading Failure

At this point, my self-care was non-existent. All to maximize code output, I lived off a steady stream of junk food and caffeine. I've always had some level of insomnia, but it got much worse. The final straw was when I traded sleep for code.

At this point the stress became a massive black hole in my mind. No other analogy fits. It physically felt crushing. No emotions and no thoughts could escape. I could only go over and over how much it hurt and that I wanted it to stop. This state is what I think of when I hear "Amazombie."

During this time I cried. A lot. Usually when going to sleep, as I knew it would just all start again the next day. Sometimes with my wife. A couple of times in the bathroom stall. But no, (you masochists) not at my desk.

With my brain producing only two thought types ("Pain" and "Please stop pain"), it wasn't long before thoughts of suicide crept in.

To be clear: I never took any action on these thoughts. I did not want to kill myself. I kept thoughts of planning away as much as I could. But that's the thing with suicidal ideation: despite what you really want, the thought comes back again and again and finally replaces "Please stop pain" with "Please stop Everything." => The Final Loop.

#### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='26'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='933' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://gist.github.com/bricker/cb811b3b86d767124801#endgame)Endgame

I finally sought psychiatric help. I remember the decision coming so matter-of-fact. Almost with the enthusiasm that you hire a handyman to fix something. "Hm. A leaky pipe. Better get a plumber." "Ruminating thoughts of ending it? I should have someone to look at that."

Up until this point, the only person who knew what was really going on was my wife. I cannot (but will try to) express my gratitude to her during this time. She was there exactly when I needed her. She helped even when she didn't understand why I was putting myself through it. She saw the signs much sooner than I did and tried to tell me. When I did realize I needed help, she put me in touch.

I was put on Celexa. Eventually the Death Spiral's loops unwound. The project launched. Things went back to mostly normal. I went off of Celexa after a couple of months. I didn't feel fully recovered until months later. I felt on eggshells. I rigorously prioritized self-care by leaving work at 8 hours in, on the dot. I started reaching back out to my friends for hangouts.

My manager gave me a couple of extra vacation days in return for my efforts. I was promoted to SDE II and was even healthy enough to celebrate and enjoy it.

#### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='27'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='939' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://gist.github.com/bricker/cb811b3b86d767124801#have-backbone)Have Backbone

"So what? So you burned yourself out and got burned out. What did you expect?" I wrote this because I needed to put my story down and as a cautionary tale. I am NOT here to set some silly bar of what a "real" programmer does to get things done. I am NOT here to demonize Amazon.

As far as what I have to say to Amazon/Jeff Bezos, I only have a few things:

- Revisit your bonus/relocation payback strategy. I don't know what the "right" solution is, but if that's what you need to keep employees, that's fucked.
- Be upfront and as precise as possible with what a position entails. "Working alongside smart and passionate people" is lazy hiring.
- Encourage employees to be critical not just of ideas, but also of expectations. Getting them to buy into the idea that they have to give up everything else to get validation from you is abusive.
- Realize that productivity and happy employees is not a zero-sum game. The customer is not a wrathful god that demands a sacrifice

This cautionary tale is not Amazon-specific. This could happen to nearly anyone, but especially people working in intense workplaces and especially developers working in intense workplaces.

There's a saying that I saw over and over again in forums and subreddits, but never believed until I lived it:

> It's your professional obligation to push back on unreasonable expectations. Your bosses may not like it at first, but they will respect you for it.

My other piece of advice-you-didn't-come-here-for: save some Fuck You money.

#### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='28'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='953' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://gist.github.com/bricker/cb811b3b86d767124801#common-reactions)Common Reactions

I know that by posting this anonymously I'm not facilitating a discussion. An anon post is me talking at you.

However, I wouldn't be posting in this manner if I wasn't authentically afraid of losing my job. The only other voices we've heard from current employees have been gag-worthy in favor of Amazon: https://www.linkedin.com/pulse/amazonians-response-inside-amazon-wrestling-big-ideas-nick-ciubotariu, https://www.linkedin.com/pulse/my-name-brittan-im-amazonian-brittan-cole-ma

A few major criticisms of these two articles:

- They're on LinkedIn. I abhor anything posted on LinkedIn. All criticism is toothless; all words watered down. Because everything is scoured by future employers, everyone is afraid of actually saying anything controversial.
- They're from employees that aren't "on the ground," but rather a manager-of-managers and an HR-rep respectively.

Does no one else find it interesting that we're not seeing any negative criticism from current employees? I don't care what company you work for, there is never any shortage of people willing to complain. So why no negative articles from current employees?

Fear. Fear breeds a culture of silence.

There are a few common responses I've seen to articles and I would like to pre-empt those here:

"Working more than exactly 40 hours is part of being a professional." (and variants thereof) I agree wholeheartedly, but these should be occasional events. 70+ hour weeks shouldn't be the holding pattern. They should be appreciated by management. Hell, buy us dinner if you're going to fuck us over a door desk.

"Why didn't you just work less? It seems like a lot of it was your own fault." I go over this question again and again in my own head. Along with the reasons mentioned before, I just felt compelled to push through it. I felt that after getting hired at such a "big name" company, that if I didn't put everything I could into it that I was doing a disservice to all those who helped me get here. What I didn't realize was that the opposite was true: that by breaking myself, I did show that I wasn't ready in a way. Thankfully I did make it through as was able to learn from it.

"You're just a ball of negativity, no wonder you got depressed" Which brings me to my next section...

#### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='29'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='967' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://gist.github.com/bricker/cb811b3b86d767124801#happy-trails)Happy Trails

In addition to my story, I do want to enumerate the things I enjoy about working at Amazon. I am still working here after all and I have no plans of putting in my notice.

- Lax working hours & can work from home “What?!? After all you just said?!?” But seriously, when things are not in crisis, which is 80%+ of the time, a developer's day rarely starts before 9am. You can usually work from home about once a week. If you need to leave work early for a good reason, that's fine (though it's usually common courtesy to work from home afterward).
- No Dress Code This may be a given in most places, but coming from a business-casual-only place, t-shirts are a godsend.
- Pay It has to be mentioned. I won’t give out numbers, as that could be identifying, but Glassdoor.com can satisfy your curiosity. When a good portion of my friends struggle to stay gainfully employed, it is nice. Despite the issues I described above, I still come from a privileged position of being financially stable and now have a good amount of job security.
- Work with and build on top of "giants" One of the common hiring catch phrases of tech companies is to "work alongside smart people." While I usually roll my eyes at that, it actually is important to a developer's growth to not always be the smartest one in the room.
- Recruiting Jeff Bezos's email mentioned how we get contacted by recruiters all the time; with that aspect was in touch with our reality. I've heard from Google, Facebook, Netflix, and others. I got more recruiting emails in my first month in Seattle than I did in a year in my previous location.
- Near-Instant Gratification There is something great about having code you wrote be actually executed by thousands of people every day. So few people get to show their friends and family a site they visit often and say "I did that thing there." Maybe it will wear off eventually, but it's still my favorite.

#### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='30'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='983' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://gist.github.com/bricker/cb811b3b86d767124801#event-horizon)Event Horizon

I'm on a new loaner project now. Another "DEFCON ZEROMG!" project, but now I have boundaries,and the knowledge that Amazon will not topple over if I don’t work 70-hour weeks. Work-life balance can be largely subjective, but I now know what that balance looks like for me and enforce that while still putting my best efforts into my work I had to learn that the hard way. I can only hope you don't have to as well.

*-amznymous (https://www.reddit.com/user/amznymous/)*

 [![27011](../_resources/ebb0e315460194409ae4c7e1ce39dcae.png)](https://gist.github.com/BillBarnhill)

 ![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' aria-label='Show options' class='octicon octicon-kebab-horizontal js-evernote-checked' viewBox='0 0 13 16' version='1.1' width='13' height='16' role='img' data-evernote-id='34'%3e%3cpath fill-rule='evenodd' d='M1.5 9a1.5 1.5 0 100-3 1.5 1.5 0 000 3zm5 0a1.5 1.5 0 100-3 1.5 1.5 0 000 3zM13 7.5a1.5 1.5 0 11-3 0 1.5 1.5 0 013 0z' data-evernote-id='1018' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)

###   **  [BillBarnhill](https://gist.github.com/BillBarnhill)  ** commented [yesterday](https://gist.github.com/bricker/cb811b3b86d767124801#gistcomment-3313314)

|     |
| --- |
| +1, and thank you. As someone who was there (albeit a different there) at one point, it helps to hear similar stories from others. |

 [![1066583](../_resources/22e2706d68a2af8f13cd6f2fc30c699c.jpg)](https://gist.github.com/WriteCodeEveryday)

 ![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' aria-label='Show options' class='octicon octicon-kebab-horizontal js-evernote-checked' viewBox='0 0 13 16' version='1.1' width='13' height='16' role='img' data-evernote-id='38'%3e%3cpath fill-rule='evenodd' d='M1.5 9a1.5 1.5 0 100-3 1.5 1.5 0 000 3zm5 0a1.5 1.5 0 100-3 1.5 1.5 0 000 3zM13 7.5a1.5 1.5 0 11-3 0 1.5 1.5 0 013 0z' data-evernote-id='1060' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)

###   **  [WriteCodeEveryday](https://gist.github.com/WriteCodeEveryday)  ** commented [yesterday](https://gist.github.com/bricker/cb811b3b86d767124801#gistcomment-3313358)

|     |
| --- |
| One of the most brightest people I knew ended up on the same downward spiral where bugs became more lines and more hours. He eventually turned to drinking himself to cope with a shitty work environment. I do think he also had suicidal ideation but ended up just ragequitting his job instead. |

 [![8009085](../_resources/5a48d0c9725417881ebe9c03f5020676.png)](https://gist.github.com/aahmed-se)

 ![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' aria-label='Show options' class='octicon octicon-kebab-horizontal js-evernote-checked' viewBox='0 0 13 16' version='1.1' width='13' height='16' role='img' data-evernote-id='42'%3e%3cpath fill-rule='evenodd' d='M1.5 9a1.5 1.5 0 100-3 1.5 1.5 0 000 3zm5 0a1.5 1.5 0 100-3 1.5 1.5 0 000 3zM13 7.5a1.5 1.5 0 11-3 0 1.5 1.5 0 013 0z' data-evernote-id='1102' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)

###   **  [aahmed-se](https://gist.github.com/aahmed-se)  ** commented [yesterday](https://gist.github.com/bricker/cb811b3b86d767124801#gistcomment-3313385)

|     |
| --- |
| +1  |

 [![74927](../_resources/ed40a7bfd75efe98ae89fca2ca59e177.jpg)](https://gist.github.com/gknauth)

 ![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' aria-label='Show options' class='octicon octicon-kebab-horizontal js-evernote-checked' viewBox='0 0 13 16' version='1.1' width='13' height='16' role='img' data-evernote-id='46'%3e%3cpath fill-rule='evenodd' d='M1.5 9a1.5 1.5 0 100-3 1.5 1.5 0 000 3zm5 0a1.5 1.5 0 100-3 1.5 1.5 0 000 3zM13 7.5a1.5 1.5 0 11-3 0 1.5 1.5 0 013 0z' data-evernote-id='1144' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)

###   **  [gknauth](https://gist.github.com/gknauth)  ** commented [yesterday](https://gist.github.com/bricker/cb811b3b86d767124801#gistcomment-3313391)

|     |
| --- |
| Thank you for writing this. I'm sure it will help many people. |

 [![27534106](../_resources/328d8c72d1607d8a8d0e5690e66e223d.png)](https://gist.github.com/willsliou)

 ![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' aria-label='Show options' class='octicon octicon-kebab-horizontal js-evernote-checked' viewBox='0 0 13 16' version='1.1' width='13' height='16' role='img' data-evernote-id='50'%3e%3cpath fill-rule='evenodd' d='M1.5 9a1.5 1.5 0 100-3 1.5 1.5 0 000 3zm5 0a1.5 1.5 0 100-3 1.5 1.5 0 000 3zM13 7.5a1.5 1.5 0 11-3 0 1.5 1.5 0 013 0z' data-evernote-id='1186' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)

###   **  [willsliou](https://gist.github.com/willsliou)  ** commented [yesterday](https://gist.github.com/bricker/cb811b3b86d767124801#gistcomment-3313395)

|     |
| --- |
| Came here from Hacker News. Interesting write up - hope you're feeling better |

 [![63891960](../_resources/8525d473cdc8dc0485781cfa1eedee25.jpg)](https://gist.github.com/mtclinton)

 ![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' aria-label='Show options' class='octicon octicon-kebab-horizontal js-evernote-checked' viewBox='0 0 13 16' version='1.1' width='13' height='16' role='img' data-evernote-id='54'%3e%3cpath fill-rule='evenodd' d='M1.5 9a1.5 1.5 0 100-3 1.5 1.5 0 000 3zm5 0a1.5 1.5 0 100-3 1.5 1.5 0 000 3zM13 7.5a1.5 1.5 0 11-3 0 1.5 1.5 0 013 0z' data-evernote-id='1231' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)

###   **  [mtclinton](https://gist.github.com/mtclinton)  ** commented [yesterday](https://gist.github.com/bricker/cb811b3b86d767124801#gistcomment-3313396)

|     |
| --- |
| "I am NOT here to demonize Amazon."<br>They almost pushed you to suicide, told you "we are family", and you are fearful of them enough to post a review anonymously.<br>The buck needs to stop somewhere. Amazon and Jeff Bezos are responsible for their employees<br>The US government needs to step in to help these people being exploited |

 [![18623](../_resources/6731023c8d1d107184406b2fa11a2b77.jpg)](https://gist.github.com/lawwantsin)

 ![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' aria-label='Show options' class='octicon octicon-kebab-horizontal js-evernote-checked' viewBox='0 0 13 16' version='1.1' width='13' height='16' role='img' data-evernote-id='58'%3e%3cpath fill-rule='evenodd' d='M1.5 9a1.5 1.5 0 100-3 1.5 1.5 0 000 3zm5 0a1.5 1.5 0 100-3 1.5 1.5 0 000 3zM13 7.5a1.5 1.5 0 11-3 0 1.5 1.5 0 013 0z' data-evernote-id='1276' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)

###   **  [lawwantsin](https://gist.github.com/lawwantsin)  ** commented [yesterday](https://gist.github.com/bricker/cb811b3b86d767124801#gistcomment-3313401)    •

  edited   ![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' height='11' class='octicon octicon-triangle-down v-align-middle js-evernote-checked' viewBox='0 0 12 16' version='1.1' width='8' aria-hidden='true' data-evernote-id='59'%3e%3cpath fill-rule='evenodd' d='M0 5l6 6 6-6H0z' data-evernote-id='1286' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)

|     |
| --- |
| Every industry works its young people to the bone. I had the same hours in television as a PA. Eventually freelance is the only way to keep the bosses from riding your back all the way to the bank. Thanks for reminding me why I don't want to code for a Unicorn. |

 [![63891960](../_resources/8525d473cdc8dc0485781cfa1eedee25.jpg)](https://gist.github.com/mtclinton)

 ![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' aria-label='Show options' class='octicon octicon-kebab-horizontal js-evernote-checked' viewBox='0 0 13 16' version='1.1' width='13' height='16' role='img' data-evernote-id='63'%3e%3cpath fill-rule='evenodd' d='M1.5 9a1.5 1.5 0 100-3 1.5 1.5 0 000 3zm5 0a1.5 1.5 0 100-3 1.5 1.5 0 000 3zM13 7.5a1.5 1.5 0 11-3 0 1.5 1.5 0 013 0z' data-evernote-id='1325' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)

###   **  [mtclinton](https://gist.github.com/mtclinton)  ** commented [yesterday](https://gist.github.com/bricker/cb811b3b86d767124801#gistcomment-3313410)    •

  edited   ![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' height='11' class='octicon octicon-triangle-down v-align-middle js-evernote-checked' viewBox='0 0 12 16' version='1.1' width='8' aria-hidden='true' data-evernote-id='64'%3e%3cpath fill-rule='evenodd' d='M0 5l6 6 6-6H0z' data-evernote-id='1335' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)

|     |
| --- |
| Then the US government should go through every industry and regulate every company that is exploiting its young people to the point of suicide<br>And if the US government can give trillions to large corporations but can't help the average man from being exploited then the US government is illegitimate. |

 [![423827](../_resources/4ea0c9bf520b49d9b0dc6f96f00270e1.jpg)](https://gist.github.com/danesparza)

 ![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' aria-label='Show options' class='octicon octicon-kebab-horizontal js-evernote-checked' viewBox='0 0 13 16' version='1.1' width='13' height='16' role='img' data-evernote-id='68'%3e%3cpath fill-rule='evenodd' d='M1.5 9a1.5 1.5 0 100-3 1.5 1.5 0 000 3zm5 0a1.5 1.5 0 100-3 1.5 1.5 0 000 3zM13 7.5a1.5 1.5 0 11-3 0 1.5 1.5 0 013 0z' data-evernote-id='1378' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)

###   **  [danesparza](https://gist.github.com/danesparza)  ** commented [yesterday](https://gist.github.com/bricker/cb811b3b86d767124801#gistcomment-3313434)

|     |
| --- |
| As somebody who worked at a startup (that became a billion dollar company in the years that I worked there) I completely agree with you on many of these points.<br>> it actually is important to a developer's growth to not always be the smartest one in the room<br>I have found this to be paramount. You will be bored, otherwise. In my book, try to not *ever* be the smartest one on your dev team. That gets difficult as the years go on (and I've been doing this for 25+ years) -- but it's doable. Just be picky. It's important. |

 [![60978500](../_resources/32874181bbe6e3b3948e6eb7a5943ad5.jpg)](https://gist.github.com/semanticbodger)

 ![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' aria-label='Show options' class='octicon octicon-kebab-horizontal js-evernote-checked' viewBox='0 0 13 16' version='1.1' width='13' height='16' role='img' data-evernote-id='72'%3e%3cpath fill-rule='evenodd' d='M1.5 9a1.5 1.5 0 100-3 1.5 1.5 0 000 3zm5 0a1.5 1.5 0 100-3 1.5 1.5 0 000 3zM13 7.5a1.5 1.5 0 11-3 0 1.5 1.5 0 013 0z' data-evernote-id='1431' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)

###   **  [semanticbodger](https://gist.github.com/semanticbodger)  ** commented [22 hours ago](https://gist.github.com/bricker/cb811b3b86d767124801#gistcomment-3313556)

|     |
| --- |
| > I mention on-call duty because it is “peculiar” in that the only other profession requiring this kind of responsiveness is doctors, literal lifesavers.<br>I appreciate the struggles you've experienced, but this particular statement is not well-grounded in reality. There are many professions - that have nothing to do with life-saving - where on-call (pager) duty is a necessary fact of life. Just because no one's *dying* doesn't necessarily mean that the employer, or the client, is willing to wait until 9AM of the next workday to have the situation fixed. When my internet connection dies at midnight, I call the ISP. And they dispatch someone to fix it - *that night* - if there's a confirmed outage. My father worked for a welding supply company, and he used to get off-hours calls when a client ran out of gas. There are many other such examples.<br>In software development, this is not "the norm", but neither is it *abnormal*. Every shop I've worked in with high transaction volumes had some kind of on-call expectation once I was up-to-speed. In some environments, it's the kind of "obligation" that you'll only be called to fulfill in rare, extreme scenarios. In other environments, taking on-call duty is almost a guarantee that you'll be called, at least once, at some point during your on-call shift.<br>If that's unacceptable to you (and there's nothing wrong if it is), then you should be careful to screen for those requirements when considering a potential job offer. |

 [![65744716](../_resources/7fe0bcc17bc7b7e276c7e2eaa550b869.png)](https://gist.github.com/jupytersalad)

 ![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' aria-label='Show options' class='octicon octicon-kebab-horizontal js-evernote-checked' viewBox='0 0 13 16' version='1.1' width='13' height='16' role='img' data-evernote-id='76'%3e%3cpath fill-rule='evenodd' d='M1.5 9a1.5 1.5 0 100-3 1.5 1.5 0 000 3zm5 0a1.5 1.5 0 100-3 1.5 1.5 0 000 3zM13 7.5a1.5 1.5 0 11-3 0 1.5 1.5 0 013 0z' data-evernote-id='1480' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)

###   **  [jupytersalad](https://gist.github.com/jupytersalad)  ** commented [20 hours ago](https://gist.github.com/bricker/cb811b3b86d767124801#gistcomment-3313643)

|     |
| --- |
| semanticbodger said it best, imo. I agree 70+ hours as the norm is unreasonable. I also know several people that worked on Wall Street in the early 2000s that slept at work several times a week. This happens in so many industries, not just Amazon. You also mention several of the other FAANG companies that have attempted to recruit you. You can expect more of the same from them. Every semi-decent developer wants a role at one of these companies. The stock options alone will make you a millionaire. They know they can work you to the bone because finding the next person that is willing to work 70+ hours is easy. I'm happy to hear you're doing better. But I would expect more of the same at another FAANG company or a startup. Remember, the first million is always the hardest. |

 [![25436433](../_resources/af9d419376949b57ef3a1465abf3bf06.png)](https://gist.github.com/mburszley)

 ![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' aria-label='Show options' class='octicon octicon-kebab-horizontal js-evernote-checked' viewBox='0 0 13 16' version='1.1' width='13' height='16' role='img' data-evernote-id='80'%3e%3cpath fill-rule='evenodd' d='M1.5 9a1.5 1.5 0 100-3 1.5 1.5 0 000 3zm5 0a1.5 1.5 0 100-3 1.5 1.5 0 000 3zM13 7.5a1.5 1.5 0 11-3 0 1.5 1.5 0 013 0z' data-evernote-id='1524' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)

###   **  [mburszley](https://gist.github.com/mburszley)  ** commented [19 hours ago](https://gist.github.com/bricker/cb811b3b86d767124801#gistcomment-3313690)

|     |
| --- |
| > Every semi-decent developer wants a role at one of these companies.<br>[@jupytersalad](https://github.com/jupytersalad) solid nope. We all read these stories. I'd rather have a cushy job in the midwest where COL is low but pay is still way above average. |

 [![12391](../_resources/d36d3b7f01a3ee97e7b162196c06ca2a.jpg)](https://gist.github.com/dai)

 ![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' aria-label='Show options' class='octicon octicon-kebab-horizontal js-evernote-checked' viewBox='0 0 13 16' version='1.1' width='13' height='16' role='img' data-evernote-id='84'%3e%3cpath fill-rule='evenodd' d='M1.5 9a1.5 1.5 0 100-3 1.5 1.5 0 000 3zm5 0a1.5 1.5 0 100-3 1.5 1.5 0 000 3zM13 7.5a1.5 1.5 0 11-3 0 1.5 1.5 0 013 0z' data-evernote-id='1568' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)

###   **  [dai](https://gist.github.com/dai)  ** commented [18 hours ago](https://gist.github.com/bricker/cb811b3b86d767124801#gistcomment-3313733)

|     |
| --- |
| +1  |

 [![1375512](../_resources/398fd9148ade1bd30781aa4fdafe305f.jpg)](https://gist.github.com/johnwildes)

 ![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' aria-label='Show options' class='octicon octicon-kebab-horizontal js-evernote-checked' viewBox='0 0 13 16' version='1.1' width='13' height='16' role='img' data-evernote-id='88'%3e%3cpath fill-rule='evenodd' d='M1.5 9a1.5 1.5 0 100-3 1.5 1.5 0 000 3zm5 0a1.5 1.5 0 100-3 1.5 1.5 0 000 3zM13 7.5a1.5 1.5 0 11-3 0 1.5 1.5 0 013 0z' data-evernote-id='1610' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)

###   **  [johnwildes](https://gist.github.com/johnwildes)  ** commented [17 hours ago](https://gist.github.com/bricker/cb811b3b86d767124801#gistcomment-3313778)

|     |
| --- |
| Thanks for sharing! |

 [![58410019](../_resources/2a1fbe8c1a0158a4f07a296064ec778e.png)](https://gist.github.com/AlphaHot)

 ![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' aria-label='Show options' class='octicon octicon-kebab-horizontal js-evernote-checked' viewBox='0 0 13 16' version='1.1' width='13' height='16' role='img' data-evernote-id='92'%3e%3cpath fill-rule='evenodd' d='M1.5 9a1.5 1.5 0 100-3 1.5 1.5 0 000 3zm5 0a1.5 1.5 0 100-3 1.5 1.5 0 000 3zM13 7.5a1.5 1.5 0 11-3 0 1.5 1.5 0 013 0z' data-evernote-id='1652' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)

###   **  [AlphaHot](https://gist.github.com/AlphaHot)  ** commented [16 hours ago](https://gist.github.com/bricker/cb811b3b86d767124801#gistcomment-3313820)

|     |
| --- |
| +1  |

 [![91933](../_resources/a6d1b7eb96bcd58de908ccc074338b0c.jpg)](https://gist.github.com/Daniel15)

 ![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' aria-label='Show options' class='octicon octicon-kebab-horizontal js-evernote-checked' viewBox='0 0 13 16' version='1.1' width='13' height='16' role='img' data-evernote-id='96'%3e%3cpath fill-rule='evenodd' d='M1.5 9a1.5 1.5 0 100-3 1.5 1.5 0 000 3zm5 0a1.5 1.5 0 100-3 1.5 1.5 0 000 3zM13 7.5a1.5 1.5 0 11-3 0 1.5 1.5 0 013 0z' data-evernote-id='1695' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)

###   **  [Daniel15](https://gist.github.com/Daniel15)  ** commented [14 hours ago](https://gist.github.com/bricker/cb811b3b86d767124801#gistcomment-3313930)

|     |
| --- |
| This is from 2015... Not sure why it's getting so much attention again today?<br>I wonder if anything has changed at Amazon since this was written. |

 [![30738853](../_resources/5d064ea115fb9b6dd05da28f45d1e1d4.jpg)](https://gist.github.com/rodmirsantana)

 ![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' aria-label='Show options' class='octicon octicon-kebab-horizontal js-evernote-checked' viewBox='0 0 13 16' version='1.1' width='13' height='16' role='img' data-evernote-id='100'%3e%3cpath fill-rule='evenodd' d='M1.5 9a1.5 1.5 0 100-3 1.5 1.5 0 000 3zm5 0a1.5 1.5 0 100-3 1.5 1.5 0 000 3zM13 7.5a1.5 1.5 0 11-3 0 1.5 1.5 0 013 0z' data-evernote-id='1738' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)

###   **  [rodmirsantana](https://gist.github.com/rodmirsantana)  ** commented [9 hours ago](https://gist.github.com/bricker/cb811b3b86d767124801#gistcomment-3314256)

|     |
| --- |
| Nice article. I've read similar stories about working in one of these big tech companies, but didn't know that Amazon have these particular conditions. I currently work at a software company (not a big one) and feel that it can be better for work/life balance in many ways when compared to the big ones. |

 [![60978500](../_resources/32874181bbe6e3b3948e6eb7a5943ad5.jpg)](https://gist.github.com/semanticbodger)

 ![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' aria-label='Show options' class='octicon octicon-kebab-horizontal js-evernote-checked' viewBox='0 0 13 16' version='1.1' width='13' height='16' role='img' data-evernote-id='104'%3e%3cpath fill-rule='evenodd' d='M1.5 9a1.5 1.5 0 100-3 1.5 1.5 0 000 3zm5 0a1.5 1.5 0 100-3 1.5 1.5 0 000 3zM13 7.5a1.5 1.5 0 11-3 0 1.5 1.5 0 013 0z' data-evernote-id='1783' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)

###   **  [semanticbodger](https://gist.github.com/semanticbodger)  ** commented [8 hours ago](https://gist.github.com/bricker/cb811b3b86d767124801#gistcomment-3314318)

|     |
| --- |
| > This is from 2015... Not sure why it's getting so much attention again today?<br>> I wonder if anything has changed at Amazon since this was written.<br>It was featured on Digg recently. |

 [![25484711](../_resources/562c4568cfca2cf01aa22c81b0f80e8d.jpg)](https://gist.github.com/orlyyani)

 ![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' aria-label='Show options' class='octicon octicon-kebab-horizontal js-evernote-checked' viewBox='0 0 13 16' version='1.1' width='13' height='16' role='img' data-evernote-id='108'%3e%3cpath fill-rule='evenodd' d='M1.5 9a1.5 1.5 0 100-3 1.5 1.5 0 000 3zm5 0a1.5 1.5 0 100-3 1.5 1.5 0 000 3zM13 7.5a1.5 1.5 0 11-3 0 1.5 1.5 0 013 0z' data-evernote-id='1828' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)

###   **  [orlyyani](https://gist.github.com/orlyyani)  ** commented [6 hours ago](https://gist.github.com/bricker/cb811b3b86d767124801#gistcomment-3314434)

|     |
| --- |
| +1  |

 [![15316378](../_resources/ea6d32123c629cbd9a7508273f37c6b6.png)](https://gist.github.com/kamalhm)

 ![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' aria-label='Show options' class='octicon octicon-kebab-horizontal js-evernote-checked' viewBox='0 0 13 16' version='1.1' width='13' height='16' role='img' data-evernote-id='112'%3e%3cpath fill-rule='evenodd' d='M1.5 9a1.5 1.5 0 100-3 1.5 1.5 0 000 3zm5 0a1.5 1.5 0 100-3 1.5 1.5 0 000 3zM13 7.5a1.5 1.5 0 11-3 0 1.5 1.5 0 013 0z' data-evernote-id='1871' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)

###   **  [kamalhm](https://gist.github.com/kamalhm)  ** commented [5 hours ago](https://gist.github.com/bricker/cb811b3b86d767124801#gistcomment-3314557)

|     |
| --- |
| ❤   |

 [![658327](../_resources/912a6f88549d7d06d6c90928224dd4ab.jpg)](https://gist.github.com/marcacohen)

   ![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-text-size js-evernote-checked' viewBox='0 0 18 16' version='1.1' width='18' height='16' aria-hidden='true' data-evernote-id='113'%3e%3cpath fill-rule='evenodd' d='M13.62 9.08L12.1 3.66h-.06l-1.5 5.42h3.08zM5.7 10.13S4.68 6.52 4.53 6.02h-.08l-1.13 4.11H5.7zM17.31 14h-2.25l-.95-3.25h-4.07L9.09 14H6.84l-.69-2.33H2.87L2.17 14H0l3.3-9.59h2.5l2.17 6.34L10.86 2h2.52l3.94 12h-.01z' data-evernote-id='1898' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)  Add header text    ![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-bold js-evernote-checked' viewBox='0 0 10 16' version='1.1' width='10' height='16' aria-hidden='true' data-evernote-id='114'%3e%3cpath fill-rule='evenodd' d='M1 2h3.83c2.48 0 4.3.75 4.3 2.95 0 1.14-.63 2.23-1.67 2.61v.06c1.33.3 2.3 1.23 2.3 2.86 0 2.39-1.97 3.52-4.61 3.52H1V2zm3.66 4.95c1.67 0 2.38-.66 2.38-1.69 0-1.17-.78-1.61-2.34-1.61H3.13v3.3h1.53zm.27 5.39c1.77 0 2.75-.64 2.75-1.98 0-1.27-.95-1.81-2.75-1.81h-1.8v3.8h1.8v-.01z' data-evernote-id='1900' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)  Add bold text <ctrl+b>    ![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-italic js-evernote-checked' viewBox='0 0 6 16' version='1.1' width='6' height='16' aria-hidden='true' data-evernote-id='115'%3e%3cpath fill-rule='evenodd' d='M2.81 5h1.98L3 14H1l1.81-9zm.36-2.7c0-.7.58-1.3 1.33-1.3.56 0 1.13.38 1.13 1.03 0 .75-.59 1.3-1.33 1.3-.58 0-1.13-.38-1.13-1.03z' data-evernote-id='1902' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)  Add italic text <ctrl+i>

   ![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-quote js-evernote-checked' viewBox='0 0 14 16' version='1.1' width='14' height='16' aria-hidden='true' data-evernote-id='116'%3e%3cpath fill-rule='evenodd' d='M6.16 3.5C3.73 5.06 2.55 6.67 2.55 9.36c.16-.05.3-.05.44-.05 1.27 0 2.5.86 2.5 2.41 0 1.61-1.03 2.61-2.5 2.61-1.9 0-2.99-1.52-2.99-4.25 0-3.8 1.75-6.53 5.02-8.42L6.16 3.5zm7 0c-2.43 1.56-3.61 3.17-3.61 5.86.16-.05.3-.05.44-.05 1.27 0 2.5.86 2.5 2.41 0 1.61-1.03 2.61-2.5 2.61-1.89 0-2.98-1.52-2.98-4.25 0-3.8 1.75-6.53 5.02-8.42l1.14 1.84h-.01z' data-evernote-id='1905' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)  Insert a quote    ![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-code js-evernote-checked' viewBox='0 0 14 16' version='1.1' width='14' height='16' aria-hidden='true' data-evernote-id='117'%3e%3cpath fill-rule='evenodd' d='M9.5 3L8 4.5 11.5 8 8 11.5 9.5 13 14 8 9.5 3zm-5 0L0 8l4.5 5L6 11.5 2.5 8 6 4.5 4.5 3z' data-evernote-id='1907' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)  Insert code    ![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='118'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1909' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)  Add a link <ctrl+k>

   ![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-list-unordered js-evernote-checked' viewBox='0 0 12 16' version='1.1' width='12' height='16' aria-hidden='true' data-evernote-id='119'%3e%3cpath fill-rule='evenodd' d='M2 13c0 .59 0 1-.59 1H.59C0 14 0 13.59 0 13c0-.59 0-1 .59-1h.81c.59 0 .59.41.59 1H2zm2.59-9h6.81c.59 0 .59-.41.59-1 0-.59 0-1-.59-1H4.59C4 2 4 2.41 4 3c0 .59 0 1 .59 1zM1.41 7H.59C0 7 0 7.41 0 8c0 .59 0 1 .59 1h.81c.59 0 .59-.41.59-1 0-.59 0-1-.59-1h.01zm0-5H.59C0 2 0 2.41 0 3c0 .59 0 1 .59 1h.81c.59 0 .59-.41.59-1 0-.59 0-1-.59-1h.01zm10 5H4.59C4 7 4 7.41 4 8c0 .59 0 1 .59 1h6.81c.59 0 .59-.41.59-1 0-.59 0-1-.59-1h.01zm0 5H4.59C4 12 4 12.41 4 13c0 .59 0 1 .59 1h6.81c.59 0 .59-.41.59-1 0-.59 0-1-.59-1h.01z' data-evernote-id='1912' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)  Add a bulleted list    ![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-list-ordered js-evernote-checked' viewBox='0 0 13 16' version='1.1' width='13' height='16' aria-hidden='true' data-evernote-id='120'%3e%3cpath fill-rule='evenodd' d='M12.01 13c0 .59 0 1-.59 1H4.6c-.59 0-.59-.41-.59-1 0-.59 0-1 .59-1h6.81c.59 0 .59.41.59 1h.01zM4.6 4h6.81C12 4 12 3.59 12 3c0-.59 0-1-.59-1H4.6c-.59 0-.59.41-.59 1 0 .59 0 1 .59 1zm6.81 3H4.6c-.59 0-.59.41-.59 1 0 .59 0 1 .59 1h6.81C12 9 12 8.59 12 8c0-.59 0-1-.59-1zm-9.4-6h-.72c-.3.19-.58.25-1.03.34V2h.75v2.14H.17V5h2.84v-.86h-1V1zm.392 8.12c-.129 0-.592.04-.802.07.53-.56 1.14-1.25 1.14-1.89C2.72 6.52 2.18 6 1.38 6c-.59 0-.97.2-1.38.64l.58.58c.19-.19.38-.38.64-.38.28 0 .48.16.48.52 0 .53-.77 1.2-1.7 2.06V10h3v-.88h-.598zm-.222 3.79v-.03c.44-.19.64-.47.64-.86 0-.7-.56-1.11-1.44-1.11-.48 0-.89.19-1.28.52l.55.64c.25-.2.44-.31.69-.31.27 0 .42.13.42.36 0 .27-.2.44-.86.44v.75c.83 0 .98.17.98.47 0 .25-.23.38-.58.38-.28 0-.56-.14-.81-.38l-.48.66c.3.36.77.56 1.41.56.83 0 1.53-.41 1.53-1.16 0-.5-.31-.81-.77-.94v.01z' data-evernote-id='1914' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)  Add a numbered list    ![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-tasklist js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='121'%3e%3cpath fill-rule='evenodd' d='M15.41 9H7.59C7 9 7 8.59 7 8c0-.59 0-1 .59-1h7.81c.59 0 .59.41.59 1 0 .59 0 1-.59 1h.01zM9.59 4C9 4 9 3.59 9 3c0-.59 0-1 .59-1h5.81c.59 0 .59.41.59 1 0 .59 0 1-.59 1H9.59zM0 3.91l1.41-1.3L3 4.2 7.09 0 8.5 1.41 3 6.91l-3-3zM7.59 12h7.81c.59 0 .59.41.59 1 0 .59 0 1-.59 1H7.59C7 14 7 13.59 7 13c0-.59 0-1 .59-1z' data-evernote-id='1916' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)  Add a task list

   ![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-mention js-evernote-checked' viewBox='0 0 14 16' version='1.1' width='14' height='16' aria-hidden='true' data-evernote-id='122'%3e%3cpath fill-rule='evenodd' d='M6.58 15c1.25 0 2.52-.31 3.56-.94l-.42-.94c-.84.52-1.89.83-3.03.83-3.23 0-5.64-2.08-5.64-5.72 0-4.37 3.23-7.18 6.58-7.18 3.45 0 5.22 2.19 5.22 5.2 0 2.39-1.34 3.86-2.5 3.86-1.05 0-1.36-.73-1.05-2.19l.73-3.75H8.98l-.11.72c-.41-.63-.94-.83-1.56-.83-2.19 0-3.66 2.39-3.66 4.38 0 1.67.94 2.61 2.3 2.61.84 0 1.67-.53 2.3-1.25.11.94.94 1.45 1.98 1.45 1.67 0 3.77-1.67 3.77-5C14 2.61 11.59 0 7.83 0 3.66 0 0 3.33 0 8.33 0 12.71 2.92 15 6.58 15zm-.31-5c-.73 0-1.36-.52-1.36-1.67 0-1.45.94-3.22 2.41-3.22.52 0 .84.2 1.25.83l-.52 3.02c-.63.73-1.25 1.05-1.78 1.05V10z' data-evernote-id='1919' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)  Directly mention a user or team    ![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-bookmark js-evernote-checked' viewBox='0 0 10 16' version='1.1' width='10' height='16' aria-hidden='true' data-evernote-id='123'%3e%3cpath fill-rule='evenodd' d='M9 0H1C.27 0 0 .27 0 1v15l5-3.09L10 16V1c0-.73-.27-1-1-1zm-.78 4.25L6.36 5.61l.72 2.16c.06.22-.02.28-.2.17L5 6.6 3.12 7.94c-.19.11-.25.05-.2-.17l.72-2.16-1.86-1.36c-.17-.16-.14-.23.09-.23l2.3-.03.7-2.16h.25l.7 2.16 2.3.03c.23 0 .27.08.09.23h.01z' data-evernote-id='1921' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)  Reference an issue or pull request

            Attach files by dragging & dropping, selecting or pasting them.       [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-markdown v-align-bottom js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='124'%3e%3cpath fill-rule='evenodd' d='M14.85 3H1.15C.52 3 0 3.52 0 4.15v7.69C0 12.48.52 13 1.15 13h13.69c.64 0 1.15-.52 1.15-1.15v-7.7C16 3.52 15.48 3 14.85 3zM9 11H7V8L5.5 9.92 4 8v3H2V5h2l1.5 2L7 5h2v6zm2.99.5L9.5 8H11V5h2v3h1.5l-2.51 3.5z' data-evernote-id='1952' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://guides.github.com/features/mastering-markdown/)  Styling with Markdown is supported