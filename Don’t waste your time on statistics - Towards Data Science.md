Don’t waste your time on statistics - Towards Data Science

# Don’t waste your time on statistics

[ ![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='57' height='57' viewBox='0 0 57 57' data-evernote-id='182' class='js-evernote-checked'%3e%3cpath fill-rule='evenodd' clip-rule='evenodd' d='M28.5 1.2A27.45 27.45 0 0 0 4.06 15.82L3 15.27A28.65 28.65 0 0 1 28.5 0C39.64 0 49.29 6.2 54 15.27l-1.06.55A27.45 27.45 0 0 0 28.5 1.2zM4.06 41.18A27.45 27.45 0 0 0 28.5 55.8a27.45 27.45 0 0 0 24.44-14.62l1.06.55A28.65 28.65 0 0 1 28.5 57 28.65 28.65 0 0 1 3 41.73l1.06-.55z' data-evernote-id='183' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e) ![1*IL0mnvzNcpG2ZD0JBqo7zQ.jpeg](../_resources/bdd198bb8510e1e6545d3079c7910a2b.jpg)](https://towardsdatascience.com/@kozyrkov?source=post_page-----8163635da56c----------------------)

[Cassie Kozyrkov](https://towardsdatascience.com/@kozyrkov?source=post_page-----8163635da56c----------------------)

[May 29, 2018](https://towardsdatascience.com/whats-the-point-of-statistics-8163635da56c?source=post_page-----8163635da56c----------------------) · 3 min read

I recently discovered that a dear friend of mine managed to earn a PhD in [statistics](http://bit.ly/quaesita_statistics) without ever having asked himself this question: *what’s the point of statistics, anyway?* Oh, dear. If you don’t know what it’s for, you also don’t know when it’s not for you. Turns out professors don’t make this obvious, so let me see if I can help.

![1*GJkO3eM8h79TJaICi8y_sw.jpeg](../_resources/081a88c41488d0917bd17d25b2534ac2.jpg)

[***Statistics*  **is the science of changing your mind under uncertainty](http://bit.ly/quaesita_statistics). What might your mind be set to? A [***default action***](http://bit.ly/quaesita_damnedlies) or a ***prior belief***. But what should you do if your mind isn’t set? What if you have no opinions whatsoever?

Just go with your estimate (that’s just a fancy way of saying “best guess based on what you know”). How do you get one? Just look at the data and report what’s there. This is called [analytics](http://bit.ly/quaesita_datasci) (a.k.a. data-mining) and if you’ve ever used a spreadsheet, you’ve already done it. The good news is that your gut is actually pretty good at giving you the right estimate. No need for complex mathemagics.

“But it could be wrong!” Of course it could be wrong, that’s what it means to be uncertain. There’s no mathemagic in the world that can make certainty out of uncertainty. Your best guess might be a mistake, but it is your *best *guess, which makes any other guess a worse guess and even more likely to be wrong.

So just go with your gut, it doesn’t even matter how much data you have!
“Wait, but I need to know if I have enough data!” Mmmm? Enough for what?

Pause for a moment and imagine you’re choosing between blue and orange hats. If you are truly indifferent between them and the data stack up in favor of orange, you’d be insane to end up with blue. Even you only had 3 data points total. Even if it’s only 0.0000000000001% in favor of orange. By what madness did you get blue?! Go with orange, no math required.

![1*dI9a1zzjHwfW5spudK9-Ag.png](../_resources/526da5f1c90273f08f6a85a8c7c738b8.png)
![1*dI9a1zzjHwfW5spudK9-Ag.png](../_resources/89292244851e0d8935adabb74b059cde.png)

If you’re indifferent between these hats to begin with and you get more votes for orange than blue, there’s no math in the world that should tell you to pick blue. Math isn’t magic and it doesn’t violate common sense.

The only way it makes sense to end up choosing blue is if you had a preference for the blue hat to begin with. Then you’re asking whether the evidence in favor of orange is strong enough. In other words, whether there’s enough data to change your mind. Okay, so how can you tell? Welcome to [statistics](http://bit.ly/quaesita_statistics).

![1*YGiMaGU8xq1xS3hp6IFXCg.png](../_resources/04c83ef113a9edd7794cffe55722e1f9.png)
![1*YGiMaGU8xq1xS3hp6IFXCg.png](../_resources/2cd64743a7f7be9910f9220b56fb1ecb.png)

In the top half of the table, the evidence doesn’t contradict your starting preference, there’s no need for statistical calculations. You can make your decision immediately. If your evidence is out of line with your preference, you can use statistical calculations to find out whether the evidence should make you want to change your mind.

> Statistics is the science of changing your mind.

So if you’re dealing with uncertainty (e.g. “Will this machine learning system work on tomorrow’s data?”) and the options aren’t each alike in dignity (e.g. “We probably shouldn’t launch it unless it works.”) then you’ve come to the right place: statistics is for you. [Zoom through its main ideas here](http://bit.ly/quaesita_statistics). Everyone else, flee now before you end up crunching a bunch of numbers meticulously… and uselessly. [Analytics](http://bit.ly/quaesita_analysts) is a better option for you.