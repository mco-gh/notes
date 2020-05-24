The Hercules System/370, ESA/390, and z/Architecture Emulator

|     |     |
| --- | --- |
|     |  ![hercpic-rblk-256.gif](../_resources/c3166abf347a69d4fd02e39d3d2b2d6c.gif) |
|     |  [![](../_resources/5d1c58c4635715b78c31f96cdcbfa99f.png)](http://www.opensource.org/) |

# The Hercules System/370, ESA/390, and z/Architecture Emulator

* * *

**Hercules** is an open source software implementation of the mainframe System/370 and ESA/390 architectures, in addition to the new 64-bit z/Architecture. Hercules runs under Linux, Windows (98, NT, 2000, and XP), Solaris, FreeBSD, and Mac OS X (10.3 and later).

Hercules is [OSI Certified Open Source Software](http://www.opensource.org/)licensed under the terms of the [Q Public Licence](http://www.hercules-390.org/herclic.html).

Hercules was created by [Roger Bowler](http://perso.wanadoo.fr/rbowler/) and is maintained by Jay Maynard. Jan Jaeger designed and implemented many of the advanced features of Hercules, including dynamic reconfiguration, integrated console, interpretive execution and z/Architecture support. A dedicated crew of programmers is constantly at work implementing new features and fixing bugs.

### To find out more about Hercules, follow these links:

#### Web documentation:

- [Hercules Installation and Operation](http://www.hercules-390.org/hercinst.html)
- [Hercules Configuration File](http://www.hercules-390.org/hercconf.html)
- [Hercules System Messages](http://www.hercules-390.org/hercmsg.html)
- [What's new in this release](http://www.hercules-390.org/hercnew.html)
- [Release notes](http://www.hercules-390.org/hercrnot.html)
- [Hercules Frequently-Asked Questions](http://www.hercules-390.org/hercfaq.html)
- [Technical Support](http://www.hercules-390.org/hercsupp.html)
- [The Q Public Licence](http://www.hercules-390.org/herclic.html)

#### PDF manuals:

- [Hercules General Information](http://www.hercules-390.org/HerculesGeneralInfo.pdf)
- [Hercules Reference Summary](http://www.hercules-390.org/HerculesReferenceSummary.pdf)
- [Hercules Installation Guide](http://www.hercules-390.org/HerculesInstallation.pdf)
- [Hercules User Reference Guide](http://www.hercules-390.org/HerculesUserReference.pdf)
- [Hercules Messages and Codes](http://www.hercules-390.org/HerculesMessagesandCodes.pdf)

### To download the current release version, use the following links:

- Source tarball:
    - [hercules-3.07.tar.gz](http://www.hercules-390.org/hercules-3.07.tar.gz)

- Linux:
    - [hercules-3.07-1.i686.rpm](http://www.hercules-390.org/hercules-3.07-1.i686.rpm): 32-bit Intel RPM
    - [hercules-3.07-1.x86_64.rpm](http://www.hercules-390.org/hercules-3.07-1.x86_64.rpm): 64-bit Intel RPM
    - [hercules-3.07-1.src.rpm](http://www.hercules-390.org/hercules-3.07-1.src.rpm): Source RPM (if you want to build RPMs yourself)

- Windows native program:
    - [hercules-3.07-w32.msi](http://www.hercules-390.org/hercules-3.07-w32.msi): Windows 32-bit Installer package
    - [hercules-3.07-w32.zip](http://www.hercules-390.org/hercules-3.07-w32.zip): 32-bit binaries only archive
    - [hercules-3.07-w64.msi](http://www.hercules-390.org/hercules-3.07-w64.msi): Windows 64-bit Installer package
    - [hercules-3.07-w64.zip](http://www.hercules-390.org/hercules-3.07-w64.zip): 64-bit binaries only archive

**Note:** Installing the .msi Windows Installer package ensures the required Microsoft Runtime components are installed and also provides convenience shortcuts in the programs menu. If the required components are already present and the shortcuts are not needed on the target system, the self-extracting or .zip archive may be used instead.

The required component for this build is the x86 version of the C runtime at level 8.50727.762.

- Mac OS X:
    - [hercules-3.07-tiger.dmg](http://www.hercules-390.org/hercules-3.07-tiger.dmg): Mac OS X 10.4 (Tiger) universal binary version, 32-bit Intel and PowerPC
    - [hercules-3.07-leopard.dmg](http://www.hercules-390.org/hercules-3.07-leopard.dmg): Mac OS X 10.5 (Leopard) universal binary version, 32- and 64-bit Intel and PowerPC
    - [hercules-3.07-snowleopard.dmg](http://www.hercules-390.org/hercules-3.07-snowleopard.dmg): Mac OS X 10.6 (Snow Leopard) universal binary version, 32- and 64-bit Intel

* * *

### What people are saying about Hercules

*“ Never in my wildest dreams did I expect to see MVS running on a machine that I personally own. Hercules is a marvelous tool. My thanks to you all for a job very well done. ”*

— Reed H. Petty

*“ I do miss my mainframe a lot, and playing with Herc sure brings back memories. Just seeing the IBM message prefixes, and responding to console messages again was a wonderful bit of nostalgia! ”*

— Bob Brown

*“ I have installed your absolutely fantastic /390 emulator. You won't believe what I felt when I saw the prompt. Congratulations, this is a terrific software. I really have not had such a fascinating and interesting time on my PC lately. ”*

— IBM Large Systems Specialist

*“ Such simulators have been available for a long time. One of the most complete (up to modern 64-bit z/Architecture) is hercules. ”*

— Michel Hack, IBM Thomas J. Watson Research Center

*“ An apparently excellent emulator that allows those open source developers with an "itch to scratch", to come to the S/390 table and contribute. ”*

— Mike MacIsaac, IBM

*“ BTW grab a copy of Hercules and you can test it at home. It's a very good S/390 and zSeries (S/390 64bit) emulator.. ”*

— Alan Cox

*“ It works even better than I imagined. Hercules is a fine piece of software! ”*

— Dave Sienkiewicz
*“ Hercules is a systems programmer's dream come true. ”*
— René Vincent Jansen

*“ Aside from the electric trains my parents got me in 1953, this is the best toy I've ever been given, bar none.”*

— Jeffrey Broido
*“ Congratulations to you and your team on a fine piece of work! ”*
— Rich Smrcina
*“ Congratulations on a magnificent achievement! ”*
— Mike Ross

*“ For anyone thinking running Hercules is too much trouble or too hard or whatever, I came home from work one day and my 13 year old 8th grade son had MVS running under VM under Hercules on Linux. He had gotten all the information about how to do this from the Internet. When he complained about MVS console configuration and figuring out how to get it to work with VM, I knew he had felt all the pain he ever needed to feel about mainframes. ”*

— Scott Ledbetter, StorageTek

*“ I am running a fully graphical Centos z/Linux environment on my desktop. The Hercules emulator is an amazing feat of engineering. I just wanted to send my compliments to the team for an excellent job! Thanks much for making this product part of the open-source community! ”*

— Roby Gamboa

*“ I have DOS and DOS/VS running on Hercules with some demo applications, both batch and on-line. It does bring back some good memories. My compliments go to the Hercules team. Thank you. ”*

— Bill Carlborg

*“ This is stunning piece of work. To say that I am blown away is an understatement. I have a mainframe on my notebook!!!!!! P.S. Now if I can just remember my JCL ”*

— Roger Tunnicliffe

Read Hesh Wiener's Technology News article about Hercules athttp://www.tech-news.com/another/ap200601b.html

Read Moshe Bar's BYTE.com article about Hercules athttp://www.byte.com/documents/s=429/byt20000801s0002/

For eighteen months, the IBM Redbook*SG24-4987 Linux for S/390* athttp://www.redbooks.ibm.com/abstracts/sg244987.htmlcontained a chapter written by Richard Higson describing how to run Linux/390 under Hercules. Then suddenly, all mention of Hercules was mysteriously removed from the online edition of the book! Read the story of the disappearing Redbook chapter athttp://www2.marist.edu/htbin/wlvtype?LINUX-VM.25658

View the foils from Jay Maynard's presentation given at SHARE Session 2880 in San Francisco on 20 August 2002 as a PDF file (815K) fromhttp://linuxvm.org/Present/SHARE99/S2880JMa.pdf

* * *

### The Subversion source code repository

The complete source code for the current *development* version of Hercules is also available via anonymous access from our Subversion source code repository. The Subversion URL is:

**svn://svn.hercules-390.org/hercules**

Doing a checkout on module "hercules" will get you the source for all of Hercules. You'll want to check out the trunk, instead of the whole repository:

>  svn checkout svn://svn.hercules-390.org/hercules/trunk hercules

(The last hercules specifies the directory the checked out copy is placed into.) Please note that this will get you the current*development* version of Hercules, which is *not*release quality and thus might not even work (since it's still under development). If you want the current, stable, *release* version of Hercules (i.e. one that is known to work properly), then use the previously mentioned links instead.

Please read the file README.CVS included with the source for additional and updated instructions for building the development version.

* * *

### Other Hercules-related sites

- http://www.ibiblio.org/jmaynard/

Jay Maynard's IBM S/360 and S/370 Public Domain Software Collection

- http://www.bsp-gmbh.com/hercules

Volker Bandke's Hercules site. This is *the* site for users of Hercules on Windows, and here you can also obtain Volker's MVS 3.8J turnkey system.

- [http://www.softdevlabs.com/Hercules/hercgui-index.html

Fish's Hercules GUI for Windows.

- http://cbttape.org/~jmorrison/

Jim Morrison's downloads (includes 3380 support for MVS 3.8!)

- http://www.jaymoseley.com/hercules

Jay Moseley's Hercules site - lots of Hercules and MVS information

- http://www.tommysprinkle.com/mvs

Tommy Sprinkle's MVS 3.8 documentation

- http://hansen-family.com/mvs

Bob Hansen's MVS 3.8 documentation

- http://www.schaefernet.de/hercules

Wolfgang Schäfer's Hercules site - MVT/MVS tutorials and add-ons

* * *

![note.gif](../_resources/6f26ae70f340a066af11737233ce2e74.gif)**If you have any questions or comments** please consider joining the hercules-390 discussion group athttp://groups.yahoo.com/group/hercules-390.

Bug reports (together with your diagnosis of the fault, please) may be sent to me, [Jay Maynard](http://www.conmicro.com/), at [*jmaynard *@*conmicro.com*](http://www.hercules-390.org/mailto:jmaynard@conmicro.com).

* * *

IBM, System/370, ESA/390, and z/Architecture are trademarks or registered trademarks of [IBM Corporation](http://www.ibm.com/). Other product names mentioned here are trademarks of other companies.

Last updated $Date: 2010-03-09 23:01:33 -0600 (Tue, 09 Mar 2010) $ $Revision: 5665 $