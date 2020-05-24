webslides/WebSlides

# [(L)](https://github.com/webslides/WebSlides#webslides--create-stories-with-karma)WebSlides = Create stories with Karma

[[68747470733a2f2f696d672e736869656c64732e696f2f747769747465722f75726c2f68747470732f6769746875622e636f6d2f776562736c696465732f776562736c696465732e7376673f7374796c653d736f6369616c](../_resources/399db293155251b88bab6ce76ff00949.bin)](http://opensource.org/licenses/MIT)[[68747470733a2f2f636f6465636f762e696f2f67682f776562736c696465732f576562536c696465732f6272616e63682f6d61737465722f67726170682f62616467652e737667](../_resources/912435e25b6919213e9aed5f3d595063.bin)](https://github.com/webslides/webslides/releases/latest)[[68747470733a2f2f696d672e736869656c64732e696f2f62616467652f6c6963656e73652d4d49542d626c75652e737667](../_resources/a9509a96b7cc29dbbc97125400c3c23c.bin)](https://codecov.io/gh/webslides/WebSlides)[[68747470733a2f2f696d672e736869656c64732e696f2f62616467652f446f6e6174652d50617950616c2d677265656e2e737667](../_resources/9876cdc5561b4afee683145c754e55d5.bin)](https://www.paypal.me/jlantunez/8)[[68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f72656c656173652f776562736c696465732f776562736c696465732e737667](../_resources/55156e8027ff1ca75a9dfec2ee5582a5.bin)](https://twitter.com/webslides)

Finally, everything you need to make HTML presentations, landings, and longforms in a beautiful way. Just a basic knowledge of HTML and CSS is required. Designers, marketers, and journalists can now focus on the content. — https://webslides.tv/demos.

* * *

### [(L)](https://github.com/webslides/WebSlides#download)Download

Simply choose a demo and customize it in seconds. Latest version: [webslides.tv/webslides-latest.zip](https://webslides.tv/webslides-latest.zip).

* * *

### [(L)](https://github.com/webslides/WebSlides#whats-in-the-download)What's in the download?

The download includes demos and images (devices and logos). All content is for demo purposes only. Images are property of their respective owners.

	webslides/
	├── index.html
	├── css/
	│   ├── base.css
	│   └── colors.css
	│   └── svg-icons.css (optional)
	├── js/
	│   ├── webslides.js
	│   └── svg-icons.js (optional)
	└── demos/
	└── images/

## [(L)](https://github.com/webslides/WebSlides#features)Features

- Navigation (horizontal and vertical sliding): remote presenters, touchpad, keyboard shortcuts, and swipe.
- Slide counter.
- Permalinks: go to a specific slide.
- Autoslide.
- Click to nav.
- Simple CSS alignments. Put content wherever you want (vertical centering...)
- 40+ components: background images/videos, quotes, cards, covers...
- Flexible blocks with auto-fill and equal height.
- Fonts: Roboto, Maitree (Serif), and San Francisco.
- Vertical rhythm (use multiples of 8).

## [(L)](https://github.com/webslides/WebSlides#markup)Markup

- Code is clean and scalable. It uses intuitive markup with popular naming conventions. There's no need to overuse classes or nesting.
- Each parent `<section>` in the `#webslides` element is an individual slide.

<article  id="webslides">
<section>
<h1>Slide 1</h1>
</section>

<section  class="bg-black aligncenter"> <!-- .wrap = container 1200px --> <div  class="wrap">

<h1>Slide 2</h1>
</div>
</section>
</article>

### [(L)](https://github.com/webslides/WebSlides#vertical-sliding)Vertical Sliding

<article  id="webslides"  class="vertical">

### [(L)](https://github.com/webslides/WebSlides#css-syntax-classes)CSS Syntax (classes)

- Typography: `.text-landing`, `.text-data`, `.text-intro`...
- Background Colors: `.bg-primary`, `.bg-apple`, `.bg-blue`...
- Background Images: `.background`,`.background-center-bottom`...
- Cards: `.card-50`, `.card-40`...
- Flexible Blocks: `.flexblock.clients`, `.flexblock.metrics`...

### [(L)](https://github.com/webslides/WebSlides#extensions)Extensions

You can add:

- [Unsplash](https://unsplash.com/) photos
- [animate.css](https://daneden.github.io/animate.css)
- [particles.js](https://github.com/VincentGarreau/particles.js)
- [Animate on scroll](http://michalsnik.github.io/aos/) (Useful for longform articles)
- [pt](http://williamngan.github.io/pt/)

### [(L)](https://github.com/webslides/WebSlides#dive-in)Dive In!

- Do not miss [our demos](https://webslides.tv/).
- Want to get techie? Read [our wiki](https://github.com/webslides/WebSlides/blob/master/wiki):
    - [FAQ](https://github.com/webslides/WebSlides/wiki)
    - [Core API](https://github.com/webslides/WebSlides/wiki/Core-API)
    - [Plugin Docs](https://github.com/webslides/WebSlides/wiki/Plugin-docs)
    - [Plugin Development](https://github.com/webslides/WebSlides/wiki/Plugin-development)

### [(L)](https://github.com/webslides/WebSlides#credits)Credits

- WebSlides was created by [@jlantunez](https://twitter.com/jlantunez) using [Cactus](https://github.com/eudicots/Cactus).
- Javascript: [@Belelros](https://twitter.com/Belelros) and [@LuisSacristan](https://twitter.com/luissacristan).
- Based on [SimpleSlides](https://github.com/jennschiffer/SimpleSlides), by [@JennSchiffer](https://twitter.com/jennschiffer).