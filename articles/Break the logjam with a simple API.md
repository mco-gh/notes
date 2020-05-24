Break the logjam with a simple API

[**](http://scripting.com/2017/01/05/weStillNeedANetflixForNews.html)
[**](http://scripting.com/2017/01/05/mediumsPivot.html)

Break the logjam with a simple API

Some say to get independence from silos, users have to run servers, but that's not true. A small new connection can break the logjam.

by Dave Winer[@davewiner](http://twitter.com/davewiner)Jan 5

It just takes one storage service to decide to bridge the gap and a wonderful era of innovation can begin.

#### Background

Some people assume that for a user to be independent of silos, they would need to run a server. This is not true. With a tiny connection between JavaScript running in the browser and a cloud-based storage service, we can do anything a server can do without the server, entirely in the browser.

This isn't a question. In 2016, the technology is mature, we know how it works.

#### How to

Here's a sketch of how the service would work.

1. Start with a user-facing service like Dropbox, Google Drive, Amazon Cloud Drive.

2. Add an API that allows a JavaScript app running in the browser to write into a folder in a user's space. The user grants access via oAuth, as they do with Twitter, Facebook, etc.

3. Connect to a registrar to allow a user to associate a domain name with a folder. Or map a domain they register elsewhere. A revenue opportunity.

That's it. Now I can hook my JS-in-the-browser app to your service. The user manages it through the UI you already support. And we've opened up a new area for developers to be creative. And most important, it says the exploration of great writing tools can advance outside of Medium. (That's how important Medium has been for the last few years.)

BTW, for Amazon, they would use the S3 API, which is supported everywhere. The apps would pop up very quickly for their service.

It's a total logjam and could be broken by one storage service deciding to help the users break free of silos.

© copyright 1994-2017 Dave Winer.
Created: Thu, Jan 5, 2017 at 3:56 PM.
Updated: Fri, Jan 6, 2017 at 4:35 PM.
Greetings, citizen of Planet Earth. We are your overlords. :-)

[**](http://twitter.com/davewiner)[**](http://facebook.com/dave.winer.12)[**](http://github.com/scripting)[**](http://www.linkedin.com/in/scripting)[**](http://scripting.com/rss.xml)