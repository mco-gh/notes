burtonator/polar-bookshelf: Polar is a personal knowledge repository for PDF and web content supporting incremental reading and document annotation.

 [![icon.ico](../_resources/5540369288d16ed0b183f4994fdc5fd2.png)](https://github.com/burtonator/polar-bookshelf/blob/master/icon.ico)

# [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='90'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1476' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/burtonator/polar-bookshelf#polar-bookshelf)Polar Bookshelf

[![68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f646f776e6c6f6164732f627572746f6e61746f722f706f6c61722d626f6f6b7368656c662f746f74616c2e737667](../_resources/81901ac9be096d457f2381e2554d991e.png)](https://github.com/burtonator/polar-bookshelf/releases)[![68747470733a2f2f696d672e736869656c64732e696f2f646973636f72642f3437373536303936343333343734373636382e7376673f6c6f676f3d646973636f7264](../_resources/4ec9aa337237d4a377fd892233448db7.png)](https://discord.gg/GT8MhA6)[![68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f73746172732f627572746f6e61746f722f706f6c61722d626f6f6b7368656c662e7376673f7374796c653d736f6369616c266c6162656c3d53746172](../_resources/970a22c833ec885043507f597aa103ab.png)](https://github.com/burtonator/polar-bookshelf)[![68747470733a2f2f696d672e736869656c64732e696f2f747769747465722f666f6c6c6f772f676574706f6c6172697a65642e7376673f7374796c653d736f6369616c266c6162656c3d466f6c6c6f77](../_resources/19f3155e544b35543d177c99b26f7140.png)](https://twitter.com/getpolarized?ref_src=twsrc%5Etfw)[![68747470733a2f2f6f70656e636f6c6c6563746976652e636f6d2f706f6c61722d626f6f6b7368656c662f6261636b6572732f62616467652e737667](../_resources/f9b109f070d9ec43dc51324ec9cfebd4.png)](https://github.com/burtonator/polar-bookshelf#backers)  [![68747470733a2f2f6f70656e636f6c6c6563746976652e636f6d2f706f6c61722d626f6f6b7368656c662f73706f6e736f72732f62616467652e737667](../_resources/6ebb96c9ca7ffeb4880c0521dd423dfa.png)](https://github.com/burtonator/polar-bookshelf#sponsors)

Polar Bookshelf is personal knowledge repository which supports advanced features like incremental reading, annotation, comments, and spaced repetition. It supports reading PDF and the web content and was created using the [Electron framework](https://electron.atom.io/) and[PDF.js](https://mozilla.github.io/pdf.js)

# [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='91'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1480' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/burtonator/polar-bookshelf#features)Features

- **PDF support** We have first-class PDF support thanks to [PDF.js](https://mozilla.github.io/pdf.js/). PDFs work well when reading content in book format or when reading scientific research which is often stored as PDF.
- **Captured Web Pages** Download HTML content and save them as offline documents which can be annotated.
- **Pagemarks** Easily keep track of what you're reading and the progress of each document.
- **Text Highlights** Highlight text in PDF and web pages.
- **Area Highlights** Capture a region of the page as a highlight which can be a chart, figure, infographic, etc.
- **Local Storage** All content is stored locally.
- **Hackable** The entire system is based on `Electron`, `Node`, `pdf.js`, `React` and other web standards. If you're a developer - welcome home!
- **Standards Based** All content is stored as JSON in a well documented schema. Annotations never mutate the original content.
- **Portable** Run across any platform. `Linux`, `MacOS`, and `Windows` supported. We also product snaps which means you can install our `.deb` files on `Ubuntu` or `Debian` but also any `Linux` distribution that supports snaps!

We hit 1.0 in 2018, and Polar's mature enough to be nearing—or already—best-in-class for PDF and (especially) web annotations.

# [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='92'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1501' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/burtonator/polar-bookshelf#screenshots)Screenshots

[![pdf-loaded-shadow.png](../_resources/448c21f0a0b37caa2601bfc8359c934d.png)](https://raw.githubusercontent.com/burtonator/polar-bookshelf/master/docs/screenshots/pdf-loaded-shadow.png)

 **PDF Document** Polar has excellent PDF support.

[![captured-web-content-shadow.png](../_resources/18796aa72371c4e271c6f28ecc26eaaa.png)](https://raw.githubusercontent.com/burtonator/polar-bookshelf/master/docs/screenshots/captured-web-content-shadow.png)

 **Captured Web Content** Polar supports fetching and storing web content locally for annotating.

[![annotations-shadow.png](../_resources/97d8e0fcc314018d7903274ba3f87d75.png)](https://raw.githubusercontent.com/burtonator/polar-bookshelf/master/docs/screenshots/annotations-shadow.png)

 **Annotations** Annotating a PDF including pagemarks showing content already read, an area highlight, and a text highlight.

[![repository-shadow.png](../_resources/01e71bdf9f834c3787ff1551be8fc4eb.png)](https://raw.githubusercontent.com/burtonator/polar-bookshelf/master/docs/screenshots/repository-shadow.png)

 **Repository** Polar includes a document repository manager to manage all your documents, open up a new editor, sort them as a queue or by priority, etc.

# [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='93'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1510' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/burtonator/polar-bookshelf#downloads)[Downloads](https://getpolarized.io/download.html)

Packages for Windows, MacOS, and Linux are available on the [downloads](https://getpolarized.io/download.html) page.

We also have a [CHANGELOG](https://github.com/burtonator/polar-bookshelf/blob/master/docs/CHANGELOG.md) available if you're interested into what went into each release.

# [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='94'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1513' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/burtonator/polar-bookshelf#discussion)Discussion

We have both a [Discord](https://discord.gg/GT8MhA6) group and[Reddit](https://www.reddit.com/r/PolarBookshelf/) group if you want to discuss Polar.

If it's a very technical issue it might be best to [create a Github Issue](https://github.com/burtonator/polar-bookshelf/issues/new).

# [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='95'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1516' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/burtonator/polar-bookshelf#personal-knowledge-repository)Personal Knowledge Repository

Polar is a document manager for PDF and web content as well as a personal knowledge repository.

Polar allows you to keep all important reading material in one place including annotations and flashcards for spaced repetition.

It supports for features like pagemarks, text highlights, and progress tracking by keeping track of how much you've read including restoring pagemarks when you re-open documents.

Pagemarks are a new concept for tracking your reading inspired from [incremental reading](https://getpolarized.io/incremental-reading.html). They allow suspend and resume of reading for weeks and months in the future until you're ready to resume, without losing your place.

Since you can create multiple pagemarks they work even if you jump around in a book (which is often in technical or research work).

# [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='96'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1522' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/burtonator/polar-bookshelf#web-content)Web Content

PDF is an excellent document format but we've found that many HTML pages don't convert to PDF well since they were not intended to be printed.

Captured pages contain HTML content stored in `phz` (Polar HTML zip) files.

We fetch all resources, render the page as DOM and apply CSS, then de-activate the page by removing all scripts.

We then store the content in the phz archive format and serve the content directly to Electron.

This means you have long term storage for all your content. You can annotate it and use pagemarks without risk of the content changing.

To capture a new page just select `File | Capture Web Page` then enter a URL.
After that the page will be captured and then loaded.

# [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='97'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1530' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/burtonator/polar-bookshelf#local-storage)Local Storage

All annotations, documents, PHZ files and other data are persisted on disk in your `~/.polar` directory (different on each platform) and when you re-open a PDF or PHZ file your pagemarks and other annotations are restored.

Since storage is local you're not reliant on one specific cloud provider. You can also use tools like git or Dropbox to synchronize across machines.

# [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='98'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1533' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/burtonator/polar-bookshelf#text-highlights)Text Highlights

[![text-highlight-shadow.png](../_resources/ed9d662d86ed9e6fe5508cb93e53e251.png)](https://raw.githubusercontent.com/burtonator/polar-bookshelf/master/docs/screenshots/text-highlight-shadow.png)

Text highlights allow you to work with content like you're using a text highlighter in a book.

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='99'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1537' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/burtonator/polar-bookshelf#create-a-text-highlight)Create a text highlight.

Select text you want to highlight then hit Ctrl-Alt-T

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='100'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1540' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/burtonator/polar-bookshelf#delete-a-text-highlight)Delete a text highlight.

Right click the highlight and select delete.

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='101'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1543' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/burtonator/polar-bookshelf#key-bindings)Key bindings:

- Ctrl-Alt-T - create a new text highlight from the current selected text.

# [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='102'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1546' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/burtonator/polar-bookshelf#area-highlights)Area Highlights

[![area-highlight-shadow.png](../_resources/7863d2e7fdea954f2697df2cb2afec3e.png)](https://raw.githubusercontent.com/burtonator/polar-bookshelf/master/docs/screenshots/area-highlight-shadow.png)

Area highlights allow you highlight a figure, infographic, or anything visual in a document.

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='103'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1550' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/burtonator/polar-bookshelf#create-an-area-highlight)Create an area highlight.

Right click on a page and select "Create area highlight"

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='104'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1553' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/burtonator/polar-bookshelf#delete-an-highlight)Delete an highlight.

Right click the highlight and select delete.

# [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='105'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1555' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/burtonator/polar-bookshelf#flashcards)Flashcards

[![flashcard2-shadow.png](../_resources/1451d03bacd3da37966c756cbff1ed58.png)](https://raw.githubusercontent.com/burtonator/polar-bookshelf/master/docs/screenshots/flashcard2-shadow.png)

Flashcards allow you to retain information long term by using a spaced repetition system like Anki to continually re-train yourself on material you want to retain.

Flashcards can be created by right clicking an annotation and selecting "Create Flashcard". The resulting flashcards are stored as annotations in your repository.

To specify the Anki deck for a document, add a tag starting with `deck:`. Slashes are used to specify subdecks. For instance, to set a document to the Anki deck ML::100PageMLBook, use the Polar tag `deck:ML/100PageMLBook`.

# [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='106'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1560' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/burtonator/polar-bookshelf#hackable)Hackable

Since the entire platform is based on Electron (Node + Chromium) the platform is very easy to work with which means developers can contribute easily.

Feel free to fork and send a pull request if there's some interesting feature you would like to add. [Here](https://github.com/burtonator/polar-bookshelf/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+first+issue%22) is a list of good newcomer issues.

# [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='107'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1563' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/burtonator/polar-bookshelf#data)Data

All data is stored on disk in JSON format. This also includes extracted metadata from the document. For example, text highlights include the source text that you copied as well as pointers into the original document where they can be found.

# [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='108'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1565' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/burtonator/polar-bookshelf#principles)Principles

We believe the following design principles are core to seeing this as a successful project.

- All the data should support long term file formats. The on disk format we use is JSON.
- Portability to all platforms is critical. We're initially targeting Linux (Ubuntu), MacOS, and Windows. You shouldn't have to pick a tool, which you might be using for the next 5-10 years, and then get stuck to a platform which may or may not exist in the future.

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='109'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1573' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/burtonator/polar-bookshelf#build-from-source)Build from source

Install NodeJS and npm for your platform.

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='110'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1576' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/burtonator/polar-bookshelf#to-run)To run:

Install latest **stable** node and npm versions.
You can check which version you need at
https://nodejs.org/
... then run:

	$ git clone https://github.com/burtonator/polar-bookshelf
	$ cd polar-bookshelf
	$ npm install && npm run-script compile && npm start

# [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='111'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1581' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/burtonator/polar-bookshelf#donations)Donations

Polar is supported by [community donations](https://opencollective.com/polar-bookshelf)

All donations go to supporting Polar which include website hosting costs, web designer costs, continual integration services, etc.

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='112'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1585' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/burtonator/polar-bookshelf#contributors)Contributors

This project exists thanks to all the people who contribute. [![68747470733a2f2f6f70656e636f6c6c6563746976652e636f6d2f706f6c61722d626f6f6b7368656c662f636f6e7472696275746f72732e7376673f77696474683d38393026627574746f6e3d66616c7365](../_resources/48d41cde84e1abd51f24529980fc86d6.png)](https://camo.githubusercontent.com/4a502739b7bd440dfab232386081cce1058fdd71/68747470733a2f2f6f70656e636f6c6c6563746976652e636f6d2f706f6c61722d626f6f6b7368656c662f636f6e7472696275746f72732e7376673f77696474683d38393026627574746f6e3d66616c7365)

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='113'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1588' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/burtonator/polar-bookshelf#backers)Backers

Thank you to all our backers!  [[Become a backer](https://opencollective.com/polar-bookshelf#backer)]

[![68747470733a2f2f6f70656e636f6c6c6563746976652e636f6d2f706f6c61722d626f6f6b7368656c662f6261636b6572732e7376673f77696474683d383930](../_resources/f9b3fbd2a0adf3cdb4707835b24d6c3b.png)](https://opencollective.com/polar-bookshelf#backers)

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='114'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1593' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/burtonator/polar-bookshelf#sponsors)Sponsors

Support this project by becoming a sponsor. Your logo will show up here with a link to your website. [[Become a sponsor](https://opencollective.com/polar-bookshelf#sponsor)]

[![68747470733a2f2f6f70656e636f6c6c6563746976652e636f6d2f706f6c61722d626f6f6b7368656c662f73706f6e736f722f302f6176617461722e737667](../_resources/846ba45612f2cc5d1bd31df6dfebf440.png)](https://opencollective.com/polar-bookshelf/sponsor/0/website)[![68747470733a2f2f6f70656e636f6c6c6563746976652e636f6d2f706f6c61722d626f6f6b7368656c662f73706f6e736f722f312f6176617461722e737667](../_resources/7108f7d2e18f23164ee4f9c7bf233650.png)](https://opencollective.com/polar-bookshelf/sponsor/1/website)[![68747470733a2f2f6f70656e636f6c6c6563746976652e636f6d2f706f6c61722d626f6f6b7368656c662f73706f6e736f722f322f6176617461722e737667](../_resources/201f4bf26fb16892fcd73a82cebd4327.png)](https://opencollective.com/polar-bookshelf/sponsor/2/website)[![68747470733a2f2f6f70656e636f6c6c6563746976652e636f6d2f706f6c61722d626f6f6b7368656c662f73706f6e736f722f382f6176617461722e737667](../_resources/978c1bee49d7ad5fc1a4d81099b13e18.png)](https://opencollective.com/polar-bookshelf/sponsor/3/website)[(L)](https://opencollective.com/polar-bookshelf/sponsor/4/website)[(L)](https://opencollective.com/polar-bookshelf/sponsor/5/website)[(L)](https://opencollective.com/polar-bookshelf/sponsor/6/website)[(L)](https://opencollective.com/polar-bookshelf/sponsor/7/website)[(L)](https://opencollective.com/polar-bookshelf/sponsor/8/website)[(L)](https://opencollective.com/polar-bookshelf/sponsor/9/website)

# [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='115'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1596' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/burtonator/polar-bookshelf#license)License

Polar is distributed under the GPLv3.

[PDF.js](https://github.com/mozilla/pdf.js) is available under the Apache License.[Electron](https://github.com/electron/electron) is released under the MIT License. Rest of the code is MIT-licensed.

Icons made by [Freepik](http://www.freepik.com/) from [www.flaticon.com](https://www.flaticon.com/) is licensed by [CC 3.0 BY](http://creativecommons.org/licenses/by/3.0/)