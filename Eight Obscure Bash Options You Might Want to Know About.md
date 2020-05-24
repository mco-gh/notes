Eight Obscure Bash Options You Might Want to Know About

# Eight Obscure Bash Options You Might Want to Know About

[zwischenzugs](https://zwischenzugs.com/author/zwischenzugs/)[Uncategorized](https://zwischenzugs.com/category/uncategorized/)April 3, 20194 Minutes

Some bash options are well known, and well-used. For example, many people put
set -o xtrace
at the top of their scripts to debug them,
set -o errexit
to exit on error, or
set -o errunset
to exit if a variable is referenced but not set.

But there are many other options you can set. Many of them can seem confusing if you read the man page, so I’ve collected some of the ones I think are more useful here and explained them further.

***NOTE**
If you are using a Mac, then you may be running
an older version of bash (3.x rather than 4.x) *
*that does not have all these

options available. If so, see [here](https://akrabat.com/upgrading-to-bash-4-on-macos/) or [here](https://itnext.io/upgrading-bash-on-macos-7138bd1066ba).*

## `set` vs `shopt`?

There are two ways to set bash options from within scripts or on the command line. You can use the `set` builtin command, or the `shopt` builtin command. They both manipulate the behaviour of the shell, and differ in their [lineage](https://unix.stackexchange.com/questions/32409/set-and-shopt-why-two). The `set` options are inherited, or borrowed, from other shells’ options, while the `shopt` ones were originated in bash.

If you want to see how your current settings look, then run:
$ set -o
$ shopt

To switch on a setting using set, you can use the long version, or a shorter flag that is equivalent. For example:

$ set -o errunset
$ set -e
both have the same effect.
To switch off a setting using set, you use `+` instead of `-`:
$ set +e

For a long time I couldn’t remember which way round it goes, as the logic of (`-` = on), and (`+` = off) seems wrong to me.

To switch on and off a `shopt` setting, you use the (more logical)`-s` (set) and `-u` (unset) flags:

$ shopt -s cdspell # <= on
$ shopt -u cdspell # <= off

## Changing Directories

There are a few options that can help dealing with directories.

### 1. cdspell

If you set this up, then bash will work around your mis-spellings and go to the folder you were going for anyway.

$ shopt -s cdspell
$ mkdir abcdefg
$ cd abcdeg
abcdefg
$ cd ..

I’ve used this for years, and very occasionally (maybe once a year) it will make a decision that surprises me. But it probably proves useful at least once a day.

### 2. autocd

If the inefficiency of typing `cd` is something you can’t bear, then you can set this option to move to folder if the command doesn’t exist.

$ shopt -s autocd
$ abcdefg
$ cd ..
You can also use it in conjunction with autocompletion to quickly hop around:
$ ./abc[TAB][RETURN]
cd -- ./abcdefg
Just don’t call a folder ‘`rm -rf *`‘ (yes, you can, by the way).

### 3. direxpand

This is a neat option that gets the shell to perform any expansions of variables, tildes and the like right there for you in the command line if you tab to complete:

$ shopt -s direxpand
$ ./[TAB] # is replaced by...
$ /full/path/to/current_working_folder
$ ~/[TAB] # is replaced by...
$ /full/path/to/home/folder
$ $HOME/[TAB] # is replaced by
$ /full/path/to/home/folder

## A Clean Exit

### 4. `checkjobs`

This option stops the shell session from exiting if there are any jobs running in the background that haven’t finished yet.

Instead, the unfinished jobs are listed for you. If you still want to exit, you can if you enter `exit` immediately afterwards again.

$ shopt -s checkjobs
$ echo $$
68125 # <= Process ID of the shell
$ sleep 999 &
$ exit
There are running jobs.
[1]+  Running                 sleep 999 &
$ echo $$
68125 # <= Process ID of the shell is the same
$ exit
There are running jobs.
[1]+  Running                 sleep 999 &
$ exit
$ echo $$
$ 59316 # <= Process ID has changed this time

## Globbing Superpowers

### 5. `globstar`

This option gives you globbing superpowers! If you type:
$ shopt -s globstar
$ ls **
then the shell will output recursively all folders and subfolders.

Combined with `direxpand`, you can quickly page through all the files and subfolders beneath you:

$ shopt -s direxpand
$ ls **[TAB][TAB]
Display all 2033 possibilities? (y or n)

### 6. extglob

This option gives your globbing powers more commonly associated with full-on regular expressions. Occasionally, this is very useful, as it allows you to do nifty things like this:

$ shopt -s extglob
$ touch afile bfile cfile
$ ls
afile bfile cfile
$ ls ?(a*|b*)
afile bfile
$ ls !(a*|b*)
cfile

where the patterns are placed in parentheses, separated by pipes, and the operators available are:

? = match zero or one occurences of the patterns given
! = match anything that doesn't match any patterns given
* = zero or more occurences
+ = one or more occurrences
@ = exactly one occurence

## Accident-prone?

### 7. `histverify`

If you’re accident prone, then using the history shortcuts like `!!` and `!$` can be scary, especially when you’re just learning them.

The `histverify` option allows you to see how bash interprets the command before it actually gets run:

$ shopt -s histverify
$ echo !$ # <= On hitting return, command is not run
$ echo histverify # <= Command is redisplayed ready to run
histverify # <= command gets run

* * *

**This is based on some of the contents of my book** [Learn Bash the Hard Way](https://leanpub.com/learnbashthehardway), available at $6.99.

[![hero.png](../_resources/6e4b6a4d64605466dbd8f2aa8815697e.png)](https://leanpub.com/learnbashthehardway)

* * *

### 8. Noclobber

Again, if you’re accident-prone, you might want to set this one up.

Clobbering is the act of overwriting a file that already exists with the redirect operator (`>`). This can be disastrous if you’ve not got the file backed up anywhere else.

Using `set -C` prevents this from happening when you use the redirect operator. If you are sure you want to clobber, you can override with the `>|` operator instead:

$ touch afile
$ set -C
$ echo something > afile
-bash: afile: cannot overwrite existing file
$ echo something >| afile
$

* * *

***If you like this, you might like one of my books:
[Learn Bash the Hard Way](https://leanpub.com/learnbashthehardway?p=4369)***
***[Learn Git the Hard Way](https://leanpub.com/learngitthehardway?p=4369)***

***[Learn Terraform the Hard Way](https://leanpub.com/learnterraformthehardway)***

[![learngitbashandterraformthehardway.png](../_resources/92467394f3b6b98da322bffd3834971c.png)](https://leanpub.com/b/learngitbashandterraformthehardway)

![eda41-0v9jkbliyi3uzefqq.jpg](../_resources/35fd3a4fcaa684fcaa821ad7be6813e7.jpg)

***[Get 39% off Docker in Practice with the code: 39miell2](https://www.manning.com/books/docker-in-practice-second-edition?a_aid=zwischenzugs&a_bid=550032fc)***

Advertisements

Report this ad

Report this ad

### Share this:

- [Email](https://zwischenzugs.com/2019/04/03/eight-obscure-bash-options-you-might-want-to-know-about/?share=email&nb=1)

-

- [reddit](https://www.reddit.com/submit?url=https%3A%2F%2Fzwischenzugs.com%2F2019%2F04%2F03%2Feight-obscure-bash-options-you-might-want-to-know-about%2F&title=Eight%20Obscure%20Bash%20Options%20You%20Might%20Want%20to%20Know%20About)

[Upvote](https://www.reddit.com/submit?url=https%3A%2F%2Fzwischenzugs.com%2F2019%2F04%2F03%2Feight-obscure-bash-options-you-might-want-to-know-about%2F&title=Eight%20Obscure%20Bash%20Options%20You%20Might%20Want%20to%20Know%20About)[Downvote](https://www.reddit.com/submit?url=https%3A%2F%2Fzwischenzugs.com%2F2019%2F04%2F03%2Feight-obscure-bash-options-you-might-want-to-know-about%2F&title=Eight%20Obscure%20Bash%20Options%20You%20Might%20Want%20to%20Know%20About)[(L)](https://www.reddit.com/submit?url=https%3A%2F%2Fzwischenzugs.com%2F2019%2F04%2F03%2Feight-obscure-bash-options-you-might-want-to-know-about%2F&title=Eight%20Obscure%20Bash%20Options%20You%20Might%20Want%20to%20Know%20About)

- [**Tweet](https://twitter.com/intent/tweet?original_referer=https%3A%2F%2Fzwischenzugs.com%2F2019%2F04%2F03%2Feight-obscure-bash-options-you-might-want-to-know-about%2F&ref_src=twsrc%5Etfw&related=wordpressdotcom&text=Eight%20Obscure%20Bash%20Options%20You%20Might%20Want%20to%20Know%20About&tw_p=tweetbutton&url=https%3A%2F%2Fzwischenzugs.com%2F2019%2F04%2F03%2Feight-obscure-bash-options-you-might-want-to-know-about%2F&via=ianmiell)
- [ Post]()
- [*46*********]()
- [(L)](https://www.facebook.com/sharer/sharer.php?kid_directed_site=0&sdk=joey&u=https%3A%2F%2Fzwischenzugs.com%2F2019%2F04%2F03%2Feight-obscure-bash-options-you-might-want-to-know-about%2F&display=popup&ref=plugin&src=share_button)

-
.

[Like](https://widgets.wp.com/likes/index.html?ver=20190321#)
Be the first to like this.

### *Related*

[Eleven bash Tips You Might Want to Know](https://zwischenzugs.com/2018/10/12/eleven-bash-tips-you-might-want-to-know/)With 16 comments

[Ten Things I Wish I'd Known About bash](https://zwischenzugs.com/2018/01/06/ten-things-i-wish-id-known-about-bash/)With 51 comments

[Ten More Things I Wish I&#039;d Known About bash](https://zwischenzugs.com/2018/01/21/ten-more-things-i-wish-id-known-about-bash/)With 17 comments

![4f37af910d4d089ee4a4b5d4782ca78e](../_resources/365723b69f9da32a02af435caa81a453.jpg)

## Published by zwischenzugs

[View all posts by zwischenzugs](https://zwischenzugs.com/author/zwischenzugs/)

**Published**April 3, 2019