Robin Hood Hashing should be your default Hash Table implementation

Robin Hood Hashing should be your default Hash Table implementation
![](../_resources/47597dc9a11d541d85efb398f527bd7f.png)

![](../_resources/50df0e6f20f7f000c7f99fc5c4f9dbd0.png)https://www.sebastiansylvan.com/post/robin-hood-hashing-should-be-your-default-hash-table-implementation/

Robin Hood Hashing should be your default Hash Table implementation 8 / May 2013 There’s a neat variation on open-addressing based hash tables called Robin Hood hashing . This technique isn’t very well-known, but it makes a huge practical difference because it both improves performance and space utilization compared to other “standard” hash tables (e.g. chaining ). It also eliminates the major downside of other open addressing hash tables. Here are the benefits, summarized: High load factors can be used without seriously affecting performance. 0.9 is perfectly reasonable as a default (0.95 or higher works too, it mainly affects insertion cost a bit).