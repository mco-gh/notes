The JavaScript Framework That Puts Web Pages on a Diet | WIRED

[Klint Finley](https://www.wired.com/contributor/klint-finley)
[Business](https://www.wired.com/category/business)
04.04.2020 10:00 AM

# The JavaScript Framework That Puts Web Pages on a Diet

Svelte, created by a graphics editor for the New York Times, has attracted a following among programmers who want their pages to load faster.

![svelte-javascript-508482075.jpg](../_resources/2bad44c87837e72f857883f7766fc39c.jpg)
​Illustration: Elena Lacey; Getty Images

- [![](data:image/svg+xml,%3csvg class='icon icon-facebook js-evernote-checked' focusable='false' viewBox='0 0 32 32' width='32' height='32' xmlns='http://www.w3.org/2000/svg' data-evernote-id='178'%3e%3ctitle data-evernote-id='460' class='js-evernote-checked'%3eFacebook%3c/title%3e%3cpath d='M13.621 11.099v2.203H12v2.693h1.621V24h3.33v-8.005h2.235s.209-1.291.31-2.703h-2.532V11.45c0-.275.363-.646.722-.646H19.5V8h-2.467c-3.494 0-3.412 2.696-3.412 3.099z' fill-rule='nonzero' data-evernote-id='461' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://www.facebook.com/dialog/feed?&display=popup&caption=&app_id=719405864858490&link=https%3A%2F%2Fwww.wired.com%2Fstory%2Fjavascript-framework-puts-web-pages-diet%2F%3Futm_source%3Dfacebook%26utm_medium%3Dsocial%26utm_campaign%3Donsite-share%26utm_brand%3Dwired%26utm_social-type%3Dearned)
- [![](data:image/svg+xml,%3csvg class='icon icon-twitter js-evernote-checked' focusable='false' viewBox='0 0 32 32' width='32' height='32' xmlns='http://www.w3.org/2000/svg' data-evernote-id='179'%3e%3ctitle data-evernote-id='464' class='js-evernote-checked'%3eTwitter%3c/title%3e%3cpath d='M13.032 22.003c6.038 0 9.34-5.002 9.34-9.34a9.16 9.16 0 0 0-.01-.424A6.678 6.678 0 0 0 24 10.54a6.553 6.553 0 0 1-1.885.517 3.293 3.293 0 0 0 1.443-1.816 6.578 6.578 0 0 1-2.084.797 3.283 3.283 0 0 0-5.594 2.994A9.32 9.32 0 0 1 9.114 9.6a3.28 3.28 0 0 0 1.016 4.382 3.258 3.258 0 0 1-1.487-.41v.042a3.284 3.284 0 0 0 2.633 3.218 3.292 3.292 0 0 1-1.483.056 3.286 3.286 0 0 0 3.067 2.28 6.587 6.587 0 0 1-4.077 1.405c-.265 0-.526-.015-.783-.045a9.294 9.294 0 0 0 5.032 1.474' fill-rule='evenodd' data-evernote-id='465' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://twitter.com/intent/tweet/?url=https%3A%2F%2Fwww.wired.com%2Fstory%2Fjavascript-framework-puts-web-pages-diet%2F%3Futm_source%3Dtwitter%26utm_medium%3Dsocial%26utm_campaign%3Donsite-share%26utm_brand%3Dwired%26utm_social-type%3Dearned&text=&via=wired)
- [![](data:image/svg+xml,%3csvg class='icon icon-email js-evernote-checked' focusable='false' viewBox='0 0 32 32' width='32' height='32' xmlns='http://www.w3.org/2000/svg' data-evernote-id='180'%3e%3ctitle data-evernote-id='468' class='js-evernote-checked'%3eEmail%3c/title%3e%3cpath d='M6 23h20V9H6v14zm3.631-12H22.37l-6.368 5.661L9.631 11zM24 12.227V21H8v-8.773l8.002 7.109L24 12.227z' fill-rule='evenodd' data-evernote-id='469' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://www.wired.com/story/javascript-framework-puts-web-pages-diet/mailto:?subject=&body=https%3A%2F%2Fwww.wired.com%2Fstory%2Fjavascript-framework-puts-web-pages-diet%2F%3Futm_source%3Donsite-share%26utm_medium%3Demail%26utm_campaign%3Donsite-share%26utm_brand%3Dwired)

Websites are too damn big.

The average web page is about 2 megabytes, according to [HTTP Archive](https://www.httparchive.org/reports/state-of-the-web?start=latest), a site that tracks the performance of websites and the technologies they use. Sure you can download 2 megabytes in less than a second on a good 4G mobile connection. But today’s web pages are problematic for people on slow connections or with small bandwidth caps. Not all that long ago, a [complex game](https://www.wired.com/2016/04/average-webpage-now-size-original-doom/) or software program fit on a 1.4 megabyte floppy disk.

There are many reasons today’s web is so bloated, including the ads and tracking scripts that saddle so many pages. Another reason is that websites do much more than just display text and images. Many sites now look and feel like full-blown desktop applications.

To build these interactive sites, many web developers turn to open source packages that handle common tasks. These tools liberate programmers from a lot of grunt work, but can add heft to a project. Facebook's popular open source React library for building user interfaces, for example, weighs in at 100 kilobytes. Throw in some other tools, and graphics, and soon you’re talking many megabytes.

The up and coming JavaScript framework [Svelte](https://svelte.dev/), created by visual journalist and software developer Rich Harris, aims to make it easier to write faster, smaller interactive websites and applications. Web developer Shawn Wang says he cut the size of his [personal website](https://www.swyx.io/) from 187 kilobytes to 9 kilobytes by switching from React to Svelte.

"It was a big 'wow' moment," Wang says. "I wasn't even trying to optimize for size and it just dropped."

Harris, a graphics editor for the *New York Times*, created and released the first version of Svelte in 2016 while working for the *Guardian*. Many of his projects involved interactive graphics and animations, but he worried that the graphics could take too long to load or chew through users’ data limits.

Frameworks add heft to websites because they traditionally serve as a middle layer between an app's code and the user's browser. That means developers need to bundle the entire framework, in addition to their own code, with an app, even if they don't use all of the framework's features. Wang compares this to a rocket ship that needs massive fuel tanks to launch into space.

Harris took a different approach. Svelte performs its middle-layer work before a developer uploads code to a web server, well before a user ever downloads it. This makes it possible to remove unnecessary features, shrinking the resulting app. It also reduces the number of moving parts when a user runs the app, which can make Svelte apps faster and more efficient. “Svelte is like a space elevator,” Wang says. The framework was tricky to create, but advocates say it makes it easier for developers to build efficient apps.

![Guide_to_open_source_software_02.jpg](../_resources/7da0208075ae96edde3dc3a92bd81015.jpg)

### [The WIRED Guide to Open Source Software](https://www.wired.com/story/wired-guide-open-source-software)

Everything you ever wanted to know about Linux, GNU, and how big companies are making money off of free, collaboration-based software.

By Klint Finley

Wang says he likes to use Svelte for web pages, but he still uses React for larger applications, including his professional work. For one thing, the larger an app, the more likely a developer will use all of React's features. That makes it less wasteful. In fact, some Svelte apps are bigger than apps made with React or similar tools. And there’s much greater demand for React developers than [Svelte developers](https://twitter.com/sveltejobs).

In the [State of JavaScript 2019](https://2019.stateofjs.com/front-end-frameworks/svelte/) survey of more than 21,000 developers, 88 percent of respondents who had used Svelte said they were satisfied with it, giving it the second highest satisfaction rating in the survey, just behind React’s 89 percent satisfaction rate. But only 7.8 percent of respondents had used Svelte, and 24.7 percent had never heard of it. Meanwhile, 80.3 percent had used React.

Most Popular

- [![How-to-Keep-Your-Zoom-Chats-Private-and-Secure.jpg](../_resources/5daa9b262c554da351bc26ca7167f36e.jpg)](https://www.wired.com/story/keep-zoom-chats-private-secure#intcid=recommendations_wired-right-rail-popular_76df4dbd-adcb-4058-9148-72c90ad429af_popular4-1)

Security

[ How to Keep Your Zoom Chats Private and Secure](https://www.wired.com/story/keep-zoom-chats-private-secure#intcid=recommendations_wired-right-rail-popular_76df4dbd-adcb-4058-9148-72c90ad429af_popular4-1)

David Nield

- [![Science_emissions_covid19-1208249265.jpg](../_resources/1a02674590f69fc474934bad3fc447bf.jpg)](https://www.wired.com/story/the-pandemic-has-led-to-a-huge-global-drop-in-air-pollution#intcid=recommendations_wired-right-rail-popular_76df4dbd-adcb-4058-9148-72c90ad429af_popular4-1)

Science

[ The Pandemic Has Led to a Huge, Global Drop in Air Pollution](https://www.wired.com/story/the-pandemic-has-led-to-a-huge-global-drop-in-air-pollution#intcid=recommendations_wired-right-rail-popular_76df4dbd-adcb-4058-9148-72c90ad429af_popular4-1)

Jonathan Watts and Niko Kommenda

- [![BC-Avigan-457969078.jpg](../_resources/74e3b82c4c92a6357d93d96c752f1d73.jpg)](https://www.wired.com/story/japan-is-racing-to-test-a-drug-to-treat-covid-19#intcid=recommendations_wired-right-rail-popular_76df4dbd-adcb-4058-9148-72c90ad429af_popular4-1)

Backchannel

[ Japan Is Racing to Test a Drug to Treat Covid-19](https://www.wired.com/story/japan-is-racing-to-test-a-drug-to-treat-covid-19#intcid=recommendations_wired-right-rail-popular_76df4dbd-adcb-4058-9148-72c90ad429af_popular4-1)

Joshua Hunt
-

- [![CULTURE_GEEKSGUIDE_MCDTHHU_EC039.jpg](../_resources/66700a1a6a3f2577677acc9b783e864e.jpg)](https://www.wired.com/2020/03/geeks-guide-spartans#intcid=recommendations_wired-right-rail-popular_76df4dbd-adcb-4058-9148-72c90ad429af_popular4-1)

Culture

[ Actually, the Spartans Weren't All That Great](https://www.wired.com/2020/03/geeks-guide-spartans#intcid=recommendations_wired-right-rail-popular_76df4dbd-adcb-4058-9148-72c90ad429af_popular4-1)

Geek's Guide to the Galaxy

Advertisement

Harris understands why many developers would be hesitant to invest in learning Svelte. The world of JavaScript development moves fast, and programmers already have a [dizzying number of tools](https://www.wired.com/story/javascript-developers-more-choices-mean-hard-choices/) to choose from and learn. "React has the advantage of being backed by Facebook, a strong job market, and a huge ecosystem of third-party things that work with it," he says. Although Harris uses Svelte to make graphics and animations for the *New York Times*, the publisher's site is still based on React.

Svelte is still a hobby project that Harris and other developers work on primarily in their free time. Harris only works on it "on the clock" when he needs to fix something or add a feature that helps him with his work for the *Times*.

Harris says Svelte is best suited for cases where performance and file sizes are particularly important, such as apps that run on smart TVs or low-power devices.

But some Svelte developers use it to build larger apps. Ryan Atkinson is the founder of [Felt Social](https://felt.social/), which makes tools for building highly customizable social websites. He says he chose Svelte because it makes for faster, more responsive applications, even if they’re not always the smallest. “Svelte’s architecture can fundamentally change the game of building user interfaces,” he says.

Atkinson says programmers often dismiss tools that are good for building small things, thinking they're "toys" that can't be used to build big things.

"I think that's a fallacy," he says. After all, he points out, JavaScript was once considered a “toy language.” Now it’s used to write apps like Gmail and Google Docs.

* * *

More Great WIRED Stories

- DIY rockets, daredevils, and the [tragedy of Mad Mike Hughes](https://www.wired.com/story/diy-rockets-tragedy-mad-mike-hughes/?itm_campaign=BottomRelatedStories_Sections_4&itm_content=footer-recirc)
- The “surreal” frenzy inside [the US’ biggest mask maker](https://www.wired.com/story/surreal-frenzy-inside-us-biggest-mask-maker/?itm_campaign=BottomRelatedStories_Sections_4&itm_content=footer-recirc)
- I played a “perp” on a popular TV show—[except it wasn’t me](https://www.wired.com/story/i-played-a-perp-on-a-popular-tv-show-imdb/?itm_campaign=BottomRelatedStories_Sections_4&itm_content=footer-recirc)
- Airlines use empty passenger jets [to ease the cargo crunch](https://www.wired.com/story/airlines-use-empty-passenger-jets-ease-cargo-crunch/?itm_campaign=BottomRelatedStories_Sections_4&itm_content=footer-recirc)
- Panic, pandemic, [and the body politic](https://www.wired.com/story/what-coronavirus-pandemic-says-about-society/?itm_campaign=BottomRelatedStories_Sections_4&itm_content=footer-recirc)
- Why can't AI [grasp cause and effect](https://www.wired.com/story/ai-smart-cant-grasp-cause-effect/?itm_campaign=BottomRelatedStories_Sections_4&itm_content=footer-recirc)? Plus: [Get the latest AI news](https://www.wired.com/category/business/artificial-intelligence/?itm_campaign=BottomRelatedStories_Sections_4&itm_content=footer-recirc)
- Torn between the latest phones? Never fear—check out our [iPhone buying guide](https://wired.com/gallery/iphone-buying-guide/?itm_campaign=BottomRelatedStories&itm_content=footer-recirc) and [favorite Android phones](https://wired.com/gallery/best-android-phones/?itm_campaign=BottomRelatedStories&itm_content=footer-recirc)