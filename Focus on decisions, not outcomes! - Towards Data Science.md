Focus on decisions, not outcomes! - Towards Data Science

# Focus on decisions, not outcomes!

## The terrible price that society pays for outcome bias

[ ![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='57' height='57' viewBox='0 0 57 57' data-evernote-id='273' class='js-evernote-checked'%3e%3cpath fill-rule='evenodd' clip-rule='evenodd' d='M28.5 1.2A27.45 27.45 0 0 0 4.06 15.82L3 15.27A28.65 28.65 0 0 1 28.5 0C39.64 0 49.29 6.2 54 15.27l-1.06.55A27.45 27.45 0 0 0 28.5 1.2zM4.06 41.18A27.45 27.45 0 0 0 28.5 55.8a27.45 27.45 0 0 0 24.44-14.62l1.06.55A28.65 28.65 0 0 1 28.5 57 28.65 28.65 0 0 1 3 41.73l1.06-.55z' data-evernote-id='274' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e) ![1*IL0mnvzNcpG2ZD0JBqo7zQ.jpeg](../_resources/bdd198bb8510e1e6545d3079c7910a2b.jpg)](https://towardsdatascience.com/@kozyrkov?source=post_page-----bf6e99cf5e4f----------------------)

[Cassie Kozyrkov](https://towardsdatascience.com/@kozyrkov?source=post_page-----bf6e99cf5e4f----------------------)

[May 17](https://towardsdatascience.com/focus-on-decisions-not-outcomes-bf6e99cf5e4f?source=post_page-----bf6e99cf5e4f----------------------) · 3 min read

[![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='29' height='29' class='bo js-evernote-checked' data-evernote-id='293'%3e%3cpath d='M22.05 7.54a4.47 4.47 0 0 0-3.3-1.46 4.53 4.53 0 0 0-4.53 4.53c0 .35.04.7.08 1.05A12.9 12.9 0 0 1 5 6.89a5.1 5.1 0 0 0-.65 2.26c.03 1.6.83 2.99 2.02 3.79a4.3 4.3 0 0 1-2.02-.57v.08a4.55 4.55 0 0 0 3.63 4.44c-.4.08-.8.13-1.21.16l-.81-.08a4.54 4.54 0 0 0 4.2 3.15 9.56 9.56 0 0 1-5.66 1.94l-1.05-.08c2 1.27 4.38 2.02 6.94 2.02 8.3 0 12.86-6.9 12.84-12.85.02-.24 0-.43 0-.65a8.68 8.68 0 0 0 2.26-2.34c-.82.38-1.7.62-2.6.72a4.37 4.37 0 0 0 1.95-2.51c-.84.53-1.81.9-2.83 1.13z' data-evernote-id='294' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://medium.com/p/bf6e99cf5e4f/share/twitter?source=post_actions_header---------------------------)

[![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='29' height='29' class='bo js-evernote-checked' data-evernote-id='302'%3e%3cpath d='M23.2 5H5.8a.8.8 0 0 0-.8.8V23.2c0 .44.35.8.8.8h9.3v-7.13h-2.38V13.9h2.38v-2.38c0-2.45 1.55-3.66 3.74-3.66 1.05 0 1.95.08 2.2.11v2.57h-1.5c-1.2 0-1.48.57-1.48 1.4v1.96h2.97l-.6 2.97h-2.37l.05 7.12h5.1a.8.8 0 0 0 .79-.8V5.8a.8.8 0 0 0-.8-.79' data-evernote-id='303' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://medium.com/p/bf6e99cf5e4f/share/facebook?source=post_actions_header---------------------------)

*(For added flavor, take *[*my quick quiz*](http://bit.ly/quaesita_outcomebias)* before you read on.)*

Learning is a good thing, but don’t learn the wrong lessons by misdiagnosing your mistakes. Sometimes, life throws you a random curveball you couldn’t have anticipated no matter your level of [decision](http://bit.ly/quaesita_di) genius. When that happens, adjusting your decision process is bad thinking.

Let me explain with an example.

Imagine that you’re about to observe the simultaneous flip of a fair coin and roll of a fair six-sided die. Before it happens, you are offered the choice between two gambles:

1. *Gamble on the coin, ignore the die: get $100 if it’s heads, nothing otherwise.*

2. *Gamble on the die, ignore the coin: get $100 if it’s a 6, nothing otherwise.*

Which do you choose?
![0*RrdaI7tuc_KJ-H6C.jpg](../_resources/1567cb068291b4477cfc44ae81013f05.jpg)
![0*RrdaI7tuc_KJ-H6C.jpg](../_resources/9dc57918a888d5dd268251c01f18259c.jpg)

Image: [SOURCE](https://pixabay.com/photos/dice-gambling-gold-pounds-game-4499089/)

The better decision appears to be the coin, which has a 1/2 chance of giving you money compared with the 1/6 chance on the die. Right? Right. If you’re motivated by the $100, it should be a no-brainer.

Now the action happens and we see the outcomes: the coin lands tails up while the die shows a 6. Dang, you should have chosen the die!

No. No, you shouldn’t have. Definitely not. That’s ***outcome bias*** and it’s a habit you should kick as soon as you can — especially if you have any hopes of being a good leader or decision-maker.

> Always evaluate decision quality based only on what was known at the time the decision was made.

If we look at outcomes, you got $0 when you could have had $100. Can we fix that? Nope, that decision is over. What should you learn from it? Nothing, I hope. Otherwise, you might choose a fair die instead of a fair coin next time. That would be a stupid choice if you like money. No matter how you slice it, 50% to win is a better gamble than 17% for the same prize.

# A menace to society

Perhaps more alarmingly, outcome bias threatens society’s ability to promote and retain competent leaders. Suppose the decision between betting on the coin and the die wasn’t yours to make. Instead, you watched [Heather](http://bit.ly/quaesita_heather) make it. Like Heather, you would have chosen the coin, but you’re not thinking about that. You’re too busy focusing on the bad outcome she got: tails+6 = missed opportunity for $100. If you’re outcome-biased, you’ll blame *her *for the outcome — forgetting that she made the decision wisely — and you’ll clamor for her to be replaced with another decision-maker who is doesn’t have bad outcomes to their name because:

- They’re less experienced than Heather, so they have a spotless track record.
- They’ve been lucky. (Look up [***survivorship bias***](https://twitter.com/quaesita/status/1233041495407636482) when you get a moment.)

Either way, you’ve just voted to shrink society’s pool of competent decision-makers, punishing Heather for randomness (***outcome***) when you should have celebrated her wise action in light of what she knew at the time (***decision***).

> Outcome bias exerts a terrible price on society.

Outcome bias exerts a terrible price on society. Our wise decision-makers are our best asset, yet many people are willing to sacrifice them as scapegoats when the real culprit is randomness. If you have reason to believe that someone’s decision process is top notch, don’t hold a bad outcome against them.

# ***Practical advice***

*When evaluating the skill of a decision-maker, ignore outcomes. Look only at what was known at the time of the decision. In our example, that was 50% versus 17% chance to win. The decision-maker chose 50%? Good. I hope they’ll choose the same way next time too.*

# Footnote

Outcome bias is not an argument about moral philosophy.*  *[*Here’s why.*](https://bit.ly/quaesita_consequentialism)

# Thanks for reading!

If you’re curious to learn about the role that outcome bias plays in perpetuating prejudice, check of the last section of my related article:

[ ## Are you a bad decision-maker?   ### The golden rule of decision analysis: avoid outcome bias    #### medium.com](https://medium.com/@kozyrkov/are-you-a-bad-decision-maker-34690deae223)