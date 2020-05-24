I just launched a free full-length Flexbox course where you can build projects interactively

# I just launched a free full-length Flexbox course where you can build projects interactively

Click the image to get to the course.

After the success of the [CSS Grid course I launched](https://medium.freecodecamp.org/heres-my-free-css-grid-course-merry-christmas-3826dd24f098) with freeCodeCamp in December (over 14,000 students so far!) I decided to launch a second free course.

This time you can learn Flexbox, which has become a must-have skill for front-end developers.

Flexbox was also one of the most frequent requests I got from students who took the CSS Grid course.

In this article I’ll explain how the Flexbox course is laid out, so that you can decide whether it’s a good fit for you.

But if you want to jump straight into the course immediately, you can just [go there directly and get started](https://scrimba.com/g/gflexbox).

![resize.jpg](../_resources/c6f6e9b9ba67588564fd597b7760211f.jpg)

### What my Flexbox course covers

The course consists of twelve interactive screencasts, which take you from beginner to advanced. It’s focused on giving you relevant skills as early as possible, meaning that I’ve prioritized the properties based on how useful I think they are in a real-world setting.

So if you only work through the five first, you’ll still learn new concepts you can start using in your projects. This said, I still recommend to working through the whole thing.

Throughout the course you’ll be building and experimenting with a navbar, since this is a very typical use case for Flexbox.

Let’s have a look at each of the screencasts:

#### Lesson #1: Your first Flexbox

![1*U9_BLWNTbc91G8zGb9kXFQ.png](../_resources/f682a960fc4bc983d4cff815f0b45dd0.png)
![1*rPzIll98F0gHToNeKZE3RQ.png](../_resources/05d1fd445e302a79672459809ee2531b.png)

You’ll start off by creating a simple layout. This will teach you the concept of a flex **container** and flex **items**, the two core ingredients of a Flexbox layout.

#### Lesson #2: Main axis and cross axis

![1*NVE8i0fzYR_lkztjmhgN5w.png](../_resources/e8c21039d87116f1707193ffe8d383d5.png)
![1*1z53nj8_eUtwkdyr6UEAfg.png](../_resources/17422fd3a6bdd45f5d5a4ce5ada07ca5.png)

In the second screencast, I explain a core concept of Flexbox that’s critical to understand early on: axes. A Flexbox layout has two axes: the main axis and the cross axis. By default, the main axis is horizontal and the cross axis vertical, but they can also flip roles.

#### Lesson #3: How to justify content

![1*bpDqaWA3uSwUtdXDKAwg6w.png](../_resources/2633fc5393ab2117d561c3d3f030d944.png)
![1*oX0mCKg4caqQE7X04CvIiw.png](../_resources/656e92c576bc21c316326babb0ea55f9.png)

The `justify-content` property controls the content along the main axis. Throughout the course, your main axis will be mostly horizontal, as opposed to vertical. I’ve chosen to do it this way as I’ve found horizontal Flexbox layouts to be more common than vertical ones in real life.

#### Lesson #4: How to position single items

![1*1z53nj8_eUtwkdyr6UEAfg.png](../_resources/f46b7bdd677341218e3326a73b2c52b9.png)
![1*TK1nvZSGCbi3EfQBwMQbgQ.png](../_resources/d69b54c61a9862de2963ee4b802ff954.png)

In this lesson, you’ll learn how to position single items using the good old technique of setting the `margin` to auto.

#### Lesson #5: The flex property

![1*rPzIll98F0gHToNeKZE3RQ.png](../_resources/2f0594de78b04de8461e9a7ba998af5b.png)
![1*gnO8ugL8stVg0ytPlTJNEQ.png](../_resources/a1f538e43f9bbeef3e8a78315c14c300.png)

The `flex` property allows you give your items responsive widths. It’s actually a shorthand for three other properties: `flex-grow`, `flex-shrink` and `flex-basis`. But we’ll save those for the end of the course, as they’re more advanced.

#### Lesson #6: How to align items

![1*oX0mCKg4caqQE7X04CvIiw.png](../_resources/1454fbc4d23baab03b694081b8000994.png)
![1*bpDqaWA3uSwUtdXDKAwg6w.png](../_resources/9e349b68a5f3006ba178075ecdc0550c.png)

The `align-items` property controls the items along the cross axis, which in our case is vertical. In the image above, we’ve centered the items along this axis.

#### Lesson #7: Flex direction column

![1*Xbb_jKfJ9rbXTeWqs89MRw.gif.jpg](../_resources/b1b086bd8ccd9ccc9d99f87bb7c50000.png)
![1*U9_BLWNTbc91G8zGb9kXFQ.png](../_resources/c04ab4404becc54d63a4323f5caae662.png)

Setting the `flex-direction` to column will flip the main axis and cross axis, so that the items are laid our downwards as opposed to sideways.

#### Lesson #8: Wrapping

![1*TK1nvZSGCbi3EfQBwMQbgQ.png](../_resources/cfa5e033fc86b38af5c86c284c81aee8.png)
![1*NVE8i0fzYR_lkztjmhgN5w.png](../_resources/46483bae2e3f612c8b4cb600f4833b2a.png)

By default, Flexbox won’t allow you to wrap your items, meaning they’ll stay on a single line or a row. If you set `flex-wrap` to wrap you’ll be able to, though. I’ll show how this would play out.

#### Lesson #9: Flex grow, shrink, and basis

![1*gnO8ugL8stVg0ytPlTJNEQ.png](../_resources/d28246386b277fd2f569704a25b9feb1.jpg)
![1*Xbb_jKfJ9rbXTeWqs89MRw.gif](../_resources/aca712514c18c77fc1564c48f98cbe99.gif)

Flex grow, shrink, and basis are a bit complex to understand, so this is the longest screencast in the course. In short, `flex-basis` sets the base width of the item, `flex-grow` controls how it’ll grow above it’s basis width, and `flex-shrink` controls how it’ll shrink when the item is narrower than its base width.

#### Lesson #10: Order

![1*CZikqoB4iZIIrV_rAW_qdg.gif.jpg](../_resources/f48e15a3cb7c71298e360659dfa7604a.png)
![1*hyzXwySi5-ep_j8rfCEi9A.png](../_resources/8cad070bdadf97ed006d07ecd3332614.png)

We’ll end the course with a lecture on the `order` property. This will introduce you to *source order independence*, which allows you to set the order of the items independently of how they’re laid out in the HTML.

#### Bonus section

In the bonus section you’ll create two real-world layouts from beginning to end.

In the first one you’ll take everything you’ve learned through the course and use it to create a navbar which adapts itself to various screen sizes.

![1*hyzXwySi5-ep_j8rfCEi9A.png](../_resources/70f0139bb1b23c9d5360ef207cb96e72.jpg)
![1*CZikqoB4iZIIrV_rAW_qdg.gif](../_resources/a3cbfb95542614cd70bb71b1b923fe73.gif)

In the second bonus lecture, you’ll experiment with creating an image grid with Flexbox. If you’ve taken my CSS Grid course, you’ll recognize the setup from there:

![1*e7EoeCwxU6RCPKsj72KkUg.png](../_resources/fe46a8bc35aa057151ebeb118cd487a2.png)
![1*e7EoeCwxU6RCPKsj72KkUg.png](../_resources/9d9423cfc18d4e6015381a6eaa3a5559.png)
And that’s all.

### The Scrimba format

Let’s also finally look at the technology behind the course. It’s built using Scrimba, an interactive coding screencast tool which has been built by my two awesome co-founders [Sindre](https://medium.com/@somebee) and [Magnus](https://medium.com/@judofyr).

Scrimba screencasts look like normal videos, but they’re fully interactive. You can edit the code inside the casts.

Here’s a gif which explains the concept: