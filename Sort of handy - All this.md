Sort of handy - All this

 [Next post](https://leancrew.com/all-this/2020/05/arrangements-and-derangements/)  [Previous post](https://leancrew.com/all-this/2020/05/timing-in-ssh/)

# [Sort of handy](https://leancrew.com/all-this/2020/05/sort-of-handy/)

May 19, 2020 at 5:38 PM by Dr. Drang

This afternoon, I wanted to see how much disk space I had left on the server that runs this blog. As is often the case with Unix/Linux commands, after I getting the needed information, I started thinking about other ways to do things. And, as is also often the case, I learned something new. New to me, anyway.

First, I logged into the server and ran the [`df` command](http://man7.org/linux/man-pages/man1/df.1.html):

`df -h .`

The output, which summarizes the disk usage of the file system containing the given file (in this case, the current directory, `.`, was my home directory) was

	Filesystem                 Size  Used Avail Use% Mounted on
	/dev/disk/by-label/DOROOT   25G  9.5G   14G  41% /

This shows I’m using 41% of the 25 GB I’m paying for. The `-h` option told `df` to use a “human” format for the output, Instead of showing the usage in “1-K blocks,” it shows it in kilobytes, megabytes, and gigabytes. Lots of GNU utilities have an `-h` option that works this way.

This disk usage includes everything on my virtual server—all the executables, libraries, and support files in addition to the files specific to the blog. I wanted to refine this to see just what the blog was using. That called for the [`du` command](http://man7.org/linux/man-pages/man1/du.1.html):

`du -hd 1 .`

Once again, the `-h` option meant “human formatted values.” The `-d 1` option told `du` to go only one directory level deep. The output was

	8.0K    ./.gnupg
	68K     ./pagelogs
	114M    ./all-this
	9.0M    ./.local
	116K    ./php-markdown
	1.5M    ./.cache
	68K     ./.ipython
	20K     ./.pip
	8.0K    ./.ssh
	522M    ./tmp
	16K     ./bin
	8.0K    ./.conda
	1.1G    ./public_html
	4.0K    ./.nano
	3.4G    ./anaconda3
	5.1G    .

The line for `public_html` was what I was looking for: 1.1 GB. So relatively little of the space on the server is being used for the blog.

As I looked at the `du` output, I thought it would be more useful to have it in numerical order. I thought about adding an `-s` option to `du`, but that doesn’t work. The [`du` man page](http://man7.org/linux/man-pages/man1/du.1.html) shows no option for sorting the output.

The standard Unix way of doing things would suggest piping the output to [`sort`](http://man7.org/linux/man-pages/man1/sort.1.html), but I was sure that wouldn’t work here. Because although `sort` has an `-n` option for sorting numerically, the numbers in `du`’s human output weren’t what needed to be sorted. It’s the *quantities* I wanted sorted, and that means the suffixes had to be accounted for. A test with

`du -hd 1 . | sort -n`
gave me

	1.1G    ./public_html
	1.5M    ./.cache
	3.4G    ./anaconda3
	4.0K    ./.nano
	5.1G    .
	8.0K    ./.conda
	8.0K    ./.gnupg
	8.0K    ./.ssh
	9.0M    ./.local
	16K     ./bin
	20K     ./.pip
	68K     ./.ipython
	68K     ./pagelogs
	114M    ./all-this
	116K    ./php-markdown
	522M    ./tmp

which confirmed my suspicions. Perfect for sorting the numbers but useless for sorting the quantities.

I could use a different output switch for `du`:
`du -kd 1 . | sort -n`
The `-k` tells `du` to output the sizes in kilobytes. The sorted output is

	4       ./.nano
	8       ./.conda
	8       ./.gnupg
	8       ./.ssh
	16      ./bin
	20      ./.pip
	68      ./.ipython
	68      ./pagelogs
	116     ./php-markdown
	1448    ./.cache
	9184    ./.local
	115896  ./all-this
	534104  ./tmp
	1098316 ./public_html
	3470796 ./anaconda3
	5333936 .

which is great until the numbers get up past five or six digits and you lose track of the order of magnitude.

But here comes the part where I learn something. It turns out the GNU folks recognized the need to *read* human-formatted values as well as write them, and they added an `-h` option to `sort`. So

`du -hd 1 . | sort -hr`
gives

	5.1G    .
	3.4G    ./anaconda3
	1.1G    ./public_html
	522M    ./tmp
	114M    ./all-this
	9.0M    ./.local
	1.5M    ./.cache
	116K    ./php-markdown
	68K     ./pagelogs
	68K     ./.ipython
	20K     ./.pip
	16K     ./bin
	8.0K    ./.ssh
	8.0K    ./.gnupg
	8.0K    ./.conda
	4.0K    ./.nano

which is exactly what I wanted: easy to read and properly sorted. (The `-r` switch tells `sort` to reverse so the biggest directories come first.)

The `-h` option was added to GNU `sort`  [in 2009](https://github.com/coreutils/coreutils/blob/master/NEWS), four or five years after I moved back to the Mac and stopped being as intense a command line user as I had been. I don’t feel too bad about not knowing of it.

 [Next post](https://leancrew.com/all-this/2020/05/arrangements-and-derangements/)  [Previous post](https://leancrew.com/all-this/2020/05/timing-in-ssh/)