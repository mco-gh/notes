What Is Ray Kurzweil Up to at Google? Writing Your Emails

- Author: Tom Simonite[Tom Simonite](https://www.wired.com/author/tom-simonite)
- business
- 08.02.17
- 07:00 am

# What Is Ray Kurzweil Up to at Google? Writing Your Emails

![RK-TA.jpg](../_resources/2a66a1c4dd3c970954786c7f3c25cf44.jpg)

Ray Kurzweil speaking with Amy Kurzweil at SXSW on March 13, 2017 in Austin, TX.

**Katrina Barber/Getty Images

Ray Kurzweil has invented a few things in his time. In his teens, he built a computer that [composed classical music](https://www.youtube.com/watch?v=X4Neivqp2K4&feature=youtu.be&t=140), which won him an audience with President Lyndon B. Johnson. In his 20s, he pioneered software that could digitize printed text, and in his 30s he cofounded a synthesizer company with Stevie Wonder. More recently, he’s known for popularizing the idea of the [singularity](https://www.wired.com/2008/03/ff-kurzweil/)—a moment sometime in the future when superintelligent machines transform humanity—and making optimistic predictions about immortality. For now, though, Kurzweil, 69, leads a team of about 35 people at Google whose code helps you write emails.

His group powers Smart Reply, the feature on the Gmail mobile app that offers three suggested email replies for you to select with a tap. In May it rolled out to [all of the service’s](https://www.wired.com/2017/05/google-just-made-email-heckuva-lot-easier-deal/) English-speaking users, and last week was presented to Spanish speakers too. The responses may be short—“Let’s do Monday” “Yay! Awesome!” “La semana que viene”—but they sure can be useful. (A tip: You can edit them before sending.) “It’s a good example of artificial intelligence working hand in glove with human intelligence,” Kurzweil says.

And Kurzweil claims he’s just getting started. His team is experimenting with empowering Smart Reply to elaborate on its initial terse suggestions. Tapping a Continue button might cause “Sure I’d love to come to your party!” to expand to include, for example, “Can I bring something?” He likes the idea of having AI pitch in anytime you’re typing, a bit like an omnipresent, smarter version of Google’s search autocomplete. “You could have similar technology to help you compose documents or emails by giving you suggestions of how to complete your sentence,” Kurzweil says.

Looking further ahead—as Kurzweil likes to do—all those ideas are eventually supposed to seem rather small. Smart Reply, he says, is just the first visible part of the group’s main project: a system for understanding the meaning of language. Codenamed Kona, the effort is aiming for nothing less than creating software as linguistically fluent as you or me. “I would not say it’s at human levels, but I think we’ll get there,” he says. Should you believe him? It depends on whether you believe Kurzweil has cracked the mystery of how human intelligence works.

### Like Minds?

Google cofounder Larry Page oversaw some surprising initiatives during his second stint as the company's CEO, from 2011 to 2013, including a robot acquisition spree, a new division to [cure aging](https://www.wired.com/2013/09/google-page-calico/), and the ill-fated [Google Barge](https://www.wired.com/2013/11/googles-pretty-publicity-stunt/). Hiring Ray Kurzweil in 2012 arguably ranks among those head-scratchers.

The company already employed some of the most influential thinkers in machine learning and AI, and was rapidly expanding its roster of engineers building machine learning systems to power new products. Kurzweil was known for selling books predicting a weird future in which you’ll upload your consciousness into cyberspace, not for building AI systems for research or useful work today.

The way Kurzweil tells it, it was one of those books that got him in the door of the Googleplex. Page called him in to talk about ideas in the soon-to-be-published *How to Create a Mind*. The 2012 book lays out Kurzweil’s theory of the workings of the neocortex, the outer part of our brain and the seat of human intelligence. “He basically recruited me to bring this thesis to Google,” Kurzweil says. “I made the case that applying this model to machine learning would make it very good at understanding language.”

Kurzweil’s thesis is that the neocortex is built from many repeating units, each capable of recognizing patterns in information and stacked into a hierarchical structure. This, he says, allows many not-so-smart modules to collectively display the powers of abstraction and reasoning that distinguish human intelligence.

The model has yet to win universal acceptance among people who study the human brain. When cognitive science professor Gary Marcus [reviewed _How to Create a Mind](http://www.newyorker.com/books/page-turner/ray-kurzweils-dubious-new-theory-of-mind), he found the theory simultaneously unoriginal and light on empirical backing. Kurzweil, who says his book distills ideas about the brain that he has been developing since the age of 14, has a different view. “There’s really been an explosion of neuroscience evidence to support my thesis,” he says. He describes his hierarchical theory of intelligence as the guiding principle behind his group’s Kona system, and says it’s at work in Smart Reply.

### Starting Over

Although their code powers it today, Kurzweil’s group didn’t invent Smart Reply. It was first built by engineers and researchers from the Gmail product team and the Google Brain AI research lab.

They showed that artificial neural networks, which had revamped Google’s [image search and speech-recognition services](https://www.wired.com/2015/04/jeff-dean/), could also respond to emails if given enough examples to learn from. In late 2015 the system was [added to Inbox](https://www.wired.com/2016/03/google-inbox-auto-answers-emails/), Google’s [alternative mobile Gmail client](https://www.wired.com/2014/10/gmails-new-inbox-app/). About six months later, Smart Reply was being used for 10 percent of all emails sent with the Inbox app.

#### Related Stories

Kurzweil’s group got involved to help roll Smart Reply out to everybody using the regular, and much more popular, Gmail app. Google has a lot of computers but still has to pay electricity bills, and the original Smart Reply needed a lot of computing power. It used a type of neural network with a kind of short-term memory, giving it an awareness of the order in which words occur. The technology is good at understanding the meaning of sentences—it’s [at work in Google Translate](https://www.wired.com/2016/09/google-claims-ai-breakthrough-machine-translation/)—but it takes a lot of computational effort.

The Kurzweil-ized Smart Reply uses neural networks too, but they are unconcerned with the order of words, and thus are much cheaper to run. It crunches the words in an email’s body or subject line into numbers, all in one go. And it has multiple neural networks stacked into a two-layer hierarchy. The bottom level digests text from emails and the top layer synthesizes the results to select the most appropriate replies from a list of 29,000 prewritten options, generated by analyzing the most common phrases written by Gmail users. In a [paper](https://arxiv.org/abs/1705.00652) released in May, Kurzweil and his colleagues reported that their system offers replies just as popular with users for a fraction of the computational work.

### Much to Prove

Smart Reply may be impressive, but Kurzweil’s team still has miles to go before it can prove their ideas really make software much better at understanding language.

Yoav Goldberg, who researches natural language processing at Bar Ilan University in Tel Aviv, says Google’s paper on the new Smart Reply system describes a solid piece of engineering rather than a scientific breakthrough. It’s the kind of thing a company like Google needs to do day in, day out, if it’s to make good on its ambition to deploy machine learning everywhere. “For most problems, what we need is a well-engineered solution using established techniques and not a novel breakthrough approach,” Goldberg says.

The validity of Kurzweil’s analogy between his team’s system and the brain is less clear. Sure, there’s a hierarchy of similar components that boil input data into more abstract representations used to make a decision. But you could describe any machine learning system built with artificial neural networks that way, and none made yet is really very brain-like. “I find the analogy so loose that it is practically meaningless,” Goldberg says.

Meanwhile, Kurzweil is calmy, monotonously confident of being proven right. “It’s not using the same mathematics, but it’s the same concept I believe makes the neocortex work,” he says. “And it does capture the meaning of language based on our tests.” More applications of Kona are in the works and will surface in future Google products, he promises. And when asked to look further ahead, he casually tosses out a provocative prognostication. “My consistent prediction, going back a couple of decades, has been that in 2029 computers will understand language at human levels,” he says. If it comes to that, Kurzweil’s code will be doing a lot more than just writing emails.

####  Related Video

Culture

##### Ray Kurzweil & Steve Aoki Talk Technology, the Future & Humanity

Steve Aoki talks with famed futurist Ray Kurzweil about how technology will shape our future, in terms of creativity, consciousness, and the coming singularity.

- [#ray kurzweil](https://www.wired.com/tag/ray-kurzweil/)
- [#singularity](https://www.wired.com/tag/singularity/)
- [#google](https://www.wired.com/tag/google/)
- [#gmail](https://www.wired.com/tag/gmail/)