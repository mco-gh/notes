Interns with toasters: how I taught people about load balancers

## Interns with toasters: how I taught people about load balancers

Several years ago, I wrote a description of a problem that could happen in a large load-balanced environment. When it landed on certain web sites, some of the commenters dismissed either it ("impossible") or me ("doesn't know anything about load balancing"). Those are both wrong. I suspect what happened is that they didn't understand the problem, and so resorted to ineffective means to steer the attention away from their own inadequacies.

I've since come up with another way to tell the story of what happened. It was refined over many years of teaching new employees about outages. I will now attempt to present a sanitized version of it here.

One day, someone decided to chase down a weird pattern on a graph. There was a strange "quadruple-hump" figure in the pattern of failed requests to the site. First, they narrowed it down to a specific region, then a specific group of machines. Within that group, they tried to narrow it down more, and attempted to select it out by the load balancer reporting the problem. It didn't help: all of them were reporting it equally.

Next, they grouped the graph by the web servers which reported the failed requests. This also did not expose the quadruple-hump pattern which was desired, but there was another interesting thing which was then exposed. One of the web servers was reporting perhaps 200 times as many failed requests as every other one of its friends in that location.

The question I used to ask the class is: how can this happen? How can a big sophisticated operation have a single machine out of many become an outlier in this regard? What's going on?

It was at this point I asked them to roll with me, and imagine a scenario I would then describe. First, let's say that we get 100 interns to test this, because interns are great and you can use them to test anything. You tell them to report to a room much like the classroom, and have them line up and await further instructions.

Upon entering the room, they would find 100 small tables I had previously procured. Atop each table was a toaster, since I had gone out and bought every toaster I could find, by hitting Target, Walmart, CVS, and any other place that sells small appliances. Finally, I had the facilities team bring in a whole bunch of extra power feeds, because we were going to need a lot. We wanted to run all 100 toasters *at the same time*. That's a lot of juice!

So the interns come in, find their stations, and are waiting to find out what happens. They're chattering about what this could be for. That's the point when I enter the room carrying a massive bag of bread. I'm talking about something comically sized, like an oversized beach ball, and it's packed with slices of bread.

I go up to the first intern, and hand them two of the slices. They put them in their toaster, push it down, wait a minute or two, and ... hey, toast. (What did you think would happen at this point in the story? It's just a toaster. This isn't Harry Potter.)

Meanwhile, naturally, I had gone on to the second intern, who got their bread, and put it in their toaster, and the third, and the fourth, and the fifth, and so on down the line until everyone had bread.

At various points, a toaster would finish and would pop up. Toasters are all slightly different, so they wouldn't take the same amount of time. I'd notice that they were done and would run over to give them more toast. Oh, you're done! Have some more. Oh, you too! Here you go. Ready for more? Yep, here it is. Over here now. Gotcha. Oh and there? Okay!

This is how the load balancers work. The whole time (oh, you're done, have some more), they are constantly looking to see who's not busy (two more for you, got it) and then send more traffic that way. I'm the human load balancer in this thought experiment, handing bread to my friends the interns.

Trouble is, one of the interns wasn't playing by the rules.

Instead, they'd take the bread from me, and they'd look at it. "That's some nice bread", they'd think. They'd continue, "it would look even better *over there*", and they'd throw it away without even putting it anywhere near the toaster. Of course, I didn't notice this. I wasn't even watching for it.

But hey, I'd see they were ready for more, so I'd give them two more slices of bread. They'd take them, size them up again, and *foop* throw them away. The pile behind them grew.

This would go on over and over and over. It would go on forever if nothing stopped us.

This is what happened when one bad web server decided it was going to fail all of its requests, and would do so while incurring the absolute minimum amount of load on itself. Maybe it never even got the request anywhere near the normal processing guts. It became a failure machine, turning out those HTTP 500s just as fast as it was handed requests.

Because it never got backlogged or busy, and was always available for more work, the load balancers just kept sending traffic that way. In so doing, one machine out of a very large group managed to scarf down a substantial fraction of the traffic bound for that entire area.

I told my students the story this way because I wanted them to take it with them through their career, no matter where they ended up. Some day, if they see some problem with one widget out of thousands or millions "capturing" all of the traffic, maybe they'll remember me and my little story about interns and toasters.

Of course, when I taught that class, I was there in person, physically moving around to denote the size of the line of interns, picking spots in the audience to be intern #1, #2, #3, and so on, all the while "interrupting" myself to say "oh you're done, have another". (I did this above with parentheticals. Did you catch it?) When I got to the point about the one intern not playing by the rules, that's when I'd break out some props and start flinging pens or markers over my shoulder, making sure they audibly caromed off something (like the wall). It worked great. Students loved it.

I do miss giving those classes. But hey, there's a way forward from here. Maybe I'll start doing this stuff in the real world, bringing these lessons to life on stage somehow. Would people want to see that?