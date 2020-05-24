Publish Technical Tutorials in Google Codelab Format

# The Execution

The first step was getting my environment setup so that I can test this out myself. Let's do that.

## Install Software

- [**Go**](https://golang.org/dl/?source=post_page---------------------------) language
- [**Node.js v10+**](https://nodejs.org/en/download/?source=post_page---------------------------) and [**npm**](https://www.npmjs.com/get-npm?source=post_page---------------------------)
- [**claat**](https://github.com/googlecodelabs/tools/tree/master/claat?source=post_page---------------------------#install) (open source command line tool maintained by Google)

## Configure Go Environment

After you install Go, add the following to your `bash_profile`:

## not required if you’re only using Go modules

export GOPATH=$HOME/go
export GOROOT=/usr/local/go/bin## required
export PATH=$PATH:$HOME/go/bin

## Manage claat

Download the binary and move it to the `$HOME/go/bin` directory. Double check if you have execution privileges on that binary. If you are not sure, run the following command in the same directory the binary is in:

chmod u+x claat

## Setup the Landing Page

The codelabs landing page was generously developed by a group of people and has made its way to GitHub. All we have to do is clone the project:

git clone [https://github.com/googlecodelabs/tools](https://github.com/googlecodelabs/tools?source=post_page---------------------------)

Once you have the project cloned, go into the `[site](https://github.com/googlecodelabs/tools/tree/master/site?source=post_page---------------------------)` folder and install all the dependencies:

## navigate to folder

cd site/## install dependencies
npm install
npm install -g gulp-cli

To serve this site in development mode, run the following and you should see your server running on `http://localhost:8000` by default.

gulp serve
![1*09tMp3Uqrey3pXlK7EbfMA.png](../_resources/162b4ad94be3836576d3a76b162a60ce.png)
Running via Terminal
![1*axAF5WNhc3CZeeHx8edqaw.png](../_resources/441b42b90e01abbe1f1d09414c2da1b0.png)
Codelab landing page running locally
Now that we have setup the landing page, let’s write a codelab.

## Write a Sample Codelab

The wonderful part about writing a codelab, is that you do not have to suffer through writing this out in HTML. You have your choice of either markdown or a Google Doc. For logistical reasons I had to use markdown since the word docs had to be published on Google Docs, and again, I work for a bank, so that was not going to happen.

The best way that I can show you the power of a codelab is just by giving you a sample markdown file and showing you almost every possible item you can display.

First, let’s start by creating a `codelabs` directory under the `site` directory. Then create an `assets` folder within the `codelabs` folder, so that you can put any images or additional items in there that you might require for your codelabs.

## create codelabs folder

mkdir codelabs## go into directory
cd codelabs/## create assets folder
mkdir assets
Your folder structure should now look like this:
tools
|-- site
|--|-- codelabs
|--|--|-- assets

In the `codelabs` folder, create a markdown file with the following name and contents:

File name: `how-to-write-a-codelab.md`
Contents:
summary: How to Write a Codelab
id: how-to-write-a-codelab
categories: Sample
tags: medium
status: Published
authors: Zarin
Feedback Link: https://zarin.io

# How to Write a Codelab<!-- ------------------------ -->

## Overview

Duration: 1

### What You’ll Learn

- how to set the amount of time each slide will take to finish
- how to include code snippets
- how to hyperlink items
- how to include images
- other stuff

<!-- ------------------------ -->

## Setting Duration

Duration: 2

To indicate how long each slide will take to go through, set the `Duration` under each Heading 2 (i.e. `##`) to an integer.

The integers refer to minutes. If you set `Duration: 4` then a particular slide will take 4 minutes to complete.

The total time will automatically be calculated for you and will be displayed on the codelab once you create it.

<!-- ------------------------ -->

## Code Snippets

Duration: 3

To include code snippets you can do a few things.

- Inline highlighting can be done using the tiny tick mark on your keyboard: "`"
- Embedded code

### JavaScript

```javascript
{
key1: "string",
key2: integer,
key3: "string"
}
```

### Java

```java
for (statement 1; statement 2; statement 3) {
// code block to be executed
}
```

<!-- ------------------------ -->

## Hyperlinking and Embedded Images

Duration: 1### Hyperlinking
[Youtube - Halsey Playlists](https://www.youtube.com/user/iamhalsey/playlists)

### Images

![alt-text-here](assets/puppy.jpg)

<!-- ------------------------ -->

## Other Stuff

Duration: 1

Checkout the official documentation here: [Codelab Formatting Guide](https://github.com/googlecodelabs/tools/blob/master/FORMAT-GUIDE.md)

In the assets folder, add a JPEG image and rename it the image: `puppy.jpg`. This is just for demo purposes.

Once you have your markdown saved, you now want to export it to HTML using the `claat` tool. In the `codelabs` directory, run the following command to do just that:

## go into codelabs folder

cd codelabs## export md to html
claat export how-to-write-a-codelab.md
![1*h7wpUXnkpCklB4L1w2WqYQ.gif](../_resources/32426f67cc624ccd8418ecb9dbd7b072.png)
Output for claat command

When you export a markdown, `claat` will generate a folder based on the `id` of that markdown file, which you specified in the metadata at the top of the sample markdown shown above. Each time you modify the markdown file, you must export it, in order for changes to be propagated. Your new filesystem should look something like this:

![1*-oHH6QCMkOUXFmHjKi_HyA.png](../_resources/c69d2557f14d2d3bdb6c5e26914b5347.png)
Filesystem after running claat export within codelabs directory

Now that you have written your first codelab, you want to be able to see this displayed on the landing page. Kill your initial session that was running your application and this time, in the `site` directory, run the following command:

## go back to site folder

cd ..## re-run command
gulp serve --codelabs-dir=codelabs
![1*7D9oqia6NaWXhmTzA2ckrg.png](../_resources/0a4d9c0387f3876ca7c8e3d272a6c3de.png)
Landing page now rendering newly written codelab
![1*KEVaOxmwpWcf0_1m2LaHWQ.png](../_resources/b2db1f20b34c27170846cca597d3d9fc.jpg)
Sample codelab on desktop

It’s important to note that the UI is responsive and mobile friendly, so landing pages and codelabs look and work well not just on desktops, but on phones and tablets as well.

![1*4aeoEWSBu-CKBROi-zIyww.gif](../_resources/b436153d4d4a54ab2b6a54eb923a3cfa.jpg)
Sample codelab on iPhone 6/7

We are almost done. Let’s add some color to this page and make sure we categorize this new codelab as a `Sample`.

## Categorize Codelabs

Under `/site/app/styles` there is a file named `_categories.scss`. Open that and add your own entry at the bottom, if you would like to create a new category, the way I am about to. I have added the following:

@include codelab-card(['sample'], #FC0023, 'sample.svg');

Then, I went to[**flaticon.com**](https://flaticon.com/?source=post_page---------------------------) and searched for the word "Sample” and downloaded the `svg` of a test-tube, since that is what popped up in my search results . I renamed the `svg` to `sample.svg` and added it to `/site/app/images/icons` directory.

Once again, I kill my running session and run the command again:
gulp serve --codelabs-dir=codelabs
![1*RcoSHWseHzktpVI3ylTI5g.png](../_resources/6ed82e853c16e5ab1655a1eaebb9b58c.png)
Your codelab formatted nicely

However, you do not see your codelab under any category called “Sample”, do you ?

Try this:

- copy your initial markdown
- rename the file
- rename the `id`
- change the `categories` to “Web”
- export the new markdown using `claat`
- kill and start a new terminal session

You should now see another drop-down to filter based on Category on the UI:
![1*lbPDFsuan6qIraRT2gbb2w.png](../_resources/87e6f5349cb343cab1ad5db958d1d2e5.png)
“Web” is a predefined Category, and “Sample” is the one we just created

Note: Only if you have more than one category to filter by, will the drop-down be populated.

## Create Multiple Homepages (Views)

Now for one last thing. If you click on the “Choose an event” drop-down, you will see “Visual Studio Live”. This is called a `view` and, if you navigate to it, you will see the URL change to: `http://localhost:8000/vslive`

If you want to remove or modify that view, simply go to the `site/app/views` and either delete the `vslive` folder or modify it to something more appropriate. Lets modify the `vslive` folder and create a view called `medium`.

Your folder should now say `medium` and the contents of the `view.json` within that folder should have changed to:

{
"title": "Medium Articles",
"description": "Hosting codelabs that have been used to write Medium articles",
"logoUrl": "/medium/medium.png",
"tags": ["medium"],
"exclude": [
".*-about$",
"^lang-.*"
]
}

I found the Medium logo in `PNG` format online and saved it under the `medium` folder. Notice that `logoUrl` has updated with the correct image.

In order to have codelabs appear under a certain view, you must add one more metadata tag at the top of your codelab. It’s called the `tag` attribute. Your markdown metadata should look like this now:

summary: How to Write a Codelab
id: how-to-write-a-codelab
categories: Sample
tags: medium
status: Published
authors: Zarin
Feedback Link: https://zarin.io
Repeat the same process:

- save your codelab
- export your codelab
- restart your session
- navigate to localhost

![1*HXx_oJH6sngPGSgJyllOaQ.png](../_resources/58119e0e2f0aa7423022f47ddb83990c.png)
You should see the Medium view appear in the drop-down
![1*nkGy5E03Me-f1fKa0FDlWA.png](../_resources/738e39f35b4e02bf48bd6620b121c756.png)
Example of associating a codelab to a view