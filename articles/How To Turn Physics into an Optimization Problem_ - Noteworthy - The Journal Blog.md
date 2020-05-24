How To Turn Physics into an Optimization Problem? - Noteworthy - The Journal Blog

# How To Turn Physics into an Optimization Problem?

[![2*UBGeW9Ot2tJIjlyTPVV1YQ.png](../_resources/aa4f21d9c15fc21421967f8fc84bd7f0.png)](https://blog.usejournal.com/@marksaroufim?source=post_page-----11b3fbf83062----------------------)

[Mark Saroufim](https://blog.usejournal.com/@marksaroufim?source=post_page-----11b3fbf83062----------------------)

[Nov 5](https://blog.usejournal.com/how-to-turn-physics-into-an-optimization-problem-11b3fbf83062?source=post_page-----11b3fbf83062----------------------) · 11 min read

If you know the basics of Machine Learning you already know how to solve a large body of physics problems without realizing it.

This post is mostly about a tool called Lagrangian Mechanics which lets you solve physical problems like an optimization problem.

> In Machine Learning you minimize the loss between the prediction and the label to find the best predictor

> In Lagrangian Mechanics you minimize the total action of a system to find its motion

# Representation Matters

Lagrangian Mechanics has a huge benefit over traditional Newtonian Mechanics in that it’s representation invariant which means you have the freedom to choose the easiest representation to work with.

As an example we’ll discuss the simplest kind of robot, a 2-d pendulum — each of your limbs is a pendulum and your body is made up of a bunch of pendulums.

![1*3h8VXKLp-1NHysliHgUFSg.gif](../_resources/ddc16bca71d1179570766d2bded4a6cd.png)
![1*oa-_eiagcBQlwZMTZVVxeQ.png](../_resources/4e75dbd0d032a711f966fb58699bac1a.png)

What we’re interested in this case is describing the motion of the center of the mass at the end of the string so at every time t we need to find 3 variables

1. p → position of the mass
2. v → velocity of the mass
3. a → acceleration of the mass
v is the rate of change of p over time
a is the rate of change of v over time
![1*dDRfwPQKb0rOtbiJf_uedw.png](../_resources/e917c624f1143b70aecfe9d144cab34b.jpg)
![1*htSToWCVOSC67ul13Dq9OA.gif](../_resources/28988f08bb221c3ae332560800e67625.gif)
So we really just need to predict a single variable p.
p is a sequence of positions of a body from a starting time s to a final time
![1*VFXsc3B-ijy7sVDv95PnfA.gif](../_resources/d15f7b5e2686e186f5b9e25c282b5007.jpg)
![1*3h8VXKLp-1NHysliHgUFSg.gif](../_resources/f08cd628c632d0f200c14d032fd53d07.gif)

But how exactly do we go about representing the position of the center of the mass exactly? The obvious first choice is to use Cartesian coordinates x, y.

![1*tJh54POqYVLdYib7i3irIw.png](../_resources/4860f6ce693ea6bea9744db7495fc459.png)
![1*tJh54POqYVLdYib7i3irIw.png](../_resources/a07b15d19a74225262f9fdab73931add.png)

But now we’re faced with a dilemma — should we center coordinates on the ball itself, the wall, someplace else? Is there any principled way of deciding which coordinate is better?

An alternate representation we could use for the pendulum is:
![1*yQgQXmKGrmFmhCV7FNXpDw.png](../_resources/c2fa2849382175142dc3149ba73a5be8.png)
![1*yQgQXmKGrmFmhCV7FNXpDw.png](../_resources/086d86a68b488b0e1522c8276afeaab8.png)
We can fully characterize all the possible positions of the pendulum

- θ → angle between the ceiling and the rope
- l → length of the rope

Taken together you just end up with the polar coordinates.

The Polar and Cartesian representations are isomorphic (same mathematically) but polar has more advantages in this case.

![1*w6YahCcwLqucUoO0ggwVyQ.gif](../_resources/32e82c6ffe2e01b8551817e3058bf84b.jpg)
![1*11MbobfHe7wSkExtRNvA7A.gif](../_resources/144a02c542a265e262ce6f7fc472f980.gif)
![1*WsvUmtdKsytvgFNL5fIP4w.png](../_resources/cb4f2ade07cbd6c806bfac5162ee9717.jpg)
![1*eqLR-gV_PDVV1BnC6NNGfg.gif](../_resources/f2f13a598d007d692abe2b364add6a96.gif)

l never changes through the evolution of the system so effectively we can describe the motion of this entire system using only 1 variable θ instead of 2 variables x and y.

# Configuration spaces

One major reason that the θ representation is better is because if we’re trying from time t to predict the position of the ball at time t + 1 there are only 3 possible solutions

![1*w6YahCcwLqucUoO0ggwVyQ.gif](../_resources/5193b29716a4e00008a7d953ebd0a733.jpg)
![1*79gyiRuU-u0cQsLlnJ7Ozw.gif](../_resources/e5712c8aa95caa2a7e174970d88e1eb4.gif)

In the Cartesian setting, the solution lies somewhere on the x, y plane but there infinitely many possible directions from time t to t + 1.

![1*LwA7BCikZy4p7i9s_8kG4w.png](../_resources/5602c560cd1051ab151038896a9ed2c7.png)
![1*LwA7BCikZy4p7i9s_8kG4w.png](../_resources/e994b08155a39ee07506c5bd747e2750.png)
But in the Polar setting, the solution can only go in one of two directions.
![1*u6RMscAhvCGa4f0ViF6Swg.png](../_resources/1e92fcb3ee6794f185e49d22fd6c3ca8.png)
![1*u6RMscAhvCGa4f0ViF6Swg.png](../_resources/1f7deb31eed29a96ce4b67692523a5ca.png)

> The circle is the **> configuration space**>  as in the set of all realizable solutions to the pendulum problem and the specific path the particle takes via this space describes its actual movement and is called the **> configuration path**> .

Studying the “shapes” of systems in this manner is part of larger field called Topology. Topology is tremendously useful to study the motion of physical systems so here’s a taste of it.

Let’s take a more complex system, a double pendulum — imagine the first ball as your elbow and you can see how this represents something a bit more interesting, namely your arm.

![1*QSvK2FYOW3GcyeE6aYcVnA.png](../_resources/d5d4044d891590f7893984bd62de0110.png)
![1*QSvK2FYOW3GcyeE6aYcVnA.png](../_resources/47da5e132d7e28c963ceeda5067800fc.png)
You can describe this system via two angles
![1*4-EAOwCj0DK93lxu3aQF2g.gif](../_resources/d82f158df80827f4f15b669f084dc3e7.jpg)
![1*NpF1db56c3RjHtpWsjWR_g.gif](../_resources/fbb589683c10d4e3ca1ff94bc183a9d5.gif)

If you fix the first angle then configuration space of the second angle is again a circle so the new space for both angles would look like.

![1*nEqluhj-l_5hEGebFVhKWg.png](../_resources/595865c5130211c8b28a6bfde4c3c845.png)
![1*nEqluhj-l_5hEGebFVhKWg.png](../_resources/de1464c232d3b95faf55bcb4d9ac3178.png)

And since there’s infinitely many small circles on top of the larger one the shape we end up with is the famous torus (donut) from topology.

![1*qIM4f4ffVr97MEjqrwC0Rg.png](../_resources/0ad0bde312b7369814b4c4a97607eb29.png)
![1*qIM4f4ffVr97MEjqrwC0Rg.png](../_resources/10ea12aec83053c857143dcb38b4a992.png)

Each point on this 3-d object represents a possible solution to where the double pendulum can be. We’re essentially characterizing the solution of this system as a space.

The actual motion of an example pendulum is then described by a path on this torus.

![1*vpyeevMYT2pnIYFlxodI_g.png](../_resources/9adb792c6c85c23d743042a101d49ac2.png)
![1*vpyeevMYT2pnIYFlxodI_g.png](../_resources/9b797acd4b47c790e67c19be6dff5cc5.png)

If you work with Newtonian Mechanics and need to change your representation to see what works best you need to re-derive all your formulas which when you go into the double pendulum realm involves some tricky trigonometry.

The Lagrangian L on the other hand is representation independent which means.
![1*jSdWpoeOgupsMLsYzhLa6Q.gif](../_resources/3ee36db02d791c4e363890214c386e5d.jpg)
![1*BKxw93T9gybTG55wD2LF1A.gif](../_resources/1cabccb1141f0b5b6317f063ec3b6d80.gif)
Now let’s define what the Lagrangian is and see how it works.

# Lagrangian

Now we know that we can describe the motion of a system using a path but which path will a system actually take in its configuration space?

> Nature is lazy
All physical processes take the path that minimizes **total action**.

A famous example is refraction where the light bends because it’s faster for it to do so.

![1*IhXKOWkkvmCqu0BvJwMY8Q.gif](../_resources/4e65d4924533a7e81619d9957ca309fc.png)
![1*WsvUmtdKsytvgFNL5fIP4w.png](../_resources/d9b2b3c35c640d82d455db09d6b347be.png)

The Lagrangian of a system L can be understood as its “liveliness”. It’s defined formally as

![1*-CtnHTDgs-0V9yl5aMw-OQ.gif](../_resources/4b72339ce941522288a2e90d41c6211c.jpg)
![1*MfglxTpfTLkmByCG_CLX-g.gif](../_resources/43b904fb039ca39d6f444a84260f3af6.gif)
where T is the kinetic energy and V is the potential energy.
The kinetic energy T is always the same
![1*t6YuH_lRXZTBtL-n2qejBw.gif](../_resources/23884d1b1a3fb6eabaa43bc932b80eec.jpg)
![1*rQi_sl7OJqRPmPUQ2tocqw.gif](../_resources/f410185c7dfe805b82291b6a3581c264.gif)

And the potential energy depends on the type of system being described but for us we’ll mostly be looking at gravitational potential

![1*oa-_eiagcBQlwZMTZVVxeQ.png](../_resources/2c026f261ad303699903069264f60a3b.jpg)
![1*6TJV6RqkI7TehS-j5FzsJg.gif](../_resources/839703d6a5fbcce1e00499dd339f0963.gif)
where
m → mass of object
g → gravitational constant
h → height from ground

The more famous conservation of energy law takes the sum of potential and kinetic energy and it’s been tremendously reliable in pruning out bad physics theories.

![1*eqLR-gV_PDVV1BnC6NNGfg.gif](../_resources/761b90266337c5084da3c76ba2f093bd.jpg)
![1*htSToWCVOSC67ul13Dq9OA.gif](../_resources/f299eb942ab4286d1f11251cece99ff8.gif)

What the conservation of energy law tells us is that no new energy can be created and no energy can be lost. Instead we have a trade-off where if T increases then V decreases and if T decreases then V increases.

![1*5ankPECGcVeZ3RBQt5HgIg.png](../_resources/392c061db5a935d97302c73936a85101.png)
![1*5ankPECGcVeZ3RBQt5HgIg.png](../_resources/cce58c3b7431ce4619ad9e659113acf4.png)

The total action generated by a system is denoted S and can be calculated by summing up all the Lagrangian of each position the configuration space.

![1*EHX18BKbI1TatsWhPjATmg.gif](../_resources/e294cc462d7f156ca475e87287c4d2a9.jpg)
![1*xAE_PCuMpK_fsMsICv_BUw.gif](../_resources/abaf8be6eaa691c8bad41944d87c9672.gif)

# Euler-Lagrange Equation

So now that we can derive the Lagrangian L of any system, how do we get the minimum S and the path that generates it.

> The transition from Lagrangian to a solution is done via the Euler-Lagrange equation which will find the **> path of least action**> .

The Euler-Lagrange equation is
![1*9swS-HP4-KYb6EyfueEPFw.gif](../_resources/ccb86bf07a97b5fe80eceaf0853a7f8a.jpg)
![1*-CtnHTDgs-0V9yl5aMw-OQ.gif](../_resources/8fc5beeda8e5ba954c504d34aafe717a.gif)

The formula looks more complicated than it actually is and it’s best understood via a couple of examples.

**Falling Ball**

Both of my examples are heavily inspired by [this series](https://www.youtube.com/watch?v=pVVMNsidI0g&t=156s)

Suppose we have a ball of mass m falling to the ground
![1*plFACpN9UInwb-Aa26ebaA.gif](../_resources/f0cc1aad182725f0385abd20187726ef.png)
![1*-SDPC5qF7NVgo8MXoBvsGQ.png](../_resources/a994ad2ed1b711ead2d06b2a90494283.png)

The kinetic energy T is only a function of y because there is no sideways movement

![1*gBbmpT80UhAIG5tP0iaOGw.gif](../_resources/d306714999f9c5586a9b7e0098d5bfc4.jpg)
![1*t6YuH_lRXZTBtL-n2qejBw.gif](../_resources/f00a7bcf48438feb9e78a927079cd1cf.gif)
The potential energy V is
![1*1yGoji_ULCFVA0ea4MJ2_Q.gif](../_resources/86d195e34b9a6b1fc911c4a2916713c9.jpg)
![1*jSdWpoeOgupsMLsYzhLa6Q.gif](../_resources/18dfb181aec74e0aef52da9e4a9cf643.gif)
So the Lagrangian is
![1*HIbj0UPlh1QdKHZieip6mQ.gif](../_resources/f66b80d1ce7d9e06d9e2e37ada73ce31.jpg)
![1*plFACpN9UInwb-Aa26ebaA.gif](../_resources/15f351fd8016d6bc85f07d7fbd18611e.gif)
The Euler Lagrange equation will only be a function of y so we can simplify it
![1*NpF1db56c3RjHtpWsjWR_g.gif](../_resources/4d5880d21f317993852094628c609042.jpg)
![1*NedeFdc513o1GYqqOTbzWg.gif](../_resources/9d6840eacc24171de9bad6a3472ebde8.gif)
Plugging in L
![1*BKxw93T9gybTG55wD2LF1A.gif](../_resources/2cb4f6dd82e1eccf2a711a2284dba3e5.jpg)
![1*VFXsc3B-ijy7sVDv95PnfA.gif](../_resources/f17303e32227063eb153dbfc706c9d61.gif)
Which simplifies to
![1*11MbobfHe7wSkExtRNvA7A.gif](../_resources/699b31e3167f7934e931211a377a65fc.jpg)
![1*vzRUMAfx6Vx-JaAQZnlAaw.gif](../_resources/efbed4b7e33ab555d51a206fda32d969.gif)
So we end up with deriving Newton’s law from scratch
![1*NedeFdc513o1GYqqOTbzWg.gif](../_resources/94483f1ae1170b01ae3a91ce4a0bc844.jpg)
![1*vzRUMAfx6Vx-JaAQZnlAaw.gif](../_resources/e647320376fea2ce53d9c331785a2215.gif)

# Moving Cart Pendulum

The last example was to show you how Lagrangian Mechanics works but it’s not an example where Lagrangian Mechanics shines.

> Lagrangian Mechanics shines when the system is complex with many variables that would be painfully difficult to model with Newtonian Mechanics.

So we’re going to instead imagine that we have some sort of moving cart with mass M with a dangling pendulum of mass m. My head hurts thinking about the number of different forces I need to model here.

![1*MfglxTpfTLkmByCG_CLX-g.gif](../_resources/8b80ba7ac74f6f07378eb93e7ea3ad04.png)
![1*aBhvfgKIvXmwAVTPDbXz1A.png](../_resources/caef0d1425a099894af655a15ba0fde7.png)

Thankfully Lagrangian makes solving this system far easier since we can just sum up each objects Lagrangian independently.

![1*1yGoji_ULCFVA0ea4MJ2_Q.gif](../_resources/afc940eb8e07664abd25fd1c67da1274.jpg)
![1*igr9CvxuIDJnvwWYSCzpKA.gif](../_resources/61d7227d8205248bf9d8d799ef6be10f.gif)

We can model the position of the cart and ball with 2 variables each for a total of 4 or we can use a trick where we change the coordinate system to make our lives easier.

We make the following 2 substitutions
![1*9Y12-75lUPxZj4PtN8Yf9g.gif](../_resources/cf8d574930e38bebc5c094e910913400.jpg)
![1*aBhvfgKIvXmwAVTPDbXz1A.png](../_resources/74319d2c535b387875754d09c9b1d9df.gif)
![1*TEEr9trqhV2De93GBtsWWg.gif](../_resources/6358be7c9987d547409faa23ed6b47ac.jpg)
![1*igr9CvxuIDJnvwWYSCzpKA.gif](../_resources/3a8543b06fde629d24245d4dc477f79c.gif)
With this change of variable in place we can derive the Lagrangian L.
> Remember, nature doesn't’ care about how we represent it

Kinetic energy is easy. The cart only moves in the x direction and the pendulum can move both in the x and y direction.

![1*9swS-HP4-KYb6EyfueEPFw.gif](../_resources/6f54260c983b60ae8740ae9f7f62b984.jpg)
![1*79gyiRuU-u0cQsLlnJ7Ozw.gif](../_resources/7e52617e3cc9606d10df3b0cd4b786a8.gif)
Potential energy
![1*EHX18BKbI1TatsWhPjATmg.gif](../_resources/974953e9b964f47886c1a01e927ddee1.jpg)
![1*IhXKOWkkvmCqu0BvJwMY8Q.gif](../_resources/c5c4f98b79c70190622543b115ec998f.gif)
So the total Lagrangian is
![1*xAE_PCuMpK_fsMsICv_BUw.gif](../_resources/859977a2a42d9a7efafe8451e3172983.jpg)
![1*9Y12-75lUPxZj4PtN8Yf9g.gif](../_resources/7ec1e949f42005eb6613293ece5d4364.gif)

Once you have L you can just apply the Euler Lagrange equation to see how this system behaves.

Contrast this approach to the Newtonian Mechanics one where

1. Create a force diagram between each object and every other one to create a set of equations — potentially exponentially many

2. Plug those equations into an ODE solver since most derivatives in physics have no closed form solution — and pray

> The difference between Newtonian Mechanics and Lagrangian Mechanics is the difference between imperative and declarative programming. An efficient declarative paradigm like Lagrangian Mechanics will always be preferable in the same that SQL is preferred over UNIX scripting.

# Modeling constraints

A final advantage of Lagrangian mechanics that I want to briefly touch on is that it’s trivial to add constraints to a system.

A constraint is some function that f such that
![1*TEEr9trqhV2De93GBtsWWg.gif](../_resources/1a2397e65d4c86db45f97c8b98213fe9.jpg)
![1*gBbmpT80UhAIG5tP0iaOGw.gif](../_resources/437a0b1c0025968e13332ca0401a4e45.gif)

f could be a constraint on the max velocity or it could be a constraint on how far a joint can bend or it can be a constraint on how soft the collision of two objects should be.

You can have as many constraints as you want
![1*-SDPC5qF7NVgo8MXoBvsGQ.png](../_resources/7af9b159e376a8a6bf682063a25faed3.jpg)
![1*4-EAOwCj0DK93lxu3aQF2g.gif](../_resources/2144758c05a176152995dcb75069ec6f.gif)

And all you need to is instead of plugging L into the Euler Lagrange equation you would plug in where λ’s are weights for how important each constraint is. This trick is called “Lagrangian Multipliers” and is used extensively in convex optimization.

![1*HIbj0UPlh1QdKHZieip6mQ.gif](../_resources/df369962f476399158d57c1a28d6853a.jpg)
![1*6TJV6RqkI7TehS-j5FzsJg.gif](../_resources/9d21687924d5fe710a0b9ef982c9ce3e.gif)

# Code

Even though Lagrangian Mechanics is a powerful idea that lets you heavily simplify implementing physics engines, as far as I know it’s not a mainstream idea yet. If you do know of any physics engines that do use it, please let me know and I’ll describe how it works in a real physics engine in a future blog post.

The first time I saw an full implementation of Lagrangian Mechanics was in the fantastic book — [Structure and Interpretation of Classical Mechanics](https://amzn.to/2PQ2h2a). The implementation here is in LISP which is a great language to learn but in my experience a tough language to use on larger projects.

So instead I’d recommend taking a look at the project https://github.com/MasonProtter/Symbolics.jl which offers a Julia implementation heavily inspired by the SICM implementation.

The README specifically talks about the harmonic oscillator which is just a fancy term for a weight attached to a spring.

![1*rQi_sl7OJqRPmPUQ2tocqw.gif](../_resources/228e4a12cf8ac6b4e49fe936d275ce70.png)
![1*dDRfwPQKb0rOtbiJf_uedw.png](../_resources/2ebe93086904a377355ed56ebcebc3e2.png)