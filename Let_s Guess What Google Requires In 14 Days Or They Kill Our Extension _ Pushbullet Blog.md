Let's Guess What Google Requires In 14 Days Or They Kill Our Extension | Pushbullet Blog

## Let's Guess What Google Requires In 14 Days Or They Kill Our Extension

 Published on May 13, 2020

[**Tweet](https://twitter.com/intent/tweet?original_referer=https%3A%2F%2Fblog.pushbullet.com%2F2020%2F05%2F13%2Flets-guess-what-google-requires-in-14-days-or-they-kill-our-extension%2F&ref_src=twsrc%5Etfw&text=Let%27s%20guess%20what%20Google%20requires%20in%2014%20days%20or%20they%20kill%20our%20extension&tw_p=tweetbutton&url=https%3A%2F%2Fblog.pushbullet.com%2F2020%2F05%2F13%2Flets-guess-what-google-requires-in-14-days-or-they-kill-our-extension&via=pushbullet)

**We at Pushbullet have received some bad news from Google. It appears our extension will be removed from the Chrome Web Store if we don’t make required changes within 14 days. Not good! The bigger problem? Google hasn’t told us what those required changes are.**

[Here’s the full text of the email if you’d like to read it for yourself.](https://gist.github.com/guzba/7a971459f2f6dd8a208d57c5b2e2bfb2)

The Pushbullet Chrome extension has been on the Chrome Web store for over 6 years, currently has over 1,000,000 users, and has a 4.5 star average rating. [See for yourself here.](https://chrome.google.com/webstore/detail/pushbullet/chlffgpmiacpedhhbkiomidkjlcfhogd) We are very proud of this. In addition to the large number of users and excellent rating, our extension is also frequently featured by Chrome Web Store team which we really appreciate! [Here’s us in the Work From Home collection.](https://chrome.google.com/webstore/category/collection/workfromhome)

Considering all of the work we’ve done over the years to make an exceptional Chrome extension that this worthy of being featured by the Chrome Web Store team, it was shocking to read we are less than 14 days away from being removed from the Web Store.

The Pushbullet extension is our most-installed app for desktop. It being removed may very well be the end of Pushbullet altogether. This is a big deal for us.

**14 days and counting. What do we have to go on to guess the required changes to not get kicked off the Chrome Web Store?**

Fortunately, Google has given us a hint of what changes we need to make. Here’s what the email said:

Your item did not comply with the following section of our Program Policies:
"User Data Privacy"

Your product violates the "Use of Permissions" section of the policy, which requires that you:

- Request access to the narrowest permissions necessary to implement your product’s features or services.
- If more than one permission could be used to implement a feature, you must request those with the least access to data or functionality.
- Don't attempt to "future proof" your product by requesting a permission that might benefit services or features that have not yet been implemented.

**We appear to violate the “Use of Permissions” section of the Chrome Web Store policy. That’s not good!**

Based on my interpretation of bullet points listed, I believe Google wants us to find ways to reduce the permissions our extension requests. Ok, fair enough. I’ll accept that challenge. It’s not clear what permissions Google wants us to remove (or how many, or anything like that) but lets make a good-faith effort to reduce the permissions our extension requests!

**What permissions does our extension request?**

Our extension requires these permissions: **tabs**, **activeTab**, **contextMenu**, **cookies**, **notifications**, **idle**, **https://*/***, and **http://*/***. We also optionally request these permissions if a user wants to enable certain features: **background**, **clipboardRead**, **clipboardWrite**.

**So, can we cut any of these permissions?**

First, let’s start off by prioritizing. I believe the Chrome team are most concerned with the required permissions (these are all granted at install). Optional permissions are requested later and must be manually granted by the user. Since the optional permissions are specifically approved by a user, they seem pretty tame. Let’s focus on reducing the required permissions!

As I looked at the permissions and what our extension actually needs to operate, I noticed a great opportunity to reduce our permissions requests. We do not need to request access to data on **https://*/*** and **http://*/***. Instead, we can simply request data access for **https://*.pushbullet.com/***, **http://*.pushbullet.com/***, and **http://localhost/***. This is a huge reduction in the private data our extension could theoretically access. A big win!

The other opportunity is the **tabs** permission. This permission lets extensions see what tabs are open. Pushbullet uses this permission to avoid opening new tabs for websites that are already open when [mirrored notifications](https://blog.pushbullet.com/2013/11/12/real-time-notification-mirroring-from-android-to-your-computer/) are clicked. This is a small sacrifice to make to let go of a big permission. Let’s let it go!

**What permissions are required now?**

Our extension will now only require: **activeTab**, **contextMenu**, **cookies**, **notifications**, **idle**, **https://*.pushbullet.com/***, **http://*.pushbullet.com/***, and **http://localhost/***.

This is a huge reduction in the level of access Pushbullet requires to operate! A big success. Let’s get it submitted to the Chrome Web Store!

**Submitted and rejected.**

Around 24 hours after submitting the updated extension, it was rejected. Unfortunately, it appears the changes we’ve made are not the changes Google requires.

Google has provided no further guidance on what changes they require. The reason for rejection was exactly the same as our original notice. I also replied to the email asking for further guidance but have not received any response. I obviously don’t expect one but it was no harm to try.

**7 days left now. Where do we go from here?**

I’ve tried coming up with a few theories of other changes we could make to potentially get past whatever is blocking our extension. Here are my current theories:

- Change the **http(s)://*.pushbullet.com/*** data permissions to **http(s)://www.pushbullet.com**. This shouldn’t really matter since it is our own first-party domain after all, but perhaps reducing the scope would help?

- Remove the clipboardRead and clipboardWrite permissions. These permissions are optional and only requested if a user enables [Universal copy & paste](https://blog.pushbullet.com/2014/08/20/introducing-universal-copy-and-paste/). However, perhaps Chrome is unwilling to allow extensions to request these permissions now? [Google did kill clipboard managers on Android recently after all.](https://www.androidpolice.com/2019/03/14/android-q-will-kill-clipboard-manager-apps-in-the-name-of-privacy/) This will mean removing the feature from our extension.

**Why not just keep trying submissions with changes that might help until it passes review?**

I think I don’t have any choice to do this, but it isn’t without risk. I fear Google’s automated system will think I am trying to find a way around the rules and permaban my entire Google account. Their policy does specifically state: **This may also result in the suspension of related Google services associated with your Google account.**

**Giving it another try, stay tuned for updates.**

Later today I am going to give another submission a try with the 2 changes I listed above. Follow our blog and [@pushbullet](http://twitter.com/pushbullet) for updates!

**What do you think of all of this?**

I’m eager to hear what people think so far. Am I missing something obvious? Do you have a good suggestion I may not have thought of? Do you have a friend that works on Chrome? Please share! [I have made a post on the Pushbullet subreddit for us to discuss this here.](https://www.reddit.com/r/PushBullet/comments/gj2dio/lets_guess_what_google_requires_in_14_days_or/)