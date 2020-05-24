Microsoft Open-Sources GW-BASIC | Windows Command Line

# Microsoft Open-Sources GW-BASIC

![17323e64ced8eaf243bf348f751f6e21](../_resources/dd32f452c20032a2667f32d67f20d620.jpg)
Rich

May 21st, 2020

We are excited to announce the open-sourcing of [Microsoft GW-BASIC](https://github.com/microsoft/GW-BASIC) on GitHub!

Yes, seriously

## Why?

Since [re-open-sourcing MS-DOS 1.25 & 2.0 on GitHub last year](https://devblogs.microsoft.com/commandline/re-open-sourcing-ms-dos-1-25-and-2-0/), we’ve received numerous requests to also open-source Microsoft BASIC.

Well, here we are!

## The Source

[These sources](https://github.com/microsoft/GW-BASIC), as clearly stated in [the repo’s readme](https://github.com/microsoft/GW-BASIC/blob/master/README.md), are the 8088 assembly language sources from 10th Feb 1983, and are being open-sourced for historical reference and educational purposes. This means we will not be accepting PRs that modify the source in any way.

## A little historical context

[The GW-BASIC source code being published](https://github.com/microsoft/GW-BASIC) is dated Feb 10th 1983. That was quite a while ago, so just to set a little historical perspective:

The week this source was created Men At Work topped the US and UK singles charts with “Down Under”, Dustin Hoffman starred in the #1 US box-office movie, “Tootsie”. In 1983, “Star Wars Episode VI – Return of the Jedi” was released, as was “War Games”! And, Emily Blunt, Kate Mara, Jonah Hill, Chris Hemsworth, and Henry Cavill, were born! Ronald Reagan was President of the USA, and Margaret Thatcher was the UK’s Prime Minister.

That same year, [Bjarne Stroustrup](https://en.wikipedia.org/wiki/Bjarne_Stroustrup) was in the middle of developing the first version of [the C++ programming language](https://en.wikipedia.org/wiki/C%2B%2B), [ARPANET](https://en.wikipedia.org/wiki/ARPANET) standardized [TCP/IP](https://en.wikipedia.org/wiki/Internet_protocol_suite). [Borland](https://en.wikipedia.org/wiki/Borland) announced [Turbo Pascal](https://en.wikipedia.org/wiki/Turbo_Pascal), created by [Anders Hejlsberg](https://en.wikipedia.org/wiki/Anders_Hejlsberg) (who went on to join Microsoft, and create [J++](https://en.wikipedia.org/wiki/Visual_J%2B%2B), [C#](https://en.wikipedia.org/wiki/C_Sharp_(programming_language)) and [TypeScript](https://en.wikipedia.org/wiki/TypeScript)).

1983 was also the year AT&T released [UNIX System V R1](https://en.wikipedia.org/wiki/UNIX_System_V), and [BSD](https://en.wikipedia.org/wiki/Berkeley_Software_Distribution) 4.2 was released, introducing the [pseudoterminal](https://en.wikipedia.org/wiki/Pseudoterminal) for the first time (the progenitor to [Windows’ ConPTY](https://devblogs.microsoft.com/commandline/windows-command-line-introducing-the-windows-pseudo-console-conpty/) we introduced to Windows in 2018 )

I was 13, and spent every spare second that I wasn’t finishing my homework or doing my chores, writing BASIC and assembly code on one of the hottest home computers of the time – the [BBC Micro](https://en.wikipedia.org/wiki/BBC_Micro) sporting 32KB RAM (yes, 32,768 ***bytes***, total!), powered by a [6502 processor](https://en.wikipedia.org/wiki/MOS_Technology_6502) running at a BLAZING 2MHz. When not coding, I was usually playing one of the most groundbreaking games of all time: “[Elite](https://en.wikipedia.org/wiki/Elite_(video_game))” by [David Braben](https://en.wikipedia.org/wiki/David_Braben) & [Ian Bell](https://en.wikipedia.org/wiki/Ian_Bell_(programmer)).

In 1983, Apple launched the 1MHz [6502](https://en.wikipedia.org/wiki/6502)-powered [Apple IIe](https://en.wikipedia.org/wiki/Apple_IIe) for US$1,395 (> $3,500 in 2020). Apple also launched the first retail-available computer with a GUI – the [Apple Lisa](https://en.wikipedia.org/wiki/Apple_Lisa). The Lisa contained a staggering 1MB RAM, and ran the awesome [Motorola 68000](https://en.wikipedia.org/wiki/Motorola_68000) processor at an astounding 5MHz, but it cost $9,995 (> $25,000 in 2020 dollars), so all I could do was peer at it through the window of the one computer store in our town authorized to sell Apple’s products … and dream.

And, in 1983 Microsoft released MS-DOS 2.0 ([source here](https://github.com/microsoft/MS-DOS)), and GW-BASIC for the [IBM PC XT](https://en.wikipedia.org/wiki/IBM_Personal_Computer) and compatibles.

## What IS GW-BASIC?

[GW-BASIC](https://en.wikipedia.org/wiki/GW-BASIC) was a BASIC interpreter derived from [IBM’s Advanced BASIC/BASICA](https://en.wikipedia.org/wiki/IBM_BASIC#IBM_Advanced_BASIC), which itself was a port of [Microsoft BASIC](https://en.wikipedia.org/wiki/MBASIC).

[Microsoft’s various BASIC implementations](https://en.wikipedia.org/wiki/Microsoft_BASIC) can trace their origins all the way back to Bill Gates & Paul Allen’s implementation of Microsoft’s first product – a [BASIC interpreter for the Altair 8800](https://en.wikipedia.org/wiki/Altair_BASIC).

During the late ’70s and 80s, Microsoft’s BASIC was ported to many OEM’s specific platform and hardware needs, and for several processors popular at that time, including the [8088](https://en.wikipedia.org/wiki/Intel_8088), [6502](https://en.wikipedia.org/wiki/MOS_Technology_6502), [6809](https://en.wikipedia.org/wiki/Motorola_6809), [Z80](https://en.wikipedia.org/wiki/Zilog_Z80), and others.

## FAQ

### Wait – where’s the C source code?

There is no C source code!

Like much software from the 70s and 80s, and just like [the source for MS-DOS](https://github.com/microsoft/MS-DOS), the source code of GW-BASIC is 100% assembly language.

### Why assembly? Why didn’t developers use higher-level languages like C, or Pascal?

When developing on/for mainframes and minicomputers of the day, developers were sometimes able to use higher-level languages like FORTRAN, LISP, COBOL, RPG, CPL/BCPL, C, etc. but the compilers for such languages were often hugely expensive, rarely generated efficient code, and were generally unavailable for the space and performance constrained home and personal computers of the day.

When writing software for early PCs, every single byte and every single instruction mattered, so developers often wrote code entirely in assembly language simply to be able to physically fit their software into the available memory, and to be able to access the computer’s resources and internal workings.

Thus, all the source code for GW-BASIC is pure assembly code, translated on a per-processor/per-machine basis from core/master sources.

### This source was ‘translated’?

Each of the assembly source files contains a header stating `This translation created 10-Feb-83 by Version 4.3`

Since the Instruction Set Architecture (ISA) of the early processors used in home and personal computers weren’t spectacularly different from one another, Microsoft was able to generate a substantial amount of the code for a port from the sources of a master implementation. (Alas, sorry, we’re unable to open-source the ISA translator.)

### What about other ports?

Many have asked if we can also open-source implementations for processors other than the 808x. Alas, we’re unable to provide sources for these ports and/or customizations.

## Enjoy!

We hope you enjoy exploring this fascinating snapshot of what software development looked like during the glorious, exciting, heady days of the ’70s and early ’80s at the dawn of “the personal computer”

*Many thanks to Amy, [Julia Liuson](https://www.linkedin.com/in/julia-liuson-6703441/), [Amanda Silver](https://twitter.com/amandaksilver), and our awesome CELA team for their approval and help finding, reviewing, and open-sourcing GW-BASIC*.

![17323e64ced8eaf243bf348f751f6e21](../_resources/217ccbd895b382f2dbaccdf9b6491717.jpg)

##### [Rich Turner](https://devblogs.microsoft.com/commandline/author/richturnmicrosoft-com/)

Sr. Program Manager, Windows Console & Command-Line

**Follow **[**](https://twitter.com/richturn_ms)[**](https://github.com/bitcrazed)[**](https://stackoverflow.com/users/229232/rich-turner)[**](https://devblogs.microsoft.com/commandline/author/richturnmicrosoft-com/feed/)