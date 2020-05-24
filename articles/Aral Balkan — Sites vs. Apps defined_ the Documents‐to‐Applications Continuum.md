Aral Balkan — Sites vs. Apps defined: the Documents‐to‐Applications Continuum.

## Sites vs. Apps defined: the Documents‐to‐Applications Continuum.

15 May, 2013 Documents and applications sit at opposite ends of a continuum.

There seems to be a fundamental misunderstanding being perpetuated in the web community that there is no difference between what we call a web site and what we call a web application. At the excellent [Responsive Day Out](http://responsiveconf.com/), a member of the audience asked whether there are different considerations to be aware of in responsive design when making a web application versus a web site. I thought that this was a well‐articulated and, furthermore, timely and important question. Unfortunately, it was brushed aside and ridiculed, with our host (and my good friend), Jeremy, stating that it was impossible to provide a definition for sites that would differentiate them from apps. [Jeremy has since articulated his point in a blog post](http://adactio.com/journal/6246/) in which he states:

> Remember when we were all publishing documents on the web, but then there was that all-changing event and then we all started making web apps instead? No? Me neither.

> In fact, I have yet to hear a definition of what exactly constitutes a web app… I’ve heard plenty of descriptions of web apps; there are many, many facets that could be used to describe a web app …but no hard’n’fast definitions.

This perplexes me because not only is it exceedingly simple to articulate definitions for sites and apps that makes the difference plainly clear but I also feel that understanding that difference is an essential prerequisite to understanding the scope of our medium in general and of our products in particular. It has ramifications that extend to calculating the amount of risk involved in a product and affects the making of important decisions like who to hire and which tools and technologies to use.

So, let me quickly define the two so we can get to the actual point of the post, which is that the dichotomy — false, or otherwise — is not what’s important because what we are really talking about is a continuum.

### What is a site?

Web sites are documents; they are content‐centric. Sites are geared towards content consumption.

### What is an app?

Web apps are tools; they are behaviour‐centric. Apps are geared towards content creation and manipulation.

### The dichotomy: not false, but not very valuable either.

Although it is certainly possible to define a site as separate to an app, as I demonstrate above, it does not benefit us greatly to think of the relationship as a dichotomy. However, if we wanted to, we could; it is not a false dichotomy. There definitely are products that fall squarely in each camp. For example, a simple online brochure for a university programme that contains nothing but text, images, and hyperlinks is clearly a document. It is clearly a site. An HTML‐based Photoshop clone, on the other hand, is clearly an app — it has no inherent content of its own. Instead, it is used to *create* and *manipulate* content.

To easily differentiate between sites and apps, ask yourself the following question:

‘If I was to remove all behaviour from this product, would the content still have value?’

If so, it is a site; it was content‐centric to begin with. Any behaviour that was added — hopefully via progressive enhancement — was simply a nice‐to‐have; perhaps to aid in the navigation of the content.

If we apply this question to the university brochure, it becomes clear that it is a site. Even if we removed all the behaviour, the content itself would have value because that’s where the value was in the first instance. It is content‐centric. On the other hand, if we strip all behaviour from a Photoshop clone, what content are we left with? Nothing. Because the Photoshop clone is an application that is used to *create* and *manipulate* content. It is behaviour‐centric, not content‐centric.

If you think of it as graceful degradation, there is nothing to degrade to in an application because there was no content to start with, only behaviour. The opposite is true for sites.

The most important point to understand, however, is that most products will not fall into either extreme; because that is exactly what these are: they are the extremes on a continuum: The Documents‐to‐Applications Continuum.

### The Documents‐to‐Applications Continuum

![The documents‐to‐applications continuum.](../_resources/4a7f8342f6acab54a79850614ed90d80.png)

Although I have been mentioning the concept for several years in my talks (for example, see my opening keynote from Fronteers 2011, titled [The Future is Native](https://vimeo.com/30659519)), I only wrote about it last year in the Smashing Book article [Mobile Considerations in User Experience Design](http://mobile.smashingmagazine.com/2012/06/18/mobile-considerations-in-user-experience-design-web-or-native/):

> When a product falls closer to the documents side of the continuum, we can use progressive enhancement to layer features and interactions on top of the content-based core while keeping that core accessible to the largest number of people possible. These progressively enhanced features usually either layer advanced formatting or layout on these documents or add fanciful interactions for navigating within or between them. We can make the content adapt to different screen sizes and make the limited interactions that are used to navigate the content adapt to different input mechanisms. This isn’t an easy task, but nor is it impossible.

> As products shift from the documents side of the spectrum to the applications side, however, implementing progressive enhancement gets harder. In fact, it might become entirely meaningless or impossible. How would you gracefully degrade an online image editor, for example? How would an image editor work on feature handsets without graphical displays? What content would you actually fall back to displaying?

> In order to create exemplary user experiences, we need to maintain focus. This focus has to be placed squarely on meeting the needs of our users in the best way possible. No product team on Earth has the resources to create applications that provide the best possible user experience for every user.

> Given unlimited time and resources, we could optimize the user experience of our apps on every device and platform known to humankind. However, given limited time and budget we have to work with in the real world, we must be selective with our audience, problem domain, platforms and devices. We do this not to exclude people unnecessarily but because we realize that including everyone and giving everyone a great user experience is impractical.

The article goes on to dissect how *where* a product falls on the Documents‐to‐Applications Continuum can affect the design decisions that we make. And, it is precisely for this reason that it is important that we have both the vocabulary and the precision within that vocabulary to have these conversations in a meaningful way. Because it affects the degree to which we understand the products we are building, which in turn affects our ability to communicate with precision about the requirements of our products with others.

If someone told me they were building a ‘web thang’ — as Jeremy suggests —  I would tell them to come back once they’ve got the vocabulary for us to have a meaningful conversation about what they’re building.

The distinction between sites and apps is an essential one that every designer and developer should be aware of because it directly affects our design decisions (and, *ergo*, the business decisions) for your product. The thing not to do is to fixate on the dichotomy itself and to realise that your product will most likely fall somewhere on the continuum.

### The Documents‐to‐Applications Continuum as antidote to ‘We Need an App’ Syndrome.

In addition to being a valuable framework for helping you to glean a deeper understanding of the nature of the product that you want to build, using the Documents‐to‐Applications Continuum can also give you the defence you need against the dreaded ‘We Need an App’ virus. You know, when your boss comes to you with ‘We need an app of the site’.

When this happens, simply pull out the Documents‐to-Applications Continuum and show your boss how your web site, being content‐centric and not behaviour‐centric, falls closer to the documents side of the spectrum and how it doesn’t make sense to make an app of it. Instead, you can tell them, ‘what we should do is to iterate over our existing web site to make it responsive’.

I firmly believe that having precise definitions for — and a good understanding of the distinction between — what is a web site and what is a web app, coupled with an appreciation for the Documents‐to‐Applications Continuum, will greatly help to reduce the number of projects where people mistakenly make apps when what they really need is a responsive web site. And, anything that can reduce the number of designer and developer hours wasted in solving the wrong problem cannot be a bad thing.

So, far from being a meaningless distinction and far from being impossible to define, it is absolutely essential that we precisely define what is a web site and what is a web application and understand that while there definitely is a dichotomy, the dichotomy lies at the extremes of a continuum and the real value is in using the continuum itself as a framework for discussion within our design conversations.