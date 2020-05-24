Linting HTML using CSS

# Linting HTML using CSS

 Date  ** Mar 07, 2017

 Tags  **  [html](https://bitsofco.de/tag/html/), [css](https://bitsofco.de/tag/css/)

When HTML is written incorrectly, nothing much happens. Because of this, it's easy to have invalid, unsemantic, or unaccessible bits in markup without it being obvious.

There are many ways we can lint our HTML to discover and fix these issues, for example using the [W3C Markup Validation Service](https://validator.w3.org/). Another thing we can do, which can be more easily integrated into a development workflow, is to use some slightly advanced CSS selectors to highlight potential problem areas. Here are a few things we can use CSS selectors to help us catch out.

## Inline Styles

CSS

	*[style] {
	    border: 5px solid red; /* Style to make the elements noticeable */
	}

This selector will target any element on the page that has inline styles applied to it. As a general rule, inline styles should be avoided as they are difficult to override due to their increased level of specificity. Although inline styles may be necessary in some cases, this selector will help highlight them so a decision can be made on a case-by-case basis.

With the problem elements selected, we can apply any style to make them more visibly obvious on the page, e.g. a big red border.

## Faulty or Missing Link Targets

CSS

	a:not([href]),
	a[href="#"],
	a[href=""],
	a[href*="javascript:void(0)"] { … }

These selectors will highlight any anchor elements that either do not have any `href` attribute at all, or have a meaningless one.

## Unaccessible Images

CSS

	img:not([alt]) { ... }

As a blanket rule, [all images should have an `alt` attribute](https://bitsofco.de/alternative-text-and-images/). When this attribute is missing, most screenreaders will read out the value of the `src` attribute instead which, of course, is not useful to the user and can in fact be confusing.

It should be noted that the above selector will not select images with a null/empty `alt` attribute, i.e. images with `alt=""`. This is because a null `alt` attribute can be an intentional way of having a screen reader skip over the image, which is useful if, for example, the image is purely decorative. It could, however, still be useful to have these highlighted, which we can do with the following selector -

CSS

	img[alt=""] { ... }

## Missing Document Language

CSS

	html:not([lang]),
	html[lang=""] { ... }

An important attribute that should be present on all `html` elements is the language attribute. This attribute is a signal to screen readers what language the page is in, which can determine how the content of the page is read aloud.

Here's an example of what can happen when the `lang` attribute is missing -

## Incorrect Character Set

CSS

	meta[charset]:not([charset="UTF-8"]) { ... }

This selector targets any meta character set tag that is not set to `UTF-8`. This tag tells the browser to use the UTF-8 form of character encoding, which is presently the recommended form for HTML documents. Having this tag is therefore [required for valid HTML](http://validator.w3.org/docs/help.html#faq-charset).

Ideally, this tag should also be the first element after the opening `<head>` tag. We can check for this using the following selector -

CSS

	meta[charset="UTF-8"]:not(:first-child) { ... }

## Unaccessible Viewport Attributes

CSS

	meta[name="viewport"][content*="user-scalable=no"],
	meta[name="viewport"][content*="maximum-scale"],
	meta[name="viewport"][content*="minimum-scale"] { ... }

This selector can be used to highlight unaccessible viewport meta attributes. It is generally advised that we avoid restricting the user's ability to manipulate the viewport by shrinking and enlarging it. So, using `user-scalable=no`, `maximum-scale`, or `minimum-scale` should never be used.

## Unlabelled Form Elements

CSS

	input:not([id]),
	select:not([id]),
	textarea:not([id]) { ... }

	label:not([for]) { ... }

Form elements are perhaps the most important elements when it comes to labelling. Although there are [several ways to label a form element](https://bitsofco.de/labelling-form-elements/), the most common way is by having an ID on the element that is referenced by a label element. The above selector checks for form elements that do not have an ID, and label elements that are not explicitly linked to a form element using the `for` attribute.

Another type of labelling that is important for form elements is via the `name` attribute. While the `id` attribute is used for labelling the element in the context of the HTML document, the `name` attribute is used to reference the the element when submitted with the form data.

CSS

	input:not([name]),
	select:not([name]),
	textarea:not([name]) { ... }

Additionally, besides the form elements themselves, it is useful to give the form element itself a name and/or id.

CSS

	form:not([name]):not([id]) { ... }

This selector will highlight any form element that is missing both `name` and `id` attributes.

## Empty Interactive Elements

CSS

	button:empty,
	a:empty { ... }

Interactive elements like links or buttons are typically labelled by their content. Although it is possible to label these elements using other methods, such as an `aria-label` attribute, having them be empty is likely a sign of something wrong. This selector will highlight any links of buttons that have no HTML content inside them.

## Unnecessary or Deprecated Attributes

CSS

	script[type="text/javascript"],
	link[rel="stylesheet"][type="text/css"] { ... }

Finally, we can use CSS selectors to highlight attributes in our HTML that are deprecated or no longer needed.

**Edit (14/03/2017)**: To apply this concept, I made a [Chrome Extension](https://chrome.google.com/webstore/detail/alix-for-chrome/aepmadgjacfjcneccddiccnkbpimobge). I wrote about it in my followup post, [Making Alix, a Chrome Extension for Linting HTML](https://bitsofco.de/making-alix-a-chrome-extension-for-linting-html/)

- [** Share on Twitter](https://twitter.com/intent/tweet/?text=%27Linting%20HTML%20using%20CSS%27%20from%20bitsofco.de&url=https://bitsofco.de/linting-html-using-css/&via=ireaderinokun)
- [** Share on Facebook](https://www.facebook.com/sharer/sharer.php?u=https://bitsofco.de/linting-html-using-css/)
- [** Post to Reddit](https://www.reddit.com/submit?url=https://bitsofco.de/linting-html-using-css/)

#### [Asynchronous vs Deferred JavaScript](https://bitsofco.de/async-vs-defer/)

 Previous

### [Making Alix, a Chrome Extension for Linting HTML](https://bitsofco.de/making-alix-a-chrome-extension-for-linting-html/)

 Next

- [66 comments]()
- [**bitsofcode**](https://disqus.com/home/forums/bitsofcode/)
- [Login](https://disqus.com/embed/comments/?base=default&version=60c69418f14a8b7401cd956e1062204c&f=bitsofcode&t_i=%2Flinting-html-using-css%2F&t_u=https%3A%2F%2Fbitsofco.de%2Flinting-html-using-css%2F&t_d=Linting%20HTML%20using%20CSS&t_t=Linting%20HTML%20using%20CSS&s_o=default#)
- [1](https://disqus.com/home/inbox/)
- [ Recommend10](https://disqus.com/embed/comments/?base=default&version=60c69418f14a8b7401cd956e1062204c&f=bitsofcode&t_i=%2Flinting-html-using-css%2F&t_u=https%3A%2F%2Fbitsofco.de%2Flinting-html-using-css%2F&t_d=Linting%20HTML%20using%20CSS&t_t=Linting%20HTML%20using%20CSS&s_o=default#)
- [⤤Share](https://disqus.com/embed/comments/?base=default&version=60c69418f14a8b7401cd956e1062204c&f=bitsofcode&t_i=%2Flinting-html-using-css%2F&t_u=https%3A%2F%2Fbitsofco.de%2Flinting-html-using-css%2F&t_d=Linting%20HTML%20using%20CSS&t_t=Linting%20HTML%20using%20CSS&s_o=default#)
- [Sort by Best](https://disqus.com/embed/comments/?base=default&version=60c69418f14a8b7401cd956e1062204c&f=bitsofcode&t_i=%2Flinting-html-using-css%2F&t_u=https%3A%2F%2Fbitsofco.de%2Flinting-html-using-css%2F&t_d=Linting%20HTML%20using%20CSS&t_t=Linting%20HTML%20using%20CSS&s_o=default#)

![Avatar](../_resources/7b2fde640943965cc88df0cdee365907.png)
Join the discussion…

- [Attach](https://disqus.com/embed/comments/?base=default&version=60c69418f14a8b7401cd956e1062204c&f=bitsofcode&t_i=%2Flinting-html-using-css%2F&t_u=https%3A%2F%2Fbitsofco.de%2Flinting-html-using-css%2F&t_d=Linting%20HTML%20using%20CSS&t_t=Linting%20HTML%20using%20CSS&s_o=default#)

-

    - [−](https://disqus.com/embed/comments/?base=default&version=60c69418f14a8b7401cd956e1062204c&f=bitsofcode&t_i=%2Flinting-html-using-css%2F&t_u=https%3A%2F%2Fbitsofco.de%2Flinting-html-using-css%2F&t_d=Linting%20HTML%20using%20CSS&t_t=Linting%20HTML%20using%20CSS&s_o=default#)
    - [*⚑*](https://disqus.com/embed/comments/?base=default&version=60c69418f14a8b7401cd956e1062204c&f=bitsofcode&t_i=%2Flinting-html-using-css%2F&t_u=https%3A%2F%2Fbitsofco.de%2Flinting-html-using-css%2F&t_d=Linting%20HTML%20using%20CSS&t_t=Linting%20HTML%20using%20CSS&s_o=default#)

[![Avatar](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/robertadrianbogdan/)

[Robert Adrian Bogdan](https://disqus.com/by/robertadrianbogdan/)•[7 days ago](https://bitsofco.de/linting-html-using-css/#comment-3194960068)

a:not([href])
a:[href="#"],
a:[href=""],
a[href*="javascript:void(0)"] { … }
Second and third line are wrong . Peace.

    -

        - [−](https://disqus.com/embed/comments/?base=default&version=60c69418f14a8b7401cd956e1062204c&f=bitsofcode&t_i=%2Flinting-html-using-css%2F&t_u=https%3A%2F%2Fbitsofco.de%2Flinting-html-using-css%2F&t_d=Linting%20HTML%20using%20CSS&t_t=Linting%20HTML%20using%20CSS&s_o=default#)
        - [*⚑*](https://disqus.com/embed/comments/?base=default&version=60c69418f14a8b7401cd956e1062204c&f=bitsofcode&t_i=%2Flinting-html-using-css%2F&t_u=https%3A%2F%2Fbitsofco.de%2Flinting-html-using-css%2F&t_d=Linting%20HTML%20using%20CSS&t_t=Linting%20HTML%20using%20CSS&s_o=default#)

![Avatar](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)

Damian[*>* Robert Adrian Bogdan](https://bitsofco.de/linting-html-using-css/#comment-3194960068)•[5 days ago](https://bitsofco.de/linting-html-using-css/#comment-3200183593)

And also missing comma after the first rule.

    -

        - [−](https://disqus.com/embed/comments/?base=default&version=60c69418f14a8b7401cd956e1062204c&f=bitsofcode&t_i=%2Flinting-html-using-css%2F&t_u=https%3A%2F%2Fbitsofco.de%2Flinting-html-using-css%2F&t_d=Linting%20HTML%20using%20CSS&t_t=Linting%20HTML%20using%20CSS&s_o=default#)
        - [*⚑*](https://disqus.com/embed/comments/?base=default&version=60c69418f14a8b7401cd956e1062204c&f=bitsofcode&t_i=%2Flinting-html-using-css%2F&t_u=https%3A%2F%2Fbitsofco.de%2Flinting-html-using-css%2F&t_d=Linting%20HTML%20using%20CSS&t_t=Linting%20HTML%20using%20CSS&s_o=default#)

[![Avatar](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/ireaderinokun/)

[Ire Aderinokun](https://disqus.com/by/ireaderinokun/)Mod[*>* Robert Adrian Bogdan](https://bitsofco.de/linting-html-using-css/#comment-3194960068)•[6 days ago](https://bitsofco.de/linting-html-using-css/#comment-3198266685)

Thanks, I've fixed this!

    -

        - [−](https://disqus.com/embed/comments/?base=default&version=60c69418f14a8b7401cd956e1062204c&f=bitsofcode&t_i=%2Flinting-html-using-css%2F&t_u=https%3A%2F%2Fbitsofco.de%2Flinting-html-using-css%2F&t_d=Linting%20HTML%20using%20CSS&t_t=Linting%20HTML%20using%20CSS&s_o=default#)
        - [*⚑*](https://disqus.com/embed/comments/?base=default&version=60c69418f14a8b7401cd956e1062204c&f=bitsofcode&t_i=%2Flinting-html-using-css%2F&t_u=https%3A%2F%2Fbitsofco.de%2Flinting-html-using-css%2F&t_d=Linting%20HTML%20using%20CSS&t_t=Linting%20HTML%20using%20CSS&s_o=default#)

[![Avatar](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/claireelaineomalley/)

[Claire-Elaine O'Malley](https://disqus.com/by/claireelaineomalley/)[*>* Robert Adrian Bogdan](https://bitsofco.de/linting-html-using-css/#comment-3194960068)•[7 days ago](https://bitsofco.de/linting-html-using-css/#comment-3194978614)

Why are they "wrong"? A link with href of # or empty href is going to cause trouble for many Assistive Technology (AT).

        -

            - [−](https://disqus.com/embed/comments/?base=default&version=60c69418f14a8b7401cd956e1062204c&f=bitsofcode&t_i=%2Flinting-html-using-css%2F&t_u=https%3A%2F%2Fbitsofco.de%2Flinting-html-using-css%2F&t_d=Linting%20HTML%20using%20CSS&t_t=Linting%20HTML%20using%20CSS&s_o=default#)
            - [*⚑*](https://disqus.com/embed/comments/?base=default&version=60c69418f14a8b7401cd956e1062204c&f=bitsofcode&t_i=%2Flinting-html-using-css%2F&t_u=https%3A%2F%2Fbitsofco.de%2Flinting-html-using-css%2F&t_d=Linting%20HTML%20using%20CSS&t_t=Linting%20HTML%20using%20CSS&s_o=default#)

[![Avatar](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/robertadrianbogdan/)

[Robert Adrian Bogdan](https://disqus.com/by/robertadrianbogdan/)[*>* Claire-Elaine O'Malley](https://bitsofco.de/linting-html-using-css/#comment-3194978614)•[7 days ago](https://bitsofco.de/linting-html-using-css/#comment-3195814502)

Wrong version of css:
a:[href="#"],
a:[href=""] {}
Right version of css :
a[href="#"],
a[href=""]{} . Have an nice day !

        -

            - [−](https://disqus.com/embed/comments/?base=default&version=60c69418f14a8b7401cd956e1062204c&f=bitsofcode&t_i=%2Flinting-html-using-css%2F&t_u=https%3A%2F%2Fbitsofco.de%2Flinting-html-using-css%2F&t_d=Linting%20HTML%20using%20CSS&t_t=Linting%20HTML%20using%20CSS&s_o=default#)
            - [*⚑*](https://disqus.com/embed/comments/?base=default&version=60c69418f14a8b7401cd956e1062204c&f=bitsofcode&t_i=%2Flinting-html-using-css%2F&t_u=https%3A%2F%2Fbitsofco.de%2Flinting-html-using-css%2F&t_d=Linting%20HTML%20using%20CSS&t_t=Linting%20HTML%20using%20CSS&s_o=default#)

[![Avatar](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/pfernandom/)

[Pedro Marquez Soto](https://disqus.com/by/pfernandom/)[*>* Claire-Elaine O'Malley](https://bitsofco.de/linting-html-using-css/#comment-3194978614)•[5 days ago](https://bitsofco.de/linting-html-using-css/#comment-3199899870)

How do you deal with Single Page Applications? Things like AngularJS or ReactJS relaa lot on links with no href

            -

                - [−](https://disqus.com/embed/comments/?base=default&version=60c69418f14a8b7401cd956e1062204c&f=bitsofcode&t_i=%2Flinting-html-using-css%2F&t_u=https%3A%2F%2Fbitsofco.de%2Flinting-html-using-css%2F&t_d=Linting%20HTML%20using%20CSS&t_t=Linting%20HTML%20using%20CSS&s_o=default#)
                - [*⚑*](https://disqus.com/embed/comments/?base=default&version=60c69418f14a8b7401cd956e1062204c&f=bitsofcode&t_i=%2Flinting-html-using-css%2F&t_u=https%3A%2F%2Fbitsofco.de%2Flinting-html-using-css%2F&t_d=Linting%20HTML%20using%20CSS&t_t=Linting%20HTML%20using%20CSS&s_o=default#)

[![Avatar](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/mttmccb/)

[Matt McCabe](https://disqus.com/by/mttmccb/)[*>* Pedro Marquez Soto](https://bitsofco.de/linting-html-using-css/#comment-3199899870)•[5 days ago](https://bitsofco.de/linting-html-using-css/#comment-3200108323)

Maybe a link tag isn't the best option or if it is then why not have something in the href?, maybe a button is a better choice

            -

                - [−](https://disqus.com/embed/comments/?base=default&version=60c69418f14a8b7401cd956e1062204c&f=bitsofcode&t_i=%2Flinting-html-using-css%2F&t_u=https%3A%2F%2Fbitsofco.de%2Flinting-html-using-css%2F&t_d=Linting%20HTML%20using%20CSS&t_t=Linting%20HTML%20using%20CSS&s_o=default#)
                - [*⚑*](https://disqus.com/embed/comments/?base=default&version=60c69418f14a8b7401cd956e1062204c&f=bitsofcode&t_i=%2Flinting-html-using-css%2F&t_u=https%3A%2F%2Fbitsofco.de%2Flinting-html-using-css%2F&t_d=Linting%20HTML%20using%20CSS&t_t=Linting%20HTML%20using%20CSS&s_o=default#)

[![Avatar](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/ShirtlessKirk/)

[ShirtlessKirk](https://disqus.com/by/ShirtlessKirk/)[*>* Pedro Marquez Soto](https://bitsofco.de/linting-html-using-css/#comment-3199899870)•[4 days ago](https://bitsofco.de/linting-html-using-css/#comment-3200408302)

Exactly: a tags can be anchors (hence the short form) for bookmarks in the document. These explicitly​ do *not* have href attributes (they have name attributes instead) and predate links to other resources.

                -

                    - [−](https://disqus.com/embed/comments/?base=default&version=60c69418f14a8b7401cd956e1062204c&f=bitsofcode&t_i=%2Flinting-html-using-css%2F&t_u=https%3A%2F%2Fbitsofco.de%2Flinting-html-using-css%2F&t_d=Linting%20HTML%20using%20CSS&t_t=Linting%20HTML%20using%20CSS&s_o=default#)
                    - [*⚑*](https://disqus.com/embed/comments/?base=default&version=60c69418f14a8b7401cd956e1062204c&f=bitsofcode&t_i=%2Flinting-html-using-css%2F&t_u=https%3A%2F%2Fbitsofco.de%2Flinting-html-using-css%2F&t_d=Linting%20HTML%20using%20CSS&t_t=Linting%20HTML%20using%20CSS&s_o=default#)

[![Avatar](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/xiugraag/)

[Steve Hansen](https://disqus.com/by/xiugraag/)[*>* ShirtlessKirk](https://bitsofco.de/linting-html-using-css/#comment-3200408302)•[3 days ago](https://bitsofco.de/linting-html-using-css/#comment-3201965596)

Since HTML5 this is no longer true (and the use is deprecated), any element can have an id that can be referenced using #id

[https://www.w3schools.com/t...](https://disq.us/url?url=https%3A%2F%2Fwww.w3schools.com%2Ftags%2Fatt_a_name.asp%3AJukd3CI5YKWEZugll8cm8I4mlag&cuid=3490249)

            -

                - [−](https://disqus.com/embed/comments/?base=default&version=60c69418f14a8b7401cd956e1062204c&f=bitsofcode&t_i=%2Flinting-html-using-css%2F&t_u=https%3A%2F%2Fbitsofco.de%2Flinting-html-using-css%2F&t_d=Linting%20HTML%20using%20CSS&t_t=Linting%20HTML%20using%20CSS&s_o=default#)
                - [*⚑*](https://disqus.com/embed/comments/?base=default&version=60c69418f14a8b7401cd956e1062204c&f=bitsofcode&t_i=%2Flinting-html-using-css%2F&t_u=https%3A%2F%2Fbitsofco.de%2Flinting-html-using-css%2F&t_d=Linting%20HTML%20using%20CSS&t_t=Linting%20HTML%20using%20CSS&s_o=default#)

[![Avatar](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/claireelaineomalley/)

[Claire-Elaine O'Malley](https://disqus.com/by/claireelaineomalley/)[*>* Pedro Marquez Soto](https://bitsofco.de/linting-html-using-css/#comment-3199899870)•[a day ago](https://bitsofco.de/linting-html-using-css/#comment-3205919165)

You use a button. As a general rule, if an element performs action that is not navigation, it is a button. <button type="button"> will get you far in SPA.

-

    - [−](https://disqus.com/embed/comments/?base=default&version=60c69418f14a8b7401cd956e1062204c&f=bitsofcode&t_i=%2Flinting-html-using-css%2F&t_u=https%3A%2F%2Fbitsofco.de%2Flinting-html-using-css%2F&t_d=Linting%20HTML%20using%20CSS&t_t=Linting%20HTML%20using%20CSS&s_o=default#)
    - [*⚑*](https://disqus.com/embed/comments/?base=default&version=60c69418f14a8b7401cd956e1062204c&f=bitsofcode&t_i=%2Flinting-html-using-css%2F&t_u=https%3A%2F%2Fbitsofco.de%2Flinting-html-using-css%2F&t_d=Linting%20HTML%20using%20CSS&t_t=Linting%20HTML%20using%20CSS&s_o=default#)

[![Avatar](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/ashley_sheridan/)

[Ashley Sheridan](https://disqus.com/by/ashley_sheridan/)•[4 days ago](https://bitsofco.de/linting-html-using-css/#comment-3200496952)

This reminds me of a comment from Jamie Zawinski:
Some people, when confronted with a problem, think
“I know, I'll use regular expressions.” Now they have two problems.

This just smacks of someone knowing CSS and deciding it's good for everything. There are a ton of better tools that can be used to validate HTML, including many command line ones which can be made part of whatever build process you have in place, such as Tidy, or even the W3 validator which is available as source code to run as a local Jar file. CSS is most definitely *not* the tool to use for this task, and it's folly to think it can be.

    -

        - [−](https://disqus.com/embed/comments/?base=default&version=60c69418f14a8b7401cd956e1062204c&f=bitsofcode&t_i=%2Flinting-html-using-css%2F&t_u=https%3A%2F%2Fbitsofco.de%2Flinting-html-using-css%2F&t_d=Linting%20HTML%20using%20CSS&t_t=Linting%20HTML%20using%20CSS&s_o=default#)
        - [*⚑*](https://disqus.com/embed/comments/?base=default&version=60c69418f14a8b7401cd956e1062204c&f=bitsofcode&t_i=%2Flinting-html-using-css%2F&t_u=https%3A%2F%2Fbitsofco.de%2Flinting-html-using-css%2F&t_d=Linting%20HTML%20using%20CSS&t_t=Linting%20HTML%20using%20CSS&s_o=default#)

[![Avatar](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/luke_pacholski/)

[Luke Pacholski](https://disqus.com/by/luke_pacholski/)[*>* Ashley Sheridan](https://bitsofco.de/linting-html-using-css/#comment-3200496952)•[a day ago](https://bitsofco.de/linting-html-using-css/#comment-3206224545)

In our case, we're trying to think of ways to help beginners write better HTML in an editor, and this seems like a light-weight way to add some of that functionality. While we can integrate some linters, the errors messages are often not helpful for novices. So anyway, this seems pretty cool for some light-weight uses like ours.

-

    - [−](https://disqus.com/embed/comments/?base=default&version=60c69418f14a8b7401cd956e1062204c&f=bitsofcode&t_i=%2Flinting-html-using-css%2F&t_u=https%3A%2F%2Fbitsofco.de%2Flinting-html-using-css%2F&t_d=Linting%20HTML%20using%20CSS&t_t=Linting%20HTML%20using%20CSS&s_o=default#)
    - [*⚑*](https://disqus.com/embed/comments/?base=default&version=60c69418f14a8b7401cd956e1062204c&f=bitsofcode&t_i=%2Flinting-html-using-css%2F&t_u=https%3A%2F%2Fbitsofco.de%2Flinting-html-using-css%2F&t_d=Linting%20HTML%20using%20CSS&t_t=Linting%20HTML%20using%20CSS&s_o=default#)

[![Avatar](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/rajveersaini/)

[rajveer saini](https://disqus.com/by/rajveersaini/)•[8 days ago](https://bitsofco.de/linting-html-using-css/#comment-3193957549)

Thanks for share useful tips and trick !!!

    -

        - [−](https://disqus.com/embed/comments/?base=default&version=60c69418f14a8b7401cd956e1062204c&f=bitsofcode&t_i=%2Flinting-html-using-css%2F&t_u=https%3A%2F%2Fbitsofco.de%2Flinting-html-using-css%2F&t_d=Linting%20HTML%20using%20CSS&t_t=Linting%20HTML%20using%20CSS&s_o=default#)
        - [*⚑*](https://disqus.com/embed/comments/?base=default&version=60c69418f14a8b7401cd956e1062204c&f=bitsofcode&t_i=%2Flinting-html-using-css%2F&t_u=https%3A%2F%2Fbitsofco.de%2Flinting-html-using-css%2F&t_d=Linting%20HTML%20using%20CSS&t_t=Linting%20HTML%20using%20CSS&s_o=default#)

[![Avatar](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/ireaderinokun/)

[Ire Aderinokun](https://disqus.com/by/ireaderinokun/)Mod[*>* rajveer saini](https://bitsofco.de/linting-html-using-css/#comment-3193957549)•[8 days ago](https://bitsofco.de/linting-html-using-css/#comment-3194090290)

You're welcome :)

-

    - [−](https://disqus.com/embed/comments/?base=default&version=60c69418f14a8b7401cd956e1062204c&f=bitsofcode&t_i=%2Flinting-html-using-css%2F&t_u=https%3A%2F%2Fbitsofco.de%2Flinting-html-using-css%2F&t_d=Linting%20HTML%20using%20CSS&t_t=Linting%20HTML%20using%20CSS&s_o=default#)
    - [*⚑*](https://disqus.com/embed/comments/?base=default&version=60c69418f14a8b7401cd956e1062204c&f=bitsofcode&t_i=%2Flinting-html-using-css%2F&t_u=https%3A%2F%2Fbitsofco.de%2Flinting-html-using-css%2F&t_d=Linting%20HTML%20using%20CSS&t_t=Linting%20HTML%20using%20CSS&s_o=default#)

![Avatar](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)

lendk•[8 days ago](https://bitsofco.de/linting-html-using-css/#comment-3193267009)

I kinda modified your code to a usable state and posted it on github, is that ok with you ?

[https://github.com/lendk/Li...](https://disq.us/url?url=https%3A%2F%2Fgithub.com%2Flendk%2FLint-HTML-with-SCSS-CSS%3AeghwGqGjEsab17x-imzYaOIB1Jc&cuid=3490249)

    -

        - [−](https://disqus.com/embed/comments/?base=default&version=60c69418f14a8b7401cd956e1062204c&f=bitsofcode&t_i=%2Flinting-html-using-css%2F&t_u=https%3A%2F%2Fbitsofco.de%2Flinting-html-using-css%2F&t_d=Linting%20HTML%20using%20CSS&t_t=Linting%20HTML%20using%20CSS&s_o=default#)
        - [*⚑*](https://disqus.com/embed/comments/?base=default&version=60c69418f14a8b7401cd956e1062204c&f=bitsofcode&t_i=%2Flinting-html-using-css%2F&t_u=https%3A%2F%2Fbitsofco.de%2Flinting-html-using-css%2F&t_d=Linting%20HTML%20using%20CSS&t_t=Linting%20HTML%20using%20CSS&s_o=default#)

[![Avatar](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/ireaderinokun/)

[Ire Aderinokun](https://disqus.com/by/ireaderinokun/)Mod[*>* lendk](https://bitsofco.de/linting-html-using-css/#comment-3193267009)•[8 days ago](https://bitsofco.de/linting-html-using-css/#comment-3194090379)

That's fine with me

-

    - [−](https://disqus.com/embed/comments/?base=default&version=60c69418f14a8b7401cd956e1062204c&f=bitsofcode&t_i=%2Flinting-html-using-css%2F&t_u=https%3A%2F%2Fbitsofco.de%2Flinting-html-using-css%2F&t_d=Linting%20HTML%20using%20CSS&t_t=Linting%20HTML%20using%20CSS&s_o=default#)
    - [*⚑*](https://disqus.com/embed/comments/?base=default&version=60c69418f14a8b7401cd956e1062204c&f=bitsofcode&t_i=%2Flinting-html-using-css%2F&t_u=https%3A%2F%2Fbitsofco.de%2Flinting-html-using-css%2F&t_d=Linting%20HTML%20using%20CSS&t_t=Linting%20HTML%20using%20CSS&s_o=default#)

[![Avatar](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/disqus_Nmiim2UfXr/)

[star2017](https://disqus.com/by/disqus_Nmiim2UfXr/)•[9 days ago](https://bitsofco.de/linting-html-using-css/#comment-3190957423)

Thanks Ire, good material as always

    -

        - [−](https://disqus.com/embed/comments/?base=default&version=60c69418f14a8b7401cd956e1062204c&f=bitsofcode&t_i=%2Flinting-html-using-css%2F&t_u=https%3A%2F%2Fbitsofco.de%2Flinting-html-using-css%2F&t_d=Linting%20HTML%20using%20CSS&t_t=Linting%20HTML%20using%20CSS&s_o=default#)
        - [*⚑*](https://disqus.com/embed/comments/?base=default&version=60c69418f14a8b7401cd956e1062204c&f=bitsofcode&t_i=%2Flinting-html-using-css%2F&t_u=https%3A%2F%2Fbitsofco.de%2Flinting-html-using-css%2F&t_d=Linting%20HTML%20using%20CSS&t_t=Linting%20HTML%20using%20CSS&s_o=default#)

[![Avatar](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/ireaderinokun/)

[Ire Aderinokun](https://disqus.com/by/ireaderinokun/)Mod[*>* star2017](https://bitsofco.de/linting-html-using-css/#comment-3190957423)•[8 days ago](https://bitsofco.de/linting-html-using-css/#comment-3194089300)

Thank you :)

-

    - [−](https://disqus.com/embed/comments/?base=default&version=60c69418f14a8b7401cd956e1062204c&f=bitsofcode&t_i=%2Flinting-html-using-css%2F&t_u=https%3A%2F%2Fbitsofco.de%2Flinting-html-using-css%2F&t_d=Linting%20HTML%20using%20CSS&t_t=Linting%20HTML%20using%20CSS&s_o=default#)
    - [*⚑*](https://disqus.com/embed/comments/?base=default&version=60c69418f14a8b7401cd956e1062204c&f=bitsofcode&t_i=%2Flinting-html-using-css%2F&t_u=https%3A%2F%2Fbitsofco.de%2Flinting-html-using-css%2F&t_d=Linting%20HTML%20using%20CSS&t_t=Linting%20HTML%20using%20CSS&s_o=default#)

[![Avatar](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/markstickling/)

[Mark Stickling](https://disqus.com/by/markstickling/)•[8 days ago](https://bitsofco.de/linting-html-using-css/#comment-3194375040)

This is fantastic. I've learned so many new things. I used to have something like this for spotting

tags in WYWISYG text but this is next level. Thank you!

-

    - [−](https://disqus.com/embed/comments/?base=default&version=60c69418f14a8b7401cd956e1062204c&f=bitsofcode&t_i=%2Flinting-html-using-css%2F&t_u=https%3A%2F%2Fbitsofco.de%2Flinting-html-using-css%2F&t_d=Linting%20HTML%20using%20CSS&t_t=Linting%20HTML%20using%20CSS&s_o=default#)
    - [*⚑*](https://disqus.com/embed/comments/?base=default&version=60c69418f14a8b7401cd956e1062204c&f=bitsofcode&t_i=%2Flinting-html-using-css%2F&t_u=https%3A%2F%2Fbitsofco.de%2Flinting-html-using-css%2F&t_d=Linting%20HTML%20using%20CSS&t_t=Linting%20HTML%20using%20CSS&s_o=default#)

[![Avatar](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/emanuelsaramago/)

[Emanuel Saramago](https://disqus.com/by/emanuelsaramago/)•[8 days ago](https://bitsofco.de/linting-html-using-css/#comment-3194204524)

"When HTML is written incorrectly, nothing much happens", when you're not a person with disabilities.

    -

        - [−](https://disqus.com/embed/comments/?base=default&version=60c69418f14a8b7401cd956e1062204c&f=bitsofcode&t_i=%2Flinting-html-using-css%2F&t_u=https%3A%2F%2Fbitsofco.de%2Flinting-html-using-css%2F&t_d=Linting%20HTML%20using%20CSS&t_t=Linting%20HTML%20using%20CSS&s_o=default#)
        - [*⚑*](https://disqus.com/embed/comments/?base=default&version=60c69418f14a8b7401cd956e1062204c&f=bitsofcode&t_i=%2Flinting-html-using-css%2F&t_u=https%3A%2F%2Fbitsofco.de%2Flinting-html-using-css%2F&t_d=Linting%20HTML%20using%20CSS&t_t=Linting%20HTML%20using%20CSS&s_o=default#)

[![Avatar](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/ireaderinokun/)

[Ire Aderinokun](https://disqus.com/by/ireaderinokun/)Mod[*>* Emanuel Saramago](https://bitsofco.de/linting-html-using-css/#comment-3194204524)•[6 days ago](https://bitsofco.de/linting-html-using-css/#comment-3198271776)

Well what I meant was that, unlike a language like JavaScript, we don't get error messages or our markup doesn't not show.

        -

            - [−](https://disqus.com/embed/comments/?base=default&version=60c69418f14a8b7401cd956e1062204c&f=bitsofcode&t_i=%2Flinting-html-using-css%2F&t_u=https%3A%2F%2Fbitsofco.de%2Flinting-html-using-css%2F&t_d=Linting%20HTML%20using%20CSS&t_t=Linting%20HTML%20using%20CSS&s_o=default#)
            - [*⚑*](https://disqus.com/embed/comments/?base=default&version=60c69418f14a8b7401cd956e1062204c&f=bitsofcode&t_i=%2Flinting-html-using-css%2F&t_u=https%3A%2F%2Fbitsofco.de%2Flinting-html-using-css%2F&t_d=Linting%20HTML%20using%20CSS&t_t=Linting%20HTML%20using%20CSS&s_o=default#)

[![Avatar](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/mttmccb/)

[Matt McCabe](https://disqus.com/by/mttmccb/)[*>* Ire Aderinokun](https://bitsofco.de/linting-html-using-css/#comment-3198271776)•[5 days ago](https://bitsofco.de/linting-html-using-css/#comment-3200107600)

HTML is very forgiving, you can get away with a lot and it still 'works'

-

    - [−](https://disqus.com/embed/comments/?base=default&version=60c69418f14a8b7401cd956e1062204c&f=bitsofcode&t_i=%2Flinting-html-using-css%2F&t_u=https%3A%2F%2Fbitsofco.de%2Flinting-html-using-css%2F&t_d=Linting%20HTML%20using%20CSS&t_t=Linting%20HTML%20using%20CSS&s_o=default#)
    - [*⚑*](https://disqus.com/embed/comments/?base=default&version=60c69418f14a8b7401cd956e1062204c&f=bitsofcode&t_i=%2Flinting-html-using-css%2F&t_u=https%3A%2F%2Fbitsofco.de%2Flinting-html-using-css%2F&t_d=Linting%20HTML%20using%20CSS&t_t=Linting%20HTML%20using%20CSS&s_o=default#)

[![Avatar](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/galpoupard/)

[Gaël Poupard](https://disqus.com/by/galpoupard/)•[10 days ago](https://bitsofco.de/linting-html-using-css/#comment-3190511953)

Hi! Thanks for your post, it gives tons of ideas :)

For the history part, the first post exploring this idea was written by Eric Meyer on 07/21/2000: [http://archive.oreilly.com/...](http://disq.us/url?url=http%3A%2F%2Farchive.oreilly.com%2Fpub%2Fa%2Fnetwork%2F2000%2F07%2F21%2Fmagazine%2Fcss_tool.html%3Aq4ix0_OUH1ABT47phcu1age-5Tw&cuid=3490249)

Not really new — but so much more powerful thanks to modern selectors!!

I use this concept on a daily basis and came up with a (very large) CSS file, I'd love to hear your thought about it: [https://github.com/ffoodd/a...](https://disq.us/url?url=https%3A%2F%2Fgithub.com%2Fffoodd%2Fa11y.css%3A7Tfrp5i8lnHLnxoshgMmHGEMrtM&cuid=3490249)

There's an updated wiki and a documentation / test website. I'm going to take some of your ideas in my "Candidate test" project, since you thought about test I didn't use (such as viewports' ones).

Thanks a lot :)

    -

        - [−](https://disqus.com/embed/comments/?base=default&version=60c69418f14a8b7401cd956e1062204c&f=bitsofcode&t_i=%2Flinting-html-using-css%2F&t_u=https%3A%2F%2Fbitsofco.de%2Flinting-html-using-css%2F&t_d=Linting%20HTML%20using%20CSS&t_t=Linting%20HTML%20using%20CSS&s_o=default#)
        - [*⚑*](https://disqus.com/embed/comments/?base=default&version=60c69418f14a8b7401cd956e1062204c&f=bitsofcode&t_i=%2Flinting-html-using-css%2F&t_u=https%3A%2F%2Fbitsofco.de%2Flinting-html-using-css%2F&t_d=Linting%20HTML%20using%20CSS&t_t=Linting%20HTML%20using%20CSS&s_o=default#)

[![Avatar](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/ireaderinokun/)

[Ire Aderinokun](https://disqus.com/by/ireaderinokun/)Mod[*>* Gaël Poupard](https://bitsofco.de/linting-html-using-css/#comment-3190511953)•[10 days ago](https://bitsofco.de/linting-html-using-css/#comment-3190554437)

Hey!

Your a11y.css looks awesome! I'll definitely take a much more detailed look. I actually also had an idea for this concept, i'll contact you about it

-

    - [−](https://disqus.com/embed/comments/?base=default&version=60c69418f14a8b7401cd956e1062204c&f=bitsofcode&t_i=%2Flinting-html-using-css%2F&t_u=https%3A%2F%2Fbitsofco.de%2Flinting-html-using-css%2F&t_d=Linting%20HTML%20using%20CSS&t_t=Linting%20HTML%20using%20CSS&s_o=default#)
    - [*⚑*](https://disqus.com/embed/comments/?base=default&version=60c69418f14a8b7401cd956e1062204c&f=bitsofcode&t_i=%2Flinting-html-using-css%2F&t_u=https%3A%2F%2Fbitsofco.de%2Flinting-html-using-css%2F&t_d=Linting%20HTML%20using%20CSS&t_t=Linting%20HTML%20using%20CSS&s_o=default#)

[![Avatar](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/zardozcs/)

[zardoz](https://disqus.com/by/zardozcs/)•[11 hours ago](https://bitsofco.de/linting-html-using-css/#comment-3207284630)

You should probably use a big red outline instead of a big red border to highlight things because that's what it's for, dev related highlighting of things.

-

    - [−](https://disqus.com/embed/comments/?base=default&version=60c69418f14a8b7401cd956e1062204c&f=bitsofcode&t_i=%2Flinting-html-using-css%2F&t_u=https%3A%2F%2Fbitsofco.de%2Flinting-html-using-css%2F&t_d=Linting%20HTML%20using%20CSS&t_t=Linting%20HTML%20using%20CSS&s_o=default#)
    - [*⚑*](https://disqus.com/embed/comments/?base=default&version=60c69418f14a8b7401cd956e1062204c&f=bitsofcode&t_i=%2Flinting-html-using-css%2F&t_u=https%3A%2F%2Fbitsofco.de%2Flinting-html-using-css%2F&t_d=Linting%20HTML%20using%20CSS&t_t=Linting%20HTML%20using%20CSS&s_o=default#)

[![Avatar](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/disqus_lkS33eHOdk/)

[Ian Oliver](https://disqus.com/by/disqus_lkS33eHOdk/)•[12 hours ago](https://bitsofco.de/linting-html-using-css/#comment-3207126331)

Great idea. I'd also recommend flagging up CSS style blocks, elements with inline CSS, and inline scripts, which will likely be issues when a good Content Security Policy is in place.

-

    - [−](https://disqus.com/embed/comments/?base=default&version=60c69418f14a8b7401cd956e1062204c&f=bitsofcode&t_i=%2Flinting-html-using-css%2F&t_u=https%3A%2F%2Fbitsofco.de%2Flinting-html-using-css%2F&t_d=Linting%20HTML%20using%20CSS&t_t=Linting%20HTML%20using%20CSS&s_o=default#)
    - [*⚑*](https://disqus.com/embed/comments/?base=default&version=60c69418f14a8b7401cd956e1062204c&f=bitsofcode&t_i=%2Flinting-html-using-css%2F&t_u=https%3A%2F%2Fbitsofco.de%2Flinting-html-using-css%2F&t_d=Linting%20HTML%20using%20CSS&t_t=Linting%20HTML%20using%20CSS&s_o=default#)

![Avatar](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)

Jens Oliver Meiert•[a day ago](https://bitsofco.de/linting-html-using-css/#comment-3206134622)

Quick thoughts on two specific issues (sorry if these are dups):

1. Highlighting missing language markup may be questionable for two reasons: one, because document language can be specified through other means (server side, for example) and may, ideally, be determined programmatically [1]; two, that the mentioned use case is not indicating a markup, but a _user agent_ problem.

2. Highlighting unlabelled form elements, at least in the form presented (or as I understand it), should take into account (and not penalize) cases like <label><input></label>. That should be fairly easy to accommodate, if it’s not already covered.

[1] [https://meiert.com/en/blog/...](https://disq.us/url?url=https%3A%2F%2Fmeiert.com%2Fen%2Fblog%2F20140825%2Fhtml-and-language%2F%3ACGtcv_Nt-CawoR26eZhC5Ww9teY&cuid=3490249)

-

    - [−](https://disqus.com/embed/comments/?base=default&version=60c69418f14a8b7401cd956e1062204c&f=bitsofcode&t_i=%2Flinting-html-using-css%2F&t_u=https%3A%2F%2Fbitsofco.de%2Flinting-html-using-css%2F&t_d=Linting%20HTML%20using%20CSS&t_t=Linting%20HTML%20using%20CSS&s_o=default#)
    - [*⚑*](https://disqus.com/embed/comments/?base=default&version=60c69418f14a8b7401cd956e1062204c&f=bitsofcode&t_i=%2Flinting-html-using-css%2F&t_u=https%3A%2F%2Fbitsofco.de%2Flinting-html-using-css%2F&t_d=Linting%20HTML%20using%20CSS&t_t=Linting%20HTML%20using%20CSS&s_o=default#)

[![Avatar](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/j_castillo/)

[J Castillo](https://disqus.com/by/j_castillo/)•[a day ago](https://bitsofco.de/linting-html-using-css/#comment-3205959505)

Thank you for sharing, great idea! Since there are so many comments and good ideas from different people I would recommend to move this post to [github.com](http://disq.us/url?url=http%3A%2F%2Fgithub.com%3AtVcH9ZiWpbdqzIvqccGefNkob1E&cuid=3490249). this way when people suggest changes/additions they can simply do a pull request ;)

-

    - [−](https://disqus.com/embed/comments/?base=default&version=60c69418f14a8b7401cd956e1062204c&f=bitsofcode&t_i=%2Flinting-html-using-css%2F&t_u=https%3A%2F%2Fbitsofco.de%2Flinting-html-using-css%2F&t_d=Linting%20HTML%20using%20CSS&t_t=Linting%20HTML%20using%20CSS&s_o=default#)
    - [*⚑*](https://disqus.com/embed/comments/?base=default&version=60c69418f14a8b7401cd956e1062204c&f=bitsofcode&t_i=%2Flinting-html-using-css%2F&t_u=https%3A%2F%2Fbitsofco.de%2Flinting-html-using-css%2F&t_d=Linting%20HTML%20using%20CSS&t_t=Linting%20HTML%20using%20CSS&s_o=default#)

[![Avatar](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/egorvkraevsky/)

[Egor V Kraevsky](https://disqus.com/by/egorvkraevsky/)•[2 days ago](https://bitsofco.de/linting-html-using-css/#comment-3204831643)

gosh what "Linting" means in this context, am an russian sry? :)

-

    - [−](https://disqus.com/embed/comments/?base=default&version=60c69418f14a8b7401cd956e1062204c&f=bitsofcode&t_i=%2Flinting-html-using-css%2F&t_u=https%3A%2F%2Fbitsofco.de%2Flinting-html-using-css%2F&t_d=Linting%20HTML%20using%20CSS&t_t=Linting%20HTML%20using%20CSS&s_o=default#)
    - [*⚑*](https://disqus.com/embed/comments/?base=default&version=60c69418f14a8b7401cd956e1062204c&f=bitsofcode&t_i=%2Flinting-html-using-css%2F&t_u=https%3A%2F%2Fbitsofco.de%2Flinting-html-using-css%2F&t_d=Linting%20HTML%20using%20CSS&t_t=Linting%20HTML%20using%20CSS&s_o=default#)

[![Avatar](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/chrisopedia/)

[Newton](https://disqus.com/by/chrisopedia/)•[2 days ago](https://bitsofco.de/linting-html-using-css/#comment-3204336992)

I built a SCSS library a while back that was based off a few different ones like this. I think Heydon Pickering started this with Revenge.css.

[https://github.com/chrisope...](https://disq.us/url?url=https%3A%2F%2Fgithub.com%2Fchrisopedia%2Fhtml-verify%3ADt39keUov4xLmoV8x9LQKl89-Cc&cuid=3490249)

[https://github.com/diagnost...](https://disq.us/url?url=https%3A%2F%2Fgithub.com%2Fdiagnosticss%2Fdiagnosticss%3Aq8ShFJl7wAv_4qd2hgBHCGll-T8&cuid=3490249)

[https://github.com/Heydon/R...](https://disq.us/url?url=https%3A%2F%2Fgithub.com%2FHeydon%2FREVENGE.CSS%3A3CeIlV0Oo3Joc7IIj2xf1rsWYWE&cuid=3490249)

-

    - [−](https://disqus.com/embed/comments/?base=default&version=60c69418f14a8b7401cd956e1062204c&f=bitsofcode&t_i=%2Flinting-html-using-css%2F&t_u=https%3A%2F%2Fbitsofco.de%2Flinting-html-using-css%2F&t_d=Linting%20HTML%20using%20CSS&t_t=Linting%20HTML%20using%20CSS&s_o=default#)
    - [*⚑*](https://disqus.com/embed/comments/?base=default&version=60c69418f14a8b7401cd956e1062204c&f=bitsofcode&t_i=%2Flinting-html-using-css%2F&t_u=https%3A%2F%2Fbitsofco.de%2Flinting-html-using-css%2F&t_d=Linting%20HTML%20using%20CSS&t_t=Linting%20HTML%20using%20CSS&s_o=default#)

[![Avatar](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/kenneth_davila/)

[Kenneth Davila](https://disqus.com/by/kenneth_davila/)•[2 days ago](https://bitsofco.de/linting-html-using-css/#comment-3203738551)

this is good, book marked!

-

    - [−](https://disqus.com/embed/comments/?base=default&version=60c69418f14a8b7401cd956e1062204c&f=bitsofcode&t_i=%2Flinting-html-using-css%2F&t_u=https%3A%2F%2Fbitsofco.de%2Flinting-html-using-css%2F&t_d=Linting%20HTML%20using%20CSS&t_t=Linting%20HTML%20using%20CSS&s_o=default#)
    - [*⚑*](https://disqus.com/embed/comments/?base=default&version=60c69418f14a8b7401cd956e1062204c&f=bitsofcode&t_i=%2Flinting-html-using-css%2F&t_u=https%3A%2F%2Fbitsofco.de%2Flinting-html-using-css%2F&t_d=Linting%20HTML%20using%20CSS&t_t=Linting%20HTML%20using%20CSS&s_o=default#)

[![Avatar](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/disqus_kJ79bnvByP/)

[Cory Long](https://disqus.com/by/disqus_kJ79bnvByP/)•[4 days ago](https://bitsofco.de/linting-html-using-css/#comment-3201709159)

rel="stylesheet" isnot depreciated, and is generally considered to be required. A problem particularly may arise when the CSS is server from a URL that does not end in .css, such as dynamic generated CSS.

-

    - [−](https://disqus.com/embed/comments/?base=default&version=60c69418f14a8b7401cd956e1062204c&f=bitsofcode&t_i=%2Flinting-html-using-css%2F&t_u=https%3A%2F%2Fbitsofco.de%2Flinting-html-using-css%2F&t_d=Linting%20HTML%20using%20CSS&t_t=Linting%20HTML%20using%20CSS&s_o=default#)
    - [*⚑*](https://disqus.com/embed/comments/?base=default&version=60c69418f14a8b7401cd956e1062204c&f=bitsofcode&t_i=%2Flinting-html-using-css%2F&t_u=https%3A%2F%2Fbitsofco.de%2Flinting-html-using-css%2F&t_d=Linting%20HTML%20using%20CSS&t_t=Linting%20HTML%20using%20CSS&s_o=default#)

[![Avatar](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/disqus_DHjuUMpmqB/)

[Rémi](https://disqus.com/by/disqus_DHjuUMpmqB/)•[4 days ago](https://bitsofco.de/linting-html-using-css/#comment-3201576032)

There's also a 1-line Javascript solution from Addy Osmani I use :

[].forEach.call($$("*"), function (a) { a.style.outline = "1px solid #" + (~~(Math.random() * (1 << 24))).toString(16) });

This is the shortened unreadable way but what it does is applying a random color to every HTML div

-

    - [−](https://disqus.com/embed/comments/?base=default&version=60c69418f14a8b7401cd956e1062204c&f=bitsofcode&t_i=%2Flinting-html-using-css%2F&t_u=https%3A%2F%2Fbitsofco.de%2Flinting-html-using-css%2F&t_d=Linting%20HTML%20using%20CSS&t_t=Linting%20HTML%20using%20CSS&s_o=default#)
    - [*⚑*](https://disqus.com/embed/comments/?base=default&version=60c69418f14a8b7401cd956e1062204c&f=bitsofcode&t_i=%2Flinting-html-using-css%2F&t_u=https%3A%2F%2Fbitsofco.de%2Flinting-html-using-css%2F&t_d=Linting%20HTML%20using%20CSS&t_t=Linting%20HTML%20using%20CSS&s_o=default#)

[![Avatar](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/MaxArt2501/)

[MaxArt](https://disqus.com/by/MaxArt2501/)•[4 days ago](https://bitsofco.de/linting-html-using-css/#comment-3200429058)

I think it's fine to have labels without for, and field without an id, as long as you put the fields inside the label element. Yes, that works.

-

    - [−](https://disqus.com/embed/comments/?base=default&version=60c69418f14a8b7401cd956e1062204c&f=bitsofcode&t_i=%2Flinting-html-using-css%2F&t_u=https%3A%2F%2Fbitsofco.de%2Flinting-html-using-css%2F&t_d=Linting%20HTML%20using%20CSS&t_t=Linting%20HTML%20using%20CSS&s_o=default#)
    - [*⚑*](https://disqus.com/embed/comments/?base=default&version=60c69418f14a8b7401cd956e1062204c&f=bitsofcode&t_i=%2Flinting-html-using-css%2F&t_u=https%3A%2F%2Fbitsofco.de%2Flinting-html-using-css%2F&t_d=Linting%20HTML%20using%20CSS&t_t=Linting%20HTML%20using%20CSS&s_o=default#)

[![Avatar](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/mttmccb/)

[Matt McCabe](https://disqus.com/by/mttmccb/)•[5 days ago](https://bitsofco.de/linting-html-using-css/#comment-3200109479)

Looks like it would make a nice helper file, I wonder if it could be automated easily. Rather than displaying it, it could be Javascript that counts the things selected.

-

    - [−](https://disqus.com/embed/comments/?base=default&version=60c69418f14a8b7401cd956e1062204c&f=bitsofcode&t_i=%2Flinting-html-using-css%2F&t_u=https%3A%2F%2Fbitsofco.de%2Flinting-html-using-css%2F&t_d=Linting%20HTML%20using%20CSS&t_t=Linting%20HTML%20using%20CSS&s_o=default#)
    - [*⚑*](https://disqus.com/embed/comments/?base=default&version=60c69418f14a8b7401cd956e1062204c&f=bitsofcode&t_i=%2Flinting-html-using-css%2F&t_u=https%3A%2F%2Fbitsofco.de%2Flinting-html-using-css%2F&t_d=Linting%20HTML%20using%20CSS&t_t=Linting%20HTML%20using%20CSS&s_o=default#)

[![Avatar](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/jfaquinojr/)

[jokab](https://disqus.com/by/jfaquinojr/)•[5 days ago](https://bitsofco.de/linting-html-using-css/#comment-3199775224)

Thank you from the beautiful islands of the Philippines. Lel

-

    - [−](https://disqus.com/embed/comments/?base=default&version=60c69418f14a8b7401cd956e1062204c&f=bitsofcode&t_i=%2Flinting-html-using-css%2F&t_u=https%3A%2F%2Fbitsofco.de%2Flinting-html-using-css%2F&t_d=Linting%20HTML%20using%20CSS&t_t=Linting%20HTML%20using%20CSS&s_o=default#)
    - [*⚑*](https://disqus.com/embed/comments/?base=default&version=60c69418f14a8b7401cd956e1062204c&f=bitsofcode&t_i=%2Flinting-html-using-css%2F&t_u=https%3A%2F%2Fbitsofco.de%2Flinting-html-using-css%2F&t_d=Linting%20HTML%20using%20CSS&t_t=Linting%20HTML%20using%20CSS&s_o=default#)

[![Avatar](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/ichderfisch/)

[ichderfisch](https://disqus.com/by/ichderfisch/)•[7 days ago](https://bitsofco.de/linting-html-using-css/#comment-3195953010)

You should check heydon's revenge.css, which uses much the same strategies.

[http://heydonworks.com/reve...](http://disq.us/url?url=http%3A%2F%2Fheydonworks.com%2Frevenge_css_bookmarklet%2F%3ASkdDPMymwuWgs0z5IolgSdCpx8E&cuid=3490249)

-

    - [−](https://disqus.com/embed/comments/?base=default&version=60c69418f14a8b7401cd956e1062204c&f=bitsofcode&t_i=%2Flinting-html-using-css%2F&t_u=https%3A%2F%2Fbitsofco.de%2Flinting-html-using-css%2F&t_d=Linting%20HTML%20using%20CSS&t_t=Linting%20HTML%20using%20CSS&s_o=default#)
    - [*⚑*](https://disqus.com/embed/comments/?base=default&version=60c69418f14a8b7401cd956e1062204c&f=bitsofcode&t_i=%2Flinting-html-using-css%2F&t_u=https%3A%2F%2Fbitsofco.de%2Flinting-html-using-css%2F&t_d=Linting%20HTML%20using%20CSS&t_t=Linting%20HTML%20using%20CSS&s_o=default#)

![Avatar](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)

Alex•[7 days ago](https://bitsofco.de/linting-html-using-css/#comment-3194999214)

Thanks for your post!

It seems there is a typo in "Faulty or Missing Link Targets" section: the selectors should be 'a[href="#"]' and 'a[href=""]' (without the colons).

    -

        - [−](https://disqus.com/embed/comments/?base=default&version=60c69418f14a8b7401cd956e1062204c&f=bitsofcode&t_i=%2Flinting-html-using-css%2F&t_u=https%3A%2F%2Fbitsofco.de%2Flinting-html-using-css%2F&t_d=Linting%20HTML%20using%20CSS&t_t=Linting%20HTML%20using%20CSS&s_o=default#)
        - [*⚑*](https://disqus.com/embed/comments/?base=default&version=60c69418f14a8b7401cd956e1062204c&f=bitsofcode&t_i=%2Flinting-html-using-css%2F&t_u=https%3A%2F%2Fbitsofco.de%2Flinting-html-using-css%2F&t_d=Linting%20HTML%20using%20CSS&t_t=Linting%20HTML%20using%20CSS&s_o=default#)

[![Avatar](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/ireaderinokun/)

[Ire Aderinokun](https://disqus.com/by/ireaderinokun/)Mod[*>* Alex](https://bitsofco.de/linting-html-using-css/#comment-3194999214)•[6 days ago](https://bitsofco.de/linting-html-using-css/#comment-3198272632)

Thanks! Fixed

-

    - [−](https://disqus.com/embed/comments/?base=default&version=60c69418f14a8b7401cd956e1062204c&f=bitsofcode&t_i=%2Flinting-html-using-css%2F&t_u=https%3A%2F%2Fbitsofco.de%2Flinting-html-using-css%2F&t_d=Linting%20HTML%20using%20CSS&t_t=Linting%20HTML%20using%20CSS&s_o=default#)
    - [*⚑*](https://disqus.com/embed/comments/?base=default&version=60c69418f14a8b7401cd956e1062204c&f=bitsofcode&t_i=%2Flinting-html-using-css%2F&t_u=https%3A%2F%2Fbitsofco.de%2Flinting-html-using-css%2F&t_d=Linting%20HTML%20using%20CSS&t_t=Linting%20HTML%20using%20CSS&s_o=default#)

[![Avatar](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/torrancescott/)

[Torrance Scott](https://disqus.com/by/torrancescott/)•[7 days ago](https://bitsofco.de/linting-html-using-css/#comment-3194858915)

Excellent idea Ire, I just put this into my dev builds on all my projects. I feel a bit silly this hasn't crossed my mind sooner...such a simple, unobtrusive reminder to devs that there are people who rely on the unseen parts of html.

-

    - [−](https://disqus.com/embed/comments/?base=default&version=60c69418f14a8b7401cd956e1062204c&f=bitsofcode&t_i=%2Flinting-html-using-css%2F&t_u=https%3A%2F%2Fbitsofco.de%2Flinting-html-using-css%2F&t_d=Linting%20HTML%20using%20CSS&t_t=Linting%20HTML%20using%20CSS&s_o=default#)
    - [*⚑*](https://disqus.com/embed/comments/?base=default&version=60c69418f14a8b7401cd956e1062204c&f=bitsofcode&t_i=%2Flinting-html-using-css%2F&t_u=https%3A%2F%2Fbitsofco.de%2Flinting-html-using-css%2F&t_d=Linting%20HTML%20using%20CSS&t_t=Linting%20HTML%20using%20CSS&s_o=default#)

[![Avatar](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/disqus_aJCOpnBnuA/)

[Spell](https://disqus.com/by/disqus_aJCOpnBnuA/)•[7 days ago](https://bitsofco.de/linting-html-using-css/#comment-3194493356)

Thanks for this. Looking for improperly nested elements another possibility, too. button + a, etc.

-

    - [−](https://disqus.com/embed/comments/?base=default&version=60c69418f14a8b7401cd956e1062204c&f=bitsofcode&t_i=%2Flinting-html-using-css%2F&t_u=https%3A%2F%2Fbitsofco.de%2Flinting-html-using-css%2F&t_d=Linting%20HTML%20using%20CSS&t_t=Linting%20HTML%20using%20CSS&s_o=default#)
    - [*⚑*](https://disqus.com/embed/comments/?base=default&version=60c69418f14a8b7401cd956e1062204c&f=bitsofcode&t_i=%2Flinting-html-using-css%2F&t_u=https%3A%2F%2Fbitsofco.de%2Flinting-html-using-css%2F&t_d=Linting%20HTML%20using%20CSS&t_t=Linting%20HTML%20using%20CSS&s_o=default#)

![Avatar](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)

Skadelig•[8 days ago](https://bitsofco.de/linting-html-using-css/#comment-3194002645)

What do you think about button whit icon only (with background image and without text)?

    -

        - [−](https://disqus.com/embed/comments/?base=default&version=60c69418f14a8b7401cd956e1062204c&f=bitsofcode&t_i=%2Flinting-html-using-css%2F&t_u=https%3A%2F%2Fbitsofco.de%2Flinting-html-using-css%2F&t_d=Linting%20HTML%20using%20CSS&t_t=Linting%20HTML%20using%20CSS&s_o=default#)
        - [*⚑*](https://disqus.com/embed/comments/?base=default&version=60c69418f14a8b7401cd956e1062204c&f=bitsofcode&t_i=%2Flinting-html-using-css%2F&t_u=https%3A%2F%2Fbitsofco.de%2Flinting-html-using-css%2F&t_d=Linting%20HTML%20using%20CSS&t_t=Linting%20HTML%20using%20CSS&s_o=default#)

[![Avatar](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/ireaderinokun/)

[Ire Aderinokun](https://disqus.com/by/ireaderinokun/)Mod[*>* Skadelig](https://bitsofco.de/linting-html-using-css/#comment-3194002645)•[8 days ago](https://bitsofco.de/linting-html-using-css/#comment-3194089799)

The way I always do that is to also have text within the button, but just hide it from visible view. Alternatively, you can add an aria-label to the button to label it

    -

        - [−](https://disqus.com/embed/comments/?base=default&version=60c69418f14a8b7401cd956e1062204c&f=bitsofcode&t_i=%2Flinting-html-using-css%2F&t_u=https%3A%2F%2Fbitsofco.de%2Flinting-html-using-css%2F&t_d=Linting%20HTML%20using%20CSS&t_t=Linting%20HTML%20using%20CSS&s_o=default#)
        - [*⚑*](https://disqus.com/embed/comments/?base=default&version=60c69418f14a8b7401cd956e1062204c&f=bitsofcode&t_i=%2Flinting-html-using-css%2F&t_u=https%3A%2F%2Fbitsofco.de%2Flinting-html-using-css%2F&t_d=Linting%20HTML%20using%20CSS&t_t=Linting%20HTML%20using%20CSS&s_o=default#)

[![Avatar](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/slavickk/)

[Slavick K](https://disqus.com/by/slavickk/)[*>* Skadelig](https://bitsofco.de/linting-html-using-css/#comment-3194002645)•[8 days ago](https://bitsofco.de/linting-html-using-css/#comment-3194087886)

You can use .myButton { content: "whatever content you'd like to specify for screenreaders"; }

        -

            - [−](https://disqus.com/embed/comments/?base=default&version=60c69418f14a8b7401cd956e1062204c&f=bitsofcode&t_i=%2Flinting-html-using-css%2F&t_u=https%3A%2F%2Fbitsofco.de%2Flinting-html-using-css%2F&t_d=Linting%20HTML%20using%20CSS&t_t=Linting%20HTML%20using%20CSS&s_o=default#)
            - [*⚑*](https://disqus.com/embed/comments/?base=default&version=60c69418f14a8b7401cd956e1062204c&f=bitsofcode&t_i=%2Flinting-html-using-css%2F&t_u=https%3A%2F%2Fbitsofco.de%2Flinting-html-using-css%2F&t_d=Linting%20HTML%20using%20CSS&t_t=Linting%20HTML%20using%20CSS&s_o=default#)

[![Avatar](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/ireaderinokun/)

[Ire Aderinokun](https://disqus.com/by/ireaderinokun/)Mod[*>* Slavick K](https://bitsofco.de/linting-html-using-css/#comment-3194087886)•[8 days ago](https://bitsofco.de/linting-html-using-css/#comment-3194090167)

You can't add content to a regular element, only pseudo-elements. Plus, content shouldn't be specified through stylesheets, it should be in markup

            -

                - [−](https://disqus.com/embed/comments/?base=default&version=60c69418f14a8b7401cd956e1062204c&f=bitsofcode&t_i=%2Flinting-html-using-css%2F&t_u=https%3A%2F%2Fbitsofco.de%2Flinting-html-using-css%2F&t_d=Linting%20HTML%20using%20CSS&t_t=Linting%20HTML%20using%20CSS&s_o=default#)
                - [*⚑*](https://disqus.com/embed/comments/?base=default&version=60c69418f14a8b7401cd956e1062204c&f=bitsofcode&t_i=%2Flinting-html-using-css%2F&t_u=https%3A%2F%2Fbitsofco.de%2Flinting-html-using-css%2F&t_d=Linting%20HTML%20using%20CSS&t_t=Linting%20HTML%20using%20CSS&s_o=default#)

[![Avatar](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/slavickk/)

[Slavick K](https://disqus.com/by/slavickk/)[*>* Ire Aderinokun](https://bitsofco.de/linting-html-using-css/#comment-3194090167)•[8 days ago](https://bitsofco.de/linting-html-using-css/#comment-3194095583)

Thank you for clearing that out for me!

So how should we add content to a buttons like those @Skadelig was asking about? display:none'd span? Or is there a really right way for that?

                -

                    - [−](https://disqus.com/embed/comments/?base=default&version=60c69418f14a8b7401cd956e1062204c&f=bitsofcode&t_i=%2Flinting-html-using-css%2F&t_u=https%3A%2F%2Fbitsofco.de%2Flinting-html-using-css%2F&t_d=Linting%20HTML%20using%20CSS&t_t=Linting%20HTML%20using%20CSS&s_o=default#)
                    - [*⚑*](https://disqus.com/embed/comments/?base=default&version=60c69418f14a8b7401cd956e1062204c&f=bitsofcode&t_i=%2Flinting-html-using-css%2F&t_u=https%3A%2F%2Fbitsofco.de%2Flinting-html-using-css%2F&t_d=Linting%20HTML%20using%20CSS&t_t=Linting%20HTML%20using%20CSS&s_o=default#)

[![Avatar](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/claireelaineomalley/)

[Claire-Elaine O'Malley](https://disqus.com/by/claireelaineomalley/)[*>* Slavick K](https://bitsofco.de/linting-html-using-css/#comment-3194095583)•[7 days ago](https://bitsofco.de/linting-html-using-css/#comment-3194969115)

display:none; is also invisible to screenreaders. It will not be read to your user if you have display:none; on an element. Generally I do this to ensure the element is invisible to sighted users, but read by screenreaders:

HTML:
<button type="button">
<s*pan class="a11y-hide">Save Address</s*pan>
</button>
CSS:
.a11y-hide {
overflow: hidden;
position: absolute !important;
top: auto;
height: 1px;
width: 1px;
m*argin: -1px;
}
*Need the asterisk to make this code visible in the comment... weirdness.

                    -

                        - [−](https://disqus.com/embed/comments/?base=default&version=60c69418f14a8b7401cd956e1062204c&f=bitsofcode&t_i=%2Flinting-html-using-css%2F&t_u=https%3A%2F%2Fbitsofco.de%2Flinting-html-using-css%2F&t_d=Linting%20HTML%20using%20CSS&t_t=Linting%20HTML%20using%20CSS&s_o=default#)
                        - [*⚑*](https://disqus.com/embed/comments/?base=default&version=60c69418f14a8b7401cd956e1062204c&f=bitsofcode&t_i=%2Flinting-html-using-css%2F&t_u=https%3A%2F%2Fbitsofco.de%2Flinting-html-using-css%2F&t_d=Linting%20HTML%20using%20CSS&t_t=Linting%20HTML%20using%20CSS&s_o=default#)

[![Avatar](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/disqus_4evFlfnoEU/)

[Jeff Mcneill](https://disqus.com/by/disqus_4evFlfnoEU/)[*>* Claire-Elaine O'Malley](https://bitsofco.de/linting-html-using-css/#comment-3194969115)•[5 days ago](https://bitsofco.de/linting-html-using-css/#comment-3199760912)

Wouldn't this get flagged by Google/Bing/Yandex mobile-friendly tests? Buttons that are too small?

                        -

                            - [−](https://disqus.com/embed/comments/?base=default&version=60c69418f14a8b7401cd956e1062204c&f=bitsofcode&t_i=%2Flinting-html-using-css%2F&t_u=https%3A%2F%2Fbitsofco.de%2Flinting-html-using-css%2F&t_d=Linting%20HTML%20using%20CSS&t_t=Linting%20HTML%20using%20CSS&s_o=default#)
                            - [*⚑*](https://disqus.com/embed/comments/?base=default&version=60c69418f14a8b7401cd956e1062204c&f=bitsofcode&t_i=%2Flinting-html-using-css%2F&t_u=https%3A%2F%2Fbitsofco.de%2Flinting-html-using-css%2F&t_d=Linting%20HTML%20using%20CSS&t_t=Linting%20HTML%20using%20CSS&s_o=default#)

[![Avatar](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/claireelaineomalley/)

[Claire-Elaine O'Malley](https://disqus.com/by/claireelaineomalley/)[*>* Jeff Mcneill](https://bitsofco.de/linting-html-using-css/#comment-3199760912)•[4 days ago](https://bitsofco.de/linting-html-using-css/#comment-3200891152)

The button is not that size. The span inside it is. The button is the size of his icon, and I don't know what size his icons are, but mine are min 35px x 35px.

                -

                    - [−](https://disqus.com/embed/comments/?base=default&version=60c69418f14a8b7401cd956e1062204c&f=bitsofcode&t_i=%2Flinting-html-using-css%2F&t_u=https%3A%2F%2Fbitsofco.de%2Flinting-html-using-css%2F&t_d=Linting%20HTML%20using%20CSS&t_t=Linting%20HTML%20using%20CSS&s_o=default#)
                    - [*⚑*](https://disqus.com/embed/comments/?base=default&version=60c69418f14a8b7401cd956e1062204c&f=bitsofcode&t_i=%2Flinting-html-using-css%2F&t_u=https%3A%2F%2Fbitsofco.de%2Flinting-html-using-css%2F&t_d=Linting%20HTML%20using%20CSS&t_t=Linting%20HTML%20using%20CSS&s_o=default#)

[![Avatar](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/torrancescott/)

[Torrance Scott](https://disqus.com/by/torrancescott/)[*>* Slavick K](https://bitsofco.de/linting-html-using-css/#comment-3194095583)•[7 days ago](https://bitsofco.de/linting-html-using-css/#comment-3194892404)

aria-label is probably the best. To replace text I use
font: 0/0 a;
text-shadow: none;
color: transparent;
but I'm not sure if that hurts SEO.

[Load more comments](https://disqus.com/embed/comments/?base=default&version=60c69418f14a8b7401cd956e1062204c&f=bitsofcode&t_i=%2Flinting-html-using-css%2F&t_u=https%3A%2F%2Fbitsofco.de%2Flinting-html-using-css%2F&t_d=Linting%20HTML%20using%20CSS&t_t=Linting%20HTML%20using%20CSS&s_o=default#)

## Also on **bitsofcode**

- [ ### Making Alix, a Chrome Extension for Linting HTML       - 6 comments•      - 9 days ago•](http://disq.us/url?url=https%3A%2F%2Fbitsofco.de%2Fp%2Fd678c4c7-31e2-4efa-86db-6b138fe63736%2F%3AWbt9hGkGLRQ780oFlxI72RVtcGA&imp=90l57iv3k85q6o&prev_imp=90kj3p81h5enbn&forum_id=3490249&forum=bitsofcode&thread_id=5605954947&thread=5612840241&zone=thread&area=bottom&object_type=thread&object_id=5612840241)[Gaël Poupard— Hi there!I think this is a know issue: https://github.com/ffoodd/a... (number two). If so, there's nothing we can do (for now) since some CSS …](http://disq.us/url?url=https%3A%2F%2Fbitsofco.de%2Fp%2Fd678c4c7-31e2-4efa-86db-6b138fe63736%2F%3AWbt9hGkGLRQ780oFlxI72RVtcGA&imp=90l57iv3k85q6o&prev_imp=90kj3p81h5enbn&forum_id=3490249&forum=bitsofcode&thread_id=5605954947&thread=5612840241&zone=thread&area=bottom&object_type=thread&object_id=5612840241)
- [ ### "What's the typeof null?", and other confusing JavaScript Types       - 6 comments•      - 24 days ago•](http://disq.us/url?url=https%3A%2F%2Fbitsofco.de%2Fjavascript-typeof%2F%3A3A1VqdqqWSUxIoBbLeU72coMQFw&imp=90l57iv3k85q6o&prev_imp=90kj3p81h5enbn&forum_id=3490249&forum=bitsofcode&thread_id=5605954947&thread=5570753141&zone=thread&area=bottom&object_type=thread&object_id=5570753141)[Ire Aderinokun—Thank you 😊](http://disq.us/url?url=https%3A%2F%2Fbitsofco.de%2Fjavascript-typeof%2F%3A3A1VqdqqWSUxIoBbLeU72coMQFw&imp=90l57iv3k85q6o&prev_imp=90kj3p81h5enbn&forum_id=3490249&forum=bitsofcode&thread_id=5605954947&thread=5570753141&zone=thread&area=bottom&object_type=thread&object_id=5570753141)
- [ ### New CSS Features to Learn in 2017       - 22 comments•      - 2 months ago•](http://disq.us/url?url=https%3A%2F%2Fbitsofco.de%2Fp%2F9ffe2643-6475-43bb-9a1c-352daf3235b0%2F%3A1xoDhTtnToZQuEjskZNpombWrtc&imp=90l57iv3k85q6o&prev_imp=90kj3p81h5enbn&forum_id=3490249&forum=bitsofcode&thread_id=5605954947&thread=5443243513&zone=thread&area=bottom&object_type=thread&object_id=5443243513)[denno020— So if feature queries don't work in IE, the primary reason for ever needing to detect anything, why are they useful? I'm not trying to be smart, I'm …](http://disq.us/url?url=https%3A%2F%2Fbitsofco.de%2Fp%2F9ffe2643-6475-43bb-9a1c-352daf3235b0%2F%3A1xoDhTtnToZQuEjskZNpombWrtc&imp=90l57iv3k85q6o&prev_imp=90kj3p81h5enbn&forum_id=3490249&forum=bitsofcode&thread_id=5605954947&thread=5443243513&zone=thread&area=bottom&object_type=thread&object_id=5443243513)
- [ ### Asynchronous vs Deferred JavaScript       - 4 comments•      - 18 days ago•](http://disq.us/url?url=https%3A%2F%2Fbitsofco.de%2Fp%2F410d3917-c59d-4224-8114-7e7a4a2239d6%2F%3At6oOwlmieA71my3cMH6Uttc3uWs&imp=90l57iv3k85q6o&prev_imp=90kj3p81h5enbn&forum_id=3490249&forum=bitsofcode&thread_id=5605954947&thread=5588241704&zone=thread&area=bottom&object_type=thread&object_id=5588241704)[Lexa— Hi Ire,HTML parsing in the diagrams refers to tokenization of the provided HTML or DOM building?During the tokenization phase the browser's …](http://disq.us/url?url=https%3A%2F%2Fbitsofco.de%2Fp%2F410d3917-c59d-4224-8114-7e7a4a2239d6%2F%3At6oOwlmieA71my3cMH6Uttc3uWs&imp=90l57iv3k85q6o&prev_imp=90kj3p81h5enbn&forum_id=3490249&forum=bitsofcode&thread_id=5605954947&thread=5588241704&zone=thread&area=bottom&object_type=thread&object_id=5588241704)
- [Powered by Disqus](https://disqus.com/)
- [*✉*Subscribe  *✔*](https://disqus.com/embed/comments/?base=default&version=60c69418f14a8b7401cd956e1062204c&f=bitsofcode&t_i=%2Flinting-html-using-css%2F&t_u=https%3A%2F%2Fbitsofco.de%2Flinting-html-using-css%2F&t_d=Linting%20HTML%20using%20CSS&t_t=Linting%20HTML%20using%20CSS&s_o=default#)
- [*d*Add Disqus to your site](https://publishers.disqus.com/engage?utm_source=bitsofcode&utm_medium=Disqus-Footer)
- [*🔒*Privacy](https://help.disqus.com/customer/portal/articles/1657951?utm_source=disqus&utm_medium=embed-footer&utm_content=privacy-btn)