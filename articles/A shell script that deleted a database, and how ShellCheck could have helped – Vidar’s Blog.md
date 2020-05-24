A shell script that deleted a database, and how ShellCheck could have helped – Vidar’s Blog

# A shell script that deleted a database, and how ShellCheck could have helped

Summary: We examine a real world case of how an innocent shell scripting mistake caused the deletion of a production database, and how [ShellCheck](https://www.shellcheck.net/) (a GPLv3 shell script linting and analysis tool) would have pointed out the errors and prevented the disaster.

Disclosure: I am the ShellCheck author.

### The event

Here is the sad case, taken from a recent StackOverflow post:
**

> My developer committed a huge mistake and we cannot find our mongo database anyone in the server. Rescue please!!!

> He logged into the server, and saved the following shell under `~/crontab/mongod_back.sh`> :

	#!/bin/sh
	DUMP=mongodump
	OUT_DIR=/data/backup/mongod/tmp     // 备份文件临时目录
	TAR_DIR=/data/backup/mongod         // 备份文件正式目录
	DATE=`date +%Y_%m_%d_%H_%M_%S`      // 备份文件将以备份时间保存
	DB_USER=Guitang                     // 数据库操作员
	DB_PASS=qq____________              // 数据库操作员密码
	DAYS=14                             // 保留最新14夭的备份
	TAR_BAK="mongod_bak_$DATE.tar.gz"   // 备份文件命名格式
	cd $OUT_DIR                         // 创建文件夹
	rm -rf $OUT_DIR/*                   // 清空临时目录
	mkdir -p $OUT_DIR/$DATE             // 创建本次备份文件夹
	$DUMP -d wecard -u $DB_USER -p $DB_PASS -o $OUT_DIR/$DATE  // 执行备份命令
	tar -zcvf $TAR_DIR/$TAR_BAK $OUT_DIR/$DATE       // 将备份文件打包放入正式目
	find $TAR_DIR/ -mtime +%DAYS -delete             // 删除14天前的旧备洲

> And then he run `./mongod_back.sh`> , then there were lots of permission denied, then he did Ctrl+C. Then the server shut down automatically.

> He then contacted AliCloud, the engineer connected the disk to another working server, so that he could check the disk. Then, he realized that some folders have gone, including `/data/`>  where the mongodb is!!!

> PS: he did not take snapshot of the disk before.
**
Essentially, it’s every engineer’s nightmare.

The post-mortem of this issue is an interesting puzzle that requires only basic shell scripting knowledge. If you’d like to give it a try, now’s the time. If you’d like some hints, here’s [shellcheck’s output](https://www.shellcheck.net/?id=rescueplease) for the script.

The rest of this post details about what happened, and how ShellCheck could have averted the disaster.

### What went wrong?

The [MCVE](https://stackoverflow.com/help/mcve) for how to ruin your week is this:

	#!/bin/sh
	DIR=/data/tmp    // The directory to delete
	rm -rf $DIR/*    // Now delete it

The fatal error here is that `//` is not a comment in shell scripts. It’s a path to the root directory, equivalent to `/`.

On some platforms, the `rm` line would have been fatal by itself, because it’d boil down to `rm -rf /` with a few other arguments. Implementation these days often don’t allow this though. The disaster in question happened on Ubuntu, whose GNU `rm` would have refused:

	$ rm -rf //
	rm: it is dangerous to operate recursively on '//' (same as '/')
	rm: use --no-preserve-root to override this failsafe

This is where the assignment comes in.

The shell treats variable assignments and commands as two sides of the same coin. Here’s the description [from POSIX](http://pubs.opengroup.org/onlinepubs/9699919799/utilities/V3_chap02.html#tag_18_09_01):

**

> A “simple command” is a sequence of optional variable assignments and redirections, in any sequence, optionally followed by words and redirections, terminated by a control operator.

**

(A “simple command” is in contrast to a “compound” command, which are structures like `if` statements and `for` loops that contain one or more simple or compound commands.)

This means that `var=42` and `echo "Hello"` are both simple commands. The former has one optional assignment and zero optional words. The latter has zero optional assignments and two optional words.

It also implies that a single simple command can contain both: `var=42 echo "Hello"`

To make a long spec short, assignments in a simple command will apply only to the invoked command name. If there is no command name, they apply to the current shell. This latter explains `var=42` by itself, but when would you use the former?

It’s useful when you want to set a variable for a single command without affecting your the rest of your shell:

	$ echo "$PAGER"  # Show current pager
	less

	$ PAGER="head -n 5" man ascii
	ASCII(7)       Linux Programmer's Manual      ASCII(7)

	NAME
	       ascii  -  ASCII character set encoded in octal,
	       decimal, and hexadecimal

	$ echo "$PAGER"  # Current pager hasn't changed
	less

This is exactly what happened unintentionally in the fatal assignment. Just like how the previous example scoped `PAGER` to `man` only, this one scoped `DIR` to `//`:

	$ DIR=/data/tmp    // The directory to delete
	bash: //: Is a directory

	$ echo "$DIR"  # The variable is unset
	(no output)

This meant that `rm -rf $DIR/*` became `rm -rf /*`, and therefore bypassed the check that was is in place for `rm -rf /`

(Why can’t or won’t `rm` simply refuse to delete `/*` too? Because it never sees `/*`: the shell expands it first, so `rm` sees `/bin /boot /dev /data ...`. While `rm` could obviously refuse to remove first level directories as well, this starts getting in the way of legitimate usage – a big sin in the Unix philosophy)

### How ShellCheck could have helped

Here’s the output from this minimized snippet ([see online](https://www.shellcheck.net/?id=rescuemcve)):

	$ shellcheck myscript

	In myscript line 2:
	DIR=/data/tmp    // The directory to delete
	                 ^-- SC1127: Was this intended as a comment? Use # in sh.

	In myscript line 3:
	rm -rf $DIR/*    // Now delete it
	       ^----^ SC2115: Use "${var:?}" to ensure this never expands to /* .
	       ^--^ SC2086: Double quote to prevent globbing and word splitting.
	                 ^-- SC2114: Warning: deletes a system directory.

Two issues have already been discussed, and would have averted this disaster:

- ShellCheck noticed that the first `//` was likely intended as a comment (wiki: [SC1127](https://www.shellcheck.net/wiki/SC1127)).
- ShellCheck pointed out that the second `//` would target a system directory (wiki: [SC2114](https://www.shellcheck.net/wiki/SC2114)).

The third is a general defensive technique which would also have prevented this catastrophic `rm` independently of the two other fixes:

- ShellCheck suggested using `rm -rf ${DIR:?}/*` to abort execution if the variable for any reason is empty or unset (wiki: [SC2115](https://www.shellcheck.net/wiki/SC2115)).

This would mitigate the effect of a whole slew of pitfalls that can leave a variable empty, including `echo /tmp | read DIR` (subshells), `DIR= /tmp` (bad spacing) and `DIR=$(echo /tmp)` (potential fork/command failures).

### Conclusion

Shell scripts are really convenient, but also have a large number of potential pitfalls. Many issues that would be simple, fail-fast syntax errors in other languages would instead cause a script to misbehave in confusing, annoying, or catastrophic ways. Many examples can be found in the [Wooledge Bash Pitfalls](https://mywiki.wooledge.org/BashPitfalls) list, or ShellCheck’s own [gallery of bad code](https://github.com/koalaman/shellcheck#gallery-of-bad-code).

Since tooling exists, why not take advantage? Even if (or especially when!) you rarely write shell scripts, you can install [`shellcheck`](https://www.shellcheck.net/) from your package manager, along with a [suitable editor plugin](https://github.com/koalaman/shellcheck#how-to-use) like [Flycheck](https://www.flycheck.org/en/latest/) (Emacs) or [Syntastic](https://github.com/vim-syntastic/syntastic) (Vim), and just forget about it.

The next time you’re writing a script, your editor will show warnings and suggestions automatically. Whether or not you want to fix the more pedantic style issues, it may be worth looking at any unexpected errors and warnings. It might just save your database.

![6eb20a4fdaf38060ef4912f8daa05173](../_resources/c1861c149a57d8d48fc842a7aedd787d.png)Author   [Vidar](https://www.vidarholen.net/contents/blog/?author=1)/Posted on [2019-03-27](https://www.vidarholen.net/contents/blog/?p=746)/Categories [Basic Linux-related things](https://www.vidarholen.net/contents/blog/?cat=6), [Linux](https://www.vidarholen.net/contents/blog/?cat=4)/Tags [why-bash-is-like-that](https://www.vidarholen.net/contents/blog/?tag=why-bash-is-like-that)