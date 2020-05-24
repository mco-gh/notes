Hyperproductive development

### Hyperproductive development

**TL;DR: the most productive development happens when one person knows the system intimately because they wrote it; this is in conflict with growing a system beyond what one person maintains.**

Let's talk about why some developers, in some situations, are ten times more productive than others.

hint: it isn't the developers, so much as the situation.

When do we get that exhilarating feeling of hyperproductivity, when new features flow out of our fingertips? It happens when we know our tools like the back of our hands, and more crucially, when we know the systems we are changing. Know them intimately, like I know the contents of my backpack, when I packed it and I tuned the items in each pouch over years of travel. Know the contents of every module, both what they are and what we'd like them to be if we ever finish that refactoring. Know the edges, who uses every API and which changes will break whom, and we're friends with all of the stakeholders. Know the underpinnings, which database fields are indexed and which are obsolete and which have quirky special values. Know the infrastructure, where it runs in production and how to ssh in; where it runs in test and what version is deployed and when it is safe to push a new one. Know the output, what looks normal in the logs and what's a clue. We have scripts, one-liners that tail the logs in all three prod instances to our terminals so our magic eyes can spot the anomaly.

We know it because we wrote it, typically. It is extremely difficult to establish this level of intimacy with an existing system. [Braitenberg](https://mitpress.mit.edu/books/vehicles) calls this the Law of Downhill Invention, Uphill Analysis. Complex systems are *easier to build than to figure out after they're working*.

We know it because we are changing it. The system is alive in our head. It's a kind of symbiosis: we help the system run and grow, and the system works the way we wish. If we walk away for a month or two, begin a relationship with a different system, the magic is lost. It takes time to re-establish familiarity.

Except, I'm suspicious of this description. "We" is a plural pronoun. This depth of familiarity and comfort with a system is personal: it's usually one person. The one person who has conceived this solution, who holds in their head both the current state and where they are aiming.

If you are this person, please realize that *no one else experiences this work the way you do*. For other people, every change is scary, because they don't know what effect it will have. They spend hours forming theories about how a piece works, and then struggle to confirm this with experiment; they don't have the testing setup you do. They study every log message instead of skimming over the irrelevant ones, the ones you've skipped over so often you don't even see them anymore. By the time they do figure something out, you've changed it; they can't gain comprehension of the system as quickly as you can alter it. When they do make a change, they spend lots of time limiting the scope of it, because they don't know which changes will cause problems. They get it wrong, because they don't know the users personally; communication is hard.

If you are this person, please go easy on everyone else. You are a synthetic biologist and can alter the DNA of the system from within; they are xenosurgeons and have to cut in through the skin and try not to damage unfamiliar organs.

If you work with this person, I'm sorry. This is a tough position to be in, to always feel inferior and like you're breaking everything you touch. I'm there now, in some parts of our system. It's okay for me because the host symbiont, the author and manipulator of that software, is super nice and helpful. He doesn't expect me to work with it the same way he does.

If your team looks like this, here are some steps to take:

1. Consider: don't change it. This *really is* the fastest way to develop software. One person, coordinating with no other developers, can move faster than a whole team when the system is small enough. Until! we need the system to grow bigger. Or! the system is crucial to the business (it's an unacceptable risk for only one person to have power over it).

2. As the host symbiont who lives and breathes the system: strike the words "just", "easy," "obvious," "simple," and "straightforward" from your vocabulary. These words are contextual, and no other human shares your context.

3. Please write tests. Tests give people who are afraid of unintentional breakages a way to test their theories. Experimentation is crucial to learning how a system works, and tests make experiments possible. They also serve as documentation of intended behavior.

4. Pair program! By far the best way to transfer understanding of the system to another human is to change it together. (Or boost a whole team at once: mob program!)

5. Make a README for other developers. Describe the purpose of the system briefly, and document how you develop, test, and troubleshoot the system. Specify the command lines for running tests, for deployment, for accessing logs. Describe in detail how to obtain the necessary passwords. Write down all the environments where it runs, and the protocol around changing them.

6. Do you know your users better than anyone else? Remedy that. Bring other team members into the discussion. (There's [a sweet spot](http://blog.jessitron.com/2014/08/the-power-of-embedded-developers.html) of a single developer-type who works within a business unit. When the software becomes too important for this scale, it gets harder.) Let all the devs get to know the users. Have happy hours. Form redundant communication channels. It'll pay off in ways you never detect.

7. Slow down. Like seriously, if one person is developing at maximum speed on a project, no one else can get traction. You can't move at full speed and also add symbionts. When it is important to bring in new people, *don't do anything alone*. Pair on everything. Yes, this will slow you down. It will speed them up. Net, we'll still be slower than you working alone. This is an inherent property of the larger system, which now includes interhuman coordination. There's more overhead than when it was just you and your program. That's OK; it's a tradeoff for safety and scale from sheer speed.

Let's acknowledge that there really are developer+situations that are 10x more productive than others. Let's acknowledge that they don't scale. Make choices about when we can take advantage of the sweet spot of local or individual automation, and when the software we're building is too important for a [bus factor](https://en.wikipedia.org/wiki/Bus_factor) of one.

Distinguish between an experimental prototype, when speed of change and redirection is crucial, versus a production app which needs backwards compatibility guarantees and documentation and all that seriousness -- this requires a solid team.

Recognize that the most productive circumstance for development is a rare circumstance. Most of the time, I need to work on a system that someone else wrote. (that "someone else" could be "me, months or years ago.") The temptation to rewrite is strong, because if I rewrite it then I'll understand it.

There's a time for 10x development, and a time for team development. When you want to be serious, the 10x developer prevents this. If that's your situation, please consider the suggestions in this post.

Posted by[JessiTRON](https://www.blogger.com/profile/06220323006144102058)at[5:33 PM](http://blog.jessitron.com/2017/06/the-most-productive-circumstances-for.html)

[Email This](https://www.blogger.com/share-post.g?blogID=4534865332750558938&postID=3251743755291453260&target=email)[BlogThis!](https://www.blogger.com/share-post.g?blogID=4534865332750558938&postID=3251743755291453260&target=blog)[Share to Twitter](https://www.blogger.com/share-post.g?blogID=4534865332750558938&postID=3251743755291453260&target=twitter)[Share to Facebook](https://www.blogger.com/share-post.g?blogID=4534865332750558938&postID=3251743755291453260&target=facebook)[Share to Pinterest](https://www.blogger.com/share-post.g?blogID=4534865332750558938&postID=3251743755291453260&target=pinterest)

|     |
| --- |
| +29   Recommend this on Google |

Labels:[architecture](http://blog.jessitron.com/search/label/architecture),[complexity](http://blog.jessitron.com/search/label/complexity),[process](http://blog.jessitron.com/search/label/process),[systems](http://blog.jessitron.com/search/label/systems)