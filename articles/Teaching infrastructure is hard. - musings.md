Teaching infrastructure is hard. - musings

   [musings](https://glasnt.com/blog/)

- [Home](https://glasnt.com/blog/)

- [About](https://glasnt.com/blog/about)

- [Now](https://glasnt.com/blog/now)

- [Talks](http://glasnt.com/talks)

- [Archive](https://glasnt.com/blog/archive)

# Teaching infrastructure is hard.

 *Posted by Katie McLaughlin on November 1, 2019*

Teaching code is relatively straight forward (in comparison).

You can link out to setup docs for compilers on your system, show sample code blocks, make some basic assumptions about not having to explicitly tell people to copy this into that terminal, and you can get a majority of your learners to run your code and start to understand what you’re trying to convey.

Infrastructure, though, is harder.

It’s nigh impossible to show a sample implementation in production, unless your learning group is limited to a small handful of learners that also happen to be employed at the same company as you, with various security credentials, NDAs, and the like.

So, you need to show a way for your learners to create their own setup.

And you *could* use a local simulation, but this presents at least two problems: prior assumed knowledge and not-quite-production qualities. Telling someone it’s “just simple” to run a local Docker setup to run a composition command, you end up assuming that your learners even *know* what that is, why it’s useful, and how to take those learnings into their own environment. That container of a temporary ephemeral database does not map into how to use and maintain a production level database. And that simulation is never going to be exactly the same as the production level system: tasks and queues and pipelines and hardware are all going to be different and no simulation can directly copy every property.

And so, you demo live. You give the commands to build up the system in a real environment, just specifying that it may not be production ready because if you did, heck, there’s your startup right there. And you also want to cover your bases in case you missed something later. You know, like ACLs and authentication secrets.

But how do you show the provisioning of the system?
Well, you have a few choices. Each have their own pitfalls.

### Manual and tedious

You could take the time to take a screencast, screenshots, or like-real imagery to show all the URLs, all the checkboxes, and all the buttons the user needs to click to setup the widgets and connect them together and get a system using your web console.

But screenshots decay. Chances are by the time your tutorial is done, the next day your UX team finally lands those major changes and all your screenshots are out of date.

Screencasts in themselves have their own problems. They present accessibility concerns, and they are often hard to follow unless you have training in how to show and teach in a way that loses the least amount of followers. Your 480p YouTube screencast promotes rote learning and decays worse than screenshots, as you can’t easily splice those UI updates into a recording.

If you are fortunate enough to have a design team, you could spend the time to create a framework where you can make screens that look just enough like your environment that you can withstand minor changes in UX without too much trouble, but you ride the line of having your mock UX not being easily translated into the real UX, and losing more learners.

### Semi-manual and othering

Instead of using the web you could use that CLI that you have. It connects to the same API, mostly, and [at least it’s testable](https://dev.to/glasnt/testable-tutorials-5hfg). But then you have more issues.

You assume that your learners understand your CLI system. But that’s okay you have docs for that, how to install your CLI.

But then you assume that your learnings know what a CLI is and what it can do. And they’re using an environment that even supports your CLI on their operating system. And that they even have a terminal on their system to begin with.

And that your CLI even has feature parity with your web UI.

### Automatic and exclusionary

But that’s okay, instead you can just automate all of it. You can offer a series of arcane tomes and invocation rights to just have a configured system magically conjured into the learners environment. This is also known as provisioning automation, and it is othering.

If you chose to go down this route, you are going to have more learners than didn’t know a website, more learners that don’t get CLIs, just completely blank at what you’re offering them. Having to learn what Infrastructure As Code even *is* before getting started with documentation from these third-parties, that often make even more assumptions than normal. that learners even know how to call upon the powers contained within.

And that’s even if your system works with these technologies. Without a robust infrastructure creating the automations to make the automations for your infrastructure, this entire option is moot.

But even then, the flavour of conjuration you chose can exclude what few learners have followed you this far. Choose Terraform? You lose your Anisble techs. Choose Anisble and your Chef practitioners are looking for other resources. Choose Chef and your Terraform developers are already off at your competitors.

But that’s okay, you can just roll everything into a giant shell script that you strongly suggest, and give no other information to otherwise access, that users download and execute directly from your website, without ever looking at the contents the script and what it does. Because that never goes wrong. But worse, you’re not teaching anything, other than bad security practices.

## So what do?

Each methodology is as bad as the last, but there are ways to make your lessons as accessible as possible:

**Descriptive, scriptable commands as a middle ground**. Build a series of blocks of commands, surrounded with sans-serif meta commentary and explanations. Make the words the feature, and explain exactly what the commands are doing. Link out to every sort of resource you can think of if you can’t find the words, and roll back the major learnings back into your tome. From terminal basics to how to install whatever language requirements or tools are mandatory, explaining why these elements are needed. The result should be a page of prose with a series of executable blocks of code that can be [scraped](https://dev.to/glasnt/testable-tutorials-5hfg) for testing, but still followed by a novice.

**Plan to have learners come away with learning something, even if it’s not your system**. The series of tips, tricks, and ahas will provide value outside of learning *your* system. You can never except 100% conversion in any tutorial setup, but if your learners can learn *something*: a bash trick, a new term or concept, one neat new thing, they will have learnt something, and that’s the point, even if your product goes over their head.

**Have empathy that your learners aren’t you.** You have built the system. You have used the system for its entire existence. Your prior knowledge will be something that you can just assume. The more hints and tricks and references you include, the more chances you have to contain your audience. Experts can skip the basics and get to the meat. Novices can be guided through the experience. Anyone can learn something, and come away from your tutorial having learnt something, and know that if they need or want more in the future, they can come back.

* * *

- [← Previous Post](https://glasnt.com/blog/notes-from-devops-days-au-nz)

- [Next Post →](https://glasnt.com/blog/half-a-decade-of-public-speaking)

* * *

- [  **  **](https://glasnt.com/blog/feed.xml)

- [  **  **](https://twitter.com/glasnt)

- [  **  **](https://github.com/glasnt)