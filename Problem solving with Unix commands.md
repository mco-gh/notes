Problem solving with Unix commands

 [Vegard Stikbakke](https://www.vegardstikbakke.com/)

# Problem solving with Unix commands

February 13, 2019

I am starting to realize that the Unix command-line toolbox can fix absolutely any problem related to text wrangling. Let me tell you about a problem I had, and how I used some Unix command-line utilities to solve it.

## The problem

I’m working on research for my master thesis. As with many statisticians, I am running a lot of simulations. I first simulate some data according to some numerical seed (to ensure reproducibility), and then use an algorithm to estimate something based on that data. For each simulation run, I create some files, typically like so:

	dataset-directory/0001_data.csv
	dataset-directory/0001_A.csv

Sometimes a run fails. This doesn’t really matter in this case: For any failed simulation, I can just do another one. For the `0001` data, I had a successful run with algorithm `A`. Therefore I want to use the `0001` data on algorithm `B` as well. But I need to keep track of which runs of `A` have failed.

After running algorithm `A` on a lot of data, I end up with a large list of files like

	dataset-directory/0001_data.csv
	dataset-directory/0001_A.csv
	dataset-directory/0002_data.csv
	dataset-directory/0002_A.csv
	dataset-directory/0003_data.csv
	dataset-directory/0003_A.csv
	dataset-directory/0004_data.csv
	dataset-directory/0005_data.csv
	dataset-directory/0005_A.csv
	dataset-directory/0006_data.csv
	dataset-directory/0006_A.csv
	dataset-directory/0007_data.csv
	dataset-directory/0007_A.csv
	dataset-directory/0008_data.csv
	dataset-directory/0009_data.csv
	dataset-directory/0009_A.csv
	...
	dataset-directory/0499_A.csv

The astute observer will note that the file for algorithm `A` on data `0004` and `0008` are missing. **How can I get a list of all the numbers for which `A` didn’t succeed?**

I certainly could go over manually, but that would be error prone, and incredibly boring. It’s much better to write a program to do it!

## The solution

To be obtuse: Those that didn’t succeed are the numbers from `0001` to `0500` except those that succeeded. And one handy command to get a list of numbers is `seq`:

	$> seq 10
	1
	2
	3
	4
	5
	6
	7
	8
	9
	10

(If only one number is given, it is implied that the sequence starts with `1`. `seq 2 10` would do what you think it would, as well.)

Now, if we can get a list of all the successful runs, we should be able to get what we want by cross-checking the list of successful runs with a `seq` command which prints all possible numbers!

Most command-line utilities do one pretty specific thing. For example, with `cut` you can get the characters on specific locations on each line

	$> cat text
	Lorem ipsum
	dolor sit amet
	$> cat text | cut -c 2-5
	orem
	olor

Notice here the use of the so-called pipe operator `|`. Like I said, most utilities do one specific thing, and it does that thing well. The neat thing is that these can be combined. By using these pipes, the output from the command to the left of the pipe is directed to the command to the right. Note that these commands treat the input as a stream of lines, which is often really handy.

We can get a list of the successful file names by piping the list of files into a `grep` command, which is a command which can use regular expressions. Since all files start with an equal length of 4 digits, we can match these to the regular expression `\d\d\d\d`, matching 4 digits in a row, and add the file ending for the `A` algorithm to the regular expression. To get the list of files with one line for each file, we can simply do `ls`. (Although `ls` doesn’t give each file its own line when calling it separately, it turns out that piping the output from `ls` will.)

	$> ls dataset-directory | grep '\d\d\d\d_A.csv'
	0009_A.csv
	0001_A.csv
	0002_A.csv
	0005_A.csv
	0007_A.csv
	0003_A.csv
	0006_A.csv
	...

For some reason, these show up in a scrambled order after using `grep`. We can use `sort` to fix that. And we are only interested in the numbers, so we can use `cut -c 1-4` to extract the number parts.

	$> ls dataset-directory | grep '\d\d\d\d_A.csv' | sort | cut -c 1-4
	0001
	0002
	0003
	0005
	0006
	0007
	0009
	...
	0499

These numbers aren’t exactly the same as the numbers from the `seq` command, since these are zero-padded. Therefore we write a quick Python script to parse them as integers.

	# parse.py
	import sys

	for line in sys.stdin:
	    i = int(line)
	    print(i)

Now, piping into this script will give us the numbers that we want:

	$> ls dataset-directory | grep '\d\d\d\d_A.csv' | cut -c 1-4 | python3 parse.py
	1
	2
	3
	5
	6
	7
	9
	...
	499

We’re getting there! Now we have to figure out how to cross-check these lists of numbers. Luckily, there exists a command called `comm`, which checks for *comm*on characters in two input streams. To get the input of a sequence of commands such as the one above, we can evaluate it and redirect it, which we do by wrapping it in `<(...)`.

	$> comm <(ls dataset-directory | grep '\d\d\d\d_A.csv' | cut -c 1-4 | python3 parse.py) <(seq 500)
	        1
	        2
	        3
	    4
	        5
	        6
	        7
	    8
	        9
	    10
	...
	    500

This output is a bit disorienting. If we read the manual of `comm` (by doing `man comm`), we see that `comm` “produces three text columns as output: lines only in file1; lines only in file2; and lines in both files.” To suppress column 1 – which is empty, since no numbers are only from the file list – call `comm` with the flag `-1`. And since we are not interested in the numbers which are in both streams, we suppress with the `-3` flag as well.

	$> comm -1 -3 <(ls dataset-directory | grep '\d\d\d\d_A.csv' | cut -c 1-4 | python3 parse.py) <(seq 500)
	4
	8
	...
	500

And we’re done!

Update: This post generated [some interesting discussion on Hacker News](https://news.ycombinator.com/item?id=19160659). There are many ways to solve this problem, and the way I did it is probably not the best. Be sure to check it out for tips on how to improve. [I was also asked to post this on dev.to, which I did](https://dev.to/vegarsti/problem-solving-with-unix-commands-4j8l)!

* * *

 **Do you want to get notified of new blog posts? Go [here](https://www.vegardstikbakke.com/feed.xml) for an RSS feed.**