The Pitfalls of Boolean Trap

# The Pitfalls of Boolean Trap

[Aug 24, 2011](https://ariya.io/2011/08/hall-of-api-shame-boolean-trap)  · 7 min read  · [#api](https://ariya.io/tags/api/)  [#javascript](https://ariya.io/tags/javascript/)  [#musing](https://ariya.io/tags/musing/)  [#qt](https://ariya.io/tags/qt/)

**Update**: Read also the approach to [detect Boolean traps](https://ariya.io/2012/06/detecting-boolean-traps-with-esprima.html) (in JavaScript apps) using a simple script.

The nice thing [working for Trolltech](https://ariya.io/2008/04/i-think-im-moving-but-i-got-nowhere.html) was (among others) learning the principles behind the good API. The article [Designing Qt-Style C++ API](http://doc.qt.nokia.com/qq/qq13-apis.html) from Matthias 6 years ago is still a good reading till today. The content itself is now expanded into the wiki page [API Design Principles](http://developer.qt.nokia.com/wiki/API_Design_Principles).

The major premise behind a good API is rather straightforward:
> the code is usually **> written once**>  but **> read many times**> .

When writing the code, the developer has the time she needs to look at the API documentation and digest it. When someone else reads the code (for review or bug fix), she may not always have the API documentation handy. While this is just common sense, wait until you finish reading and see why this important fact is still overlooked these days.

Note: Qt is in C++, but surprisingly the same API design principles apply to the (wonderful) world of JavaScript, which is the focus in this blog post.

![George_Boole.jpg](../_resources/7edb96af2a1956e453c1a598b89ccad8.jpg)

[George Boole](http://en.wikipedia.org/wiki/George_Boole), inventor of the Boolean logic.

For this particular discussion, I’ll pick my favorite API design mistake: **boolean trap**. On [this topic](http://developer.qt.nokia.com/wiki/API_Design_Principles#e7794937cba47d5e9c54d50a6a32328b), the above API Design Principle wiki page says that

> it’s almost invariably a mistake to add a bool parameter to an existing function

Let’s start with the textbook example: guess what this code means?

	widget.repaint(false);

Without looking at the documentation, the usual suspect is **don’t repaint the widget**. Then, you look at the documentation and it refers the function argument as `immediate`, which is `true` if you want immediate painting or `false` for deferred painting. Thus, the correct behavior implied by the above code is actually **repaint this widget later**, which is miles away from your initial guess.

One possible solution to this problem is to use explicit function argument. In the C++ world, this can be solved using enum, e.g. `widget.repaint(WidgetClass::Deferred)`. In the JavaScript world, the alternative is using an object literal such as,

	widget.repaint({ immediate: false });

or the more verbose variant:

	widget.repaint({ mode: "immediate" });

or just create a different function for that purpose:

	widget.repaintLater();

There will be a concern of performance since an object is more expensive than just a simple boolean literal. Thus, profile your code carefully and set a sensible compromise if this above line is in your hot path. On the other hand, I also do believe that modern future JavaScript engines would be smart enough to optimize such usages that the speed penalty is negligible.

Another classic is the **confusion during construction**. Your user interface needs a bunch of sliders to allow the user to choose some values. Here is one line in the code for you to review:

	var opacitySlider = new Slider(true);

Mysteriously, there are also lines similar to:

	var volumeSlider = new Slider(false);

It turns out that `true` there means a horizontal slider and `false` means a vertical slider. Of course, the easiest way to clear this confusion is to actually name the object `HorizontalSlider` and `VerticalSlider` and get rid of the boolean argument. Heck, who knows someday you’ll need a diagonal slider!

You may scream, “Of course, I won’t be too idiot to make those rookie mistakes!”. Well, in the following paragraphs I’ll give examples of **actual** boolean traps in the API of several well-known JavaScript libraries and frameworks out there (I try to be unbiased). Consider that there are *millions* of developers using the libraries in real-world web applications, imagine the exposure of the traps.

For each of this case, imagine you are doing a code review. Your amazing coworker wants to commit a patch and he consults you to check your opinion.

### to be or not to be

This is the same as the textbook example, but coming from a real framework:

	stackView.updateHeight(false);

Yes, that `false` again refers to *immediate or not*. To the untrained developer, the above line feels like **don’t update the height**. A real crazy one might even stretch it to **update the width**!

Here is another one. To facilitate easy iteration of child widgets, you can use `next()` function which would get you the next sibling. But then, the code looks like:

	widget.next(true);

which actually does the extra magic (because of the `true` value) that the very first child widget will be returned if you hit the last one. In other words, `true` there stands for `circular`. An innocent value which does too much behind your back. Well, good luck trying to review that kind of code.

Another dangerous venture:

	widget.destroy(false);

which potentially leads you to think **don’t destroy this widget**. You can’t be more wrong, the function actually still destroys your widget, but it leaves the DOM associated with the widget intact. Only if the argument is `true` then actually every related DOM pieces is also (tore) torn down.

### optionally undecipherable

Now that we have the slider for the UI, we need to preset the value:

	volumeSlider.setValue(90, false);

Another boolean horror! The documentation reveals that `false` there indicates that the slider should *not animate* the movement of its indicator from the old value to the new value. By default, it will show the animation but since we want to set the initial value, the animation will be distracting and needs to be off. How about writing it like this instead?

	volumeSlider.setValue(90, { animation: false } );

There is this list view of all your customers. We want to find out who live in a certain city. Can you guess what the last optional argument refers to?

	customerView.filter('address', 'sunnyvale', false);

Oh, apparently the API documentation refers it to `caseSensitive`! Just by looking at it, this is not obvious and it could mean an entirely different thing, anything from `exactMatch` to `highlightMatchedLine`. One possible workaround:

	customerView.filter('address', 'sunnyvale', { caseSensitive: false });

### the more, the merrier

While *one* boolean argument is already confusing, *two* boolean arguments can’t be more fun.

To handle layout, often there is a line of code that looks like:

	cmp.setCentered(true, false);

Again, a trip to the API doc enlightens the reviewer that the function signature is actually `setCentered(centered, autoUpdate)`. This is confusing as `setCentered(centered)` only is probably fine, it’s just like a property setter, but the interplay of the `autoUpdate` argument forces the brain to think harder.

Note that a pair of values like that, especially in the context of centering/geometry purpose, might provoke a different interpretation: **center vertically and horizontally**. This is arguably the most sensible one which comes to mind if one sees that code.

Here is another one:

	menu.stop(true, false);

The boolean values there refer to *clear the animation queue or not* and *go to the animation or not*, respectively. They are not even remotely related. What is your best educated guess if you did not know this beforehand?

Of course, why stop at two if you can have more?

	event.initKeyEvent("keypress", true, true, null, null,
	    false, false, false, false, 9, );

### double negative

Now, coming back to property setter, this is one valid use of boolean argument, e.g. `dialogBox.setVisible(true)`. However, care must be taken so that there is no such **double negative**. Especially for non-native speakers, double negative requires an extra careful measure to make sure that the right meaning is communicated.

If I wake you at midnight and ask you this question “if invisible is false, does that mean my component is shown or hidden?”, there is a chance you answer it incorrectly.

Real-world examples of double negative follow:

	volumeSlider.setThumbsDisabled(false);
	component.setDisabled(false);
	filter.setCaseInsensitive(false);

Would you be less confused if this is what you read instead?

	volumeSlider.setThumbsEnabled(true);
	component.setEnabled(true);
	filter.setCaseSensitive(true);

The same principle applies to active vs inactive, modified vs unmodified, defined vs undefined, selected vs unselected, etc.

By now, hopefully you got the idea of various risky uses of boolean argument. Feel free to share your favorite freak-out moment as you encounter such a similar trap.

Most importantly, next time you design an API function, remember [George Boole](http://en.wikipedia.org/wiki/George_Boole) and don’t let him down!

**Update**: Some people on [Reddit](http://www.reddit.com/r/programming/comments/jt5dc/hall_of_api_shame_boolean_trap_its_almost/) pointed out that they would not interpret `widget.repaint(false)` as *do not repaint*. First of all, it’s subjective. In some languages it can be understood as *repaint not*, which is effectively a negation. Also, the context might pollute, e.g. if there is `fooWidget.show(false)` (which means *do not show*) right before, then it may influence a similar conclusion for the repaint issue. I was also not clear that any crazy possible interpretations are just examples, substitute them with your own imaginations. The fact that everyone can propose a different interpretation is the premise: ambiguity begets insanity.

##### Related posts:

- [ChakraCore on Linux](https://ariya.io/2017/01/chakracore-on-linux)
- [On-the-fly JavaScript Syntax Node Inspection](https://ariya.io/2016/12/on-the-fly-javascript-syntax-node-inspection)
- [Syntax Highlighting in the Terminal](https://ariya.io/2016/11/syntax-highlighting-in-the-terminal)
- [TypeScript 2.0 and Strict Null Checking](https://ariya.io/2016/10/typescript-2-and-strict-null-checking)
- [ChakraCore on macOS](https://ariya.io/2016/08/chakracore-on-macos)
- [API Names and Begging the Negatives](https://ariya.io/2016/04/api-names-and-begging-the-negatives)

♡ this article? [Explore more articles](https://ariya.io/articles) and follow me [Twitter](https://twitter.com/intent/follow?screen_name=AriyaHidayat).

Share this on[Twitter](https://twitter.com/share?text=The%20Pitfalls%20of%20Boolean%20Trap&url=https%3a%2f%2fariya.io%2f2011%2f08%2fhall-of-api-shame-boolean-trap&via=AriyaHidayat)[Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3a%2f%2fariya.io%2f2011%2f08%2fhall-of-api-shame-boolean-trap)

- [125 comments]()
- [**ariya.io**](https://disqus.com/home/forums/ariya/)
- [Marc Cohen](https://disqus.com/embed/comments/?base=default&f=ariya&t_i=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_u=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_e=The%20Pitfalls%20of%20Boolean%20Trap&t_d=The%20Pitfalls%20of%20Boolean%20Trap&t_t=The%20Pitfalls%20of%20Boolean%20Trap&s_o=default#)
- [](https://disqus.com/home/inbox/)
- [ Recommend  9](https://disqus.com/embed/comments/?base=default&f=ariya&t_i=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_u=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_e=The%20Pitfalls%20of%20Boolean%20Trap&t_d=The%20Pitfalls%20of%20Boolean%20Trap&t_t=The%20Pitfalls%20of%20Boolean%20Trap&s_o=default#)
- tTweetfShare
- [Sort by Newest](https://disqus.com/embed/comments/?base=default&f=ariya&t_i=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_u=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_e=The%20Pitfalls%20of%20Boolean%20Trap&t_d=The%20Pitfalls%20of%20Boolean%20Trap&t_t=The%20Pitfalls%20of%20Boolean%20Trap&s_o=default#)

[![noavatar92.png](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/disqus_Q5LZbDr3pW/)

Join the discussion…

![underline.59f82f5f5bbed90fd72132ef98662fe3.png](../_resources/c6501c3f7d72fc1b6c5c664055aa9562.png)

![italic.a6e1da4a89899ae5e87db9ded9f84d5b.png](../_resources/a07b7e1fcec6807578565deaf67fee1b.png)

![spoiler.eff5de8f72591c5ceeb4fa26a117c6d1.png](../_resources/81c01ba2374c675c3aeaaa782bf2e78c.png)

![link.5ef9a39f22ce49f926e304567b9d611b.png](../_resources/f7efeff64e3b50b6ed3ac56e033c7093.png)

![bold.cb366e6a49396fb0e47a01df277563c8.png](../_resources/77ac7d224499e3ad46945902c341b126.png)

![strikethrough.ced68e63961c6bc0e072ce907906b252.png](../_resources/c004e6b74d78957de021cd89afcfb140.png)

![blockquote.69435f6faa8c7a193456c46bcb7fb1ed.png](../_resources/1a93c9927335a0e22c1e2f44320b38f3.png)

![code.8f558a246aa4e9c41ef343f72f012f01.png](../_resources/7b7516fe3c1d4c3b33fd1a97f4371bc8.png)

-

    - [−](https://disqus.com/embed/comments/?base=default&f=ariya&t_i=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_u=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_e=The%20Pitfalls%20of%20Boolean%20Trap&t_d=The%20Pitfalls%20of%20Boolean%20Trap&t_t=The%20Pitfalls%20of%20Boolean%20Trap&s_o=default#)
    - [****](https://disqus.com/embed/comments/?base=default&f=ariya&t_i=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_u=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_e=The%20Pitfalls%20of%20Boolean%20Trap&t_d=The%20Pitfalls%20of%20Boolean%20Trap&t_t=The%20Pitfalls%20of%20Boolean%20Trap&s_o=default#)

[![avatar92.jpg](../_resources/d54067b6f7641d6eeb89b8f465c49aca.jpg)](https://disqus.com/by/anthonybenkhebbab/)

 [Anthony Benkhebbab](https://disqus.com/by/anthonybenkhebbab/)    •  [a year ago](https://ariya.io/2011/08/hall-of-api-shame-boolean-trap#comment-3921637648)

"If I wake you at midnight and ask you this question “if invisible is
false, does that mean my component is shown or hidden?”, there is a
chance you answer it incorrectly."
Yeah I hate when this happen tho

-

    - [−](https://disqus.com/embed/comments/?base=default&f=ariya&t_i=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_u=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_e=The%20Pitfalls%20of%20Boolean%20Trap&t_d=The%20Pitfalls%20of%20Boolean%20Trap&t_t=The%20Pitfalls%20of%20Boolean%20Trap&s_o=default#)
    - [****](https://disqus.com/embed/comments/?base=default&f=ariya&t_i=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_u=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_e=The%20Pitfalls%20of%20Boolean%20Trap&t_d=The%20Pitfalls%20of%20Boolean%20Trap&t_t=The%20Pitfalls%20of%20Boolean%20Trap&s_o=default#)

[![avatar92.jpg](../_resources/ec3095daea6cb2daa15e55f10c35418e.jpg)](https://disqus.com/by/disqus_W8jUCJnnW3/)

 [Valtid](https://disqus.com/by/disqus_W8jUCJnnW3/)    •  [a year ago](https://ariya.io/2011/08/hall-of-api-shame-boolean-trap#comment-3873964534)

repaint(defer =true ); is declarative enough i would think. also, most IDEs do provide hints of what params should be like. then again this was written in 2011. good read though.

    -

        - [−](https://disqus.com/embed/comments/?base=default&f=ariya&t_i=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_u=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_e=The%20Pitfalls%20of%20Boolean%20Trap&t_d=The%20Pitfalls%20of%20Boolean%20Trap&t_t=The%20Pitfalls%20of%20Boolean%20Trap&s_o=default#)
        - [****](https://disqus.com/embed/comments/?base=default&f=ariya&t_i=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_u=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_e=The%20Pitfalls%20of%20Boolean%20Trap&t_d=The%20Pitfalls%20of%20Boolean%20Trap&t_t=The%20Pitfalls%20of%20Boolean%20Trap&s_o=default#)

[![avatar92.jpg](../_resources/676f21296433b6fd2933827af30d8b87.jpg)](https://disqus.com/by/ariya/)

 [Ariya Hidayat](https://disqus.com/by/ariya/)  Mod  [*>* Valtid](https://ariya.io/2011/08/hall-of-api-shame-boolean-trap#comment-3873964534)  •  [a year ago](https://ariya.io/2011/08/hall-of-api-shame-boolean-trap#comment-3877714461)

That syntax is not supported in every language.

Also, keep in my mind that an IDE doesn't help you much when you're doing code review outside your IDE, e.g. taking a look at a pull request.

-

    - [−](https://disqus.com/embed/comments/?base=default&f=ariya&t_i=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_u=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_e=The%20Pitfalls%20of%20Boolean%20Trap&t_d=The%20Pitfalls%20of%20Boolean%20Trap&t_t=The%20Pitfalls%20of%20Boolean%20Trap&s_o=default#)
    - [****](https://disqus.com/embed/comments/?base=default&f=ariya&t_i=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_u=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_e=The%20Pitfalls%20of%20Boolean%20Trap&t_d=The%20Pitfalls%20of%20Boolean%20Trap&t_t=The%20Pitfalls%20of%20Boolean%20Trap&s_o=default#)

![noavatar92.png](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)

Joseph Rocca  •  [4 years ago](https://ariya.io/2011/08/hall-of-api-shame-boolean-trap#comment-1975268162)

repaint('immediate'); //Can't misinterpret and no objects to slow performance.

    -

        - [−](https://disqus.com/embed/comments/?base=default&f=ariya&t_i=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_u=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_e=The%20Pitfalls%20of%20Boolean%20Trap&t_d=The%20Pitfalls%20of%20Boolean%20Trap&t_t=The%20Pitfalls%20of%20Boolean%20Trap&s_o=default#)
        - [****](https://disqus.com/embed/comments/?base=default&f=ariya&t_i=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_u=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_e=The%20Pitfalls%20of%20Boolean%20Trap&t_d=The%20Pitfalls%20of%20Boolean%20Trap&t_t=The%20Pitfalls%20of%20Boolean%20Trap&s_o=default#)

[![avatar92.jpg](../_resources/d98c05252991f79f2ed8644f4dd39b12.jpg)](https://disqus.com/by/disqus_fuf6SGRDc1/)

 [U.K.](https://disqus.com/by/disqus_fuf6SGRDc1/)    [*>* Joseph Rocca](https://ariya.io/2011/08/hall-of-api-shame-boolean-trap#comment-1975268162)  •  [3 years ago](https://ariya.io/2011/08/hall-of-api-shame-boolean-trap#comment-2684049565)

Analyzing strings is much longer than bool vars.

        -

            - [−](https://disqus.com/embed/comments/?base=default&f=ariya&t_i=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_u=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_e=The%20Pitfalls%20of%20Boolean%20Trap&t_d=The%20Pitfalls%20of%20Boolean%20Trap&t_t=The%20Pitfalls%20of%20Boolean%20Trap&s_o=default#)
            - [****](https://disqus.com/embed/comments/?base=default&f=ariya&t_i=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_u=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_e=The%20Pitfalls%20of%20Boolean%20Trap&t_d=The%20Pitfalls%20of%20Boolean%20Trap&t_t=The%20Pitfalls%20of%20Boolean%20Trap&s_o=default#)

[![avatar92.jpg](../_resources/50c5c6b5265f11617dbf364c28c3150f.jpg)](https://disqus.com/by/disqus_A84NFET2fP/)

 [Алексей Филатьев](https://disqus.com/by/disqus_A84NFET2fP/)    [*>* U.K.](https://ariya.io/2011/08/hall-of-api-shame-boolean-trap#comment-2684049565)  •  [2 years ago](https://ariya.io/2011/08/hall-of-api-shame-boolean-trap#comment-3632034639)

And it's very easy to missprint - static code analyzer will be useless in this case.

-

    - [−](https://disqus.com/embed/comments/?base=default&f=ariya&t_i=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_u=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_e=The%20Pitfalls%20of%20Boolean%20Trap&t_d=The%20Pitfalls%20of%20Boolean%20Trap&t_t=The%20Pitfalls%20of%20Boolean%20Trap&s_o=default#)
    - [****](https://disqus.com/embed/comments/?base=default&f=ariya&t_i=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_u=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_e=The%20Pitfalls%20of%20Boolean%20Trap&t_d=The%20Pitfalls%20of%20Boolean%20Trap&t_t=The%20Pitfalls%20of%20Boolean%20Trap&s_o=default#)

[![avatar92.jpg](../_resources/d443424b371ac4f36a7675bd1f89ecb3.jpg)](https://disqus.com/by/disqus_a2sqN72ug9/)

 [fredy](https://disqus.com/by/disqus_a2sqN72ug9/)    •  [4 years ago](https://ariya.io/2011/08/hall-of-api-shame-boolean-trap#comment-1956706842)

Ariya Hidayat Great article. The link to API Design Principles is broken, i was take the task to search this on [web.archi.org](http://disq.us/url?url=http%3A%2F%2Fweb.archi.org%3APYed9fpUmgMEdFDucytbnhX2D_c&cuid=1222985) and in found it: [http://web.archive.org/web/...](http://disq.us/url?url=http%3A%2F%2Fweb.archive.org%2Fweb%2F20140408070623%2Fhttp%3A%2F%2Fqt-project.org%2Fwiki%2FAPI_Design_Principles%3AyvjjifTnVLG2TvrwNwDmx-3l2PI&cuid=1222985) thanks again.

-

    - [−](https://disqus.com/embed/comments/?base=default&f=ariya&t_i=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_u=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_e=The%20Pitfalls%20of%20Boolean%20Trap&t_d=The%20Pitfalls%20of%20Boolean%20Trap&t_t=The%20Pitfalls%20of%20Boolean%20Trap&s_o=default#)
    - [****](https://disqus.com/embed/comments/?base=default&f=ariya&t_i=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_u=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_e=The%20Pitfalls%20of%20Boolean%20Trap&t_d=The%20Pitfalls%20of%20Boolean%20Trap&t_t=The%20Pitfalls%20of%20Boolean%20Trap&s_o=default#)

[![avatar92.jpg](../_resources/d32c2e1f56e0940d17aa2361efa48e26.jpg)](https://disqus.com/by/dominic_watson/)

 [Dominic Watson](https://disqus.com/by/dominic_watson/)    •  [4 years ago](https://ariya.io/2011/08/hall-of-api-shame-boolean-trap#comment-1869824794)

To back you up. I thought "widget.repaint(false);" was: do not repaint.

-

    - [−](https://disqus.com/embed/comments/?base=default&f=ariya&t_i=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_u=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_e=The%20Pitfalls%20of%20Boolean%20Trap&t_d=The%20Pitfalls%20of%20Boolean%20Trap&t_t=The%20Pitfalls%20of%20Boolean%20Trap&s_o=default#)
    - [****](https://disqus.com/embed/comments/?base=default&f=ariya&t_i=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_u=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_e=The%20Pitfalls%20of%20Boolean%20Trap&t_d=The%20Pitfalls%20of%20Boolean%20Trap&t_t=The%20Pitfalls%20of%20Boolean%20Trap&s_o=default#)

[![avatar92.jpg](../_resources/f9f92a1451c56f669a074f014bcb8a33.jpg)](https://disqus.com/by/disqus_xnkqrczMjq/)

 [MBR](https://disqus.com/by/disqus_xnkqrczMjq/)    •  [6 years ago](https://ariya.io/2011/08/hall-of-api-shame-boolean-trap#comment-1037660773)

I'd have to agree with others here -- to say that someone would interpret:
repaint(false);
as
// repaint();

seems rather bizzare - and I'd have to also agree that the "force" pattern here has been around (in my memory at least) since the advent of event-driven GUI's, and probably before that, retained-mode display list processors.

Your wording of "do not repaint" doesn't even make sense, as typically it's impossible to tell the computer *not* to do something (with the exception of non-monotonic reasoning/planning systems) - kind of the procedural equivelent of "Don't_think_of_pink elephants()"

I do not disagree with your API design tennants here however, just with how low you set the bar and the level to which the code reader is going to misread the sematics of the statements.

The issue isn't just with bools, but with positional args in general.

In the Javascript world, object option parameters are used quite a bit it lieu of (typechecked) named parameters, and C# (like Ada) has named parameters, but typically people like short code over readable code - but it's fairly common to switch from positional to keyword after a certain # of parameters. The Smalltalk keyword selector syntax is probably the best of all worlds, where the method atPut is called (only) as "foo at: 7 put:9" rather than "foo.atPut(7,9)" that is common elsewhere.

    -

        - [−](https://disqus.com/embed/comments/?base=default&f=ariya&t_i=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_u=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_e=The%20Pitfalls%20of%20Boolean%20Trap&t_d=The%20Pitfalls%20of%20Boolean%20Trap&t_t=The%20Pitfalls%20of%20Boolean%20Trap&s_o=default#)
        - [****](https://disqus.com/embed/comments/?base=default&f=ariya&t_i=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_u=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_e=The%20Pitfalls%20of%20Boolean%20Trap&t_d=The%20Pitfalls%20of%20Boolean%20Trap&t_t=The%20Pitfalls%20of%20Boolean%20Trap&s_o=default#)

![noavatar92.png](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)

cHao  [*>* MBR](https://ariya.io/2011/08/hall-of-api-shame-boolean-trap#comment-1037660773)  •  [5 years ago](https://ariya.io/2011/08/hall-of-api-shame-boolean-trap#comment-1417904891)

`repaint(false);` could very easily be interpreted as "ignore future `repaint()` calls til i call `repaint(true)`. It's quite common to disable updates while you're doing a bunch of them, and then having a single big update at the end.

Of course, a decent design would have a `disableUpdates()` and `enableUpdates()` rather than relying on a rather cryptic boolean parameter. But that's kinda the point of the whole article.

-

    - [−](https://disqus.com/embed/comments/?base=default&f=ariya&t_i=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_u=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_e=The%20Pitfalls%20of%20Boolean%20Trap&t_d=The%20Pitfalls%20of%20Boolean%20Trap&t_t=The%20Pitfalls%20of%20Boolean%20Trap&s_o=default#)
    - [****](https://disqus.com/embed/comments/?base=default&f=ariya&t_i=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_u=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_e=The%20Pitfalls%20of%20Boolean%20Trap&t_d=The%20Pitfalls%20of%20Boolean%20Trap&t_t=The%20Pitfalls%20of%20Boolean%20Trap&s_o=default#)

![noavatar92.png](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)

touist   •  [6 years ago](https://ariya.io/2011/08/hall-of-api-shame-boolean-trap#comment-1011450111)

In Ada (designed to be read) you have named parameters : Repaint (Widget => My_Widget, Later => True);

-

    - [−](https://disqus.com/embed/comments/?base=default&f=ariya&t_i=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_u=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_e=The%20Pitfalls%20of%20Boolean%20Trap&t_d=The%20Pitfalls%20of%20Boolean%20Trap&t_t=The%20Pitfalls%20of%20Boolean%20Trap&s_o=default#)
    - [****](https://disqus.com/embed/comments/?base=default&f=ariya&t_i=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_u=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_e=The%20Pitfalls%20of%20Boolean%20Trap&t_d=The%20Pitfalls%20of%20Boolean%20Trap&t_t=The%20Pitfalls%20of%20Boolean%20Trap&s_o=default#)

[![noavatar92.png](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/sirspudd/)

 [Donald Rupert Carr](https://disqus.com/by/sirspudd/)    •  [6 years ago](https://ariya.io/2011/08/hall-of-api-shame-boolean-trap#comment-1007167949)

Hah!

"If I wake you at midnight and ask you this question "if invisible is false, does that mean my component is shown or hidden?", there is a chance you answer it incorrectly."

I am not asleep by midnight you fool! Vanishing chance of said error!

    -

        - [−](https://disqus.com/embed/comments/?base=default&f=ariya&t_i=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_u=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_e=The%20Pitfalls%20of%20Boolean%20Trap&t_d=The%20Pitfalls%20of%20Boolean%20Trap&t_t=The%20Pitfalls%20of%20Boolean%20Trap&s_o=default#)
        - [****](https://disqus.com/embed/comments/?base=default&f=ariya&t_i=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_u=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_e=The%20Pitfalls%20of%20Boolean%20Trap&t_d=The%20Pitfalls%20of%20Boolean%20Trap&t_t=The%20Pitfalls%20of%20Boolean%20Trap&s_o=default#)

[![noavatar92.png](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/dominic_watson/)

 [Dominic Watson](https://disqus.com/by/dominic_watson/)    [*>* Donald Rupert Carr](https://ariya.io/2011/08/hall-of-api-shame-boolean-trap#comment-1007167949)  •  [4 years ago](https://ariya.io/2011/08/hall-of-api-shame-boolean-trap#comment-1869825745)

I understand you're joking but... we're not always as alert as we should be.

    -

        - [−](https://disqus.com/embed/comments/?base=default&f=ariya&t_i=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_u=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_e=The%20Pitfalls%20of%20Boolean%20Trap&t_d=The%20Pitfalls%20of%20Boolean%20Trap&t_t=The%20Pitfalls%20of%20Boolean%20Trap&s_o=default#)
        - [****](https://disqus.com/embed/comments/?base=default&f=ariya&t_i=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_u=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_e=The%20Pitfalls%20of%20Boolean%20Trap&t_d=The%20Pitfalls%20of%20Boolean%20Trap&t_t=The%20Pitfalls%20of%20Boolean%20Trap&s_o=default#)

[![noavatar92.png](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/ariya/)

 [Ariya Hidayat](https://disqus.com/by/ariya/)  Mod  [*>* Donald Rupert Carr](https://ariya.io/2011/08/hall-of-api-shame-boolean-trap#comment-1007167949)  •  [6 years ago](https://ariya.io/2011/08/hall-of-api-shame-boolean-trap#comment-1007409956)

Well, the sun never sets on the British empire...

-

    - [−](https://disqus.com/embed/comments/?base=default&f=ariya&t_i=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_u=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_e=The%20Pitfalls%20of%20Boolean%20Trap&t_d=The%20Pitfalls%20of%20Boolean%20Trap&t_t=The%20Pitfalls%20of%20Boolean%20Trap&s_o=default#)
    - [****](https://disqus.com/embed/comments/?base=default&f=ariya&t_i=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_u=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_e=The%20Pitfalls%20of%20Boolean%20Trap&t_d=The%20Pitfalls%20of%20Boolean%20Trap&t_t=The%20Pitfalls%20of%20Boolean%20Trap&s_o=default#)

[![noavatar92.png](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/sergeyrozhenko/)

 [sergeyrozhenko](https://disqus.com/by/sergeyrozhenko/)    •  [6 years ago](https://ariya.io/2011/08/hall-of-api-shame-boolean-trap#comment-1005193002)

C++ IDE would easily show you what these boolean parameters do in a tooltip or at a press of a button (otherwise it's garbage that has no right to be called IDE). So, avoiding "boolean trap" is something to consider, but not always the right choice.

    -

        - [−](https://disqus.com/embed/comments/?base=default&f=ariya&t_i=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_u=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_e=The%20Pitfalls%20of%20Boolean%20Trap&t_d=The%20Pitfalls%20of%20Boolean%20Trap&t_t=The%20Pitfalls%20of%20Boolean%20Trap&s_o=default#)
        - [****](https://disqus.com/embed/comments/?base=default&f=ariya&t_i=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_u=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_e=The%20Pitfalls%20of%20Boolean%20Trap&t_d=The%20Pitfalls%20of%20Boolean%20Trap&t_t=The%20Pitfalls%20of%20Boolean%20Trap&s_o=default#)

[![noavatar92.png](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/ariya/)

 [Ariya Hidayat](https://disqus.com/by/ariya/)  Mod  [*>* sergeyrozhenko](https://ariya.io/2011/08/hall-of-api-shame-boolean-trap#comment-1005193002)  •  [6 years ago](https://ariya.io/2011/08/hall-of-api-shame-boolean-trap#comment-1005281968)

IDE is only useful when writing the code and occasionally when reading it. For code review and/or analysis, it hardly matters. How many times you read the code from somewhere and always paste it in your IDE?

-

    - [−](https://disqus.com/embed/comments/?base=default&f=ariya&t_i=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_u=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_e=The%20Pitfalls%20of%20Boolean%20Trap&t_d=The%20Pitfalls%20of%20Boolean%20Trap&t_t=The%20Pitfalls%20of%20Boolean%20Trap&s_o=default#)
    - [****](https://disqus.com/embed/comments/?base=default&f=ariya&t_i=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_u=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_e=The%20Pitfalls%20of%20Boolean%20Trap&t_d=The%20Pitfalls%20of%20Boolean%20Trap&t_t=The%20Pitfalls%20of%20Boolean%20Trap&s_o=default#)

![noavatar92.png](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)

Vitaly  •  [6 years ago](https://ariya.io/2011/08/hall-of-api-shame-boolean-trap#comment-1004233480)

How about removeAll(true, false) in Sencha Touch? I've always found it a bit confusing. The first argument stands for 'destroy' and second for 'everything', which means docked items won't be removed if 'everything' is set to false.

-

    - [−](https://disqus.com/embed/comments/?base=default&f=ariya&t_i=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_u=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_e=The%20Pitfalls%20of%20Boolean%20Trap&t_d=The%20Pitfalls%20of%20Boolean%20Trap&t_t=The%20Pitfalls%20of%20Boolean%20Trap&s_o=default#)
    - [****](https://disqus.com/embed/comments/?base=default&f=ariya&t_i=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_u=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_e=The%20Pitfalls%20of%20Boolean%20Trap&t_d=The%20Pitfalls%20of%20Boolean%20Trap&t_t=The%20Pitfalls%20of%20Boolean%20Trap&s_o=default#)

[![noavatar92.png](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/skaue/)

 [skaue](https://disqus.com/by/skaue/)    •  [6 years ago](https://ariya.io/2011/08/hall-of-api-shame-boolean-trap#comment-1003696368)

I agree with using a more explicit language when programming, allowing the developer to read out loud what the code actually does, however in many development environments, these crappy booleans would carry a tooltip or signature tooltip revealing the name of the parameter, and then explain to the developer the intention of the boolean. I remember prefixing all variables with one or two letters just to reveal its native type... I don't do that any more.

-

    - [−](https://disqus.com/embed/comments/?base=default&f=ariya&t_i=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_u=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_e=The%20Pitfalls%20of%20Boolean%20Trap&t_d=The%20Pitfalls%20of%20Boolean%20Trap&t_t=The%20Pitfalls%20of%20Boolean%20Trap&s_o=default#)
    - [****](https://disqus.com/embed/comments/?base=default&f=ariya&t_i=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_u=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_e=The%20Pitfalls%20of%20Boolean%20Trap&t_d=The%20Pitfalls%20of%20Boolean%20Trap&t_t=The%20Pitfalls%20of%20Boolean%20Trap&s_o=default#)

[![noavatar92.png](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/paultherrien/)

 [Paul Therrien](https://disqus.com/by/paultherrien/)    •  [6 years ago](https://ariya.io/2011/08/hall-of-api-shame-boolean-trap#comment-1003617262)

the moral is: Don't pass parameters into functions without first understanding what your function is doing!

-

    - [−](https://disqus.com/embed/comments/?base=default&f=ariya&t_i=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_u=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_e=The%20Pitfalls%20of%20Boolean%20Trap&t_d=The%20Pitfalls%20of%20Boolean%20Trap&t_t=The%20Pitfalls%20of%20Boolean%20Trap&s_o=default#)
    - [****](https://disqus.com/embed/comments/?base=default&f=ariya&t_i=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_u=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_e=The%20Pitfalls%20of%20Boolean%20Trap&t_d=The%20Pitfalls%20of%20Boolean%20Trap&t_t=The%20Pitfalls%20of%20Boolean%20Trap&s_o=default#)

[![noavatar92.png](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/sirspudd/)

 [Donald Rupert Carr](https://disqus.com/by/sirspudd/)    •  [6 years ago](https://ariya.io/2011/08/hall-of-api-shame-boolean-trap#comment-1003281670)

[http://developer.qt.nokia.c...](http://disq.us/url?url=http%3A%2F%2Fdeveloper.qt.nokia.com%2Fwiki%2FAPI_Design_Principles%3AeKZzL_9w5659z1QWnH1MQn7hCw8&cuid=1222985)

is unfortunately no longer a valid URL, you need to spruce that dude up to be:

[http://qt-project.org/wiki/...](http://disq.us/url?url=http%3A%2F%2Fqt-project.org%2Fwiki%2FAPI-Design-Principles%3Aww56jnn9U6WVkgkbjBnim6ljDNQ&cuid=1222985)

-

    - [−](https://disqus.com/embed/comments/?base=default&f=ariya&t_i=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_u=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_e=The%20Pitfalls%20of%20Boolean%20Trap&t_d=The%20Pitfalls%20of%20Boolean%20Trap&t_t=The%20Pitfalls%20of%20Boolean%20Trap&s_o=default#)
    - [****](https://disqus.com/embed/comments/?base=default&f=ariya&t_i=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_u=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_e=The%20Pitfalls%20of%20Boolean%20Trap&t_d=The%20Pitfalls%20of%20Boolean%20Trap&t_t=The%20Pitfalls%20of%20Boolean%20Trap&s_o=default#)

[![noavatar92.png](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/getify/)

 [getify](https://disqus.com/by/getify/)    •  [6 years ago](https://ariya.io/2011/08/hall-of-api-shame-boolean-trap#comment-1003256547)

While I agree with the spirit of this post, I don't see something particularly special about booleans. An API where you pass "magic numbers" would be equally (or more) confusing. So would an API where you pass in an array of various values.

The object-literal workaround for named-parameters is certainly a popular one to suggest, but it's often really clunky too. It's not really a magic bullet, but it shifts the burden around just enough that sometimes it makes you feel slightly better about your API design. But I don't think users instinctively prefer to pass big hashes.

You also suggest creating different API names for the different option permutations. In very limited cases, this is OK, but a lot of times it creates "API fatigue" where the API surface is just so cluttered with dozens of different closely related API calls, you get lost in documentation (or code!) trying to use it. Don't make two API calls where one will suffice.

On the other end of the spectrum, you could design your API to take natural language strings like `[widget.show](http://disq.us/url?url=http%3A%2F%2Fwidget.show%3APVyzgDvHJW6zKpvZm1VkztMo_z8&cuid=1222985)("but don't animate") and that would be perfectly semantic and readable, but then it shifts the burden of implementation too far back inside the API of having to do crazy things like parsing natural language strings.

FWIW, I'm no PHP fan or supporter, but they do have an awful lot of mature (or, at least, old) APIs with an awful lot of parameters of various types, whether they be numbers or booleans, and it seems like a lot of those APIs suggest the use of constants in place of the magic values. With numbers, it even allows you to do value masking, which I think is also a powerful technique but extremely non-idiomatic in the JS world (for some reason!?).

In another comment here you mention using a named-variable is a workaround/hack, but I disagree: I think it's actually a great balance.

`[widget.show](http://disq.us/url?url=http%3A%2F%2Fwidget.show%3APVyzgDvHJW6zKpvZm1VkztMo_z8&cuid=1222985)(widget.NO_ANIMATION)` has the appearance of named-parameter, but is less clunky than `[widget.show](http://disq.us/url?url=http%3A%2F%2Fwidget.show%3APVyzgDvHJW6zKpvZm1VkztMo_z8&cuid=1222985)({ animate: false })`.

Last point: on APIs that I am completely in control of, I would try to follow a balance of these various "best practices". But for APIs I don't control, but which are poorly designed, I do stuff like this:

`[widget.show](http://disq.us/url?url=http%3A%2F%2Fwidget.show%3APVyzgDvHJW6zKpvZm1VkztMo_z8&cuid=1222985)( /*animate=*/ false )`

[see more]()

    -

        - [−](https://disqus.com/embed/comments/?base=default&f=ariya&t_i=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_u=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_e=The%20Pitfalls%20of%20Boolean%20Trap&t_d=The%20Pitfalls%20of%20Boolean%20Trap&t_t=The%20Pitfalls%20of%20Boolean%20Trap&s_o=default#)
        - [****](https://disqus.com/embed/comments/?base=default&f=ariya&t_i=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_u=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_e=The%20Pitfalls%20of%20Boolean%20Trap&t_d=The%20Pitfalls%20of%20Boolean%20Trap&t_t=The%20Pitfalls%20of%20Boolean%20Trap&s_o=default#)

[![noavatar92.png](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/joeshelby/)

 [Joe Shelby](https://disqus.com/by/joeshelby/)    [*>* getify](https://ariya.io/2011/08/hall-of-api-shame-boolean-trap#comment-1003256547)  •  [6 years ago](https://ariya.io/2011/08/hall-of-api-shame-boolean-trap#comment-1003503382)

the object workaround is more expensive not just in the need to create the object, but on the receiving side, the need to add a null-check and handle that correctly.

you mention enums, and that's still perfectly valid.
Widget.prototype.ANIMATE = true; Widget.prototype.NO_ANIMATION = false;
and later, widget.slide(90, widget.NO_ANIMATION)

all boolean, nothing polluting the global/window workspace, and no need to remember the 'class' of the widget in question. one level of indirection is far faster than make-an-object-and-check-its-existence.

-

    - [−](https://disqus.com/embed/comments/?base=default&f=ariya&t_i=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_u=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_e=The%20Pitfalls%20of%20Boolean%20Trap&t_d=The%20Pitfalls%20of%20Boolean%20Trap&t_t=The%20Pitfalls%20of%20Boolean%20Trap&s_o=default#)
    - [****](https://disqus.com/embed/comments/?base=default&f=ariya&t_i=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_u=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_e=The%20Pitfalls%20of%20Boolean%20Trap&t_d=The%20Pitfalls%20of%20Boolean%20Trap&t_t=The%20Pitfalls%20of%20Boolean%20Trap&s_o=default#)

![noavatar92.png](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)

Karl  •  [6 years ago](https://ariya.io/2011/08/hall-of-api-shame-boolean-trap#comment-1000448440)

Boolean Traps are only a symptom; the real disease is Boolean Blindness:

[http://existentialtype.word...](http://disq.us/url?url=http%3A%2F%2Fexistentialtype.wordpress.com%2F2011%2F03%2F15%2Fboolean-blindness%2F%3AQ7KU5abRyo27BSa-szm8cvp4Ro4&cuid=1222985)

-

    - [−](https://disqus.com/embed/comments/?base=default&f=ariya&t_i=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_u=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_e=The%20Pitfalls%20of%20Boolean%20Trap&t_d=The%20Pitfalls%20of%20Boolean%20Trap&t_t=The%20Pitfalls%20of%20Boolean%20Trap&s_o=default#)
    - [****](https://disqus.com/embed/comments/?base=default&f=ariya&t_i=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_u=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_e=The%20Pitfalls%20of%20Boolean%20Trap&t_d=The%20Pitfalls%20of%20Boolean%20Trap&t_t=The%20Pitfalls%20of%20Boolean%20Trap&s_o=default#)

![noavatar92.png](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)

patternbuffer  •  [6 years ago](https://ariya.io/2011/08/hall-of-api-shame-boolean-trap#comment-1000411655)

Working link to API Design Principles: [http://qt-project.org/wiki/...](http://disq.us/url?url=http%3A%2F%2Fqt-project.org%2Fwiki%2FAPI-Design-Principles%3Aww56jnn9U6WVkgkbjBnim6ljDNQ&cuid=1222985)

-

    - [−](https://disqus.com/embed/comments/?base=default&f=ariya&t_i=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_u=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_e=The%20Pitfalls%20of%20Boolean%20Trap&t_d=The%20Pitfalls%20of%20Boolean%20Trap&t_t=The%20Pitfalls%20of%20Boolean%20Trap&s_o=default#)
    - [****](https://disqus.com/embed/comments/?base=default&f=ariya&t_i=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_u=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_e=The%20Pitfalls%20of%20Boolean%20Trap&t_d=The%20Pitfalls%20of%20Boolean%20Trap&t_t=The%20Pitfalls%20of%20Boolean%20Trap&s_o=default#)

![noavatar92.png](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)

Hatchre  •  [6 years ago](https://ariya.io/2011/08/hall-of-api-shame-boolean-trap#comment-939010634)

Here's another reason never to use bool in an API:

 [https://news.ycombinator.co...](https://disq.us/url?url=https%3A%2F%2Fnews.ycombinator.com%2Fitem%3Fid%3D4695587%3AsP8WQhO8yxObqv4VlHDYCx2Qqrk&cuid=1222985)

Curl upgraded a bool to an integer flag, but integers and bools are silently converted and Curl's users carried on using an insecure compatibility value without reading the Curl changelog.

    -

        - [−](https://disqus.com/embed/comments/?base=default&f=ariya&t_i=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_u=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_e=The%20Pitfalls%20of%20Boolean%20Trap&t_d=The%20Pitfalls%20of%20Boolean%20Trap&t_t=The%20Pitfalls%20of%20Boolean%20Trap&s_o=default#)
        - [****](https://disqus.com/embed/comments/?base=default&f=ariya&t_i=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_u=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_e=The%20Pitfalls%20of%20Boolean%20Trap&t_d=The%20Pitfalls%20of%20Boolean%20Trap&t_t=The%20Pitfalls%20of%20Boolean%20Trap&s_o=default#)

[![noavatar92.png](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/ryanscheel/)

 [Ryan Scheel](https://disqus.com/by/ryanscheel/)    [*>* Hatchre](https://ariya.io/2011/08/hall-of-api-shame-boolean-trap#comment-939010634)  •  [5 years ago](https://ariya.io/2011/08/hall-of-api-shame-boolean-trap#comment-1531058885)

That's more a reason to not use auto-casting if you can help it.

-

    - [−](https://disqus.com/embed/comments/?base=default&f=ariya&t_i=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_u=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_e=The%20Pitfalls%20of%20Boolean%20Trap&t_d=The%20Pitfalls%20of%20Boolean%20Trap&t_t=The%20Pitfalls%20of%20Boolean%20Trap&s_o=default#)
    - [****](https://disqus.com/embed/comments/?base=default&f=ariya&t_i=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_u=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_e=The%20Pitfalls%20of%20Boolean%20Trap&t_d=The%20Pitfalls%20of%20Boolean%20Trap&t_t=The%20Pitfalls%20of%20Boolean%20Trap&s_o=default#)

![noavatar92.png](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)

Kevin Smith  •  [7 years ago](https://ariya.io/2011/08/hall-of-api-shame-boolean-trap#comment-620384614)

Load of bollocks - the difficulties presented by unnamed parameters (boolean or otherwise) are insignificant compared to the difficulty in providing a consistent and elegant conceptual model.

    -

        - [−](https://disqus.com/embed/comments/?base=default&f=ariya&t_i=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_u=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_e=The%20Pitfalls%20of%20Boolean%20Trap&t_d=The%20Pitfalls%20of%20Boolean%20Trap&t_t=The%20Pitfalls%20of%20Boolean%20Trap&s_o=default#)
        - [****](https://disqus.com/embed/comments/?base=default&f=ariya&t_i=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_u=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_e=The%20Pitfalls%20of%20Boolean%20Trap&t_d=The%20Pitfalls%20of%20Boolean%20Trap&t_t=The%20Pitfalls%20of%20Boolean%20Trap&s_o=default#)

[![noavatar92.png](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/permutator/)

 [Permutator](https://disqus.com/by/permutator/)    [*>* Kevin Smith](https://ariya.io/2011/08/hall-of-api-shame-boolean-trap#comment-620384614)  •  [3 years ago](https://ariya.io/2011/08/hall-of-api-shame-boolean-trap#comment-2834253465)

So what, we should completely ignore them? It's possible to have more than one problem at once, you know.

-

    - [−](https://disqus.com/embed/comments/?base=default&f=ariya&t_i=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_u=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_e=The%20Pitfalls%20of%20Boolean%20Trap&t_d=The%20Pitfalls%20of%20Boolean%20Trap&t_t=The%20Pitfalls%20of%20Boolean%20Trap&s_o=default#)
    - [****](https://disqus.com/embed/comments/?base=default&f=ariya&t_i=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_u=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_e=The%20Pitfalls%20of%20Boolean%20Trap&t_d=The%20Pitfalls%20of%20Boolean%20Trap&t_t=The%20Pitfalls%20of%20Boolean%20Trap&s_o=default#)

![noavatar92.png](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)

Nobody  •  [7 years ago](https://ariya.io/2011/08/hall-of-api-shame-boolean-trap#comment-590078299)

"The nice thing working for Trolltech was (among others) learning the principles behind the good API."

I certainly did not expect to see "Trolltech" (or "Qt") and "good API" in a single sentence (without a bold negation, that is).

If I was to name the worst framework API to ever have worked with I'd certainly go with Qt. No-brainer.

(signed int indexing, lack of text ranges or just good old QRegExp's indexIn() & Co anybody? Sheesh… don't get me started.)

    -

        - [−](https://disqus.com/embed/comments/?base=default&f=ariya&t_i=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_u=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_e=The%20Pitfalls%20of%20Boolean%20Trap&t_d=The%20Pitfalls%20of%20Boolean%20Trap&t_t=The%20Pitfalls%20of%20Boolean%20Trap&s_o=default#)
        - [****](https://disqus.com/embed/comments/?base=default&f=ariya&t_i=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_u=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_e=The%20Pitfalls%20of%20Boolean%20Trap&t_d=The%20Pitfalls%20of%20Boolean%20Trap&t_t=The%20Pitfalls%20of%20Boolean%20Trap&s_o=default#)

[![noavatar92.png](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/ariya/)

 [Ariya Hidayat](https://disqus.com/by/ariya/)  Mod  [*>* Nobody](https://ariya.io/2011/08/hall-of-api-shame-boolean-trap#comment-590078299)  •  [7 years ago](https://ariya.io/2011/08/hall-of-api-shame-boolean-trap#comment-590185217)

That's one data point. But then, everyone's is entitled to his own opinion.

-

    - [−](https://disqus.com/embed/comments/?base=default&f=ariya&t_i=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_u=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_e=The%20Pitfalls%20of%20Boolean%20Trap&t_d=The%20Pitfalls%20of%20Boolean%20Trap&t_t=The%20Pitfalls%20of%20Boolean%20Trap&s_o=default#)
    - [****](https://disqus.com/embed/comments/?base=default&f=ariya&t_i=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_u=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_e=The%20Pitfalls%20of%20Boolean%20Trap&t_d=The%20Pitfalls%20of%20Boolean%20Trap&t_t=The%20Pitfalls%20of%20Boolean%20Trap&s_o=default#)

[![noavatar92.png](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/kamiltoman/)

 [Kamil Toman](https://disqus.com/by/kamiltoman/)    •  [7 years ago](https://ariya.io/2011/08/hall-of-api-shame-boolean-trap#comment-590002794)

This book elaborates on code readability a lot [http://www.lulu.com/shop/an...](http://disq.us/url?url=http%3A%2F%2Fwww.lulu.com%2Fshop%2Fandres-valloud%2Fa-mentoring-course-on-smalltalk%2Fpaperback%2Fproduct-3788890.html%3AwnU8IuhuFsPk86RlRxcKjMW95CA&cuid=1222985)

And it is a great book. Even if not directly applicable to your pet language don't let smalltalk scare you.

-

    - [−](https://disqus.com/embed/comments/?base=default&f=ariya&t_i=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_u=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_e=The%20Pitfalls%20of%20Boolean%20Trap&t_d=The%20Pitfalls%20of%20Boolean%20Trap&t_t=The%20Pitfalls%20of%20Boolean%20Trap&s_o=default#)
    - [****](https://disqus.com/embed/comments/?base=default&f=ariya&t_i=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_u=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_e=The%20Pitfalls%20of%20Boolean%20Trap&t_d=The%20Pitfalls%20of%20Boolean%20Trap&t_t=The%20Pitfalls%20of%20Boolean%20Trap&s_o=default#)

[![noavatar92.png](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/MisinformedDNA/)

 [Dan Friedman](https://disqus.com/by/MisinformedDNA/)    •  [7 years ago](https://ariya.io/2011/08/hall-of-api-shame-boolean-trap#comment-589711470)

If you are concerned with reading code, then the implemented could just create a well-named variable and then pass it into the method. It's not the API that's the problem, it's the implementer. So repaint(isImmediate).

    -

        - [−](https://disqus.com/embed/comments/?base=default&f=ariya&t_i=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_u=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_e=The%20Pitfalls%20of%20Boolean%20Trap&t_d=The%20Pitfalls%20of%20Boolean%20Trap&t_t=The%20Pitfalls%20of%20Boolean%20Trap&s_o=default#)
        - [****](https://disqus.com/embed/comments/?base=default&f=ariya&t_i=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_u=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_e=The%20Pitfalls%20of%20Boolean%20Trap&t_d=The%20Pitfalls%20of%20Boolean%20Trap&t_t=The%20Pitfalls%20of%20Boolean%20Trap&s_o=default#)

[![noavatar92.png](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/ariya/)

 [Ariya Hidayat](https://disqus.com/by/ariya/)  Mod  [*>* Dan Friedman](https://ariya.io/2011/08/hall-of-api-shame-boolean-trap#comment-589711470)  •  [7 years ago](https://ariya.io/2011/08/hall-of-api-shame-boolean-trap#comment-589733036)

A variable looks more a workaround to me, rather than a real solution. But yeah, it works.

-

    - [−](https://disqus.com/embed/comments/?base=default&f=ariya&t_i=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_u=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_e=The%20Pitfalls%20of%20Boolean%20Trap&t_d=The%20Pitfalls%20of%20Boolean%20Trap&t_t=The%20Pitfalls%20of%20Boolean%20Trap&s_o=default#)
    - [****](https://disqus.com/embed/comments/?base=default&f=ariya&t_i=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_u=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_e=The%20Pitfalls%20of%20Boolean%20Trap&t_d=The%20Pitfalls%20of%20Boolean%20Trap&t_t=The%20Pitfalls%20of%20Boolean%20Trap&s_o=default#)

[![noavatar92.png](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/disqus_PbaSqIEIFU/)

 [Tim Rowe](https://disqus.com/by/disqus_PbaSqIEIFU/)    •  [7 years ago](https://ariya.io/2011/08/hall-of-api-shame-boolean-trap#comment-589683121)

Sounds like user error to me. What kind of inexperienced programmer goes around assuming a boolean parameter means "don't do what the function name says it does"?

I would suggest that those still insisting they'd do things as in your update are actually Business Analysts - failed, CompSci drop-outs who couldn't program but still wanted the 6 figure salary.

    -

        - [−](https://disqus.com/embed/comments/?base=default&f=ariya&t_i=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_u=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_e=The%20Pitfalls%20of%20Boolean%20Trap&t_d=The%20Pitfalls%20of%20Boolean%20Trap&t_t=The%20Pitfalls%20of%20Boolean%20Trap&s_o=default#)
        - [****](https://disqus.com/embed/comments/?base=default&f=ariya&t_i=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_u=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_e=The%20Pitfalls%20of%20Boolean%20Trap&t_d=The%20Pitfalls%20of%20Boolean%20Trap&t_t=The%20Pitfalls%20of%20Boolean%20Trap&s_o=default#)

[![noavatar92.png](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/ryanscheel/)

 [Ryan Scheel](https://disqus.com/by/ryanscheel/)    [*>* Tim Rowe](https://ariya.io/2011/08/hall-of-api-shame-boolean-trap#comment-589683121)  •  [5 years ago](https://ariya.io/2011/08/hall-of-api-shame-boolean-trap#comment-1531061821)

Some API developers leave out key words in function names. What should be called `maybe_stop` is called `stop` instead.

    -

        - [−](https://disqus.com/embed/comments/?base=default&f=ariya&t_i=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_u=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_e=The%20Pitfalls%20of%20Boolean%20Trap&t_d=The%20Pitfalls%20of%20Boolean%20Trap&t_t=The%20Pitfalls%20of%20Boolean%20Trap&s_o=default#)
        - [****](https://disqus.com/embed/comments/?base=default&f=ariya&t_i=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_u=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_e=The%20Pitfalls%20of%20Boolean%20Trap&t_d=The%20Pitfalls%20of%20Boolean%20Trap&t_t=The%20Pitfalls%20of%20Boolean%20Trap&s_o=default#)

[![noavatar92.png](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/ariya/)

 [Ariya Hidayat](https://disqus.com/by/ariya/)  Mod  [*>* Tim Rowe](https://ariya.io/2011/08/hall-of-api-shame-boolean-trap#comment-589683121)  •  [7 years ago](https://ariya.io/2011/08/hall-of-api-shame-boolean-trap#comment-589733952)

Don't forget, there are other real-world cases like that stop(true, false). Regardless what the inexperienced programmer assumes, that is still an API design error (from whoever responsible for that).

-

    - [−](https://disqus.com/embed/comments/?base=default&f=ariya&t_i=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_u=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_e=The%20Pitfalls%20of%20Boolean%20Trap&t_d=The%20Pitfalls%20of%20Boolean%20Trap&t_t=The%20Pitfalls%20of%20Boolean%20Trap&s_o=default#)
    - [****](https://disqus.com/embed/comments/?base=default&f=ariya&t_i=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_u=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_e=The%20Pitfalls%20of%20Boolean%20Trap&t_d=The%20Pitfalls%20of%20Boolean%20Trap&t_t=The%20Pitfalls%20of%20Boolean%20Trap&s_o=default#)

![noavatar92.png](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)

\*/  •  [8 years ago](https://ariya.io/2011/08/hall-of-api-shame-boolean-trap#comment-409232769)

great post, but i can't fully agree with first example.
in javascript widget.repaint(false) is usually a user fault
because it should be called as
widget.repaint()
in 99% of places, and
widget.repaint(true) (or maybe even widget.repaint("immediate"))
in the rest.

but you are absolutely right about functions with multiple arguments or balanced usage.

    -

        - [−](https://disqus.com/embed/comments/?base=default&f=ariya&t_i=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_u=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_e=The%20Pitfalls%20of%20Boolean%20Trap&t_d=The%20Pitfalls%20of%20Boolean%20Trap&t_t=The%20Pitfalls%20of%20Boolean%20Trap&s_o=default#)
        - [****](https://disqus.com/embed/comments/?base=default&f=ariya&t_i=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_u=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_e=The%20Pitfalls%20of%20Boolean%20Trap&t_d=The%20Pitfalls%20of%20Boolean%20Trap&t_t=The%20Pitfalls%20of%20Boolean%20Trap&s_o=default#)

![noavatar92.png](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)

ariya  [*>* \*/](https://ariya.io/2011/08/hall-of-api-shame-boolean-trap#comment-409232769)  •  [8 years ago](https://ariya.io/2011/08/hall-of-api-shame-boolean-trap#comment-409276555)

And do you think you would not be confused when you see a line of code which contains that `widget.repaint(true)` ?

        -

            - [−](https://disqus.com/embed/comments/?base=default&f=ariya&t_i=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_u=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_e=The%20Pitfalls%20of%20Boolean%20Trap&t_d=The%20Pitfalls%20of%20Boolean%20Trap&t_t=The%20Pitfalls%20of%20Boolean%20Trap&s_o=default#)

This comment was deleted.

            - [−](https://disqus.com/embed/comments/?base=default&f=ariya&t_i=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_u=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_e=The%20Pitfalls%20of%20Boolean%20Trap&t_d=The%20Pitfalls%20of%20Boolean%20Trap&t_t=The%20Pitfalls%20of%20Boolean%20Trap&s_o=default#)

[Show more replies](https://disqus.com/embed/comments/?base=default&f=ariya&t_i=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_u=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_e=The%20Pitfalls%20of%20Boolean%20Trap&t_d=The%20Pitfalls%20of%20Boolean%20Trap&t_t=The%20Pitfalls%20of%20Boolean%20Trap&s_o=default#)

-

    - [−](https://disqus.com/embed/comments/?base=default&f=ariya&t_i=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_u=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_e=The%20Pitfalls%20of%20Boolean%20Trap&t_d=The%20Pitfalls%20of%20Boolean%20Trap&t_t=The%20Pitfalls%20of%20Boolean%20Trap&s_o=default#)
    - [****](https://disqus.com/embed/comments/?base=default&f=ariya&t_i=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_u=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_e=The%20Pitfalls%20of%20Boolean%20Trap&t_d=The%20Pitfalls%20of%20Boolean%20Trap&t_t=The%20Pitfalls%20of%20Boolean%20Trap&s_o=default#)

![noavatar92.png](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)

Ivan  •  [8 years ago](https://ariya.io/2011/08/hall-of-api-shame-boolean-trap#comment-409232740)

In a well done API, you don´t need read code, just read jsdoc or similar.

    -

        - [−](https://disqus.com/embed/comments/?base=default&f=ariya&t_i=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_u=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_e=The%20Pitfalls%20of%20Boolean%20Trap&t_d=The%20Pitfalls%20of%20Boolean%20Trap&t_t=The%20Pitfalls%20of%20Boolean%20Trap&s_o=default#)
        - [****](https://disqus.com/embed/comments/?base=default&f=ariya&t_i=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_u=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_e=The%20Pitfalls%20of%20Boolean%20Trap&t_d=The%20Pitfalls%20of%20Boolean%20Trap&t_t=The%20Pitfalls%20of%20Boolean%20Trap&s_o=default#)

![noavatar92.png](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)

ariya  [*>* Ivan](https://ariya.io/2011/08/hall-of-api-shame-boolean-trap#comment-409232740)  •  [8 years ago](https://ariya.io/2011/08/hall-of-api-shame-boolean-trap#comment-409276417)

I think what you mean is don't need to look at the source code. That totally misses the point, though. We are not talking about the source code of the API implementation, rather the code which uses the API (whatever it is).

-

    - [−](https://disqus.com/embed/comments/?base=default&f=ariya&t_i=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_u=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_e=The%20Pitfalls%20of%20Boolean%20Trap&t_d=The%20Pitfalls%20of%20Boolean%20Trap&t_t=The%20Pitfalls%20of%20Boolean%20Trap&s_o=default#)
    - [****](https://disqus.com/embed/comments/?base=default&f=ariya&t_i=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_u=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_e=The%20Pitfalls%20of%20Boolean%20Trap&t_d=The%20Pitfalls%20of%20Boolean%20Trap&t_t=The%20Pitfalls%20of%20Boolean%20Trap&s_o=default#)

![noavatar92.png](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)

Jeremy  •  [8 years ago](https://ariya.io/2011/08/hall-of-api-shame-boolean-trap#comment-409232737)

"may not always have the API documentation handy" - almost every language these days comes with intellisense, and arguments in parameters have names.

Hence this line:
widget.Repaint(false)
Is not that confusing when your programming and you see it expects:
widget.Repaint(bool deferRePaint)

    -

        - [−](https://disqus.com/embed/comments/?base=default&f=ariya&t_i=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_u=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_e=The%20Pitfalls%20of%20Boolean%20Trap&t_d=The%20Pitfalls%20of%20Boolean%20Trap&t_t=The%20Pitfalls%20of%20Boolean%20Trap&s_o=default#)
        - [****](https://disqus.com/embed/comments/?base=default&f=ariya&t_i=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_u=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_e=The%20Pitfalls%20of%20Boolean%20Trap&t_d=The%20Pitfalls%20of%20Boolean%20Trap&t_t=The%20Pitfalls%20of%20Boolean%20Trap&s_o=default#)

![noavatar92.png](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)

ariya  [*>* Jeremy](https://ariya.io/2011/08/hall-of-api-shame-boolean-trap#comment-409232737)  •  [8 years ago](https://ariya.io/2011/08/hall-of-api-shame-boolean-trap#comment-409276415)

This is useful only for *writing* the code. The blog post address the potential issues raised when you **read** the code (for review or other reasons).

-

    - [−](https://disqus.com/embed/comments/?base=default&f=ariya&t_i=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_u=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_e=The%20Pitfalls%20of%20Boolean%20Trap&t_d=The%20Pitfalls%20of%20Boolean%20Trap&t_t=The%20Pitfalls%20of%20Boolean%20Trap&s_o=default#)
    - [****](https://disqus.com/embed/comments/?base=default&f=ariya&t_i=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_u=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_e=The%20Pitfalls%20of%20Boolean%20Trap&t_d=The%20Pitfalls%20of%20Boolean%20Trap&t_t=The%20Pitfalls%20of%20Boolean%20Trap&s_o=default#)

![noavatar92.png](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)

Mark  •  [8 years ago](https://ariya.io/2011/08/hall-of-api-shame-boolean-trap#comment-409232736)

Not to mention that booleans (duh!) only handle two states. Im not sure how often, during development, Ive found that two states werent enough. You can make do with overloads, but Ive found its better to use enums up front.

-

    - [−](https://disqus.com/embed/comments/?base=default&f=ariya&t_i=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_u=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_e=The%20Pitfalls%20of%20Boolean%20Trap&t_d=The%20Pitfalls%20of%20Boolean%20Trap&t_t=The%20Pitfalls%20of%20Boolean%20Trap&s_o=default#)
    - [****](https://disqus.com/embed/comments/?base=default&f=ariya&t_i=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_u=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_e=The%20Pitfalls%20of%20Boolean%20Trap&t_d=The%20Pitfalls%20of%20Boolean%20Trap&t_t=The%20Pitfalls%20of%20Boolean%20Trap&s_o=default#)

![noavatar92.png](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)

metator  •  [8 years ago](https://ariya.io/2011/08/hall-of-api-shame-boolean-trap#comment-409232735)

Very interesting, Ariya!

I come from the managed languages world (C#, Java) but decided to take a look at Qt this summer, just for fun. Pretty look stuff (and very well documented)! And you are absolutely right - code should speak for itself and those design principles you've mentioned are probably the reason why everyone who tries Qt, becomes fond of it.

To add another example of good API design principles, take a look at NUnit, an unit test framework for C#. It's designed in such a way that you can almost read the code like it was written in English.

Regards

-

    - [−](https://disqus.com/embed/comments/?base=default&f=ariya&t_i=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_u=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_e=The%20Pitfalls%20of%20Boolean%20Trap&t_d=The%20Pitfalls%20of%20Boolean%20Trap&t_t=The%20Pitfalls%20of%20Boolean%20Trap&s_o=default#)
    - [****](https://disqus.com/embed/comments/?base=default&f=ariya&t_i=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_u=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_e=The%20Pitfalls%20of%20Boolean%20Trap&t_d=The%20Pitfalls%20of%20Boolean%20Trap&t_t=The%20Pitfalls%20of%20Boolean%20Trap&s_o=default#)

![noavatar92.png](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)

Rob G  •  [8 years ago](https://ariya.io/2011/08/hall-of-api-shame-boolean-trap#comment-409232732)

That's one thing I like about the Smalltalk family of languages the style of calls being keyword-value pairs means every parameter is documented:

account receive: amount from: source

makes it quite clear what the parameters are. It would force you to rethink the name in the instances you cite, quite correctly.

-

    - [−](https://disqus.com/embed/comments/?base=default&f=ariya&t_i=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_u=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_e=The%20Pitfalls%20of%20Boolean%20Trap&t_d=The%20Pitfalls%20of%20Boolean%20Trap&t_t=The%20Pitfalls%20of%20Boolean%20Trap&s_o=default#)
    - [****](https://disqus.com/embed/comments/?base=default&f=ariya&t_i=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_u=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_e=The%20Pitfalls%20of%20Boolean%20Trap&t_d=The%20Pitfalls%20of%20Boolean%20Trap&t_t=The%20Pitfalls%20of%20Boolean%20Trap&s_o=default#)

![noavatar92.png](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)

SergueiS  •  [8 years ago](https://ariya.io/2011/08/hall-of-api-shame-boolean-trap#comment-409232729)

Authors, don't pretend to be politically correct!

You refer to a programmer as "she" while the only photo in the article is a male one!

Not mentioning that among the last 100 programmers I worked with in various companies in various countries, the women were... none.

    -

        - [−](https://disqus.com/embed/comments/?base=default&f=ariya&t_i=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_u=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_e=The%20Pitfalls%20of%20Boolean%20Trap&t_d=The%20Pitfalls%20of%20Boolean%20Trap&t_t=The%20Pitfalls%20of%20Boolean%20Trap&s_o=default#)
        - [****](https://disqus.com/embed/comments/?base=default&f=ariya&t_i=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_u=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_e=The%20Pitfalls%20of%20Boolean%20Trap&t_d=The%20Pitfalls%20of%20Boolean%20Trap&t_t=The%20Pitfalls%20of%20Boolean%20Trap&s_o=default#)

![noavatar92.png](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)

ariya  [*>* SergueiS](https://ariya.io/2011/08/hall-of-api-shame-boolean-trap#comment-409232729)  •  [8 years ago](https://ariya.io/2011/08/hall-of-api-shame-boolean-trap#comment-409276409)

Please read my other reply on the same subject.

-

    - [−](https://disqus.com/embed/comments/?base=default&f=ariya&t_i=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_u=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_e=The%20Pitfalls%20of%20Boolean%20Trap&t_d=The%20Pitfalls%20of%20Boolean%20Trap&t_t=The%20Pitfalls%20of%20Boolean%20Trap&s_o=default#)
    - [****](https://disqus.com/embed/comments/?base=default&f=ariya&t_i=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_u=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_e=The%20Pitfalls%20of%20Boolean%20Trap&t_d=The%20Pitfalls%20of%20Boolean%20Trap&t_t=The%20Pitfalls%20of%20Boolean%20Trap&s_o=default#)

![noavatar92.png](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)

Coding since birth  •  [8 years ago](https://ariya.io/2011/08/hall-of-api-shame-boolean-trap#comment-409232730)

Here is the sad but true fact of the matter. We all “F” up while programming. If you are a designer programmer it is different that being a programmer who follows what others tell them to do. When I have to design it all from scratch (Which often includes things such a companies internal business procedures) I will start programming after extensive thought and then I put in some arbitrary statements to work through a programming issue. Often there are many aspects of a project that the temporary arbitrary bool variable unfortunately gets used in. It is left in not so much from negligence but rather dependency. Most of the time this has zero significance. But then there are the other times when that code graduates to the next level and others have to deal with the arbitrary vars at a much later date when someone decides to expand on what I started.

Most companies, when given the choice, will forgo the extra expense of fixing arbitrary variables and documenting coding. What’s a programmers to do?

It is sad but true that we should not do these sorts of things as programmers, but we do. Sadly we get trapped using arbitrary code which at the particular moment made perfect sense to trouble shoot the issue at hand, but later got too deep to effectively change it.

Let us all try a little harder to be more specific and adopt better Boolean habits and then maybe future generations of programmers will not have to not not try to figure out what the $#&*! is intended.

-

    - [−](https://disqus.com/embed/comments/?base=default&f=ariya&t_i=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_u=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_e=The%20Pitfalls%20of%20Boolean%20Trap&t_d=The%20Pitfalls%20of%20Boolean%20Trap&t_t=The%20Pitfalls%20of%20Boolean%20Trap&s_o=default#)
    - [****](https://disqus.com/embed/comments/?base=default&f=ariya&t_i=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_u=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_e=The%20Pitfalls%20of%20Boolean%20Trap&t_d=The%20Pitfalls%20of%20Boolean%20Trap&t_t=The%20Pitfalls%20of%20Boolean%20Trap&s_o=default#)

![noavatar92.png](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)

Chiko  •  [8 years ago](https://ariya.io/2011/08/hall-of-api-shame-boolean-trap#comment-409232726)

Every time I review code and see bool arguments, I recommend developers to use enums, multiple apis instead. But most of them don't listen as bool is easier to implement. I think I need to forward this article to all these guys.thanks. As well, I think it not just about Apis for others. All interface methods should follow this rule.

[Load more comments](https://disqus.com/embed/comments/?base=default&f=ariya&t_i=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_u=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_e=The%20Pitfalls%20of%20Boolean%20Trap&t_d=The%20Pitfalls%20of%20Boolean%20Trap&t_t=The%20Pitfalls%20of%20Boolean%20Trap&s_o=default#)

## Also on **ariya.io**

- [

### Building iOS Apps on Azure Pipelines

    - 1 comment •

    - 3 months ago

[vikrant—is apple certificate is mandatory to build ios app project in azure devops](https://disq.us/?url=https%3A%2F%2Fariya.io%2F2019%2F02%2Fbuilding-ios-apps-on-azure-pipelines&key=-3el5RvMgWUYfB1GimKcjA)](https://disq.us/?url=https%3A%2F%2Fariya.io%2F2019%2F02%2Fbuilding-ios-apps-on-azure-pipelines&key=-3el5RvMgWUYfB1GimKcjA)

- [

### Anatomy of a Bug Report

    - 1 comment •

    - 3 years ago

[Phil— I love your tweets and blogs. In our current time, can you say that a bug is when all unit and/or integration and/or BDD test pass when they ought not to? Human testing is …](https://disq.us/?url=https%3A%2F%2Fariya.io%2F2016%2F09%2Fanatomy-of-a-bug-report&key=P-G8pHwVNDWbc0rdupyPMw)](https://disq.us/?url=https%3A%2F%2Fariya.io%2F2016%2F09%2Fanatomy-of-a-bug-report&key=P-G8pHwVNDWbc0rdupyPMw)

- [

### Upgrading to HTTPS with stunnel

    - 1 comment •

    - 2 years ago

[BOB CAT—balik ke indonesia om , ajarin kami](https://disq.us/?url=https%3A%2F%2Fariya.io%2F2017%2F08%2Fupgrading-to-https-with-stunnel&key=F-l4T5vFkj_XuQd_ZdcmHQ)](https://disq.us/?url=https%3A%2F%2Fariya.io%2F2017%2F08%2Fupgrading-to-https-with-stunnel&key=F-l4T5vFkj_XuQd_ZdcmHQ)

- [

### Syntax Highlighting in the Terminal

    - 1 comment •

    - 3 years ago

[kun luo—Nice post.](https://disq.us/?url=https%3A%2F%2Fariya.io%2F2016%2F11%2Fsyntax-highlighting-in-the-terminal&key=8vMwtl3wwPxsmSb56QYR6A)](https://disq.us/?url=https%3A%2F%2Fariya.io%2F2016%2F11%2Fsyntax-highlighting-in-the-terminal&key=8vMwtl3wwPxsmSb56QYR6A)

- [Powered by Disqus](https://disqus.com/)
- [*✉*Subscribe*✔*](https://disqus.com/embed/comments/?base=default&f=ariya&t_i=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_u=https%3A%2F%2Fariya.io%2F2011%2F08%2Fhall-of-api-shame-boolean-trap&t_e=The%20Pitfalls%20of%20Boolean%20Trap&t_d=The%20Pitfalls%20of%20Boolean%20Trap&t_t=The%20Pitfalls%20of%20Boolean%20Trap&s_o=default#)
- [*d*Add Disqus to your site](https://publishers.disqus.com/engage?utm_source=ariya&utm_medium=Disqus-Footer)
- [**Disqus' Privacy Policy](https://help.disqus.com/customer/portal/articles/466259-privacy-policy)