[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Forth&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Home](https://forth-standard.org/)

[[]][Official documentation](https://forth-standard.org/standard/words)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Forth_(programming_language) "wikipedia:Forth (programming language)")

[[]][[#forth](ircs://irc.libera.chat/#forth)] ([[webchat](https://web.libera.chat/#forth)])

[[]][[#embedded](ircs://irc.libera.chat/#embedded)] ([[webchat](https://web.libera.chat/#embedded)])

[[]][[comp.lang.forth](news:comp.lang.forth) ([weblink](https://www.novabbs.com/devel/thread.php?group=comp.lang.forth))]

[[]][r/Forth](https://reddit.com/r/Forth)

**Forth** is a heavily stack-oriented self-compiling procedural programming language that is only slightly more abstract than [assembly](https://wiki.gentoo.org/wiki/Assembly_language "Assembly language"). Forth first appeared in 1970 and continues to see use in the embedded programming market, behind [C](https://wiki.gentoo.org/wiki/C "C") and assembly language. Forth interpreters can be written to run on bare metal or on top of a general purpose operating system. Forth code is self-compiling in real-time even when run from bare metal on top of simple machine language primitives. Thus, somewhat like defining a new compiler target in C, Forth is sometimes used to bootstrap entirely new hardware.

Forth programs are divided up into \"words\" (subroutines). Embedded Forth interpreters are typically written in assembly language and built from Forth-words that call machine language primitives. Forth interpreters built for server use typically are written in [C](https://wiki.gentoo.org/wiki/C "C") and built from Forth-words that call OS primitives.

Forth is infamous for requiring all mathematical operations be written in [reverse Polish notation](https://en.wikipedia.org/wiki/reverse_Polish_notation "wikipedia:reverse Polish notation"). That is, `5 + 2` is written as ` 5 2 +`. Needless to say, this syntax takes some getting used to.

Forth code runs on the most minimal of virtual machines, requiring only two CPU registers and a stack to function. Forth has been ported to extremely low spec processors, even to 8 and 16-bit CPU\'s that can make a difficult C compiler target. Forth applications are built on top of Forth interpreters; that is, the base Forth interpreter essentially becomes the application over the course of development. Consequently, Forth lacks a concept of C-style linking. This makes embedded versions of Forth extremely useful for time-critical embedded applications and even firmware development.

## Contents

-   [[1] [Forth on Gentoo]](#Forth_on_Gentoo)
-   [[2] [See Also]](#See_Also)
-   [[3] [External Resources]](#External_Resources)
    -   [[3.1] [Learning Forth Today]](#Learning_Forth_Today)
    -   [[3.2] [Forth Machine Source Code in Low Level Languages]](#Forth_Machine_Source_Code_in_Low_Level_Languages)
        -   [[3.2.1] [jonesforth]](#jonesforth)
        -   [[3.2.2] [Other]](#Other)
    -   [[3.3] [Forth Machine Source Code in High Level Languages]](#Forth_Machine_Source_Code_in_High_Level_Languages)
    -   [[3.4] [Forth Package Repositories]](#Forth_Package_Repositories)
    -   [[3.5] [Miscellaneous]](#Miscellaneous)

### [Forth on Gentoo]

Gentoo has support for the following Forth interpreters:

-   [[[dev-lang/gforth]](https://packages.gentoo.org/packages/dev-lang/gforth)[]] --- [GNU Forth](https://wiki.gentoo.org/wiki/Gforth "Gforth") is a fast and portable implementation of the ANSI Forth language.

## [See Also]

-   [Assembly language](https://wiki.gentoo.org/wiki/Assembly_language "Assembly language") --- the lowest level of all programming languages, typically represented as a series of CPU architecture specific mnemonics and related operands.
-   [Fortran](https://wiki.gentoo.org/wiki/Fortran "Fortran") --- a general-purpose, compiled imperative programming language that is especially suited to numeric computation and scientific computing.
-   [C](https://wiki.gentoo.org/wiki/C "C") --- a programming language developed for Bell Labs in the early 1970s
-   [C++](https://wiki.gentoo.org/wiki/C%2B%2B "C++") --- a general-purpose programming language that originated from C
-   [Open Firmware](https://wiki.gentoo.org/wiki/Open_Firmware "Open Firmware") --- an [IEEE 1275-1994](https://ieeexplore.ieee.org/document/763383) standard for hardware independent firmware built on top of a [Forth] machine.
-   [Rust](https://wiki.gentoo.org/wiki/Rust "Rust") --- a general-purpose, multi-paradigm, compiled, programming language.

## [External Resources]

### [Learning Forth Today]

There are many resources for learning Forth. Traditionally, it has been common for a beginner to learn the rudiments of the language and then promptly attempt to implement a Forth interpreter independently. This has the dual effect of cementing key concepts into the learner\'s mind and proving Forth competency to others. This is not done as frequently today as in the past, but it\'s still a common occurrence and a well-worn path to Forth mastery.

-   [Learn Forth in Y Minutes](https://learnxinyminutes.com/docs/forth/) --- a high level Forth tutorial focused on GForth.
-   [Starting Forth](https://www.forth.com/starting-forth/) --- the classic Forth Primer.
-   [And So Forth\...](https://thebeez.home.xs4all.nl/ForthPrimer/Forth_primer.html) --- a more advanced Forth primer.
-   [Forth Lessons](https://wiki.laptop.org/go/Forth_Lessons) --- a in-depth series of progressive lessons on the Forth programming language from the makers of the [OLPC laptop](https://en.wikipedia.org/wiki/OLPC "wikipedia:OLPC").
-   [Tumble Forth](https://tumbleforth.hardcoded.net/) --- a series of Forth related articles articles written by the author of the post-apocalyptically themed [CollapseOS](http://collapseos.org/) and [DuskOS](http://duskos.org/) operating systems. Both bare metal operating systems, the former 8-bit and the later 32-bit, are written in Forth.
-   [Code Your Own Forth](https://www.youtube.com/watch?v=gPk-e9vGSWU&list=PLGY0au-SczlkeccjBFsLIE_BKp_sRfEdb) --- a YouTube series on how to write your own Forth interpreter using Swift.
-   [Forth: The programming language that writes itself](https://ratfactor.com/forth/the_programming_language_that_writes_itself.html) --- An article adapted from a 2023 talk that provides information required to understand a Forth Machine\'s internal logic.

### [Forth Machine Source Code in Low Level Languages]

Another common way to learn Forth is by studying the source code of existing implementations for insight. Many interpreters have been written as a learning exercise. Perhaps the best known example of this in recent years is jonesforth, which is written in assembly language; despite its simplicity it can function both as an interpreter and as a primitive operating system in its own right. There are other lower level examples, including [C](https://wiki.gentoo.org/wiki/C "C") and [Go](https://wiki.gentoo.org/wiki/Go "Go") implementations.

#### [jonesforth]

-   [jonesforth.S](https://github.com/nornagon/jonesforth/blob/master/jonesforth.S) --- Forth interpreter source code, written in heavily commented [i386](https://en.wikipedia.org/wiki/i386 "wikipedia:i386") assembly intended as a learning aid.
-   [Jonesforth ARM](https://github.com/M2IHP13-admin/JonesForth-arm) --- Forth interpreter source code written in heavily commented [ARM](https://wiki.gentoo.org/wiki/Project:ARM "Project:ARM") assembly, a port of the i386 original.
-   [Jonesforth RISC-V](https://github.com/jjyr/jonesforth_riscv) --- Forth interpreter source code written in heavily commented [RISC-V](https://wiki.gentoo.org/wiki/Project:RISC-V "Project:RISC-V") assembly, a port of the i386 original.
-   [Jonesforth ported to multiple architectures](https://github.com/phf/forth) --- Forth interpreter source code written in [M68k](https://wiki.gentoo.org/wiki/Project:M68k "Project:M68k") and [PowerPC](https://wiki.gentoo.org/wiki/Project:PowerPC "Project:PowerPC") among others, ported from the i386 original.
-   [lbForth.c](https://gist.github.com/lbruder/10007431) --- A port of jonesforth to [ANSI C](https://wiki.gentoo.org/wiki/C "C").

#### [Other]

-   [durexforth](https://github.com/jkotlinski/durexforth) --- A modern Forth that implements the [Forth 2012](https://forth-standard.org/standard/index) standard on the 8-bit [6502](https://en.wikipedia.org/wiki/MOS_Technology_6502 "wikipedia:MOS Technology 6502"). It\'s open source, actively maintained, and comes bundled with a native [vi](https://wiki.gentoo.org/wiki/Vi "Vi")-like text editor.
-   [Forthress](https://github.com/sayon/forthress) --- A Forth dialect written for educational purposes that is self-bootstrapping but not intended to run on bare metal without an OS, it runs on Linux and builds using [NASM, the Netwide assembler](https://nasm.us/).
-   [milliForth](https://github.com/fuzzballcat/milliForth) --- A Forth in just 386 bytes; the smallest real programming language ever.
-   [MinForth](https://sourceforge.net/projects/minforth/) --- Minimalistic but complete standard Forth compiler in [C](https://wiki.gentoo.org/wiki/C "C"); by design no toolchain is required to adapt or rebuild MinForth.
-   [noForth](https://home.hccnet.nl/anij/nof/noforth.html) - Interactive stand-alone Forth for MSP430, RISC-V, and RP2040.
-   [pForth](https://www.softsynth.com/pforth/index.php) --- Public domain, portable ANS Forth based on a kernel written in ANSI [C](https://wiki.gentoo.org/wiki/C "C"), to make it easy to port pForth to multiple platforms.
-   [Planckforth](https://github.com/nineties/planckforth) --- A bootstrapping Forth machine handwritten in x86 assembly squeezed into a 1 kB [ELF](https://en.wikipedia.org/wiki/Executable_and_Linkable_Format "wikipedia:Executable and Linkable Format") executable.
-   [punyforth](https://github.com/zeroflag/punyforth) --- A simple Forth-like programming language that primarily targets the [ESP8266](https://en.wikipedia.org/wiki/ESP8266 "wikipedia:ESP8266"), a WiFi chip with its own TCP/IP stack that is a common component of many [IoT devices](https://en.wikipedia.org/wiki/IoT "wikipedia:IoT").
-   [sectorforth](https://github.com/cesarblum/sectorforth) --- A well-documented minimalist 16-bit Forth written in [x86](https://wiki.gentoo.org/wiki/Handbook:X86 "Handbook:X86") assembly targeting the i386. It takes its name from the fact that the self-bootstrapping code fits inside of a 512-byte disk sector.
-   [zForth](https://github.com/zevv/zForth) --- Tiny, embeddable, flexible, compact Forth scripting language for embedded systems.

### [Forth Machine Source Code in High Level Languages]

High level examples include Forth interpreters written in [Bash](https://wiki.gentoo.org/wiki/Bash "Bash"), [Perl](https://wiki.gentoo.org/wiki/Perl "Perl") and [Python](https://wiki.gentoo.org/wiki/Python "Python").

-   [Bashforth](https://github.com/Bushmills/Bashforth) --- A slow but fully functional Forth interpreter written entirely in [Bash](https://wiki.gentoo.org/wiki/Bash "Bash").
-   [cl-forth](https://github.com/gmpalter/cl-forth) --- Common Lisp implementation of the Forth 2012 Standard.
-   [cubed4th](https://github.com/cubed4th/cubed4th) --- A Forth written in [Python 3](https://wiki.gentoo.org/wiki/Python "Python").
-   [forth-awk](https://github.com/joanrieu/forth-awk) --- An interpreter Forth written in [Awk](https://wiki.gentoo.org/wiki/Awk "Awk").
-   [PGForth](https://metacpan.org/release/PETERGAL/PGForth1.3/view/Language/PGForth.pm) --- A much faster simple Forth interpreter written in a few hundred lines of [Perl 5](https://wiki.gentoo.org/wiki/Perl "Perl").
-   [Yoda](https://github.com/Bushmills/yoda) --- A pure Bash compiling Forth interpreter; Forth functions get converted to their Bash equivalents prior to execution.

### [Forth Package Repositories]

-   [The Forth.Net package repository](https://theforth.net/packages)
-   [Forth Foundation Library (FFL)](http://irdvo.nl/FFL/index.html) (no longer maintained)

### [Miscellaneous]

-   [Exercism\'s 8th track](https://exercism.org/tracks/8th); 8th is a strongly-typed variant of Forth.
-   [Rosetta Code: Forth](https://rosettacode.org/wiki/Category:Forth)
-   [The Forth 2012 language standard](https://forth-standard.org/standard/index)
-   [Forth 200*x* Standardization Committee](https://forth-standard.org/)
-   [Alphabetic list of Forth words](https://www.taygeta.com/forth/dpansf.html)
-   [Write Yourself a Forth](https://beza1e1.tuxen.de/articles/forth.html)
-   [A 3-Instruction Forth for Embedded Systems Work](https://pages.cs.wisc.edu/~bolo/shipyard/3ins4th.html)