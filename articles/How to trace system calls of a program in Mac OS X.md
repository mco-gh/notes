How to trace system calls of a program in Mac OS X

35

I wanted to trace the system calls made by the **find** command [to debug some performance issues](https://stackoverflow.com/questions/31045501/how-to-speed-up-find-for-listing-git-repositories) however I could not figure out how to do this on Mac OS X Yosemite. How can I trace system calls for an arbitrary program similarly to what **strace** does on FreeBSD? I am especially interested in tracing file-system related calls.

 [macos](https://stackoverflow.com/questions/tagged/macos)  [strace](https://stackoverflow.com/questions/tagged/strace)

[share](https://stackoverflow.com/q/31045575)|[improve this question](https://stackoverflow.com/posts/31045575/edit)

 [edited May 23 '17 at 12:17](https://stackoverflow.com/posts/31045575/revisions)

 [![2050bd47e48d2e94f3ae0e5b40286d32](../_resources/e2fae2eebb14fb10194feaec4e4d9d46.png)](https://stackoverflow.com/users/-1/community)

 [Community](https://stackoverflow.com/users/-1/community)♦
 111 silver badge

asked Jun 25 '15 at 8:52

 [![a007be5a61f6aa8f3e85ae2fc18dd66e](../_resources/0c18dafb13830b7d9961bdccaa4a2962.jpg)](https://stackoverflow.com/users/2654678/michael-le-barbier-gr%c3%bcnewald)

 [Michael Le Barbier Grünewald](https://stackoverflow.com/users/2654678/michael-le-barbier-gr%c3%bcnewald)

 4,16333 gold badges2020 silver badges5353 bronze badges

-

 2

 A quick search for ***strace osx*** gave me [this four year old blog post](https://opensourcehacker.com/2011/12/02/osx-strace-equivalent-dtruss-seeing-inside-applications-what-they-do-and-why-they-hang/). It should be easy to find other alternatives using the same search. – [Some programmer dude](https://stackoverflow.com/users/440558/some-programmer-dude)  [Jun 25 '15 at 8:54](https://stackoverflow.com/questions/31045575/how-to-trace-system-calls-of-a-program-in-mac-os-x#comment50113552_31045575)    ![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' aria-hidden='true' class='svg-icon va-text-bottom o50 iconPencilSm js-evernote-checked' width='14' height='14' viewBox='0 0 14 14' data-evernote-id='2000'%3e%3cpath d='M11.1 1.71l1.13 1.12c.2.2.2.51 0 .71L11.1 4.7 9.21 2.86l1.17-1.15c.2-.2.51-.2.71 0zM2 10.12l6.37-6.43 1.88 1.88L3.88 12H2v-1.88z' data-evernote-id='2026' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)

-

 @JoachimPileborg Nice point. I went another way, starting with ***apropos trace*** and searching from that. I overlooked ***dtruss*** and ***dtrace*** because all outcomes I have found were about a trace utility for the ***D*** language. – [Michael Le Barbier Grünewald](https://stackoverflow.com/users/2654678/michael-le-barbier-gr%c3%bcnewald)  [Jun 25 '15 at 9:16](https://stackoverflow.com/questions/31045575/how-to-trace-system-calls-of-a-program-in-mac-os-x#comment50114275_31045575)    ![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' aria-hidden='true' class='svg-icon va-text-bottom o50 iconPencilSm js-evernote-checked' width='14' height='14' viewBox='0 0 14 14' data-evernote-id='2001'%3e%3cpath d='M11.1 1.71l1.13 1.12c.2.2.2.51 0 .71L11.1 4.7 9.21 2.86l1.17-1.15c.2-.2.51-.2.71 0zM2 10.12l6.37-6.43 1.88 1.88L3.88 12H2v-1.88z' data-evernote-id='2027' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)

 [add a comment]()

##  2 Answers

 [active](https://stackoverflow.com/questions/31045575/how-to-trace-system-calls-of-a-program-in-mac-os-x?answertab=active#tab-top)  [oldest](https://stackoverflow.com/questions/31045575/how-to-trace-system-calls-of-a-program-in-mac-os-x?answertab=oldest#tab-top)  [votes](https://stackoverflow.com/questions/31045575/how-to-trace-system-calls-of-a-program-in-mac-os-x?answertab=votes#tab-top)

29

 ![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' aria-hidden='true' class='svg-icon iconCheckmarkLg js-evernote-checked' width='36' height='36' viewBox='0 0 36 36' data-evernote-id='2004'%3e%3cpath d='M6 14l8 8L30 6v8L14 30l-8-8v-8z' data-evernote-id='2030' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)

You can use **dtruss** like in

	sudo dtruss find ~/repo -depth 2 -type d -name '.git'

The [manual page](https://developer.apple.com/library/mac/documentation/Darwin/Reference/ManPages/man1/dtruss.1m.html) of that utility will help you to tailor the use of the tool to your needs.

[share](https://stackoverflow.com/a/31045613)|[improve this answer](https://stackoverflow.com/posts/31045613/edit)

 [edited Jun 25 '15 at 10:31](https://stackoverflow.com/posts/31045613/revisions)

 [![d4ab75d77a9a82e179397fd7964dc36e](../_resources/0c18dafb13830b7d9961bdccaa4a2962.jpg)](https://stackoverflow.com/users/2654678/michael-le-barbier-gr%c3%bcnewald)

 [Michael Le Barbier Grünewald](https://stackoverflow.com/users/2654678/michael-le-barbier-gr%c3%bcnewald)

 4,16333 gold badges2020 silver badges5353 bronze badges

answered Jun 25 '15 at 8:54

 [![097d761861529df52a6800744f1074d2](../_resources/0dec2abb3f5714bea511548a01aa1108.png)](https://stackoverflow.com/users/235354/jspcal)

 [jspcal](https://stackoverflow.com/users/235354/jspcal)
 43.2k44 gold badges5757 silver badges6565 bronze badges

-

 15

 dtruss did work then (June '15) but was broken by the System Integrity Protection regime of El Capitan. – [Olsonist](https://stackoverflow.com/users/4603507/olsonist)  [Feb 25 '17 at 22:09](https://stackoverflow.com/questions/31045575/how-to-trace-system-calls-of-a-program-in-mac-os-x#comment72066471_31045613)

-

 2

 @Olsonist Same issue with dtrace: `the current security restriction (rootless enabled) prevent dtrace from attaching to an executable not signed with the [com.apple.security.get-task-allow] entitlement` – [Nakilon](https://stackoverflow.com/users/322020/nakilon)  [Oct 17 '17 at 2:52](https://stackoverflow.com/questions/31045575/how-to-trace-system-calls-of-a-program-in-mac-os-x#comment80509838_31045613)    ![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' aria-hidden='true' class='svg-icon va-text-bottom o50 iconPencilSm js-evernote-checked' width='14' height='14' viewBox='0 0 14 14' data-evernote-id='2005'%3e%3cpath d='M11.1 1.71l1.13 1.12c.2.2.2.51 0 .71L11.1 4.7 9.21 2.86l1.17-1.15c.2-.2.51-.2.71 0zM2 10.12l6.37-6.43 1.88 1.88L3.88 12H2v-1.88z' data-evernote-id='2031' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)

-

 3

 It is possible to disable SIP [developer.apple.com/library/content/documentation/Security/…](https://developer.apple.com/library/content/documentation/Security/Conceptual/System_Integrity_Protection_Guide/ConfiguringSystemIntegrityProtection/ConfiguringSystemIntegrityProtection.html) – [mttrb](https://stackoverflow.com/users/1320303/mttrb)  [Oct 17 '17 at 2:55](https://stackoverflow.com/questions/31045575/how-to-trace-system-calls-of-a-program-in-mac-os-x#comment80509884_31045613)

-

 1

 Also see [stackoverflow.com/questions/33476432/…](https://stackoverflow.com/questions/33476432/is-there-a-workaround-for-dtrace-cannot-control-executables-signed-with-restri) – [mttrb](https://stackoverflow.com/users/1320303/mttrb)  [Oct 17 '17 at 2:56](https://stackoverflow.com/questions/31045575/how-to-trace-system-calls-of-a-program-in-mac-os-x#comment80509900_31045613)

 [add a comment]()

28

+50

Under current versions of macOS, executables under paths covered by SIP (like `/usr/bin`) cannot be traced.

You can bypass this by making a copy of the executable in your home directory and tracing the copy:

	cp /usr/bin/find find
	sudo dtruss ./find …

[share](https://stackoverflow.com/a/46799054)|[improve this answer](https://stackoverflow.com/posts/46799054/edit)

answered Oct 17 '17 at 20:53

 [(L)](https://stackoverflow.com/users/149341/duskwuff)

 [duskwuff](https://stackoverflow.com/users/149341/duskwuff)
 158k2424 gold badges195195 silver badges247247 bronze badges

-

 In my case after copying of the executable the bug that I wanted to debug stopped happening ..( – [Nakilon](https://stackoverflow.com/users/322020/nakilon)  [Oct 20 '17 at 8:14](https://stackoverflow.com/questions/31045575/how-to-trace-system-calls-of-a-program-in-mac-os-x#comment80637364_46799054)

-

 Probably my bug is really SIP-related so that's a success too. – [Nakilon](https://stackoverflow.com/users/322020/nakilon)  [Oct 21 '17 at 3:13](https://stackoverflow.com/questions/31045575/how-to-trace-system-calls-of-a-program-in-mac-os-x#comment80667082_46799054)

 [add a comment]()

##  Your Answer

-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-

### Sign up or [log in](https://stackoverflow.com/users/login?ssrc=question_page&returnurl=https%3a%2f%2fstackoverflow.com%2fquestions%2f31045575%2fhow-to-trace-system-calls-of-a-program-in-mac-os-x%23new-answer)

 ![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' aria-hidden='true' class='svg-icon native iconGoogle js-evernote-checked' width='18' height='18' viewBox='0 0 18 18' data-evernote-id='2010'%3e%3cpath d='M16.51 8H8.98v3h4.3c-.18 1-.74 1.48-1.6 2.04v2.01h2.6a7.8 7.8 0 0 0 2.38-5.88c0-.57-.05-.66-.15-1.18z' fill='%234285F4' data-evernote-id='2071' class='js-evernote-checked'%3e%3c/path%3e%3cpath d='M8.98 17c2.16 0 3.97-.72 5.3-1.94l-2.6-2a4.8 4.8 0 0 1-7.18-2.54H1.83v2.07A8 8 0 0 0 8.98 17z' fill='%2334A853' data-evernote-id='2072' class='js-evernote-checked'%3e%3c/path%3e%3cpath d='M4.5 10.52a4.8 4.8 0 0 1 0-3.04V5.41H1.83a8 8 0 0 0 0 7.18l2.67-2.07z' fill='%23FBBC05' data-evernote-id='2073' class='js-evernote-checked'%3e%3c/path%3e%3cpath d='M8.98 4.18c1.17 0 2.23.4 3.06 1.2l2.3-2.3A8 8 0 0 0 1.83 5.4L4.5 7.49a4.77 4.77 0 0 1 4.48-3.3z' fill='%23EA4335' data-evernote-id='2074' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e) Sign up using Google

 ![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' aria-hidden='true' class='svg-icon iconFacebook js-evernote-checked' width='18' height='18' viewBox='0 0 18 18' data-evernote-id='2011'%3e%3cpath d='M3 1a2 2 0 0 0-2 2v12c0 1.1.9 2 2 2h12a2 2 0 0 0 2-2V3a2 2 0 0 0-2-2H3zm6.55 16v-6.2H7.46V8.4h2.09V6.61c0-2.07 1.26-3.2 3.1-3.2.88 0 1.64.07 1.87.1v2.16h-1.29c-1 0-1.19.48-1.19 1.18V8.4h2.39l-.31 2.42h-2.08V17h-2.5z' fill='%234167B2' data-evernote-id='2036' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e) Sign up using Facebook

 ![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' aria-hidden='true' class='svg-icon native iconLogoGlyphXSm js-evernote-checked' width='18' height='18' viewBox='0 0 18 18' data-evernote-id='2012'%3e%3cpath d='M14 16v-5h2v7H2v-7h2v5h10z' fill='%23BCBBBB' data-evernote-id='2075' class='js-evernote-checked'%3e%3c/path%3e%3cpath d='M12.09.72l-1.21.9 4.5 6.07 1.22-.9L12.09.71zM5 15h8v-2H5v2zm9.15-5.87L8.35 4.3l.96-1.16 5.8 4.83-.96 1.16zm-7.7-1.47l6.85 3.19.63-1.37-6.85-3.2-.63 1.38zm6.53 5L5.4 11.39l.38-1.67 7.42 1.48-.22 1.46z' fill='%23F48024' data-evernote-id='2076' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e) Sign up using Email and Password

### Post as a guest

 Name

 Email
Required, but never shown

** By clicking “Post Your Answer”, you agree to our [terms of service](https://stackoverflow.com/legal/terms-of-service/public), [privacy policy](https://stackoverflow.com/legal/privacy-policy) and [cookie policy](https://stackoverflow.com/legal/cookie-policy)  **

## Not the answer you're looking for? Browse other questions tagged [macos](https://stackoverflow.com/questions/tagged/macos)  [strace](https://stackoverflow.com/questions/tagged/strace) or [ask your own question](https://stackoverflow.com/questions/ask).