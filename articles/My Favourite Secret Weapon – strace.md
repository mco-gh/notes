My Favourite Secret Weapon – strace

# My Favourite Secret Weapon – strace

## Why `strace`?

I’m often asked in my technical troubleshooting job to solve problems that development teams can’t solve. Usually these do not involve knowledge of API calls or syntax, rather some kind of insight into what the right tool to use is, and why and how to use it. Probably because they’re not taught in college, developers are often unaware that these tools exist, which is a shame, as playing with them can give a much deeper understanding of what’s going on and ultimately lead to better code.

My favourite secret weapon in this path to understanding is strace.

`strace` (or its Solaris equivalents, `truss``dtruss` is a tool that tells you which operating system (OS) calls your program is making.

An OS call (or just “system call”) is your program asking the OS to provide some service for it. Since this covers a lot of the things that cause problems not directly to do with the domain of your application development (I/O, finding files, permissions etc) its use has a very high hit rate in resolving problems out of developers’ normal problem space.

## Usage Patterns

strace is useful in all sorts of contexts. Here’s a couple of examples garnered from my experience.

### My Netcat Server Won’t Start!

Imagine you’re trying to start an executable, but it’s failing silently (no log file, no output at all). You don’t have the source, and even if you did, the source code is neither readily available, nor ready to compile, nor readily comprehensible.

Simply running through strace will likely give you clues as to what’s gone on.
$  nc -l localhost 80
nc: Permission denied

Let’s say someone’s trying to run this and doesn’t understand why it’s not working (let’s assume manuals are unavailable).

Simply put `strace` at the front of your command. Note that the following output has been heavily edited for space reasons (deep breath):

$ strace nc -l localhost 80
 execve("/bin/nc", ["nc", "-l", "localhost", "80"], [/* 54 vars */]) = 0
brk(0)                                  = 0x1e7a000
access("/etc/ld.so.nohwcap", F_OK)      = -1 ENOENT (No such file or directory)

mmap(NULL, 8192, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0x7f751c9c0000

access("/etc/ld.so.preload", R_OK)      = -1 ENOENT (No such file or directory)

open("/usr/local/lib/tls/x86_64/libglib-2.0.so.0", O_RDONLY) = -1 ENOENT (No such file or directory)

stat("/usr/local/lib/tls/x86_64", 0x7fff5686c240) = -1 ENOENT (No such file or directory)

 [...]
open("libglib-2.0.so.0", O_RDONLY)      = -1 ENOENT (No such file or directory)
open("/etc/ld.so.cache", O_RDONLY)      = 3
fstat(3, {st_mode=S_IFREG|0644, st_size=179820, ...}) = 0
mmap(NULL, 179820, PROT_READ, MAP_PRIVATE, 3, 0) = 0x7f751c994000
close(3)                                = 0
access("/etc/ld.so.nohwcap", F_OK)      = -1 ENOENT (No such file or directory)
open("/lib/x86_64-linux-gnu/libglib-2.0.so.0", O_RDONLY) = 3
read(3, "\177ELF\2\1\1\3>\1\320k\1"..., 832) = 832
fstat(3, {st_mode=S_IFREG|0644, st_size=975080, ...}) = 0

mmap(NULL, 3072520, PROT_READ|PROT_EXEC, MAP_PRIVATE|MAP_DENYWRITE, 3, 0) = 0x7f751c4b3000

mprotect(0x7f751c5a0000, 2093056, PROT_NONE) = 0

mmap(0x7f751c79f000, 8192, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0xec000) = 0x7f751c79f000

mmap(0x7f751c7a1000, 520, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_ANONYMOUS, -1, 0) = 0x7f751c7a1000

close(3)                                = 0

open("/usr/local/lib/libc.so.6", O_RDONLY) = -1 ENOENT (No such file or directory)

[...]
mmap(NULL, 179820, PROT_READ, MAP_PRIVATE, 3, 0) = 0x7f751c994000
close(3)                                = 0
access("/etc/ld.so.nohwcap", F_OK)      = -1 ENOENT (No such file or directory)
open("/lib/x86_64-linux-gnu/libnss_files.so.2", O_RDONLY) = 3
read(3, "\177ELF\2\1\1\3>\1\20\""..., 832) = 832
fstat(3, {st_mode=S_IFREG|0644, st_size=51728, ...}) = 0

mmap(NULL, 2148104, PROT_READ|PROT_EXEC, MAP_PRIVATE|MAP_DENYWRITE, 3, 0) = 0x7f751b8b0000

mprotect(0x7f751b8bc000, 2093056, PROT_NONE) = 0

mmap(0x7f751babb000, 8192, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0xb000) = 0x7f751babb000

close(3)                                = 0
mprotect(0x7f751babb000, 4096, PROT_READ) = 0
munmap(0x7f751c994000, 179820)          = 0
open("/etc/hosts", O_RDONLY|O_CLOEXEC)  = 3
fcntl(3, F_GETFD)                       = 0x1 (flags FD_CLOEXEC)
fstat(3, {st_mode=S_IFREG|0644, st_size=315, ...}) = 0

mmap(NULL, 4096, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0x7f751c9bf000

read(3, "127.0.0.1\tlocalhost\n127.0.1.1\tal"..., 4096) = 315
read(3, "", 4096)                       = 0
close(3)                                = 0
munmap(0x7f751c9bf000, 4096)            = 0
open("/etc/gai.conf", O_RDONLY)         = 3
fstat(3, {st_mode=S_IFREG|0644, st_size=3343, ...}) = 0
fstat(3, {st_mode=S_IFREG|0644, st_size=3343, ...}) = 0

mmap(NULL, 4096, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0x7f751c9bf000

read(3, "# Configuration for getaddrinfo("..., 4096) = 3343
read(3, "", 4096)                       = 0
close(3)                                = 0
munmap(0x7f751c9bf000, 4096)            = 0
futex(0x7f751c4af460, FUTEX_WAKE_PRIVATE, 2147483647) = 0
socket(PF_INET, SOCK_DGRAM, IPPROTO_IP) = 3

connect(3, {sa_family=AF_INET, sin_port=htons(80), sin_addr=inet_addr("127.0.0.1")}, 16) = 0

getsockname(3, {sa_family=AF_INET, sin_port=htons(58567), sin_addr=inet_addr("127.0.0.1")}, [16]) = 0

close(3)                                = 0
socket(PF_INET6, SOCK_DGRAM, IPPROTO_IP) = 3

connect(3, {sa_family=AF_INET6, sin6_port=htons(80), inet_pton(AF_INET6, "::1", &sin6_addr), sin6_flowinfo=0, sin6_scope_id=0}, 28) = 0

getsockname(3, {sa_family=AF_INET6, sin6_port=htons(42803), inet_pton(AF_INET6, "::1", &sin6_addr), sin6_flowinfo=0, sin6_scope_id=0}, [28]) = 0

close(3)                                = 0
socket(PF_INET6, SOCK_STREAM, IPPROTO_TCP) = 3
setsockopt(3, SOL_SOCKET, SO_REUSEADDR, [1], 4) = 0

bind(3, {sa_family=AF_INET6, sin6_port=htons(80), inet_pton(AF_INET6, "::1", &sin6_addr), sin6_flowinfo=0, sin6_scope_id=0}, 28) = -1 EACCES (Permission denied)

close(3)                                = 0
socket(PF_INET, SOCK_STREAM, IPPROTO_TCP) = 3
setsockopt(3, SOL_SOCKET, SO_REUSEADDR, [1], 4) = 0

bind(3, {sa_family=AF_INET, sin_port=htons(80), sin_addr=inet_addr("127.0.0.1")}, 16) = -1 EACCES (Permission denied)

close(3)                                = 0
write(2, "nc: ", 4nc: )                     = 4
write(2, "Permission denied\n", 18Permission denied
)     = 18
exit_group(1)                           = ?

To most people that see this flying up their terminal this initially looks like gobbledygook, but it’s really quite easy to parse when a few things are explained.

For each line:

- the first entry on the left is the system call being performed
- the bit in the parentheses are the arguments to the system call
- the right side of the equals sign is the return value of the system call

open("/etc/gai.conf", O_RDONLY)         = 3

Therefore for this particular line, the system call is `open`, the arguments are the string `/etc/gai.conf` and the constant `O_RDONLY`, and the return value was `3`.

How to make sense of this?

Some of these system calls can be guessed or enough can be inferred from context. Most readers will figure out that the above line is the attempt to open a file with read-only permission.

In the case of the above failure, we can see that before the program calls exit_group, there is a couple of calls to bind that return “Permission denied”:

bind(3, {sa_family=AF_INET6, sin6_port=htons(80), inet_pton(AF_INET6, "::1", &sin6_addr), sin6_flowinfo=0, sin6_scope_id=0}, 28) = -1 EACCES (Permission denied)

close(3)                                = 0
socket(PF_INET, SOCK_STREAM, IPPROTO_TCP) = 3
setsockopt(3, SOL_SOCKET, SO_REUSEADDR, [1], 4) = 0

bind(3, {sa_family=AF_INET, sin_port=htons(80), sin_addr=inet_addr("127.0.0.1")}, 16) = -1 EACCES (Permission denied)

close(3)                                = 0
write(2, "nc: ", 4nc: )                     = 4
write(2, "Permission denied\n", 18Permission denied
)     = 18
exit_group(1)                           = ?

We might therefore want to understand what “bind” is and why it might be failing.

You need to get a copy of the system call’s documentation. On ubuntu and related distributions of linux, the documentation is in the `manpages-dev` package, and can be invoked by eg ​​`man 2 bind` (I just used `strace` to determine which file `man 2 bind` opened and then did a `dpkg -S` to determine from which package it came!). You can also look up online if you have access, but if you can auto-install via a package manager you’re more likely to get docs that match your installation.

Right there in my `man 2 bind` page it says:
ERRORS
EACCES The address is protected, and the user is not the superuser.

So there is the answer – we’re trying to bind to a port that can only be bound to if you are the super-user.

* * *

**My book, [Learn Bash the Hard Way](https://leanpub.com/learnbashthehardway), available at [$5](https://leanpub.com/learnbashthehardway):**

[(L)](https://leanpub.com/learnbashthehardway)

[![hero](../_resources/6e4b6a4d64605466dbd8f2aa8815697e.png)](https://leanpub.com/learnbashthehardway)

Preview available [here](https://zwischenzugs.files.wordpress.com/2018/01/learnbashthehardway-sample-preview.pdf).

* * *

### My Library Is Not Loading!

Imagine a situation where developer A’s perl script is working fine, but not on developer B’s identical one is not (again, the output has been edited).

In this case, we strace the output on developer B’s computer to see how it’s working:

$ strace perl a.pl
execve("/usr/bin/perl", ["perl", "a.pl"], [/* 57 vars */]) = 0
brk(0)                                  = 0xa8f000
[...]fcntl(3, F_SETFD, FD_CLOEXEC)           = 0
fstat(3, {st_mode=S_IFREG|0664, st_size=14, ...}) = 0
rt_sigaction(SIGCHLD, NULL, {SIG_DFL, [], 0}, 8) = 0
brk(0xad1000)                           = 0xad1000
read(3, "use blahlib;\n\n", 4096)       = 14

stat("/space/myperllib/blahlib.pmc", 0x7fffbaf7f3d0) = -1 ENOENT (No such file or directory)

stat("/space/myperllib/blahlib.pm", {st_mode=S_IFREG|0644, st_size=7692, ...}) = 0

open("/space/myperllib/blahlib.pm", O_RDONLY) = 4

ioctl(4, SNDCTL_TMR_TIMEBASE or TCGETS, 0x7fffbaf7f090) = -1 ENOTTY (Inappropriate ioctl for device)

[...]mmap(0x7f4c45ea8000, 8192, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 5, 0x4000) = 0x7f4c45ea8000

close(5)                                = 0
mprotect(0x7f4c45ea8000, 4096, PROT_READ) = 0
brk(0xb55000)                           = 0xb55000
read(4, "swrite($_[0], $_[1], $_[2], $_[3"..., 4096) = 3596
brk(0xb77000)                           = 0xb77000
read(4, "", 4096)                       = 0
close(4)                                = 0
read(3, "", 4096)                       = 0
close(3)                                = 0
exit_group(0)                           = ?
We observe that the file is found in what looks like an unusual place.
open("/space/myperllib/blahlib.pm", O_RDONLY) = 4
Inspecting the environment, we see that:
$ env | grep myperl
PERL5LIB=/space/myperllib
So the solution is to set the same env variable before running:
export PERL5LIB=/space/myperllib

## Get to know the internals bit by bit

If you do this a lot, or idly run `strace` on various commands and peruse the output, you can learn all sorts of things about the internals of your OS. If you’re like me, this is a great way to learn how things work. For example, just now I’ve had a look at the file `/etc/gai.conf`, which I’d never come across before writing this.

Once your interest has been piqued, I recommend getting a copy of “Advanced Programming in the Unix Environment” by Stevens & Rago, and reading it cover to cover. Not all of it will go in, but as you use `strace` more and more, and (hopefully) browse C code more and more understanding will grow.

## Gotchas

If you’re running a program that calls other programs, it’s important to run with the -f flag, which “follows” child processes and straces them. -ff creates a separate file with the pid suffixed to the name.

If you’re on solaris, this program doesn’t exist – you need to use truss instead.

Many production environments will not have this program installed for security reasons. strace doesn’t have many library dependencies (on my machine it has the same dependencies as ‘echo’), so if you have permission, (or are feeling sneaky) you can just copy the executable up.

## Other useful tidbits

You can attach to running processes (can be handy if your program appears to hang or the issue is not readily reproducible) with `-p`.

If you’re looking at performance issues, then the time flags (`-t`, `-tt`, `-ttt`, and `-T`) can help significantly.

* * *

**My book, [Learn Bash the Hard Way](https://leanpub.com/learnbashthehardway), available at [$5](https://leanpub.com/learnbashthehardway):**

[(L)](https://leanpub.com/learnbashthehardway)

[![hero](../_resources/6e4b6a4d64605466dbd8f2aa8815697e.png)](https://leanpub.com/learnbashthehardway)

Preview available [here](https://zwischenzugs.files.wordpress.com/2018/01/learnbashthehardway-sample-preview.pdf).

Advertisements