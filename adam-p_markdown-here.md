adam-p/markdown-here

# Markdown Cheatsheet

Adam Pritchard edited this page on Feb 26, 2016 · [94 revisions](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet/_history)

###    Pages 10

- **[Home](https://github.com/adam-p/markdown-here/wiki)**

- **[Compatibility](https://github.com/adam-p/markdown-here/wiki/Compatibility)**

- **[Development Notes](https://github.com/adam-p/markdown-here/wiki/Development-Notes)**

- **[Markdown Cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)**

- **[Markdown Here Cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Here-Cheatsheet)**

- **[Other Markdown Tools](https://github.com/adam-p/markdown-here/wiki/Other-Markdown-Tools)**

- **[Press, Posts, Reviews, Etc.](https://github.com/adam-p/markdown-here/wiki/Press,-Posts,-Reviews,-Etc.)**

- **[Reviews](https://github.com/adam-p/markdown-here/wiki/Reviews)**

- **[Tips and Tricks](https://github.com/adam-p/markdown-here/wiki/Tips-and-Tricks)**

- **[Troubleshooting](https://github.com/adam-p/markdown-here/wiki/Troubleshooting)**

##### Clone this wiki locally

 [ Clone in Desktop](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet#codegithub-mac://openRepo/https://github.com/adam-p/markdown-here.wiki)

This is intended as a quick reference and showcase. For more complete info, see [John Gruber's original spec](http://daringfireball.net/projects/markdown/) and the [Github-flavored Markdown info page](http://github.github.com/github-flavored-markdown/).

Note that there is also a [Cheatsheet specific to Markdown Here](https://github.com/adam-p/markdown-here/wiki/Markdown-Here-Cheatsheet) if that's what you're looking for. You can also check out [more Markdown tools](https://github.com/adam-p/markdown-here/wiki/Other-Markdown-Tools).

##### [(L)](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet#table-of-contents)Table of Contents

[Headers](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet#headers)

[Emphasis](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet#emphasis)

[Lists](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet#lists)
[Links](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet#links)

[Images](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet#images)

[Code and Syntax Highlighting](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet#code)

[Tables](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet#tables)

[Blockquotes](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet#blockquotes)

[Inline HTML](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet#html)

[Horizontal Rule](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet#hr)

[Line Breaks](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet#lines)

[Youtube videos](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet#videos)

## [(L)](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet#headers)Headers

	normal# H1
	## H2
	### H3
	#### H4
	##### H5
	###### H6

	Alternatively, for H1 and H2, an underline-ish style:

	Alt-H1
	======

	Alt-H2
	------
	normal

# [(L)](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet#h1)H1

## [(L)](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet#h2)H2

### [(L)](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet#h3)H3

#### [(L)](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet#h4)H4

##### [(L)](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet#h5)H5

###### [(L)](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet#h6)H6

Alternatively, for H1 and H2, an underline-ish style:

# [(L)](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet#alt-h1)Alt-H1

## [(L)](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet#alt-h2)Alt-H2

## [(L)](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet#emphasis)Emphasis

	normalEmphasis, aka italics, with *asterisks* or _underscores_.

	Strong emphasis, aka bold, with **asterisks** or __underscores__.

	Combined emphasis with **asterisks and _underscores_**.

	Strikethrough uses two tildes. ~~Scratch this.~~
	normal

Emphasis, aka italics, with *asterisks* or *underscores*.
Strong emphasis, aka bold, with **asterisks** or **underscores**.
Combined emphasis with **asterisks and *underscores***.
Strikethrough uses two tildes. (Scratch this.)

## [(L)](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet#lists)Lists

(In this example, leading and trailing spaces are shown with with dots: ⋅)

	normal1. First ordered list item
	2. Another item
	⋅⋅* Unordered sub-list.
	1. Actual numbers don't matter, just that it's a number
	⋅⋅1. Ordered sub-list
	4. And another item.

	⋅⋅⋅You can have properly indented paragraphs within list items. Notice the blank line above, and the leading spaces (at least one, but we'll use three here to also align the raw Markdown).

	⋅⋅⋅To have a line break without a paragraph, you will need to use two trailing spaces.⋅⋅
	⋅⋅⋅Note that this line is separate, but within the same paragraph.⋅⋅
	⋅⋅⋅(This is contrary to the typical GFM line break behaviour, where trailing spaces are not required.)

	* Unordered list can use asterisks

	- Or minuses

	+ Or pluses
	normal

1. First ordered list item
2. Another item

    - Unordered sub-list.

3. Actual numbers don't matter, just that it's a number
    1. Ordered sub-list
4. And another item.

You can have properly indented paragraphs within list items. Notice the blank line above, and the leading spaces (at least one, but we'll use three here to also align the raw Markdown).

To have a line break without a paragraph, you will need to use two trailing spaces.

Note that this line is separate, but within the same paragraph.

(This is contrary to the typical GFM line break behaviour, where trailing spaces are not required.)

- Unordered list can use asterisks
- Or minuses
- Or pluses

## [(L)](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet#links)Links

There are two ways to create links.

	normal[I'm an inline-style link](https://www.google.com)

	[I'm an inline-style link with title](https://www.google.com "Google's Homepage")

	[I'm a reference-style link][Arbitrary case-insensitive reference text]

	[I'm a relative reference to a repository file](../blob/master/LICENSE)

	[You can use numbers for reference-style link definitions][1]

	Or leave it empty and use the [link text itself].

	URLs and URLs in angle brackets will automatically get turned into links.
	http://www.example.com or <http://www.example.com> and sometimes
	example.com (but not on Github, for example).

	Some text to show that the reference links can follow later.

	[arbitrary case-insensitive reference text]: https://www.mozilla.org
	[1]: http://slashdot.org
	[link text itself]: http://www.reddit.com
	normal

[I'm an inline-style link](https://www.google.com/)
[I'm an inline-style link with title](https://www.google.com/)
[I'm a reference-style link](https://www.mozilla.org/)

[I'm a relative reference to a repository file](https://github.com/adam-p/markdown-here/blob/master/LICENSE)

[You can use numbers for reference-style link definitions](http://slashdot.org/)

Or leave it empty and use the [link text itself](http://www.reddit.com/).

URLs and URLs in angle brackets will automatically get turned into links. [http://www.example.com](http://www.example.com/) or [http://www.example.com](http://www.example.com/) and sometimes example.com (but not on Github, for example).

Some text to show that the reference links can follow later.

## [(L)](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet#images)Images

	normalHere's our logo (hover to see the title text):

	Inline-style:
	![alt text](https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Logo Title Text 1")

	Reference-style:
	![alt text][logo]

	[logo]: https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Logo Title Text 2"
	normal

Here's our logo (hover to see the title text):
Inline-style: ![alt text](../_resources/69f6e25dba8e1b2347417d87807089ca.png)
Reference-style:

## [(L)](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet#code-and-syntax-highlighting)Code and Syntax Highlighting

Code blocks are part of the Markdown spec, but syntax highlighting isn't. However, many renderers -- like Github's and *Markdown Here* -- support syntax highlighting. Which languages are supported and how those language names should be written will vary from renderer to renderer. *Markdown Here* supports highlighting for dozens of languages (and not-really-languages, like diffs and HTTP headers); to see the complete list, and how to write the language names, see the [highlight.js demo page](http://softwaremaniacs.org/media/soft/highlight/test.html).

	normalInline `code` has `back-ticks around` it.
	normal

Inline ` code ` has ` back-ticks around ` it.

Blocks of code are either fenced by lines with three back-ticks ` ``` `, or are indented with four spaces. I recommend only using the fenced code blocks -- they're easier and only they support syntax highlighting.

	normal```javascript
	var s = "JavaScript syntax highlighting";
	alert(s);
	```

	```python
	s = "Python syntax highlighting"
	print s
	```

	```
	No language indicated, so no syntax highlighting.
	But let's throw in a <b>tag</b>.
	```
	normal

var s =  "JavaScript syntax highlighting";alert(s);
s =  "Python syntax highlighting"print s

	normalNo language indicated, so no syntax highlighting in Markdown Here (varies on Github).
	But let's throw in a <b>tag</b>.
	normal

## [(L)](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet#tables)Tables

Tables aren't part of the core Markdown spec, but they are part of GFM and *Markdown Here* supports them. They are an easy way of adding tables to your email -- a task that would otherwise require copy-pasting from another application.

	normalColons can be used to align columns.

	| Tables        | Are           | Cool  |
	| ------------- |:-------------:| -----:|
	| col 3 is      | right-aligned | $1600 |
	| col 2 is      | centered      |   $12 |
	| zebra stripes | are neat      |    $1 |

	There must be at least 3 dashes separating each header cell.
	The outer pipes (|) are optional, and you don't need to make the
	raw Markdown line up prettily. You can also use inline Markdown.

	Markdown | Less | Pretty
	--- | --- | ---
	*Still* | `renders` | **nicely**
	1 | 2 | 3
	normal

Colons can be used to align columns.

| Tables | Are | Cool |
| --- | --- | --- |
| col 3 is | right-aligned | $1600 |
| col 2 is | centered | $12 |
| zebra stripes | are neat | $1  |

There must be at least 3 dashes separating each header cell. The outer pipes (|) are optional, and you don't need to make the raw Markdown line up prettily. You can also use inline Markdown.

Markdown
Less
Pretty
*Still*
[object Object]
**nicely**
1
2
3

## [(L)](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet#blockquotes)Blockquotes

	normal> Blockquotes are very handy in email to emulate reply text.
	> This line is part of the same quote.

	Quote break.

	> This is a very long line that will still be quoted properly when it wraps. Oh boy let's keep writing to make sure this is long enough to actually wrap for everyone. Oh, you can *put* **Markdown** into a blockquote.
	normal

> Blockquotes are very handy in email to emulate reply text. This line is part of the same quote.

Quote break.

> This is a very long line that will still be quoted properly when it wraps. Oh boy let's keep writing to make sure this is long enough to actually wrap for everyone. Oh, you can *> put*>   **> Markdown**>  into a blockquote.

## [(L)](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet#inline-html)Inline HTML

You can also use raw HTML in your Markdown, and it'll mostly work pretty well.

	normal<dl>
	  <dt>Definition list</dt>
	  <dd>Is something people use sometimes.</dd>

	  <dt>Markdown in HTML</dt>
	  <dd>Does *not* work **very** well. Use HTML <em>tags</em>.</dd>
	</dl>
	normal

Definition list

Is something people use sometimes.

Markdown in HTML

Does *not* work **very** well. Use HTML *tags*.

## [(L)](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet#horizontal-rule)Horizontal Rule

	normalThree or more...

	---

	Hyphens

	***

	Asterisks

	___

	Underscores
	normal

Three or more...

* * *

Hyphens

* * *

Asterisks

* * *

Underscores

## [(L)](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet#line-breaks)Line Breaks

My basic recommendation for learning how line breaks work is to experiment and discover -- hit <Enter> once (i.e., insert one newline), then hit it twice (i.e., insert two newlines), see what happens. You'll soon learn to get what you want. "Markdown Toggle" is your friend.

Here are some things to try out:

	normalHere's a line for us to start with.

	This line is separated from the one above by two newlines, so it will be a *separate paragraph*.

	This line is also a separate paragraph, but...
	This line is only separated by a single newline, so it's a separate line in the *same paragraph*.
	normal

Here's a line for us to start with.

This line is separated from the one above by two newlines, so it will be a *separate paragraph*.

This line is also begins a separate paragraph, but...

This line is only separated by a single newline, so it's a separate line in the *same paragraph*.

(Technical note: *Markdown Here* uses GFM line breaks, so there's no need to use MD's two-space line breaks.)

## [(L)](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet#youtube-videos)Youtube videos

They can't be added directly but you can add an image with a link to the video like this:

	normal<a href="http://www.youtube.com/watch?feature=player_embedded&v=YOUTUBE_VIDEO_ID_HERE
	" target="_blank"><img src="http://img.youtube.com/vi/YOUTUBE_VIDEO_ID_HERE/0.jpg"
	alt="IMAGE ALT TEXT HERE" width="240" height="180" border="10" /></a>
	normal

Or, in pure Markdown, but losing the image sizing and border:

	normal[![IMAGE ALT TEXT HERE](http://img.youtube.com/vi/YOUTUBE_VIDEO_ID_HERE/0.jpg)](http://www.youtube.com/watch?v=YOUTUBE_VIDEO_ID_HERE)
	normal

Referencing a bug by #bugID in your git commit links it to the slip. For example #1.

* * *

License: [CC-BY](https://creativecommons.org/licenses/by/3.0/)