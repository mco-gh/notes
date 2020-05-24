7 ways we harden our KVM hypervisor at Google Cloud: security in plaintext

## [7 ways we harden our KVM hypervisor at Google Cloud: security in plaintext](https://cloudplatform.googleblog.com/2017/01/7-ways-we-harden-our-KVM-hypervisor-at-Google-Cloud-security-in-plaintext.html)

Wednesday, January 25, 2017

 By Andy Honig, Technical Lead Manager and Nelly Porter, Senior Product Manager

Google Cloud uses the open-source KVM hypervisor that has been validated by scores of researchers as the foundation of [Google Compute Engine](https://cloud.google.com/compute/) and [Google Container Engine](https://cloud.google.com/container-engine/), and invests in additional security hardening and protection based on our research and testing experience. Then we contribute back our changes to the KVM project, benefiting the overall open-source community.

What follows is a list of the main ways we security harden KVM, to help improve the safety and security of your applications.

1. Proactive vulnerability search: There are multiple layers of security and isolation built into Google’s KVM (Kernel-based Virtual Machine), and we’re always working to strengthen them. Google’s cloud security staff includes some of the world’s foremost experts in the world of KVM security, and has uncovered multiple vulnerabilities in KVM, Xen and VMware hypervisors over the years. The Google team has historically [found and fixed nine vulnerabilities](https://lwn.net/Articles/619332/) in KVM. During the same time period, the open source community discovered zero vulnerabilities in KVM that impacted [Google Cloud Platform](https://cloud.google.com/) (GCP).

2. Reduced attack surface area: Google has helped to improve KVM security by removing unused components (e.g., a legacy mouse driver and interrupt controllers) and limiting the set of emulated instructions. This presents a reduced attack and patch surface area for potential adversaries to exploit. We also modify the remaining components for enhanced security.

3. Non-QEMU implementation: Google does not use [QEMU](http://wiki.qemu.org/Main_Page), the user-space virtual machine monitor and hardware emulation. Instead, we wrote our own user-space virtual machine monitor that has the following security advantages over QEMU:

Simple host and guest architecture support matrix. QEMU supports a large matrix of host and guest architectures, along with different modes and devices that significantly increase complexity. Because we support a single architecture and a relatively small number of devices, our emulator is much simpler. We don’t currently support cross-architecture host/guest combinations, which helps avoid additional complexity and potential exploits. Google’s virtual machine monitor is composed of individual components with a strong emphasis on simplicity and testability. Unit testing leads to fewer bugs in complex system. QEMU code lacks unit tests and has many interdependencies that would make unit testing extremely difficult.

No history of security problems. QEMU has a long track record of security bugs, such as VENOM, and it's unclear what vulnerabilities may still be lurking in the code.

4. Boot and Jobs communication: The code provenance processes that we implement helps ensure that machines boot to a known good state. Each KVM host generates a peer-to-peer cryptographic key sharing system that it shares with jobs running on that host, helping to make sure that all communication between jobs running on the host is explicitly authenticated and authorized.

5. Code Provenance: We run a custom binary and configuration verification system that was developed and integrated with our development processes to track what source code is running in KVM, how it was built, how it was configured and how it was deployed. We verify code integrity on every level — from the boot-loader, to KVM, to the customers’ guest VMs.

6. Rapid and graceful vulnerability response: We've defined strict internal SLAs and processes to patch KVM in the event of a critical security vulnerability. However, in the three years since we released Compute Engine in beta, our KVM implementation has required zero critical security patches. Non-KVM vulnerabilities are rapidly patched through Google's internal infrastructure to help maximize security protection and meet all applicable compliance requirements, and are typically resolved without impact to customers. We notify customers of updates as required by contractual and legal obligations.

7. Carefully controlled releases: We have stringent rollout policies and processes for KVM updates driven by compliance requirements and Google Cloud security controls. Only a small team of Google employees has access to the KVM build system and release management control.

There’s a lot more to learn about KVM security at Google. Click the links below for more information.

- [KVM Security ](https://lwn.net/Articles/619332/)
- [KVM Security Improvements by Andrew Honig ](https://www.youtube.com/watch?v=L7ScFlkJEO8)
- [Performant Security Hardening of KVM by Steve Rutherford ](https://www.youtube.com/watch?v=vj5PA_D03Vg)

And of course, KVM is just one infrastructure component used to build Google Cloud. We take security very seriously, and hope you’ll entrust your workloads to us.

### FAQ

***Should I worry about side channel attacks?***
*

*We rarely see side channel attacks attempted. A large shared infrastructure the size of Compute Engine makes it very impractical for hackers to attempt side channel attacks, attacks based on information gained from the physical implementation (timing and memory access patterns) of a cryptosystem, rather than brute force or theoretical weaknesses in the algorithms. To mount this attack, the target VM and the attacker VM have to be collocated on the same physical host, and for any practical attack an attacker has to have some ability to induce execution of the crypto system being targeted. One common use for side channel attacks is against cryptographic keys. Side channel attacks that leak information are usually addressed quickly by cryptographic library developers. To help prevent that, we recommend that Google Cloud customers ensure that their cryptographic libraries are supported and always up-to-date.

***What about Venom? ***

Venom affects QEMU. Compute Engine and Container Engine are unaffected because both do not use QEMU.

***What about Rowhammer? ***

The Google Project Zero team led the way in [discovering practical Rowhammer attacks](https://googleprojectzero.blogspot.com/2015/03/exploiting-dram-rowhammer-bug-to-gain.html) against client platforms. Google production machines use double refresh rate to reduce errors, and ECC RAM that detects and corrects Rowhammer-induced errors. 1-bit errors are automatically corrected, and 2-bit errors are detected and cause any potentially offending guest VMs to be terminated. Alerts are generated for any projects that cause an unusual number of Rowhammer errors. Undetectable 3-bit errors are theoretically possible, but extremely improbable. A Rowhammer attack would cause a very large number of alerts for 2-bit and 3-bit errors and would be detected.

A [recent paper](http://www.cs.vu.nl/~kaveh/pubs/pdf/ffs-usenixsec16.pdf) describes a way to mount a Rowhammer attack using a KSM KVM module. KSM, the Linux implementation of memory de-duplication, uses a kernel thread that periodically scans memory to find memory pages with the same contents mapped from multiple VMs that are candidates for merging. Memory “de-duping” with KSM can help to locate the area to “hammer” the physical transistors underlying those bits of data, and can target the identical bits on someone else’s VM running on the same physical host. Compute Engine and Container Engine are not vulnerable to this kind of attack, since they do not use KSM. However, if a similar attack is attempted via a different mechanism, we have mitigations in place to detect it.

***What is Google doing to reduce the impact of KVM vulnerabilities? ***

We have evaluated the sources of vulnerabilities discovered to date within KVM. Most of the vulnerabilities have been in the code areas that are in the kernel for historic reasons, but can now be removed without a significant performance impact when run with modern operating systems on modern hardware. We’re working on relocating in-kernel emulation functionality outside of the kernel without a significant performance impact.

***

******How does the Google security team identify KVM vulnerabilities in their early stage? ***

We have built an extensive set of proprietary [fuzzing](https://en.wikipedia.org/wiki/Fuzzing) tools for KVM. We also do a thorough code review looking specifically for security issues each time we adopt a new feature or version of KVM. As a result, we've found many vulnerabilities in KVM over the past three years. About half of our discoveries come from code review and about half come from our fuzzers.

![Share on Google+](../_resources/c620b1a7b369ad2749d0baf881d4ccbb.png)![Share on Twitter](../_resources/4e2633eb72f2026ba8464540a445a45f.png)![Share on Facebook](../_resources/a4a815e062b3a04ad2cb425115438650.png)

20 comments

[![photo.jpg](../_resources/46d0e580386337d1385bccaa4ac6a5ad.jpg)](https://apis.google.com/u/0/wm/1/100180575185522802900)

Add a comment as Marc Cohen

Top comments

## Stream

[![photo.jpg.png](../_resources/99272c0f107395749dc7500cc6e547e2.png)](https://apis.google.com/u/0/wm/1/104257421720370350735)

### [nixCraft](https://apis.google.com/u/0/wm/1/104257421720370350735) via Google+

[1 month ago](https://apis.google.com/u/0/wm/1/+CybercitiBiz/posts/QjKi6Xptkh4)  -  Shared publicly

Ways we harden our KVM hypervisor at Google Cloud [#linux](https://apis.google.com/s/%23linux)  [#kvm](https://apis.google.com/s/%23kvm)  [#cloudcomputing](https://apis.google.com/s/%23cloudcomputing)

+
2
8
9
8

 ·
Reply

[![photo.jpg](../_resources/bf7a808c230de450aa826caaa560ab15.jpg)](https://apis.google.com/u/0/wm/1/117220853931310837595)

### [Elston Technology Services, LLC](https://apis.google.com/u/0/wm/1/117220853931310837595)

[1 month ago](https://apis.google.com/u/0/wm/1/+ElstonTechnologyServicesLLCTempe/posts/4MkNt8jZKcy)  -  Shared publicly

Via the wonderful people at Google... 7 ways we harden our KVM hypervisor at Google Cloud: Security in plaintext

+
0
1
0

 ·
Reply

[![photo.jpg](../_resources/9c6d10ba1b8b0392be37dcd59de6ed75.jpg)](https://apis.google.com/u/0/wm/1/107739793005277962402)

### [Josh Dvir](https://apis.google.com/u/0/wm/1/107739793005277962402)

[1 month ago](https://apis.google.com/u/0/wm/1/+shukydvir/posts/JwpoMcGUouX)  -  Shared publicly

7 ways we harden our KVM hypervisor at Google Cloud: Security in plaintext,
+
0
1
0

 ·
Reply

[![photo.jpg](../_resources/7efe579c5aab2e36ee83450384c86094.jpg)](https://apis.google.com/u/0/wm/1/112648813199640203443)

### [Jan Wildeboer](https://apis.google.com/u/0/wm/1/112648813199640203443) via Google+

[1 month ago (edited)](https://apis.google.com/u/0/wm/1/+jwildeboer/posts/5mmyVinYKUX)  -  Shared publicly

[#Google](https://apis.google.com/s/%23Google) hardening [#KVM](https://apis.google.com/s/%23KVM): "we wrote our own user-space virtual machine monitor [instead of using QEMU]", which (of course) isn't [#OpenSource](https://apis.google.com/s/%23OpenSource)

https://cloudplatform.googleblog.com/2017/01/7-ways-we-harden-our-KVM-hypervisor-at-Google-Cloud-security-in-plaintext.html

From the comments:

Q: Would you be interested in opensourcing your VMM so other people can use it also?

A: Google has not open sourced this for a variety of technical and business reasons. I'm not going to get into all of them, but for example a lot of our device emulation is built upon internal Google services. It wouldn't work outside a Google data center. It's not out of the realm of possibility that Google open sources some parts of it in the future, but I don't know if that will ever happen.

+
8
9
8

 ·
Reply

[![photo.jpg](../_resources/f429bdfd94bfbeccf94a871b4cce779e.jpg)](https://plus.google.com/+LarsMarowskyBr%C3%A9e)

[Lars Marowsky-Brée](https://plus.google.com/+LarsMarowskyBr%C3%A9e)

[1 month ago](https://apis.google.com/u/0/wm/1/+jwildeboer/posts/5mmyVinYKUX)

+
4
5
4

In the old days, making software accessible for the most part meant distributing it. That is what our concept of Free Software is build on. We need to fix this.

[![photo.jpg](../_resources/c6b85f8102d57282e2e82d57b4473033.jpg)](https://plus.google.com/112139137835193833820)

[Dor Kleiman (configurator)](https://plus.google.com/112139137835193833820)

[1 month ago](https://apis.google.com/u/0/wm/1/+jwildeboer/posts/5mmyVinYKUX)

+
0
1
0

Open source is not always easy, because it requires decoupling the code from its environment. When a program is written to only work in one specific environment, and decoupling isn't considered early on, it is often practically impossible to decouple it later.

[![photo.jpg](../_resources/e36cad3c46e082fc89e448b9495c6cda.jpg)](https://apis.google.com/u/0/wm/1/107616711159256259828)

### [Thorsten Leemhuis](https://apis.google.com/u/0/wm/1/107616711159256259828) via Google+

[1 month ago](https://apis.google.com/u/0/wm/1/+ThorstenLeemhuis/posts/eiEHmEsp4Xg)  -  Shared publicly

"What follows is a list of the main ways we security harden KVM, to help improve the safety and security of your applications. […] 3. Non-QEMU implementation: Google does not use QEMU, the user-space virtual machine monitor and hardware emulation. Instead, we wrote our own user-space virtual machine monitor that has the following security advantages over QEMU: […]"

+
6
7
6

 ·
Reply

[![photo.jpg](../_resources/48a40b5bebd00fe9492134bb0c4d6147.jpg)](https://apis.google.com/u/0/wm/1/104959515993955870947)

### [Andrew Pollock](https://apis.google.com/u/0/wm/1/104959515993955870947) via Google+

[1 month ago](https://apis.google.com/u/0/wm/1/+AndrewPollock/posts/MSz9mLywqQA)  -  Shared publicly

Dammit, we keep publishing interesting stuff about our Cloud offering faster than I can read it!

+
6
7
6

 ·
Reply

[![photo.jpg](../_resources/0c2a9c6ef6eb885a86d5c39fd91f2354.jpg)](https://apis.google.com/u/0/wm/1/109113053808810369491)

### [Andrew Schott](https://apis.google.com/u/0/wm/1/109113053808810369491) via Google+

[1 month ago](https://apis.google.com/u/0/wm/1/+AndrewSchott/posts/TCuipB2GUgi)  -  Shared publicly

Good tips.

[![photo.jpg.png](../_resources/7f096041ee9d183df0d32b81270b5170.png)](https://apis.google.com/u/0/wm/1/104257421720370350735)[nixCraft](https://apis.google.com/u/0/wm/1/104257421720370350735) originally shared [this](https://apis.google.com/u/0/wm/1/+CybercitiBiz/posts/QjKi6Xptkh4)

Ways we harden our KVM hypervisor at Google Cloud [#linux](https://apis.google.com/s/%23linux)  [#kvm](https://apis.google.com/s/%23kvm)  [#cloudcomputing](https://apis.google.com/s/%23cloudcomputing)

+
0
1
0

 ·
Reply

[![photo.jpg](../_resources/c71af8c178711a40c4ff1e6ea86c8f14.jpg)](https://apis.google.com/u/0/wm/1/111730389105401818315)

### [U Das](https://apis.google.com/u/0/wm/1/111730389105401818315) via Google+

[1 month ago](https://apis.google.com/u/0/wm/1/+UDas_MarvinWasRight/posts/ZDAQaRRqXN5)  -  Shared publicly

Google Compute uses KVM that's hardened. They have written a custom replacement for QEMU optimised for their systems, among other improvements.

[![photo.jpg.png](../_resources/7f096041ee9d183df0d32b81270b5170.png)](https://apis.google.com/u/0/wm/1/104257421720370350735)[nixCraft](https://apis.google.com/u/0/wm/1/104257421720370350735) originally shared [this](https://apis.google.com/u/0/wm/1/+CybercitiBiz/posts/QjKi6Xptkh4)

Ways we harden our KVM hypervisor at Google Cloud [#linux](https://apis.google.com/s/%23linux)  [#kvm](https://apis.google.com/s/%23kvm)  [#cloudcomputing](https://apis.google.com/s/%23cloudcomputing)

+
1
2
1

 ·
Reply

[![photo.jpg.png](../_resources/09ae59214c52cec86c2893a71b889635.png)](https://apis.google.com/u/0/wm/1/112771156790995636371)

### [HighOps](https://apis.google.com/u/0/wm/1/112771156790995636371)

[1 month ago](https://apis.google.com/u/0/wm/1/+HighopsPlus/posts/cr65B5V3qQD)  -  Shared publicly

7 ways we harden our KVM hypervisor at Google Cloud: Security in plaintext http://ow.ly/oLfR308mGvY  [#InfoSec](https://apis.google.com/s/%23InfoSec)

+
0
1
0

 ·
Reply

[![photo.jpg](../_resources/9431412075ae2bb19ca51acbd38d5cd6.jpg)](https://apis.google.com/u/0/wm/1/114901836040961691147)

### [Brian Herman](https://apis.google.com/u/0/wm/1/114901836040961691147)

[1 month ago](https://apis.google.com/u/0/wm/1/114901836040961691147/posts/UxowiRDJ8CK)  -  Shared publicly

Would you be interested in opensourcing your VMM so other people can use it also?

+
2
3
2

 ·
Reply

[![photo.jpg.png](../_resources/e276b3c7a964ae1f19c288fe0bbf70e0.png)](https://plus.google.com/111028179044005127792)

[Andrew Honig](https://plus.google.com/111028179044005127792)

[1 month ago](https://apis.google.com/u/0/wm/1/114901836040961691147/posts/UxowiRDJ8CK)

+
0
1
0

Google has not open sourced this for a variety of technical and business reasons. I'm not going to get into all of them, but for example a lot of our device emulation is built upon internal Google services. It wouldn't work outside a Google data center. It's not out of the realm of possibility that Google open sources some parts of it in the future, but I don't know if that will ever happen.

[![uFp_tsTJboUY7kue5XAsGA=s28.png](../_resources/e41982ad7fff0b3d7ae9931b4f331181.png)](https://apis.google.com/u/0/wm/1/109066353941297181010)

### [SecurityJar](https://apis.google.com/u/0/wm/1/109066353941297181010) shared this

[1 month ago](https://apis.google.com/u/0/wm/1/+Securityjar/posts/LQzMWd8A7Je)  -  Shared publicly

+
0
1
0

 ·
Reply

[![photo.jpg.png](../_resources/6376fc27bf5e9d9448e056d0d1e9b99d.png)](https://apis.google.com/u/0/wm/1/107243673123839064144)

### [HackersPews](https://apis.google.com/u/0/wm/1/107243673123839064144) shared this

[1 month ago](https://apis.google.com/u/0/wm/1/+Hackerspews0/posts/S7x4eYQEcwd)  -  Shared publicly

+
0
1
0

 ·
Reply

[![photo.jpg.png](../_resources/b4106cb3d4f0d5620d9de2d3ab8ca642.png)](https://apis.google.com/u/0/wm/1/115242946247553753667)

### [Sagi Kedmi](https://apis.google.com/u/0/wm/1/115242946247553753667) shared this via Google+

[1 month ago](https://apis.google.com/u/0/wm/1/115242946247553753667/posts/BS4tigmHYQz)  -  Shared publicly

+
0
1
0

 ·
Reply

[![photo.jpg](../_resources/235ab5dbc54f95a4ac772fac7c90fc20.jpg)](https://apis.google.com/u/0/wm/1/101910465526893717548)

### [Ko Savonije (Kobus)](https://apis.google.com/u/0/wm/1/101910465526893717548) shared this via Google+

[1 month ago](https://apis.google.com/u/0/wm/1/+KoSavonije/posts/Q2YCgV4ecPA)  -  Shared publicly

+
0
1
0

 ·
Reply

[![photo.jpg](../_resources/0d67e50f3c4ee38496f57fec70a4404a.jpg)](https://apis.google.com/u/0/wm/1/108541742594026375732)

### [Mark Piper](https://apis.google.com/u/0/wm/1/108541742594026375732) via Google+

[1 month ago](https://apis.google.com/u/0/wm/1/108541742594026375732/posts/BdR2MrN8CwD)  -  Shared publicly

Sane.
+
1
2
1

 ·
Reply

[![photo.jpg](../_resources/4c499598674a047f494189eb45dad302.jpg)](https://apis.google.com/u/0/wm/1/111545775357921947393)

### [Michael Faille](https://apis.google.com/u/0/wm/1/111545775357921947393)

[1 month ago](https://apis.google.com/u/0/wm/1/+MichaelFaille/posts/FRX9xkuUj3W)  -  Shared publicly

It's why I'm trusting Google Cloud Compute :
security by transparency
+
1
2
1

 ·
Reply

[![photo.jpg](../_resources/cd268deee1c6c1b94743c33673c1f237.jpg)](https://apis.google.com/u/0/wm/1/113865414059348172096)

### [Aldair Arkhamp](https://apis.google.com/u/0/wm/1/113865414059348172096) via Google+

[1 month ago](https://apis.google.com/u/0/wm/1/+AldairArkhamp/posts/5RowrVjTwgF)  -  Shared publicly

[![photo.jpg.png](../_resources/7f096041ee9d183df0d32b81270b5170.png)](https://apis.google.com/u/0/wm/1/104257421720370350735)[nixCraft](https://apis.google.com/u/0/wm/1/104257421720370350735) originally shared [this](https://apis.google.com/u/0/wm/1/+CybercitiBiz/posts/QjKi6Xptkh4)

Ways we harden our KVM hypervisor at Google Cloud [#linux](https://apis.google.com/s/%23linux)  [#kvm](https://apis.google.com/s/%23kvm)  [#cloudcomputing](https://apis.google.com/s/%23cloudcomputing)

+
0
1
0

 ·
Reply

Labels:[Security & Identity](https://cloudplatform.googleblog.com/search/label/Security%20%26%20Identity)