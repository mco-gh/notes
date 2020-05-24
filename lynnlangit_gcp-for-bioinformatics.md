lynnlangit/gcp-for-bioinformatics

[![68747470733a2f2f696d672e736869656c64732e696f2f6769747465722f726f6f6d2f6763702d666f722d62696f696e666f726d61746963732f6e657874666c6f772e7376673f636f6c6f72423d323661663634267374796c653d706f706f7574](../_resources/4b29d16015d98e372c3ec5598aad57d8.png)](https://gitter.im/gcp-for-bioinformatics)

# [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='65'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='893' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/lynnlangit/gcp-for-bioinformatics#google-cloud-platform-gcp-for-bioinformatics)Google Cloud Platform (GCP) for Bioinformatics

This repository covers using ☁️Google Cloud Platform public cloud services for bioinformatics data analysis tasks. The guidance is intended for researchers - in particular, this guide is for those who are **NEW to working with GCP**. The info is based on advisory work my team has done with the groups shown below:

[![logos.png](../_resources/f5759b394a9547236694be80f2fb8447.png)](https://github.com/lynnlangit/gcp-for-bioinformatics/blob/master)

* * *

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='66'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='898' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/lynnlangit/gcp-for-bioinformatics#why-would-i-choose-to-use-a-public-cloud-vendor-for-bioinformatics)Why would I choose to use a public cloud vendor for bioinformatics?

[![flow-cell.jpg](../_resources/8d31a63ab7c4fb15bd742807333d7700.jpg)](https://github.com/lynnlangit/gcp-for-bioinformatics/blob/master)

- ⭐️Top Reasons:
    - **Save Money** - run scaled analysis jobs exactly & only when you need to run them
    - **Save Time** - use vendor-managed infrastructure & best-practice patterns for repeatable research -> get analysis results faster
- READ the [FAQ for GCP bioinformatics](https://github.com/lynnlangit/gcp-for-bioinformatics/blob/master/FAQ.md) for this Repo
- READ Nature magazine: ["Cloud computing for genomic data analysis and collaboration"](https://www.nature.com/articles/nrg.2017.113)
- READ the top 4 most [common use cases](https://github.com/lynnlangit/gcp-for-bioinformatics/blob/master/USING.md) for using the public cloud for bioinformatics researchers

* * *

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='67'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='913' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/lynnlangit/gcp-for-bioinformatics#click-below-to-watch-lynns-welcome-video-4-min)Click below to WATCH 'Lynn's Welcome Video' (4 min)

[![687474703a2f2f696d672e796f75747562652e636f6d2f76692f596f466b5356446c4e366b2f302e6a7067](../_resources/df66e779571dae0f6987f3fdefe020c2.jpg)](http://www.youtube.com/watch?v=YoFkSVDlN6k)

Read about, watch demo or try out **EACH ☁️GCP service**, ordered by topic in this Repo:

1. READ - one page explaining why, what & how to use for each service
2. WATCH - short, linked screencast showing how to use for most services
3. TRY - run Jupyter notebook example using for some services

4. ![octocat.png](../_resources/ea8b6bf15eca5d4b518b441f601a3a07.png) TRY - use code examples from linked GitHub Repos

5. EXPAND - go to linked resources to learn about advanced aspects of each service

* * *

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='68'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='929' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/lynnlangit/gcp-for-bioinformatics#to-understand-the-scope-of-services-covered-in-this-repo)To Understand the Scope of Services covered in this Repo

1. SCAN - a list of [all topics](https://github.com/lynnlangit/gcp-for-bioinformatics/blob/master/TOPICS.md) covered in this Repo

2. SCAN - a diagram showing a [GCP Genomics Pipeline](https://github.com/lynnlangit/gcp-for-bioinformatics/blob/master/ARCHITECTURE.md) reference architecture

* * *