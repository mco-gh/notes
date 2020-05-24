Making It a Series · npf.io

# Making It a Series

 Aug 8, 2014
Series: [Hugo 101](https://npf.io/series/hugo-101)

I obviously have a lot to talk about with Hugo, so I decided I wanted to make this into a series of posts, and have links at the bottom of each post automatically populated with the other posts in the series. This turned out to be somewhat of a challenge, but doable with some effort… hopefully someone else can learn from my work.

This now brings us to [Taxonomies](http://hugo.spf13.com/taxonomies/overview). Taxonomies are basically just like tags, except that you can have any number of different types of tags. So you might have “Tags” as a taxonomy, and thus you can give a content tags with values of “go” and “programming”. You can also have a taxonomy of “series” and give content a series of “Hugo 101”.

Taxonomy is sort of like relatable metadata to gather multiple pieces of content together in a structured way… it’s almost like a minimal relational database. Taxonomies are listed in your site’s metadata, and consist of a list of keys. Each piece of content can specify one or more values for those keys (the Hugo documentation calls the values “Terms”). The values are completely ad-hoc, and don’t need to be pre-defined anywhere. Hugo automatically creates pages where you can view all content based on Taxonomies and see how the various values are cross-referenced against other content. This is a way to implement tags on posts, or series of posts.

So, for my example, we add a Taxonomy to my site config called “series”. Then in this post, the “Hugo: Beyond the Defaults” post, and the “Hugo is Friggin’ Awesome” post, I just add `series = ["Hugo 101"]` (note the brackets - the values for the taxonomy are actually a list, even if you only have one value). Now all these posts are magically related together under a taxonomy called “series”. And Hugo automatically generates a listing for this taxonomy value at [/series/hugo-101](http://npf.io/series/hugo-101) (the taxonomy value gets url-ized). Any other series I make will be under a similar directory.

This is fine and dandy and pretty aweomse out of the box… but I really want to automatically generate a list of posts in the series at the bottom of each post in the series. This is where things get tricky, but that’s also where things get interesting.

The examples for [displaying Taxonomies](http://hugo.spf13.com/taxonomies/displaying) all “hard code” the taxonomy value in the template… this works great if you know ahead of time what value you want to display, like “all posts with tag = ‘featured’”. However, it doesn’t work if you don’t know ahead of time what the taxonomy value will be (like the series on the current post).

This is doable, but it’s a little more complicated.

I’ll give you a dump of the relevant portion of my post template and then talk about how I got there:

	{{ if .Params.series }}
	    {{ $name := index .Params.series 0 }}
	    <hr/>
		<p><a href="" id="series"></a>This is a post in the
		<b>{{$name}}</b> series.<br/>
		Other posts in this series:</p>

	    {{ $name := $name | urlize }}
	    {{ $series := index .Site.Taxonomies.series $name }}
	    <ul class="series">
	    {{ range $series.Pages }}
	    	<li>{{.Date.Format "Jan 02, 2006"}} -
	    	<a href="{{.Permalink}}">{{.LinkTitle}}</a></li>
	    {{end}}
	    </ul>
	{{end}}

So we start off defining this part of the template to only be used if the post has a series. Right, sure, move on.

Now, the tricky part… the taxonomy values for the current page resides in the .Params values, just like any other custom metadata you assign to the page.

Taxonomy values are always a list (so you can give things multiple tags etc), but I know that I’ll never give something more than one series, so I can just grab the first item from the list. To do that, I use the index function, which is just like calling series[0] and assign it to the $name variable.

Now another tricky part… the series in the metadata is in the pretty form you put into the metadata, but the list of Taxonomies in .Site.Taxonomies is in the urlized form… How did I figure that out? Printf debugging. Hugo’s auto-reloading makes it really easy to use the template itself to figure out what’s going on with the template and the data.

When I started writing this template, I just put `{{$name}}` in my post template after the line where I got the name, and I could see it rendered on webpage of my post that the name was “Hugo 101”. Then I put `{{.Site.Taxonomies.series}}`and I saw something like `map[hugo-101:[{0 0xc20823e000} {0 0xc208048580} {0 0xc208372000}]]` which is ugly, but it showed me that the value in the map is “hugo-101”… and I realized it was using the urlized version, so I used the pre-defined hugo function `urlize` to convert the pretty series.

And from there it’s just a matter of using `index` again, this time to use`$name` as a key in the map of series…. .Site.Taxonomies is a map (dictionary) of Taxonomy names (like “series”) to maps of Taxonomy values (like “hugo-101”) to lists of pages. So, .Site.Taxonomies.series reutrns a map of series names to lists of pages… index that by the current series names, and bam, list of pages.

And then it’s just a matter of iterating over the pages and displaying them nicely. And what’s great is that this is now all automatic… all old posts get updated with links to the new posts in the series, and any new series I make, regardless of the name, will get the nice list of posts at the bottom for that series.

* * *

[(L)](https://npf.io/2014/08/making-it-a-series/)This is a post in the **Hugo 101** series.

Other posts in this series:

- Aug 08, 2014 - Making It a Series

- Aug 08, 2014 - [Hugo: Beyond the Defaults](https://npf.io/2014/08/hugo-beyond-the-defaults/)

- Aug 01, 2014 - [Hugo Is Friggin' Awesome](https://npf.io/2014/08/hugo-is-awesome/)

- [1 comment]()
- [**npf.io**](https://disqus.com/home/forums/npfio/)
- [Login](https://disqus.com/embed/comments/?base=default&version=1ff775e16a6b5e77f3abb7306025cc42&f=npfio&t_u=https%3A%2F%2Fnpf.io%2F2014%2F08%2Fmaking-it-a-series%2F&t_d=Making%20It%20a%20Series&t_t=Making%20It%20a%20Series&s_o=default#)
- [1](https://disqus.com/home/inbox/)
- [ Recommend](https://disqus.com/embed/comments/?base=default&version=1ff775e16a6b5e77f3abb7306025cc42&f=npfio&t_u=https%3A%2F%2Fnpf.io%2F2014%2F08%2Fmaking-it-a-series%2F&t_d=Making%20It%20a%20Series&t_t=Making%20It%20a%20Series&s_o=default#)
- [⤤Share](https://disqus.com/embed/comments/?base=default&version=1ff775e16a6b5e77f3abb7306025cc42&f=npfio&t_u=https%3A%2F%2Fnpf.io%2F2014%2F08%2Fmaking-it-a-series%2F&t_d=Making%20It%20a%20Series&t_t=Making%20It%20a%20Series&s_o=default#)
- [Sort by Oldest](https://disqus.com/embed/comments/?base=default&version=1ff775e16a6b5e77f3abb7306025cc42&f=npfio&t_u=https%3A%2F%2Fnpf.io%2F2014%2F08%2Fmaking-it-a-series%2F&t_d=Making%20It%20a%20Series&t_t=Making%20It%20a%20Series&s_o=default#)

[Avatar](../_resources/713bb211dca17435d03c079149496a65.webp)
Join the discussion…

- [Attach](https://disqus.com/embed/comments/?base=default&version=1ff775e16a6b5e77f3abb7306025cc42&f=npfio&t_u=https%3A%2F%2Fnpf.io%2F2014%2F08%2Fmaking-it-a-series%2F&t_d=Making%20It%20a%20Series&t_t=Making%20It%20a%20Series&s_o=default#)

-

    - [−](https://disqus.com/embed/comments/?base=default&version=1ff775e16a6b5e77f3abb7306025cc42&f=npfio&t_u=https%3A%2F%2Fnpf.io%2F2014%2F08%2Fmaking-it-a-series%2F&t_d=Making%20It%20a%20Series&t_t=Making%20It%20a%20Series&s_o=default#)
    - [*⚑*](https://disqus.com/embed/comments/?base=default&version=1ff775e16a6b5e77f3abb7306025cc42&f=npfio&t_u=https%3A%2F%2Fnpf.io%2F2014%2F08%2Fmaking-it-a-series%2F&t_d=Making%20It%20a%20Series&t_t=Making%20It%20a%20Series&s_o=default#)

[![Avatar](:/55c46c8bc3802c5c86f03ec198cfef70)](https://disqus.com/by/ericfpalmer/)

[Eric](https://disqus.com/by/ericfpalmer/)•[3 months ago](https://npf.io/2014/08/making-it-a-series/#comment-3071331729)

Nate thanks for this post. This is exactly what I needed. I'm new to hugo and go templates but I figured out where to put the code snippet and I even understand it. Very Cool.

## Also on **npf.io**

- [ ### Intro++ to Go Interfaces       - 2 comments•      - 3 years ago•](http://disq.us/url?url=http%3A%2F%2Fnpf.io%2F2014%2F05%2Fintro-to-go-interfaces%2F%3ADsq9R3Mwi5i9uy9V3e_33-VTSo0&imp=h6i1usr278ej&prev_imp=h6hfnr2ltece1&forum_id=3141942&forum=npfio&thread_id=3898620873&thread=2917953062&zone=thread&area=bottom&object_type=thread&object_id=2917953062)[![Avatar](../_resources/5b65447451544ccb5274079c6c6d6e89.jpg) Janek Píša — Thank you :) now it's clear](http://disq.us/url?url=http%3A%2F%2Fnpf.io%2F2014%2F05%2Fintro-to-go-interfaces%2F%3ADsq9R3Mwi5i9uy9V3e_33-VTSo0&imp=h6i1usr278ej&prev_imp=h6hfnr2ltece1&forum_id=3141942&forum=npfio&thread_id=3898620873&thread=2917953062&zone=thread&area=bottom&object_type=thread&object_id=2917953062)
- [ ### 3.5 Years, 500k Lines of Go (Part 1)       - 14 comments•      - 3 days ago•](http://disq.us/url?url=https%3A%2F%2Fnpf.io%2F2017%2F03%2F3.5yrs-500k-lines-of-go%2F%3AxgyACcDSBvMcBRvp2twtxct7eLU&imp=h6i1usr278ej&prev_imp=h6hfnr2ltece1&forum_id=3141942&forum=npfio&thread_id=3898620873&thread=5660356814&zone=thread&area=bottom&object_type=thread&object_id=5660356814)[![Avatar](../_resources/44e15abdd56fd75c94bd9a119cfe9217.jpg) Stuart Ellis —  "I have a lot of more specific things that I can talk about… about APIs, versioning, the database, refactoring, …](http://disq.us/url?url=https%3A%2F%2Fnpf.io%2F2017%2F03%2F3.5yrs-500k-lines-of-go%2F%3AxgyACcDSBvMcBRvp2twtxct7eLU&imp=h6i1usr278ej&prev_imp=h6hfnr2ltece1&forum_id=3141942&forum=npfio&thread_id=3898620873&thread=5660356814&zone=thread&area=bottom&object_type=thread&object_id=5660356814)
- [ ### Sharing Godoc of a WIP Branch       - 1 comment•      - 2 years ago•](http://disq.us/url?url=https%3A%2F%2Fnpf.io%2F2015%2F06%2Fwip-godoc%2F%3AOyRv8mbYeNx_4_yErzLW9B24GJk&imp=h6i1usr278ej&prev_imp=h6hfnr2ltece1&forum_id=3141942&forum=npfio&thread_id=3898620873&thread=3898620542&zone=thread&area=bottom&object_type=thread&object_id=3898620542)[![Avatar](../_resources/a7c46e17e9326af03b5f11b8e3e8e25b.jpg) bsdlp — perhaps an alternative could be use the `godoc` command to generate html and host it using github pages?](http://disq.us/url?url=https%3A%2F%2Fnpf.io%2F2015%2F06%2Fwip-godoc%2F%3AOyRv8mbYeNx_4_yErzLW9B24GJk&imp=h6i1usr278ej&prev_imp=h6hfnr2ltece1&forum_id=3141942&forum=npfio&thread_id=3898620873&thread=3898620542&zone=thread&area=bottom&object_type=thread&object_id=3898620542)
- [ ### Writing Go Applications with Reusable Logic       - 2 comments•      - 5 months ago•](http://disq.us/url?url=https%3A%2F%2Fnpf.io%2F2016%2F10%2Freusable-commands%2F%3Aa76T3SvRQoVx4gzChsR94r8RAVE&imp=h6i1usr278ej&prev_imp=h6hfnr2ltece1&forum_id=3141942&forum=npfio&thread_id=3898620873&thread=5234483263&zone=thread&area=bottom&object_type=thread&object_id=5234483263)[![Avatar](../_resources/675fb4b91ca717db030507f2d84bcfdf.png) Salah — Makes lots of sense. Thanks Nate.](http://disq.us/url?url=https%3A%2F%2Fnpf.io%2F2016%2F10%2Freusable-commands%2F%3Aa76T3SvRQoVx4gzChsR94r8RAVE&imp=h6i1usr278ej&prev_imp=h6hfnr2ltece1&forum_id=3141942&forum=npfio&thread_id=3898620873&thread=5234483263&zone=thread&area=bottom&object_type=thread&object_id=5234483263)
- [Powered by Disqus](https://disqus.com/)
- [*✉*Subscribe  *✔*](https://disqus.com/embed/comments/?base=default&version=1ff775e16a6b5e77f3abb7306025cc42&f=npfio&t_u=https%3A%2F%2Fnpf.io%2F2014%2F08%2Fmaking-it-a-series%2F&t_d=Making%20It%20a%20Series&t_t=Making%20It%20a%20Series&s_o=default#)
- [*d*Add Disqus to your site](https://publishers.disqus.com/engage?utm_source=npfio&utm_medium=Disqus-Footer)
- [*🔒*Privacy](https://help.disqus.com/customer/portal/articles/1657951?utm_source=disqus&utm_medium=embed-footer&utm_content=privacy-btn)

[noavatar92.7b2fde640943965cc88df0cdee365907.png.webp](../_resources/9b2544524e3361a02d0ce87cf2e3bd36.bin)![pixel.gif](../_resources/9606fa62df0ffe87253f3baf418f0e42.png)![getuid.png](../_resources/14d1707eda790f543c6fb8d0dcff6359.gif)![449266.gif](../_resources/6d22e4f2d2057c6e8d6fab098e76e80f.gif)![449266.gif](../_resources/d89746888da2d9510b64a9f031eaecd5.gif)