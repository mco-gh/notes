Linux utils that you might not know

# Linux utils that you might not know

 [@igor_sarcevic](https://twitter.com/igor_sarcevic) · May 21, 2017

I’ve used Linux as my primary operating system for well over ten years, yet I still stumble upon things that are completely unknown to me. For example, several days ago, I wanted to display a formated table in my terminal.

	# I had a long comma separated list

	id,name,count
	31232,test-1,21
	31,window,2
	2121,update-attributes,432

	# and I wanted to display it as a table

	id     name               count
	31232  test-1             21
	31     window             2
	2121   update-attributes  432

I know that in Ruby, I have an excellent library[Terminal Table](https://github.com/tj/terminal-table) for generating nice terminal tables, however, parsing the input, mapping the values and writing a Ruby script just for this task seemed like a huge overhead. After googling around for a quick and easy solution, I’ve learned that there is a tool in my Linux environment — column — that does just that.

	$ cat data.txt | column -t -s ','

	id     name               count
	31232  property-a         21
	31     window             2
	2121   update-attributes  432

Whoa! That was super simple. I was baffled by the fact that this program was part of the standard utilities set on Linux, and yet I’ve never used it. So I wondered what else is part of coreutils or util-linux packages that I don’t know about. I’ve found several interesting and usable tools.

For example, did you know that you have a built in calendar?

	$ cal

	      May 2017
	Su Mo Tu We Th Fr Sa
	    1  2  3  4  5  6
	 7  8  9 10 11 12 13
	14 15 16 17 18 19 20
	21 22 23 24 25 26 27
	28 29 30 31

	$ cal -3

	                            2017
	       April                  May                   June
	Su Mo Tu We Th Fr Sa  Su Mo Tu We Th Fr Sa  Su Mo Tu We Th Fr Sa
	                   1      1  2  3  4  5  6               1  2  3
	 2  3  4  5  6  7  8   7  8  9 10 11 12 13   4  5  6  7  8  9 10
	 9 10 11 12 13 14 15  14 15 16 17 18 19 20  11 12 13 14 15 16 17
	16 17 18 19 20 21 22  21 22 23 24 25 26 27  18 19 20 21 22 23 24
	23 24 25 26 27 28 29  28 29 30 31           25 26 27 28 29 30
	30

Or, did you know that you can factor numbers with the `factor` program?

	$ factor 234123421341
	234123421341: 3 67 1601 727541

	$ factor $(date +%s) # factor current timestamp
	1495329393: 3 19 47 558167

Or, that you can find out how many terabytes are in `4123412312312` bytes:

	$ numfmt --to=iec 4123412312312
	3.8T

Or that there is a hardcore version of `rm` that makes it much harder to retrieve deleted files:

	$ shred a.txt

So many interesting things to learn! I encourage you to read through the[documentation](https://www.gnu.org/software/coreutils/manual/coreutils.html#toc-System-context-1)and update your knowledge on these wonderful tools that are installed out of box on our modern Linux distributions.

Happy hacking!

[**Tweet](https://twitter.com/intent/tweet?original_referer=http%3A%2F%2Fshiroyasha.io%2Fcoreutils-that-you-might-not-know.html&ref_src=twsrc%5Etfw&text=Linux%20utils%20that%20you%20might%20not%20know&tw_p=tweetbutton&url=http%3A%2F%2Fshiroyasha.io%2Fcoreutils-that-you-might-not-know.html&via=igor_sarcevic)

[(L)](https://www.facebook.com/sharer/sharer.php?app_id=619972441395428&kid_directed_site=0&u=http%3A%2F%2Fshiroyasha.io%2Fcoreutils-that-you-might-not-know.html&display=popup&ref=plugin&src=share_button)

 ![Twitter_logo_blue.png](../_resources/585bbab4ea70e62d8261d84648d7ef8d.png) You should [follow me on Twitter.](https://twitter.com/igor_sarcevic)

- [5 comments]()
- [**Shiroyasha Blog**](https://disqus.com/home/forums/shiroyashablog/)
- [Login](https://disqus.com/embed/comments/?base=default&f=shiroyashablog&t_i=ae4cc0c4-0e9d-4d23-a51b-59ee3681bfa8&t_u=http%3A%2F%2Fshiroyasha.io%2F%2Fcoreutils-that-you-might-not-know.html&t_d=Linux%20utils%20that%20you%20might%20not%20know&t_t=Linux%20utils%20that%20you%20might%20not%20know&s_o=default#)
- [1](https://disqus.com/home/inbox/)
- [ Recommend2](https://disqus.com/embed/comments/?base=default&f=shiroyashablog&t_i=ae4cc0c4-0e9d-4d23-a51b-59ee3681bfa8&t_u=http%3A%2F%2Fshiroyasha.io%2F%2Fcoreutils-that-you-might-not-know.html&t_d=Linux%20utils%20that%20you%20might%20not%20know&t_t=Linux%20utils%20that%20you%20might%20not%20know&s_o=default#)
- [⤤Share](https://disqus.com/embed/comments/?base=default&f=shiroyashablog&t_i=ae4cc0c4-0e9d-4d23-a51b-59ee3681bfa8&t_u=http%3A%2F%2Fshiroyasha.io%2F%2Fcoreutils-that-you-might-not-know.html&t_d=Linux%20utils%20that%20you%20might%20not%20know&t_t=Linux%20utils%20that%20you%20might%20not%20know&s_o=default#)
- [Sort by Best](https://disqus.com/embed/comments/?base=default&f=shiroyashablog&t_i=ae4cc0c4-0e9d-4d23-a51b-59ee3681bfa8&t_u=http%3A%2F%2Fshiroyasha.io%2F%2Fcoreutils-that-you-might-not-know.html&t_d=Linux%20utils%20that%20you%20might%20not%20know&t_t=Linux%20utils%20that%20you%20might%20not%20know&s_o=default#)

![Avatar](../_resources/7b2fde640943965cc88df0cdee365907.png)
Join the discussion…

- [Attach](https://disqus.com/embed/comments/?base=default&f=shiroyashablog&t_i=ae4cc0c4-0e9d-4d23-a51b-59ee3681bfa8&t_u=http%3A%2F%2Fshiroyasha.io%2F%2Fcoreutils-that-you-might-not-know.html&t_d=Linux%20utils%20that%20you%20might%20not%20know&t_t=Linux%20utils%20that%20you%20might%20not%20know&s_o=default#)

-

    - [−](https://disqus.com/embed/comments/?base=default&f=shiroyashablog&t_i=ae4cc0c4-0e9d-4d23-a51b-59ee3681bfa8&t_u=http%3A%2F%2Fshiroyasha.io%2F%2Fcoreutils-that-you-might-not-know.html&t_d=Linux%20utils%20that%20you%20might%20not%20know&t_t=Linux%20utils%20that%20you%20might%20not%20know&s_o=default#)
    - [*⚑*](https://disqus.com/embed/comments/?base=default&f=shiroyashablog&t_i=ae4cc0c4-0e9d-4d23-a51b-59ee3681bfa8&t_u=http%3A%2F%2Fshiroyasha.io%2F%2Fcoreutils-that-you-might-not-know.html&t_d=Linux%20utils%20that%20you%20might%20not%20know&t_t=Linux%20utils%20that%20you%20might%20not%20know&s_o=default#)

[![Avatar](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/disqus_eLK8j6CJtJ/)

[barry day](https://disqus.com/by/disqus_eLK8j6CJtJ/)•[3 hours ago](http://shiroyasha.io/coreutils-that-you-might-not-know.html#comment-3318400796)

GNU

-

    - [−](https://disqus.com/embed/comments/?base=default&f=shiroyashablog&t_i=ae4cc0c4-0e9d-4d23-a51b-59ee3681bfa8&t_u=http%3A%2F%2Fshiroyasha.io%2F%2Fcoreutils-that-you-might-not-know.html&t_d=Linux%20utils%20that%20you%20might%20not%20know&t_t=Linux%20utils%20that%20you%20might%20not%20know&s_o=default#)
    - [*⚑*](https://disqus.com/embed/comments/?base=default&f=shiroyashablog&t_i=ae4cc0c4-0e9d-4d23-a51b-59ee3681bfa8&t_u=http%3A%2F%2Fshiroyasha.io%2F%2Fcoreutils-that-you-might-not-know.html&t_d=Linux%20utils%20that%20you%20might%20not%20know&t_t=Linux%20utils%20that%20you%20might%20not%20know&s_o=default#)

[![Avatar](../_resources/e82c626d1c8f606882f0982d5381b589.jpg)](https://disqus.com/by/shadowmar/)

[Shadowmar](https://disqus.com/by/shadowmar/)•[27 minutes ago](http://shiroyasha.io/coreutils-that-you-might-not-know.html#comment-3318509972)

You might enjoy this article with even more examples (and tools you didn't know you had) [http://ablagoev.github.io/l...](http://disq.us/url?url=http%3A%2F%2Fablagoev.github.io%2Flinux%2Fadventures%2Fcommands%2F2017%2F02%2F19%2Fadventures-in-usr-bin.html%3AfgMgGLzuoG0lSPq49BTx9prvR24&cuid=2964258)

-

    - [−](https://disqus.com/embed/comments/?base=default&f=shiroyashablog&t_i=ae4cc0c4-0e9d-4d23-a51b-59ee3681bfa8&t_u=http%3A%2F%2Fshiroyasha.io%2F%2Fcoreutils-that-you-might-not-know.html&t_d=Linux%20utils%20that%20you%20might%20not%20know&t_t=Linux%20utils%20that%20you%20might%20not%20know&s_o=default#)
    - [*⚑*](https://disqus.com/embed/comments/?base=default&f=shiroyashablog&t_i=ae4cc0c4-0e9d-4d23-a51b-59ee3681bfa8&t_u=http%3A%2F%2Fshiroyasha.io%2F%2Fcoreutils-that-you-might-not-know.html&t_d=Linux%20utils%20that%20you%20might%20not%20know&t_t=Linux%20utils%20that%20you%20might%20not%20know&s_o=default#)

[![Avatar](../_resources/65e3b43b3cb54ab6537024398410e535.jpg)](https://disqus.com/by/disqus_7YK45pEU0V/)

[Fabien Dupont](https://disqus.com/by/disqus_7YK45pEU0V/)•[34 minutes ago](http://shiroyasha.io/coreutils-that-you-might-not-know.html#comment-3318505534)

The first example is an useless use of cat. "column -t -s ',' data.txt" is sufficient.

-

    - [−](https://disqus.com/embed/comments/?base=default&f=shiroyashablog&t_i=ae4cc0c4-0e9d-4d23-a51b-59ee3681bfa8&t_u=http%3A%2F%2Fshiroyasha.io%2F%2Fcoreutils-that-you-might-not-know.html&t_d=Linux%20utils%20that%20you%20might%20not%20know&t_t=Linux%20utils%20that%20you%20might%20not%20know&s_o=default#)
    - [*⚑*](https://disqus.com/embed/comments/?base=default&f=shiroyashablog&t_i=ae4cc0c4-0e9d-4d23-a51b-59ee3681bfa8&t_u=http%3A%2F%2Fshiroyasha.io%2F%2Fcoreutils-that-you-might-not-know.html&t_d=Linux%20utils%20that%20you%20might%20not%20know&t_t=Linux%20utils%20that%20you%20might%20not%20know&s_o=default#)

[![Avatar](../_resources/fd40c94ac783856a5ad73949a9e1dbd5.jpg)](https://disqus.com/by/blubberdiblub/)

[Niels Böhm](https://disqus.com/by/blubberdiblub/)•[7 hours ago](http://shiroyasha.io/coreutils-that-you-might-not-know.html#comment-3318218609)

You might think that `factor` could be the odd one here that nobody applies to real world problems, but that's not true for me. I find myself making use of it time and time again. Partition sizes are my favorite, but I've also tested for primality with it and found number pairs that have few common divisors. It's quicker at hand than most programming languages' version of it, if they even have it.

The ones I didn't know about are `column` and `numfmt`.

-

    - [−](https://disqus.com/embed/comments/?base=default&f=shiroyashablog&t_i=ae4cc0c4-0e9d-4d23-a51b-59ee3681bfa8&t_u=http%3A%2F%2Fshiroyasha.io%2F%2Fcoreutils-that-you-might-not-know.html&t_d=Linux%20utils%20that%20you%20might%20not%20know&t_t=Linux%20utils%20that%20you%20might%20not%20know&s_o=default#)
    - [*⚑*](https://disqus.com/embed/comments/?base=default&f=shiroyashablog&t_i=ae4cc0c4-0e9d-4d23-a51b-59ee3681bfa8&t_u=http%3A%2F%2Fshiroyasha.io%2F%2Fcoreutils-that-you-might-not-know.html&t_d=Linux%20utils%20that%20you%20might%20not%20know&t_t=Linux%20utils%20that%20you%20might%20not%20know&s_o=default#)

[![Avatar](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/disqus_ebG4EvlRNp/)

[Robert Jennings](https://disqus.com/by/disqus_ebG4EvlRNp/)•[11 hours ago](http://shiroyasha.io/coreutils-that-you-might-not-know.html#comment-3318010558)

Adding the '-u' flag to shred will give you a behavior closer to 'rm', otherwise the file remains but it's filled with random bits.

## Also on **Shiroyasha Blog**

- [ ### Interfaces in Ruby - Shiroyasha       - 5 comments•      - 4 months ago•](http://disq.us/url?url=http%3A%2F%2Fshiroyasha.io%2F%2Finterfaces-in-ruby.html%3Ad07hfiXxKPDHBJ6D3oDr7cb-nn0&imp=51aslri1c8j6hp&prev_imp&forum_id=2964258&forum=shiroyashablog&thread_id=5835846578&thread=5464966642&zone=thread&area=bottom&object_type=thread&object_id=5464966642)[Matthew Berg— It seems ironic to complain about the verbosity of java, then suggest:shared_examples "a …](http://disq.us/url?url=http%3A%2F%2Fshiroyasha.io%2F%2Finterfaces-in-ruby.html%3Ad07hfiXxKPDHBJ6D3oDr7cb-nn0&imp=51aslri1c8j6hp&prev_imp&forum_id=2964258&forum=shiroyashablog&thread_id=5835846578&thread=5464966642&zone=thread&area=bottom&object_type=thread&object_id=5464966642)
- [ ### Sleak and Pretty Tmux       - 3 comments•      - 5 months ago•](http://disq.us/url?url=http%3A%2F%2Fshiroyasha.io%2F%2Fsleak-and-pretty-tmux.html%3AeH3QSZJKjOs6kFq78Dsg4azX5Ps&imp=51aslri1c8j6hp&prev_imp&forum_id=2964258&forum=shiroyashablog&thread_id=5835846578&thread=5389652624&zone=thread&area=bottom&object_type=thread&object_id=5389652624)[Andrey Morskov— By the way, an alternative for the esc key is CTRL+[ combination. It's a standard for …](http://disq.us/url?url=http%3A%2F%2Fshiroyasha.io%2F%2Fsleak-and-pretty-tmux.html%3AeH3QSZJKjOs6kFq78Dsg4azX5Ps&imp=51aslri1c8j6hp&prev_imp&forum_id=2964258&forum=shiroyashablog&thread_id=5835846578&thread=5389652624&zone=thread&area=bottom&object_type=thread&object_id=5389652624)
- [ ### Running shell commands from Ruby       - 1 comment•      - 10 months ago•](http://disq.us/url?url=http%3A%2F%2Fshiroyasha.io%2F%2Frunning-shell-commands-from-ruby.html%3AK4nF0rssDnFG27Frxd-CVLzmGxA&imp=51aslri1c8j6hp&prev_imp&forum_id=2964258&forum=shiroyashablog&thread_id=5835846578&thread=5011191714&zone=thread&area=bottom&object_type=thread&object_id=5011191714)[mangue—Nice!](http://disq.us/url?url=http%3A%2F%2Fshiroyasha.io%2F%2Frunning-shell-commands-from-ruby.html%3AK4nF0rssDnFG27Frxd-CVLzmGxA&imp=51aslri1c8j6hp&prev_imp&forum_id=2964258&forum=shiroyashablog&thread_id=5835846578&thread=5011191714&zone=thread&area=bottom&object_type=thread&object_id=5011191714)
- [ ### From Javascript to Ruby, Part 1.5       - 2 comments•      - 3 years ago•](http://disq.us/url?url=http%3A%2F%2Fshiroyasha.github.io%2Fposts%2FFrom-Javascript-to-Ruby--Part-1-5.html%3AY5wQMAiHSwYaFmsBbJA6sObeQ10&imp=51aslri1c8j6hp&prev_imp&forum_id=2964258&forum=shiroyashablog&thread_id=5835846578&thread=2621973460&zone=thread&area=bottom&object_type=thread&object_id=2621973460)[Igor Sarcevic— I can, but then I will have two different ways to call methods and blocks. Or I could implement …](http://disq.us/url?url=http%3A%2F%2Fshiroyasha.github.io%2Fposts%2FFrom-Javascript-to-Ruby--Part-1-5.html%3AY5wQMAiHSwYaFmsBbJA6sObeQ10&imp=51aslri1c8j6hp&prev_imp&forum_id=2964258&forum=shiroyashablog&thread_id=5835846578&thread=2621973460&zone=thread&area=bottom&object_type=thread&object_id=2621973460)
- [Powered by Disqus](https://disqus.com/)
- [*✉*Subscribe*✔*](https://disqus.com/embed/comments/?base=default&f=shiroyashablog&t_i=ae4cc0c4-0e9d-4d23-a51b-59ee3681bfa8&t_u=http%3A%2F%2Fshiroyasha.io%2F%2Fcoreutils-that-you-might-not-know.html&t_d=Linux%20utils%20that%20you%20might%20not%20know&t_t=Linux%20utils%20that%20you%20might%20not%20know&s_o=default#)
- [*d*Add Disqus to your site](https://publishers.disqus.com/engage?utm_source=shiroyashablog&utm_medium=Disqus-Footer)
- [*🔒*Privacy](https://help.disqus.com/customer/portal/articles/1657951?utm_source=disqus&utm_medium=embed-footer&utm_content=privacy-btn)

![getuid.png](../_resources/6d22e4f2d2057c6e8d6fab098e76e80f.gif)![449266.gif](../_resources/6d22e4f2d2057c6e8d6fab098e76e80f.gif)![px.gif](../_resources/11f8df5c41a5b8b1f9edd97a1b3337ec.gif)![noavatar92.7b2fde640943965cc88df0cdee365907.png](../_resources/9606fa62df0ffe87253f3baf418f0e42.png)