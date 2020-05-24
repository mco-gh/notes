Animated SVG favicons

[# blogccasion](https://blog.tomayac.com/)

**l'occasion**  *f* — Gelegenheit  *f*, die ~ , der ~; *bei Gelegenheit* — **à l'occasion**

[# Animated SVG favicons](https://blog.tomayac.com/2019/12/01/animated-svg-favicon/)

![](../_resources/e4dbb2fb8790c090b5fa6819fedc64d4.png)

By [Thomas Steiner](https://blog.tomayac.com/about/). Written on Sun Dec 01 2019. [**Technical**](https://blog.tomayac.com/tags/Technical)

When it comes to animating SVGs, there're three options: using CSS?, JS?, or SMIL?. Each comes with its own pros and cons, whose discussion is beyond the scope of this article, but [Sara Soueidan](https://www.sarasoueidan.com/) has a great [article](https://theblog.adobe.com/the-state-of-svg-animation) on the topic. In this post, I add a repeating *shrink* animation to a circle with all three methods, and then try to use these SVGs as favicons.

## Animating SVG with CSS [#](https://blog.tomayac.com/2019/12/01/animated-svg-favicon/#animating-svg-with-css)

Here's an example of animating an SVG with CSS based on the [`animation`](https://developer.mozilla.org/en-US/docs/Web/CSS/animation) and the [`transform`](https://developer.mozilla.org/en-US/docs/Web/CSS/transform) properties. I scale the circle from the center and repeat the animation forever:

`<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">[[NEWLINE]]  <style>[[NEWLINE]]    svg {[[NEWLINE]]      max-width: 100px;[[NEWLINE]]    }[[NEWLINE]][[NEWLINE]]    circle {[[NEWLINE]]      display: block;[[NEWLINE]]      animation: 2s linear infinite both circle-animation;[[NEWLINE]]      transform-origin: 50% 50%;[[NEWLINE]]    }[[NEWLINE]][[NEWLINE]]    @keyframes circle-animation {[[NEWLINE]]      0% {[[NEWLINE]]        transform: scale(1);[[NEWLINE]]      }[[NEWLINE]]      100% {[[NEWLINE]]        transform: scale(0);[[NEWLINE]]      }[[NEWLINE]]    }[[NEWLINE]]  </style>[[NEWLINE]]  <circle fill="red" cx="50" cy="50" r="45"/>[[NEWLINE]]</svg>`

## Animating SVG with JS [#](https://blog.tomayac.com/2019/12/01/animated-svg-favicon/#animating-svg-with-js)

The [SVG `<script>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Element/script) tag allows to add scripts to an SVG document. It has some [subtle differences](https://svgwg.org/svg2-draft/interact.html#ScriptElement) to the regular HTML `<script>`, for example, it uses the `href` instead of the `src` attribute, but above all it's important to know that any functions defined within any `<script>` tag have a *global scope* across the entire current document. Below, you can see an SVG script used to reduce the radius of the circle until it's equal to zero, then reset it to the initial value, and finally repeat this forever.

`<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">[[NEWLINE]]  <circle fill="blue" cx="50" cy="50" r="45" />[[NEWLINE]]  <script type="text/javascript"><![CDATA[[[NEWLINE]]    const circle = document.querySelector('circle');[[NEWLINE]]    let r = 45;[[NEWLINE]]    const animate = () => {[[NEWLINE]]      circle.setAttribute('r', r--);[[NEWLINE]]      if (r === 0) {[[NEWLINE]]        r = 45;[[NEWLINE]]      }[[NEWLINE]]      requestAnimationFrame(animate);[[NEWLINE]]    };[[NEWLINE]]    requestAnimationFrame(animate);[[NEWLINE]]  ]]></script>[[NEWLINE]]</svg>`

## Animating SVG with SMIL [#](https://blog.tomayac.com/2019/12/01/animated-svg-favicon/#animating-svg-with-smil)

The last example uses SMIL, where, via the [`<animate>`](https://developer.mozilla.org/en-US/docs/Web/SVG/SVG_animation_with_SMIL) tag inside of the `<circle>` tag, I declaratively describe that I want to animate the circle's `r` attribute (that determines the radius) and repeat it indefinitely.

`<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">[[NEWLINE]]  <circle fill="green" cx="50" cy="50" r="45">[[NEWLINE]]    <animate attributeName="r" from="45" to="0" dur="2s" repeatCount="indefinite"/>[[NEWLINE]]  </circle>[[NEWLINE]]</svg>`

## Using Animated SVGs as Images [#](https://blog.tomayac.com/2019/12/01/animated-svg-favicon/#using-animated-svgs-as-images)

Before using animated SVGs as favicons, I want to briefly discuss how you can use each of the three examples on a website. Again there're three options: referenced via the `src` attribute of an `<img>` tag, in an `<iframe>`, or inlined in the main document. Again, SVG scripts have access to the *global scope*, so they should definitely be used with care. Some user agents, for example, Google Chrome, don't run scripts for SVGs in `<img>`. The [Glitch](https://glitch.com/~animated-svg-favicon) embedded below shows all variants in action. My recommendation would be to stick with CSS animations whenever you can, since it's the most compatible and future-proof variant.

- assets
- README.md
- icon_css.svg
- icon_js.svg
- icon_smil.svg
- index.html
- script.js
- style.css

<svg  viewBox="0 0 100 100"  xmlns="http://www.w3.org/2000/svg">

# Animated SVG favicon

## Three methods to animate SVGs

 Choose an animated SVG as favicon:  CSS  JS  SMIL

 ![](../_resources/d9d7761cf71a85184ae9496131bcfbc2.png)
CSS animation in `img`.

CSS animation in `iframe`.

 ![](data:image/svg+xml,%3csvg viewBox='0 0 100 100' xmlns='http://www.w3.org/2000/svg' data-evernote-id='20' class='js-evernote-checked'%3e %3cstyle%3e svg %7b max-width: 100px%3b %7d circle %7b animation: 2s linear infinite both circle-animation%3b display: block%3b transform-origin: 50%25 50%25%3b %7d %40keyframes circle-animation %7b 0%25 %7b transform: scale(1)%3b %7d 100%25 %7b transform: scale(0)%3b %7d %7d %3c/style%3e %3ccircle fill='red' cx='50' cy='50' r='11' data-evernote-id='23' class='js-evernote-checked'%3e%3c/circle%3e %3c/svg%3e)

CSS animation inlined.

 ![](../_resources/3ef36a6464fce1bccd912cb215b220e5.png)
JS animation in `img`.

JS animation in `iframe`.

 ![](data:image/svg+xml,%3csvg viewBox='0 0 100 100' xmlns='http://www.w3.org/2000/svg' data-evernote-id='21' class='js-evernote-checked'%3e %3ccircle fill='blue' cx='50' cy='50' r='45' data-evernote-id='24' class='js-evernote-checked'%3e%3c/circle%3e %3cscript type='text/javascript'%3e const circle = document.querySelector('circle')%3b let r = 45%3b setInterval(() =%26gt%3b %7b circle.setAttribute('r'%2c r--)%3b if (r === 0) %7b r = 45%3b %7d %7d%2c 1000 / 60)%3b %3c/script%3e %3c/svg%3e)

JS animation inlined.

 ![](../_resources/b3e499de18128bcf86f8e2a3a414d6c3.png)
SMIL animation in `img`.

SMIL animation in `iframe`.

 ![](data:image/svg+xml,%3csvg viewBox='0 0 100 100' xmlns='http://www.w3.org/2000/svg' data-evernote-id='22' class='js-evernote-checked'%3e %3ccircle fill='green' cx='50' cy='50' r='8.88228' data-evernote-id='25' class='js-evernote-checked'%3e %3canimate attributeName='r' from='45' to='0' dur='2s' repeatCount='indefinite'%3e%3c/animate%3e %3c/circle%3e %3c/svg%3e)

SMIL animation inlined.

[![a8ad08d1-ae36-4487-9eff-b766981aa934.png](../_resources/3e7dd5512891daf9a8dd6012739f6cdb.png)animated-svg-favicon](https://glitch.com/~animated-svg-favicon)

by
tomayac[(L)](https://glitch.com/@tomayac)

[(L)](https://animated-svg-favicon.glitch.me/)
[(L)](https://glitch.com/~animated-svg-favicon)

## Using Animated SVGs as Favicons [#](https://blog.tomayac.com/2019/12/01/animated-svg-favicon/#using-animated-svgs-as-favicons)

Since [crbug.com/29417](https://crbug.com/29417) is fixed, Chrome *finally* supports SVG favicons, alongside [many other browsers](https://caniuse.com/#feat=link-icon-svg). I have recently successfully experimented with [`prefers-color-scheme` in SVG favicons](https://blog.tomayac.com/2019/09/21/prefers-color-scheme-in-svg-favicons-for-dark-mode-icons/), so I wanted to see if animated SVGs work, too. Long story short, it seems only Firefox supports them at the time of writing, and only favicons that are animated with either CSS or JS. You can see this working in Firefox in the screencast embedded below. If you open my [Glitch demo](https://animated-svg-favicon.glitch.me/) in a standalone window, you can test this yourself with the radio buttons at the top.

[(L)](https://www.youtube.com/watch?v=SlesN-eGdIE)

Should you use this in practice? Probably not, since it can be really distracting. It might be useful as a progressive enhancement to show activity during a short period of time, for example, while a web application is busy with processing data. Before considering to use this, I would definitely recommend taking the user's [`prefers-reduced-motion`](https://developers.google.com/web/updates/2019/03/prefers-reduced-motion) preferences into account.

[You can [edit this page on GitHub](https://github.com/tomayac/blogccasion/tree/master/posts/2019/2019-12-01_animated-svg-favicons.md).]

### Webmentions

#### 2 Replies

![65616ccc846223fcac9d7204e4ea4b8b26135aefd3ed25f7edc4c6e965a91c37.png](../_resources/dec638330b91aa0e0024e10d7b68ee88.png)

By [**Mr.doob**](https://twitter.com/mrdoob/status/1201130350711394304). Written on Sun Dec 01 2019 at 13:26 .

For the JS one, maybe better to use requestAnimationaFrame instead of setInterval? Unless things have changed recently, setInterval will be called at 1fps when the tab is hidden.

![05796e7c6ce8b47a935fae4489812faf9813783f9c99b9b9dbb54d2de4bb9770.jpg](../_resources/b5ce1b5df326a9ec4d6b17d6a6de146e.jpg)

By [**Thomas Steiner**](https://twitter.com/tomayac/status/1201131044730261507). Written on Sun Dec 01 2019 at 13:28 .

github.com/tomayac/blogcc… Yeah, good remark. I was honestly surprised that the inlined SVG with the JS animation played, while the referenced via `<img>` didn’t. Need to find out if this is working as intended.

## Pages

- [Home](https://blog.tomayac.com/)
- [Archive](https://blog.tomayac.com/posts/)
- [About](https://blog.tomayac.com/about/)

## Tags

- [Work](https://blog.tomayac.com/tags/Work/)
- [Private](https://blog.tomayac.com/tags/Private/)
- [France](https://blog.tomayac.com/tags/France/)
- [Technical](https://blog.tomayac.com/tags/Technical/)
- [Political](https://blog.tomayac.com/tags/Political/)

![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' data-evernote-id='512' class='js-evernote-checked'%3e%3csymbol id='icon-rss' aria-label='RSS' role='img' viewBox='0 0 512 512' data-evernote-id='513' class='js-evernote-checked'%3e%3crect width='512' height='512' rx='15%25' fill='%23f80' data-evernote-id='514' class='js-evernote-checked'%3e%3c/rect%3e%3ccircle cx='145' cy='367' r='35' fill='%23fff' data-evernote-id='515' class='js-evernote-checked'%3e%3c/circle%3e%3cpath fill='none' stroke='%23fff' stroke-width='60' d='M109 241c89 0 162 73 162 162M109 127c152 0 276 124 276 276' data-evernote-id='516' class='js-evernote-checked'%3e%3c/path%3e%3c/symbol%3e%3csymbol id='icon-twitter' aria-label='Twitter' role='img' viewBox='0 0 512 512' data-evernote-id='517' class='js-evernote-checked'%3e%3crect width='512' height='512' rx='15%25' fill='%231da1f3' data-evernote-id='518' class='js-evernote-checked'%3e%3c/rect%3e%3cpath fill='%23fff' d='M437 152a72 72 0 0 1-40 12 72 72 0 0 0 32-40 72 72 0 0 1-45 17 72 72 0 0 0-122 65 200 200 0 0 1-145-74 72 72 0 0 0 22 94 72 72 0 0 1-32-7 72 72 0 0 0 56 69 72 72 0 0 1-32 1 72 72 0 0 0 67 50 200 200 0 0 1-105 29 200 200 0 0 0 309-179 200 200 0 0 0 35-37' data-evernote-id='519' class='js-evernote-checked'%3e%3c/path%3e%3c/symbol%3e%3csymbol id='icon-mastodon' aria-label='Mastodon' role='img' viewBox='0 0 512 512' fill='%23fff' data-evernote-id='520' class='js-evernote-checked'%3e%3crect width='512' height='512' rx='15%25' data-evernote-id='521' class='js-evernote-checked'%3e%3c/rect%3e%3cpath d='M409 290c-5 24-43 50-85 56-86 11-137-6-137-6 3 13-4 54 70 52 31 0 58-7 58-7l2 27c-51 24-107 15-140 6-67-17-79-90-81-162v-59c0-74 49-96 49-96 50-24 180-22 222 0 0 0 49 22 49 96 0 0 1 55-7 93' fill='%233088d4' data-evernote-id='522' class='js-evernote-checked'%3e%3c/path%3e%3cpath d='M358 202v91h-35v-88c0-18-8-27-23-27-18 0-27 11-27 33v47h-34v-47c0-22-9-33-27-33-15 0-23 9-23 27v88h-35v-91c0-18 5-60 52-60 39 0 50 37 50 37s10-37 50-37c45 0 52 42 52 60' data-evernote-id='523' class='js-evernote-checked'%3e%3c/path%3e%3c/symbol%3e%3csymbol id='icon-pgp' aria-label='PGP Public Key' role='img' viewBox='0 0 512 512' data-evernote-id='524' class='js-evernote-checked'%3e%3crect width='512' height='512' rx='15%25' fill='%2329303d' data-evernote-id='525' class='js-evernote-checked'%3e%3c/rect%3e%3cg fill='%2329303d' data-evernote-id='526' class='js-evernote-checked'%3e%3cpath stroke='%23e0e4eb' stroke-width='32' d='M346 214v-37c0-123-180-123-180 0v37' data-evernote-id='527' class='js-evernote-checked'%3e%3c/path%3e%3crect fill='%23ff0' height='210' rx='5%25' width='280' x='115' y='210' data-evernote-id='528' class='js-evernote-checked'%3e%3c/rect%3e%3ccircle cx='256' cy='296' r='28' data-evernote-id='529' class='js-evernote-checked'%3e%3c/circle%3e%3cpath d='M262 296h-12l-16 69h44' data-evernote-id='530' class='js-evernote-checked'%3e%3c/path%3e%3c/g%3e%3c/symbol%3e%3csymbol id='icon-github' aria-label='GitHub' role='img' viewBox='0 0 512 512' data-evernote-id='531' class='js-evernote-checked'%3e%3crect width='512' height='512' rx='15%25' fill='%231B1817' data-evernote-id='532' class='js-evernote-checked'%3e%3c/rect%3e%3cpath fill='%23fff' d='M335 499c14 0 12 17 12 17H165s-2-17 12-17c13 0 16-6 16-12l-1-50c-71 16-86-28-86-28-12-30-28-37-28-37-24-16 1-16 1-16 26 2 40 26 40 26 22 39 59 28 74 22 2-17 9-28 16-35-57-6-116-28-116-126 0-28 10-51 26-69-3-6-11-32 3-67 0 0 21-7 70 26 42-12 86-12 128 0 49-33 70-26 70-26 14 35 6 61 3 67 16 18 26 41 26 69 0 98-60 120-117 126 10 8 18 24 18 48l-1 70c0 6 3 12 16 12z' data-evernote-id='533' class='js-evernote-checked'%3e%3c/path%3e%3c/symbol%3e%3c/svg%3e)

## Related

- [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='icon js-evernote-checked' data-evernote-id='538'%3e%3crect width='512' height='512' rx='15%25' fill='%23f80' data-evernote-id='514' class='js-evernote-checked'%3e%3c/rect%3e%3ccircle cx='145' cy='367' r='35' fill='%23fff' data-evernote-id='515' class='js-evernote-checked'%3e%3c/circle%3e%3cpath fill='none' stroke='%23fff' stroke-width='60' d='M109 241c89 0 162 73 162 162M109 127c152 0 276 124 276 276' data-evernote-id='516' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e) Blog Feed](https://blog.tomayac.com/feed/feed.xml)
- [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='icon js-evernote-checked' data-evernote-id='542'%3e%3crect width='512' height='512' rx='15%25' fill='%231da1f3' data-evernote-id='518' class='js-evernote-checked'%3e%3c/rect%3e%3cpath fill='%23fff' d='M437 152a72 72 0 0 1-40 12 72 72 0 0 0 32-40 72 72 0 0 1-45 17 72 72 0 0 0-122 65 200 200 0 0 1-145-74 72 72 0 0 0 22 94 72 72 0 0 1-32-7 72 72 0 0 0 56 69 72 72 0 0 1-32 1 72 72 0 0 0 67 50 200 200 0 0 1-105 29 200 200 0 0 0 309-179 200 200 0 0 0 35-37' data-evernote-id='519' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e) Twitter](https://twitter.com/tomayac)
- [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='icon js-evernote-checked' data-evernote-id='546'%3e%3c/svg%3e) Tweet Archive](https://tomayac.com/tweets)
- [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='icon js-evernote-checked' data-evernote-id='550'%3e%3crect width='512' height='512' rx='15%25' data-evernote-id='521' class='js-evernote-checked'%3e%3c/rect%3e%3cpath d='M409 290c-5 24-43 50-85 56-86 11-137-6-137-6 3 13-4 54 70 52 31 0 58-7 58-7l2 27c-51 24-107 15-140 6-67-17-79-90-81-162v-59c0-74 49-96 49-96 50-24 180-22 222 0 0 0 49 22 49 96 0 0 1 55-7 93' fill='%233088d4' data-evernote-id='522' class='js-evernote-checked'%3e%3c/path%3e%3cpath d='M358 202v91h-35v-88c0-18-8-27-23-27-18 0-27 11-27 33v47h-34v-47c0-22-9-33-27-33-15 0-23 9-23 27v88h-35v-91c0-18 5-60 52-60 39 0 50 37 50 37s10-37 50-37c45 0 52 42 52 60' data-evernote-id='523' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e) Mastodon](https://toot.cafe/@tomayac)
- [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='icon js-evernote-checked' data-evernote-id='554'%3e%3crect width='512' height='512' rx='15%25' fill='%231B1817' data-evernote-id='532' class='js-evernote-checked'%3e%3c/rect%3e%3cpath fill='%23fff' d='M335 499c14 0 12 17 12 17H165s-2-17 12-17c13 0 16-6 16-12l-1-50c-71 16-86-28-86-28-12-30-28-37-28-37-24-16 1-16 1-16 26 2 40 26 40 26 22 39 59 28 74 22 2-17 9-28 16-35-57-6-116-28-116-126 0-28 10-51 26-69-3-6-11-32 3-67 0 0 21-7 70 26 42-12 86-12 128 0 49-33 70-26 70-26 14 35 6 61 3 67 16 18 26 41 26 69 0 98-60 120-117 126 10 8 18 24 18 48l-1 70c0 6 3 12 16 12z' data-evernote-id='533' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e) GitHub](https://github.com/tomayac)
- [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='icon js-evernote-checked' data-evernote-id='558'%3e%3crect width='512' height='512' rx='15%25' fill='%2329303d' data-evernote-id='525' class='js-evernote-checked'%3e%3c/rect%3e%3cg fill='%2329303d' data-evernote-id='526' class='js-evernote-checked'%3e%3cpath stroke='%23e0e4eb' stroke-width='32' d='M346 214v-37c0-123-180-123-180 0v37' data-evernote-id='527' class='js-evernote-checked'%3e%3c/path%3e%3crect fill='%23ff0' height='210' rx='5%25' width='280' x='115' y='210' data-evernote-id='528' class='js-evernote-checked'%3e%3c/rect%3e%3ccircle cx='256' cy='296' r='28' data-evernote-id='529' class='js-evernote-checked'%3e%3c/circle%3e%3cpath d='M262 296h-12l-16 69h44' data-evernote-id='530' class='js-evernote-checked'%3e%3c/path%3e%3c/g%3e%3c/svg%3e) Public Key](https://blog.tomayac.com/pgp_public_key.asc)
- © 2005–2019 [Thomas Steiner](https://blog.tomayac.com/about).
- Distributed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).
- Contact and required [legal info](https://blog.tomayac.com/about/).

[![](../_resources/d07e448cab0d6e79298590b1b8f99533.png)](https://validator.w3.org/nu/?doc=https://blog.tomayac.com/2019/12/01/animated-svg-favicon/)