Some less known features of Google Cloud Storage

## [Some less known features of Google Cloud Storage](https://www.the-swamp.info/blog/some-less-known-features-google-cloud-storage/)

- ** Aug. 31, 2017
- **  [English](https://www.the-swamp.info/tag/English/)  [Google Cloud Platform](https://www.the-swamp.info/tag/Google%20Cloud%20Platform/)  [Google Cloud Storage](https://www.the-swamp.info/tag/Google%20Cloud%20Storage/)

When somebody tells you Google Cloud Storage, probably first thing that comes to your mind is bucket, blob, Nearline, Coldline, you can set ACL for buckets and objects in there... but lets have a look at some cool features which are not so often mentioned. All code examples are in this [github repository](https://github.com/zdenulo/gcs_features).

## Transcoding

Transcoding is feature that allows you to upload files compressed in gzip but when accessed, they are sent uncompressed. Practical use case: save $$$ by paying for compressed storage, not full size files and reduced transfered data.

To make this work, you need to upload file as gzip compressed and set **Content-Encoding** of the file in Storage to be **gzip**. That's all. Good practice is to set also **Content-Type** accordingly.

So now when you request compressed file from Storage, it will be automatically uncompressed as response.

Lets see how can this be done in Python using client library for [Google Cloud Storage](https://google-cloud-python.readthedocs.io/en/latest/storage/client.html).

[?](https://www.the-swamp.info/blog/some-less-known-features-google-cloud-storage/#)

1
2
3
4
5
6
7
8

[object Object]  [object Object][object Object]  [object Object]
[object Object][object Object]  [object Object]
[object Object][object Object]  [object Object]
[object Object][object Object]  [object Object]

[object Object][object Object]  [object Object][object Object][object Object]  [object Object]  [object Object][object Object]

[object Object][object Object]  [object Object]
[object Object][object Object][object Object][object Object]
[object Object][object Object]

I am using Service Account created in **IAM & Admin** with Role **Storage Admin** to access Cloud Storage with client library. As I mentioned before, be need to set explicitly Content Encoding. I am making it also public.

Now when I use wget to download file from public url, whole content of file (uncompressed) is downloaded:

wget <public url>

It's interesting that requests library is downloading file compressed and uncompress it afterwards. So since Python library for Storage also uses requests, this method first downloads file as compressed and then it uncompress.

blob.download_to_filename('downloaded.txt')

to download file as compressed, you need to set headers Accept-Encoding: gzip. With wget for example:

wget --header="Accept-Encoding: gzip" <public url>

Browsers usually sent such headers so files are downloaded as compressed and are then uncompressed which is another good example of this case, i.e. serving static files.

Of course compressing / decompressing makes sense for files which are well compressed, like text files. Images, binary files not much, so keep that in mind. Everything depends from case to case.

Detailed description can be found here https://cloud.google.com/storage/docs/transcoding

## Object Lifecycle Management

or in plain English "Do something with object in bucket based on date and time". Use case for this: archiving, deleting objects or object versions, moving to another storage class. Rules of actions on objects are defined per bucket. Currently two actions are supported:

1. Delete (object or some object's version)
2. SetStorageClass (change Storage type: Coldline, Nearline)
Conditions for actions are:

- Age (of object)
- CreatedBefore (based on UTC date time)
- NumberOfNewerVersions (relates to versioned objects and number of versions it has)
- IsLive (relates to versioned objects, IsLive is well live object and not live is archived :))
- MatchesStorageCLass (when object in bucket has specific storage class set (storage type)

Example to set lifecycle rules with Python library is following:

[?](https://www.the-swamp.info/blog/some-less-known-features-google-cloud-storage/#)

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
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30

[object Object]  [object Object][object Object]  [object Object]
[object Object]  [object Object][object Object]  [object Object]

[object Object][object Object]  [object Object]
[object Object][object Object]  [object Object]

[object Object][object Object]  [object Object]
[object Object][object Object]
[object Object][object Object][object Object]
[object Object][object Object][object Object][object Object][object Object]
[object Object][object Object][object Object][object Object]
[object Object][object Object]
[object Object][object Object][object Object]
[object Object][object Object][object Object][object Object]
[object Object][object Object]
[object Object][object Object]

[object Object][object Object]
[object Object][object Object][object Object]
[object Object][object Object][object Object][object Object]
[object Object][object Object]
[object Object][object Object][object Object]

[object Object][object Object][object Object][object Object][object Object][object Object][object Object]

[object Object][object Object][object Object][object Object][object Object]
[object Object][object Object]
[object Object][object Object]
[object Object]

[object Object][object Object]  [object Object]
[object Object]

Set rules for bucket in example means following:

1. When object is older than 365 days (1 year) it's storage class is set to Coldline (i.e. hope I won't need it anymore or in case of Armaggeddon happens)

2. After 10 years delete it in case it's in Coldline

This feature is like suited for backups and similar stuff. Action doesn't take immediately after condition is reached (all conditions for object need to be reached for action to be executed) but asynchronously with some time lag. More info in this link: https://cloud.google.com/storage/docs/lifecycle

## Object Versioning

Cloud Storage can keep versions of the same file. Versioning needs to be enabled on bucket level. When versioning is enabled and file under the same name is uploaded, version (or in terms of GCS - generation) is created. As usually, best is explained on example.

[?](https://www.the-swamp.info/blog/some-less-known-features-google-cloud-storage/#)

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
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47

[object Object]  [object Object][object Object]  [object Object]
[object Object]  [object Object][object Object]  [object Object]
[object Object]  [object Object][object Object]  [object Object]
[object Object]  [object Object][object Object]  [object Object]
[object Object]  [object Object][object Object]  [object Object]

[object Object][object Object]  [object Object]

[object Object][object Object]  [object Object]
[object Object][object Object]  [object Object][object Object][object Object]
[object Object][object Object]  [object Object]

[object Object][object Object]  [object Object]

[object Object]
[object Object][object Object]  [object Object]

[object Object]
[object Object]
[object Object][object Object]  [object Object]
[object Object]

[object Object]
[object Object][object Object]  [object Object]

[object Object][object Object][object Object][object Object][object Object][object Object]

[object Object][object Object][object Object][object Object][object Object][object Object]

[object Object][object Object][object Object][object Object][object Object][object Object]

[object Object]

[object Object][object Object]  [object Object][object Object][object Object][object Object][object Object][object Object][object Object][object Object]

[object Object]
[object Object][object Object]  [object Object]
[object Object][object Object]  [object Object]
[object Object][object Object]  [object Object][object Object][object Object]
[object Object]
[object Object]

[object Object][object Object]  [object Object][object Object][object Object][object Object][object Object]

[object Object][object Object]  [object Object][object Object][object Object][object Object][object Object][object Object]

[object Object][object Object]  [object Object]
[object Object]

[object Object][object Object]  [object Object]
[object Object]

[object Object][object Object][object Object][object Object]

Output of the program is:
[{'bucket': 'adventures-on-gcp',
'contentType': 'text/plain',
'crc32c': 'ZTopYw==',
'etag': 'CL/os/GogtYCEAE=',
'generation': '1504211601519679',
'id': 'adventures-on-gcp/test_versioned_file.txt/1504211601519679',
'kind': 'storage#object',
'md5Hash': '6eI3FXDa7C57cPqk8PHquA==',

'mediaLink': 'https://www.googleapis.com/download/storage/v1/b/adventures-on-gcp/o/test_versioned_file.txt?generation=1504211601519679&alt=media',

'metageneration': '1',
'name': 'test_versioned_file.txt',

'selfLink': 'https://www.googleapis.com/storage/v1/b/adventures-on-gcp/o/test_versioned_file.txt',

'size': '13',
'storageClass': 'STANDARD',
'timeCreated': '2017-08-31T20:33:21.440Z',
'timeDeleted': '2017-08-31T20:33:21.894Z',
'timeStorageClassUpdated': '2017-08-31T20:33:21.440Z',
'updated': '2017-08-31T20:33:21.440Z'},
{'bucket': 'adventures-on-gcp',
'contentType': 'text/plain',
'crc32c': 'M11WNQ==',
'etag': 'CO7YyvGogtYCEAE=',
'generation': '1504211601894510',
'id': 'adventures-on-gcp/test_versioned_file.txt/1504211601894510',
'kind': 'storage#object',
'md5Hash': '8IS+N+2E6dDSoC1NS+WXRQ==',

'mediaLink': 'https://www.googleapis.com/download/storage/v1/b/adventures-on-gcp/o/test_versioned_file.txt?generation=1504211601894510&alt=media',

'metageneration': '1',
'name': 'test_versioned_file.txt',

'selfLink': 'https://www.googleapis.com/storage/v1/b/adventures-on-gcp/o/test_versioned_file.txt',

'size': '14',
'storageClass': 'STANDARD',
'timeCreated': '2017-08-31T20:33:21.820Z',
'timeDeleted': '2017-08-31T20:33:22.355Z',
'timeStorageClassUpdated': '2017-08-31T20:33:21.820Z',
'updated': '2017-08-31T20:33:21.820Z'},
{'bucket': 'adventures-on-gcp',
'contentType': 'text/plain',
'crc32c': 'xXXOtw==',
'etag': 'CKns5vGogtYCEAE=',
'generation': '1504211602355753',
'id': 'adventures-on-gcp/test_versioned_file.txt/1504211602355753',
'kind': 'storage#object',
'md5Hash': 'gE7JlW9qdJW8bWNO4NE6hw==',

'mediaLink': 'https://www.googleapis.com/download/storage/v1/b/adventures-on-gcp/o/test_versioned_file.txt?generation=1504211602355753&alt=media',

'metageneration': '1',
'name': 'test_versioned_file.txt',

'selfLink': 'https://www.googleapis.com/storage/v1/b/adventures-on-gcp/o/test_versioned_file.txt',

'size': '13',
'storageClass': 'STANDARD',
'timeCreated': '2017-08-31T20:33:22.295Z',
'timeStorageClassUpdated': '2017-08-31T20:33:22.295Z',
'updated': '2017-08-31T20:33:22.295Z'}]
'first version'
'third version'
current content b'third version'

Briefly to explain the code: First I am updating bucket so that it has enabled versioning then I am creating blob and I am uploading 3 times different content. Since currently Python's library for Cloud Storage doesn't support versioning I am doing with "raw" REST requests, using credentials from service account file. Then I am making request to list all files in bucket. I am using prefix field as filter to get only versions for related file and I am priting info about objects. In case I didn't miss something, currently there is no endpoint to get straigh all versions for object. I get url of first and latest version of the file from 'mediaLink' field and I download them and print them. At last I download via client library current version of file which is the same as downloaded latest.

Practical use is obvious. Whenever you need to keep versions of the same file and make them available, this is built in solution. There are some gotchas still so better read more detailed info https://cloud.google.com/storage/docs/object-versioning

- [0 comments]()
- [**The Swamp**](https://disqus.com/home/forums/theswampx/)
- [Marc Cohen](https://disqus.com/embed/comments/?base=default&f=theswampx&t_i=page_58&t_u=https%3A%2F%2Fwww.the-swamp.info%2Fblog%2Fsome-less-known-features-google-cloud-storage%2F&t_e=Some%20less%20known%20features%20of%20Google%20Cloud%20Storage&t_d=Some%20less%20known%20features%20of%20Google%20Cloud%20Storage&t_t=Some%20less%20known%20features%20of%20Google%20Cloud%20Storage&s_o=default&d_m=0#)
- [](https://disqus.com/home/inbox/)
- [ Recommend](https://disqus.com/embed/comments/?base=default&f=theswampx&t_i=page_58&t_u=https%3A%2F%2Fwww.the-swamp.info%2Fblog%2Fsome-less-known-features-google-cloud-storage%2F&t_e=Some%20less%20known%20features%20of%20Google%20Cloud%20Storage&t_d=Some%20less%20known%20features%20of%20Google%20Cloud%20Storage&t_t=Some%20less%20known%20features%20of%20Google%20Cloud%20Storage&s_o=default&d_m=0#)
- tTweetfShare
- [Sort by Newest](https://disqus.com/embed/comments/?base=default&f=theswampx&t_i=page_58&t_u=https%3A%2F%2Fwww.the-swamp.info%2Fblog%2Fsome-less-known-features-google-cloud-storage%2F&t_e=Some%20less%20known%20features%20of%20Google%20Cloud%20Storage&t_d=Some%20less%20known%20features%20of%20Google%20Cloud%20Storage&t_t=Some%20less%20known%20features%20of%20Google%20Cloud%20Storage&s_o=default&d_m=0#)

[![noavatar92.png](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/disqus_Q5LZbDr3pW/)

Start the discussion…

![link.5ef9a39f22ce49f926e304567b9d611b.png](../_resources/934680108867ffa7d395fdd4bbd0355f.png)

![spoiler.eff5de8f72591c5ceeb4fa26a117c6d1.png](../_resources/96b84d4f8860873e832b36e36e2d5731.png)

![italic.a6e1da4a89899ae5e87db9ded9f84d5b.png](../_resources/ff5312def55b6769d146cc61b15420a4.png)

![attach.03c320b14aa9c071da30c904d0a0827f.png](../_resources/1593ac148112cfe84e726f315a476b6a.png)

![blockquote.69435f6faa8c7a193456c46bcb7fb1ed.png](../_resources/b941b52a67553a95c2d82654c9c21a0a.png)

![strikethrough.ced68e63961c6bc0e072ce907906b252.png](../_resources/7b3857fd068ccbd0ee35c328563b15a0.png)

![code.8f558a246aa4e9c41ef343f72f012f01.png](../_resources/b7299ccc866f016305a105091cf0ae02.png)

![underline.59f82f5f5bbed90fd72132ef98662fe3.png](../_resources/8238cb2c15a34beae1c286f5a33a73a1.png)

[![bold.cb366e6a49396fb0e47a01df277563c8.png](../_resources/d02baddf90be3d2eaf06525081255899.png)](https://disqus.com/embed/comments/?base=default&f=theswampx&t_i=page_58&t_u=https%3A%2F%2Fwww.the-swamp.info%2Fblog%2Fsome-less-known-features-google-cloud-storage%2F&t_e=Some%20less%20known%20features%20of%20Google%20Cloud%20Storage&t_d=Some%20less%20known%20features%20of%20Google%20Cloud%20Storage&t_t=Some%20less%20known%20features%20of%20Google%20Cloud%20Storage&s_o=default&d_m=0#)

![gif-picker.df38180f2d048c25fe42a2b440ff863e.png](../_resources/5f5ec942ed95355419b673488da13811.png)

Be the first to comment.

## Also on **The Swamp**

- [

### Upload data to Cloud Datastore using Dataflow

    - 8 comments •

    - 9 months ago

[Micha—How does it even run since you don't have `p.run()`?](https://disq.us/?url=https%3A%2F%2Fwww.the-swamp.info%2Fblog%2Fupload-data-cloud-datastore-using-dataflow%2F&key=aqYYtjabWAzsy1T3ToNObg)](https://disq.us/?url=https%3A%2F%2Fwww.the-swamp.info%2Fblog%2Fupload-data-cloud-datastore-using-dataflow%2F&key=aqYYtjabWAzsy1T3ToNObg)

- [

### MOOC Udacity course review: Developing Scalable Apps in Python

    - 2 comments •

    - 4 years ago

[zdenulo— Thanks for sharing your story. I am not aware of any other tutorial/resources regarding Google Cloud Endpoints and …](http://disq.us/?url=http%3A%2F%2Fwww.the-swamp.info%2Fblog%2Fmooc-udacity-course-review-developing-scalable-apps-python%2F&key=JVBRGeEl10ynw-FEk2csDw)](http://disq.us/?url=http%3A%2F%2Fwww.the-swamp.info%2Fblog%2Fmooc-udacity-course-review-developing-scalable-apps-python%2F&key=JVBRGeEl10ynw-FEk2csDw)

- [

### Setting WordPress on Google Cloud Platform

    - 2 comments •

    - 10 months ago

[zdenulo—thanks for input](https://disq.us/?url=https%3A%2F%2Fwww.the-swamp.info%2Fblog%2Fsetting-wordpress-google-cloud-platform%2F&key=xZc8rntrTfa-uyvbF2mwVA)](https://disq.us/?url=https%3A%2F%2Fwww.the-swamp.info%2Fblog%2Fsetting-wordpress-google-cloud-platform%2F&key=xZc8rntrTfa-uyvbF2mwVA)

- [

### Android Studio Problem

    - 6 comments •

    - 5 years ago

[harshvardhan goyal—ok,thank you](http://disq.us/?url=http%3A%2F%2Fwww.the-swamp.info%2Fblog%2Fandroid-studio-problem%2F&key=y4iaR--DsJ-9D8g_WsWi8w)](http://disq.us/?url=http%3A%2F%2Fwww.the-swamp.info%2Fblog%2Fandroid-studio-problem%2F&key=y4iaR--DsJ-9D8g_WsWi8w)

- [Powered by Disqus](https://disqus.com/)
- [*✉*Subscribe*✔*](https://disqus.com/embed/comments/?base=default&f=theswampx&t_i=page_58&t_u=https%3A%2F%2Fwww.the-swamp.info%2Fblog%2Fsome-less-known-features-google-cloud-storage%2F&t_e=Some%20less%20known%20features%20of%20Google%20Cloud%20Storage&t_d=Some%20less%20known%20features%20of%20Google%20Cloud%20Storage&t_t=Some%20less%20known%20features%20of%20Google%20Cloud%20Storage&s_o=default&d_m=0#)
- [*d*Add Disqus to your site](https://publishers.disqus.com/engage?utm_source=theswampx&utm_medium=Disqus-Footer)
- [**Disqus' Privacy Policy](https://help.disqus.com/customer/portal/articles/466259-privacy-policy)