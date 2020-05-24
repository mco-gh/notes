googlesamples/md2googleslides

# [(L)](https://github.com/googlesamples/md2googleslides#md2googleslides----markdown-to-google-slides)md2googleslides -- Markdown to Google Slides

Generate Google Slides from markdown & HTML. Run from the command line or embed in another application.

This project was developed as an example of how to use the[Slides API](https://developers.google.com/slides).

While it does not yet produce stunningly beautiful decks, you are encouraged to use this tool for quickly prototyping presentations.

Contributions are welcome.

## [(L)](https://github.com/googlesamples/md2googleslides#installation-and-usage)Installation and usage

For command line use, install md2gslides globally:

	$ npm install -g md2gslides

After installing, import your slides by running:

	$ md2gslides slides.md

The first time the command is run you will be prompted for authorization. Credentials will be stored locally in a file named ` ~/.credentials/md2gslides.json `.

## [(L)](https://github.com/googlesamples/md2googleslides#supported-markdown-rules)Supported markdown rules

md2gslides uses a subset of the [CommonMark](http://spec.commonmark.org/0.26/) and[Github Flavored Markdown](https://help.github.com/categories/writing-on-github/) rules for markdown.

### [(L)](https://github.com/googlesamples/md2googleslides#slides)Slides

Each slide is typically represented by a header, followed by zero or more block elements.

Begin a new slide with a horizontal rule (` --- `). The separator may be omitted for the first slide.

The following examples show how to create slides of various layouts:

#### [(L)](https://github.com/googlesamples/md2googleslides#title-slide)Title slide

---

# This is a title slide

## Your name here

[![Title slide](../_resources/61e64808ce5f156b1662784f63727345.png)](https://github.com/googlesamples/md2googleslides/raw/master/examples/title_slide.png)

#### [(L)](https://github.com/googlesamples/md2googleslides#section-title-slides)Section title slides

---

# This is a section title

[![Section title slide](../_resources/cd22f5ac34169bac3c99e6921acbc358.png)](https://github.com/googlesamples/md2googleslides/raw/master/examples/section_title_slide.png)

#### [(L)](https://github.com/googlesamples/md2googleslides#section-title--body-slides)Section title & body slides

---

# Section title & body slide

## This is a subtitle

This is the body

[![Section title & body slide](../_resources/ce6793806a92fbffe2b0a27e236bf777.png)](https://github.com/googlesamples/md2googleslides/raw/master/examples/section_title_body_slide.png)

#### [(L)](https://github.com/googlesamples/md2googleslides#title--body-slides)Title & body slides

---

# Title & body slide

This is the slide body.

[![Title & body slide](../_resources/81a511054a8fa31b743f72c0b86b742b.png)](https://github.com/googlesamples/md2googleslides/raw/master/examples/title_body_slide.png)

#### [(L)](https://github.com/googlesamples/md2googleslides#main-point-slide)Main point slide

Add ` {.big} ` to the title to make a slide with one big point
---

# This is the main point {.big}

[![Main point slide](../_resources/50a627766d65b1ec6bb57c55a4037e33.png)](https://github.com/googlesamples/md2googleslides/raw/master/examples/main_point_slide.png)

#### [(L)](https://github.com/googlesamples/md2googleslides#big-number-slide)Big number slide

Use ` {.big} ` on a header in combination with a body too.
---

# 100% {.big}

This is the body

[![Big number slide](../_resources/e3b4b17d5a0245ca8bedf69d3b405146.png)](https://github.com/googlesamples/md2googleslides/blob/master/examples/big_number_slide.png)

#### [(L)](https://github.com/googlesamples/md2googleslides#two-column-slides)Two column slides

Separate columns with ` {.column} `. The marker must appear on its own line with a blank both before and after.

---

# Two column layout

This is the left column
{.column}
This is the right column

[![Two column slide](../_resources/e54c9d297c9eccffbabe5f5aebca1376.png)](https://github.com/googlesamples/md2googleslides/raw/master/examples/two_column_slide.png)

### [(L)](https://github.com/googlesamples/md2googleslides#images)Images

#### [(L)](https://github.com/googlesamples/md2googleslides#inline-images)Inline images

Images can be placed on slides using image tags. Multiple images can be included. Mulitple images in a single paragraph are arranged in columns, mutiple paragraphs arranged as rows.

Note: Images are currently scaled and centered to fit the slide template.
---

# Slides can have images

![](https://placekitten.com/900/900)

[![Slide with image](../_resources/9cf5516f7f5886a2d5d7c2e9e6a17e9e.png)](https://github.com/googlesamples/md2googleslides/raw/master/examples/image_slide.png)

#### [(L)](https://github.com/googlesamples/md2googleslides#background-images)Background images

Set the background image of a slide by adding ` {.background} ` to the end of an image URL.

---

# Slides can have background images

![](https://placekitten.com/1600/900){.background}

[![Slide with background image](../_resources/562d85d94df1207a2bce2a41cfcfb5d5.png)](https://github.com/googlesamples/md2googleslides/raw/master/examples/background_image_slide.png)

### [(L)](https://github.com/googlesamples/md2googleslides#videos)Videos

Include YouTube videos with a modified image tag.
---

# Slides can have videos

@[youtube](MG8KADiRbOU)

[![Slide with video](../_resources/66b4cf2ec8066ea75ea26b3d0e1a025b.png)](https://github.com/googlesamples/md2googleslides/raw/master/examples/video_slide.png)

### [(L)](https://github.com/googlesamples/md2googleslides#speaker-notes)Speaker notes

Include speaker notes for a slide using HTML comments. Text inside the comments may include markdown for formatting, though only text formatting is allowed. Videos, images, and tables are ignored inside speaker notes.

---

# Slide title

![](https://placekitten.com/1600/900){.background}
<!--
These are speaker notes.
-->

### [(L)](https://github.com/googlesamples/md2googleslides#formatting)Formatting

Basic formatting rules are allowed, including:

- Bold
- Italics
- Code
- Strikethrough
- Hyperlinks
- Ordered lists
- Unordered lists

The following markdown illustrates a few common styles.
**Bold**, *italics*, and ~~strikethrough~~ may be used.
Ordered lists:
1. Item 1
1. Item 2
1. Item 2.1
Unordered lists:
* Item 1
* Item 2
* Item 2.1
Additionally, a subset of inline HTML tags are supported for styling.

- ` <span> `
- ` <sup> `
- ` <sub> `
- ` <em> `
- ` <i> `
- ` <strong> `
- ` <b> `

Supported CSS styles for use with ` <span> ` elements:

- ` color `
- ` background-color `
- ` font-weight: bold `
- ` font-style: italic `
- ` text-decoration: underline `
- ` text-decoration: line-through `
- ` font-family `
- ` font-variant: small-caps `

### [(L)](https://github.com/googlesamples/md2googleslides#emoji)Emoji

Use Github style [emoji](http://www.webpagefx.com/tools/emoji-cheat-sheet/) in your text using the ` :emoji: `.

The following example inserts emoji in the header and body of the slide.

### I :heart: cats

:heart_eyes_cat:

### [(L)](https://github.com/googlesamples/md2googleslides#code-blocks)Code blocks

Both indented and fenced code blocks are supported, with syntax highlighting.
The following example renders highlighted code.

### Hello World

```javascript
console.log('Hello world');
```

To change the syntax highlight theme specify the ` --style <theme> ` option on the command line. All [highlight.js themes](https://github.com/isagalaev/highlight.js/tree/master/src/styles)are supported. For example, to use the github theme

	$ md2gslides slides.md --style github

### [(L)](https://github.com/googlesamples/md2googleslides#tables)Tables

Tables are supported via[GFM](https://guides.github.com/features/mastering-markdown/#GitHub-flavored-markdown) syntax.

Note: Including tables and other block elements on the same slide may produce poor results with overlapping elements. Either avoid or manually adjust the layout after generating the slides.

The following generates a 2x5 table on the slide.

### Top pets in the United States

Animal | Number
-------|--------
Fish | 142 million
Cats | 88 million
Dogs | 75 million
Birds | 16 million

## [(L)](https://github.com/googlesamples/md2googleslides#contributing)Contributing

With the exception of ` /bin/md2gslides.js `, ES6 is used throughout and compiled with [Babel](https://babeljs.io/). [Mocha](https://mochajs.org/) and [Chai](http://chaijs.com/)are used for testing.

To compile:

	$ npm run compile

To run unit tests:

	$ npm run test

See [CONTRIBUTING](https://github.com/googlesamples/md2googleslides/blob/master/CONTRIBUTING.md) for additional terms.

## [(L)](https://github.com/googlesamples/md2googleslides#license)License

This library is licensed under Apache 2.0. Full license text is available in [LICENSE](https://github.com/googlesamples/md2googleslides/blob/master/LICENSE).