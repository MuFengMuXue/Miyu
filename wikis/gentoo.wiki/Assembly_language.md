[[]][Wikipedia](https://en.wikipedia.org/wiki/Assembly_language "wikipedia:Assembly language")

[[]][[#asm](ircs://irc.libera.chat/#asm)] ([[webchat](https://web.libera.chat/#asm)])

[[]][[alt.lang.asm](news:alt.lang.asm) ([weblink](https://www.novabbs.com/devel/thread.php?group=alt.lang.asm))]

[[]][r/asm](https://reddit.com/r/asm)

**Assembly language** is the lowest level of all programming languages, typically represented as a series of CPU architecture specific mnemonics and related operands. Such mnemonics stand in for precise byte sequences, called machine language, which is the code the CPU actually executes at runtime. Assembly language is imperative by nature, though clever use of macros and data structures often permits other programming paradigms. Even object oriented programming is possible at this level, with the right combination of macros and data structures.

An assembler is the first piece of software written for a new CPU architecture. Typically, a [Forth](https://wiki.gentoo.org/wiki/Forth "Forth") follows this as is it\'s a self-bootstrapping language that makes an excellent test to confirm a new assembler works as expected. Lastly, a [C compiler](https://wiki.gentoo.org/wiki/C "C") back end is added targeting the new CPU instruction set. Give or take some intermediate representation, this must ultimately emit machine language in the final stages of compilation. With these three pieces of software written and confirmed functional existing programs can now be ported to the new CPU architecture.

Writing assembly language directly isn\'t as common as it once was but it is by no means a rare or unusual skill. Security researchers make frequent use of assembly language directly, as do embedded systems programmers and compiler designers. Further, many programmers advocate at least a minimal working knowledge of assembly as it clarifies certain advanced concepts, notably pointers.

Assembly language terminology is often a source of confusion for programmers who are unaccustomed to it. Unfortunately, even official documents have been known to get assembly related terminology wrong. For clarity:

-   The act of converting assembly language source code into an executable is called **assembly**.
-   Assembly instructions are made up of **opcodes**, together with it\'s addressing mode, represent a unique sequence of bytes.
-   Each opcode accepts zero or more **operands** as arguments depending upon its addressing mode.
-   The **addressing mode** of an opcode dictates how the instruction interacts with memory.
-   The resulting binary contains **machine language** instructions that are specific to the target CPU\'s instruction set.
-   A program that performs this assembly process is called an **assembler**.
-   Modern assemblers support **macros** which combine small groups of instructions and may take arguments, to make code easier to read and maintain.
-   Most also support **pseudo operations** which are aliases built into the assembler itself, typically to stand in for an opcode with a specific set of arguments that performs a common task.
-   The term **hand written assembly** can refer to developing software directly in an assembler without the aid of a compiler, this is its usual meaning. Much more rarely, the phrase is used to mean writing an assembly language program on pen and paper then transcribing it directly into machine language byte values with a hex editor.
-   Converting an existing binary back to a human readable programming language --- assembly language or otherwise --- is called **disassembly**. This process is as much art as science because it can be difficult to differentiate CPU instructions from the surrounding data.
-   Disassembly is a useful skill in various professional circles, especially cybersecurity and malware analysis. As a hobby it is most common in retrocomputing circles.
-   Disassembling a binary to learn how it works is called **reverse engineering**, which is a legally complex topic in most jurisdictions.
-   Disassembling a binary to reconstruct previously lost source code is called **source code archaeology**. This is occasionally necessary when the original source code to an important legacy program is lost and it must be or patched to address a bug or to add new features.
-   For the sake of completeness: many modern CISC processors use **microcode** --- somewhat akin to on-chip firmware --- as part of their instruction decoding logic. In practice this means that such processors can be patched to a limited extent if hardware bugs are found. Assembly language is not microcode, they\'re different technologies.

So, yes, an assembler assembles an assembly language program into a machine language executable. A disassembler disassembles an architecture specific machine language binary into (sort of) human readable source code. The resulting code may or may not actually be assembly language, it may be C or something else, but it is still called \"disassembly\".

## Contents

-   [[1] [Adding to this page]](#Adding_to_this_page)
-   [[2] [Developing in Assembly language on Gentoo]](#Developing_in_Assembly_language_on_Gentoo)
    -   [[2.1] [Developing for Embedded Architectures]](#Developing_for_Embedded_Architectures)
-   [[3] [Learning assembly language today]](#Learning_assembly_language_today)
    -   [[3.1] [Acorn]](#Acorn)
        -   [[3.1.1] [ARM]](#ARM)
        -   [[3.1.2] [ARM 64]](#ARM_64)
    -   [[3.2] [AIM Alliance]](#AIM_Alliance)
        -   [[3.2.1] [PowerPC]](#PowerPC)
        -   [[3.2.2] [PowerPC 64]](#PowerPC_64)
    -   [[3.3] [Digital Equipment Corporation]](#Digital_Equipment_Corporation)
        -   [[3.3.1] [Alpha]](#Alpha)
    -   [[3.4] [Hewlett-Packard]](#Hewlett-Packard)
        -   [[3.4.1] [HPPA PA-RISC]](#HPPA_PA-RISC)
    -   [[3.5] [Intel]](#Intel)
        -   [[3.5.1] [x86]](#x86)
        -   [[3.5.2] [AMD64]](#AMD64)
        -   [[3.5.3] [Itanium]](#Itanium)
    -   [[3.6] [Loongson]](#Loongson)
        -   [[3.6.1] [LoongArch]](#LoongArch)
        -   [[3.6.2] [LoongISA]](#LoongISA)
    -   [[3.7] [International Business Machines]](#International_Business_Machines)
        -   [[3.7.1] [System/390]](#System.2F390)
    -   [[3.8] [MIPS Computer Systems]](#MIPS_Computer_Systems)
        -   [[3.8.1] [MIPS]](#MIPS)
    -   [[3.9] [Sun Microsystems]](#Sun_Microsystems)
        -   [[3.9.1] [SPARC]](#SPARC)
    -   [[3.10] [University of California, Berkeley]](#University_of_California.2C_Berkeley)
        -   [[3.10.1] [RISC-V]](#RISC-V)
    -   [[3.11] [Embedded Processors and Microcontrollers]](#Embedded_Processors_and_Microcontrollers)
        -   [[3.11.1] [Atmel AVR]](#Atmel_AVR)
        -   [[3.11.2] [Microchip Technology PIC]](#Microchip_Technology_PIC)
        -   [[3.11.3] [MOS Technology 65*xx*]](#MOS_Technology_65xx)
            -   [[3.11.3.1] [Emulators]](#Emulators)
        -   [[3.11.4] [Motorola M68k]](#Motorola_M68k)
        -   [[3.11.5] [Zilog Z80]](#Zilog_Z80)
    -   [[3.12] [Virtual Machine Assembly Languages]](#Virtual_Machine_Assembly_Languages)
        -   [[3.12.1] [Java Bytecode]](#Java_Bytecode)
        -   [[3.12.2] [WebAssembly]](#WebAssembly)
        -   [[3.12.3] [uxntal]](#uxntal)
-   [[4] [See also]](#See_also)
-   [[5] [External resources]](#External_resources)

## [Adding to this page]

Gentoo strives to be a Linux distribution that developers love to use.

The architectures listed here in the main section should each be credible Gentoo Linux installation targets. Less powerful CPU\'s should be placed into the embedded section towards the bottom of the page *provided an assembler ebuild exists* in Portage or GURU. Architectures that used to serve as a Gentoo installation target but are no longer suitable for some reason should get moved to a Retired Architectures section or to the embedded section, whichever makes the most sense.

In general, entries should have the following details:

1.  Who originally designed the ISA.
2.  A few short words about its history and technical details, *e.g.*, whether it is RISC or CISC and its register width, etc.
3.  What market niche the ISA fills.
4.  Anything that makes it interesting or unique about assembly language development on the ISA.
5.  Any special tendency the ISA has towards exposing bugs in code that might go unnoticed on other platforms.

Each and every architecture entry here is an invitation to write a corresponding guide that covers best practices for assembly language development on the platform --- especially if it\'s a lesser known or niche ISA. Also, **Gentoo maintainers of less popular CPU architectures need your help!** Consider contributing to one of the ISA\'s Gentoo project, linked to in the architecture\'s name.

## [Developing in Assembly language on Gentoo]

Gentoo has a wide variety of assemblers available that target many major and minor CPU architectures. While the GNU Assembler [is] the most ubiquitous, it is far from the only option.

-   [[[sys-devel/binutils]](https://packages.gentoo.org/packages/sys-devel/binutils)[]] --- Includes the GNU Assembler which is a well-worn part of the GNU compiler collection tool chain targeting multiple CPU architectures.
-   [[[dev-lang/jwasm]](https://packages.gentoo.org/packages/dev-lang/jwasm)[]] --- A MASM compatible assembler which began as a fork of WASM.
-   [[[dev-lang/mmix]](https://packages.gentoo.org/packages/dev-lang/mmix)[]] --- Donald Knuth\'s MMIX Assembler and Simulator.
-   [[[dev-lang/nasm]](https://packages.gentoo.org/packages/dev-lang/nasm)[]] --- A popular x86/amd64 assembler.
-   [[[dev-lang/yasm]](https://packages.gentoo.org/packages/dev-lang/yasm)[]] --- An assembler for the x86 and x86_64 instruction sets.

### [Developing for Embedded Architectures]

-   [[[dev-embedded/avra]](https://packages.gentoo.org/packages/dev-embedded/avra)[]] --- An Atmel AVR Assembler.
-   [[[dev-embedded/gputils]](https://packages.gentoo.org/packages/dev-embedded/gputils)[]] --- Tools including assembler, linker and librarian for PIC microcontrollers.
-   [[[dev-embedded/picasm]](https://packages.gentoo.org/packages/dev-embedded/picasm)[]] --- An assembler and disassembler for 12 and 14-bit PIC chips.
-   [[[dev-embedded/xa]](https://packages.gentoo.org/packages/dev-embedded/xa)[]] --- A high-speed, two-pass portable 6502 cross-assembler.

\

## [Learning assembly language today]

** Warning**\
**Thou shalt not link to pirated books!** Although direct links to freely available content is preferred, citing well respected texts that are readily available on the secondary (used) market is perfectly fine. That said, please **DO NOT** link to pirated copies of programming books, including long out-of-print books. Showing disrespect for the intellectual property rights of others could put the Gentoo project at legal risk and nobody wants that. Linking to **officially copies** of previously published texts that have subsequently been available for download by the original author(s) or current rights holder is acceptable.

While learning to program in assembly is challenging, it is far easier today than in the past. Antecedently, large, expensive books on a specific CPU architecture were necessary to attain fluency in that ISA. While such books remain available (primarily targeting academia), the Internet has proliferated knowledge of assembly language far and wide; there are groups of programmers entirely devoted to learning assembly, and numerous YouTube channels cover the subject in great depth for nearly every ISA, current or historical.

This list comprises two sections: the first contains CPU architectures which are solid Gentoo Linux installation targets for the present day or relatively recent past; the second covers embedded CPUs, which are often unlikely installation candidates. Admittedly, some edge cases do exist: many MIPS-based computers can indeed support a Gentoo install, although MIPS PCs are uncommon targets. Conversely, the venerable Motorola M68k line of embedded CPUs can *theoretically* support a Gentoo Linux installation, given enough RAM, but such a configuration is rare.

### [Acorn]

[Acorn Computers](https://en.wikipedia.org/wiki/Acorn_Computers "wikipedia:Acorn Computers") developed the ARM1 circa 1983 for the [Acorn Archimedes](https://en.wikipedia.org/wiki/Acorn_Archimedes "wikipedia:Acorn Archimedes") and as a 32-bit expansion module for the [BBC Micro](https://en.wikipedia.org/wiki/BBC_Micro "wikipedia:BBC Micro") line of 8-bit home computers. Famously the ARM1 CPU was designed in a few short weeks and prioritized low power consumption above nearly everything else in order to prevent thermal overload of the CPU package. (Details on the ARM\'s deign history are well covered in the YouTube documentary: [*How Amateurs created the world´s most popular Processor*](https://www.youtube.com/watch?v=nIwdhPOVOUk).) Today the 32-bit and 64-bit descendants of the original ARM1 processor run in thousands of mobile devices. It is perhaps best known as the heart of the [Raspberry Pi](https://wiki.gentoo.org/wiki/Raspberry_Pi "Raspberry Pi") line of single board computers. Knowledge of ARM assembly language is a sought after skill for firmware, embedded, and mobile developers.

#### [[ARM](https://wiki.gentoo.org/wiki/Project:ARM "Project:ARM")]

[[]][[#arm](ircs://irc.libera.chat/#arm)] ([[webchat](https://web.libera.chat/#arm)])

[[]][[comp.sys.arm](news:comp.sys.arm) ([weblink](https://www.novabbs.com/devel/thread.php?group=comp.sys.arm))]

[[]][r/arm](https://reddit.com/r/arm)

-   [*ARM Developer Suite Assembler Guide*](https://developer.arm.com/documentation/dui0068/b/ARM-Instruction-Reference) --- the official assembly language programming guide for the ARM family of processors.

#### [[ARM 64](https://wiki.gentoo.org/wiki/Project:ARM64 "Project:ARM64")]

-   [ARMv8 A64 Quick Reference](https://courses.cs.washington.edu/courses/cse469/19wi/arm64.pdf) (PDF) --- a three page printable cheat sheet for ARM64 instructions.

### [AIM Alliance]

The PowerPC is a RISC architecture that was designed by the AIM alliance in 1994. It was intended as a 32-bit ISA but it was later extended to 64-bits. It is best known for as the CPU of choice for 1990\'s Macintosh computers. Today it is promoted by the [OpenPOWER Foundation](https://openpowerfoundation.org/) as \"The Most Open and High-Performance Processor Architecture and Ecosystem in the Industry.\" With the exception of Power10 (which is a relatively closed design relative to its counterparts) this statement is true.

At present PowerPC CPUs are most commonly used as high end embedded devices. Many automotive single board computers run some form of the Power ISA. In the aerospace industry the Power ISA is common and NXP is well known for producing radiation hardened models for use in space satellites. PowerPC is not entirely absent from the personal computer market as some very high end servers run PowerPC CPU\'s. Owing to its openness the PowerPC is the CPU of source in the [Linux Open Hardware PowerPC notebook](https://www.powerpc-notebook.org/en/) currently under development.

Gentoo\'s PowerPC Project remains active, but **Gentoo\'s PowerPC project would welcome new contributors**. Even for a system as old as the [Mac Mini G4](https://wiki.gentoo.org/wiki/Mac_Mini_(PowerPC_G4) "Mac Mini (PowerPC G4)"), Gentoo remains a viable installation target for those old systems. It should be noted however that [high end Power ISA servers exist](https://www.raptorcs.com/) and are equally valid Gentoo Linux installation targets. Those seeking to learn PowerPC and PowerPC 64 assembly language run the gamut from those interested in retro Mac development to embedded development in the automotive or aerospace industries.

The PowerPC\'s endianness choices --- technically bi-endian, but historically big endian by default --- have a reputation for revealing certain kinds of programming. Such errors tend to happen when a programmer assumes all build targets are little endian like Intel and ARM CPU\'s. Endianness issues tend to be subtle, so developers are encouraged to compile their code against the PowerPC *Big Endian* and run appropriate unit tests. PowerPC(64) Big Endian can be emulated with [qemu and chroot](https://wiki.gentoo.org/wiki/Embedded_Handbook/General/Compiling_with_qemu_user_chroot "Embedded Handbook/General/Compiling with qemu user chroot").

#### [[PowerPC](https://wiki.gentoo.org/wiki/Project:PowerPC "Project:PowerPC")]

[[]][[#ppc64](ircs://irc.libera.chat/#ppc64)] ([[webchat](https://web.libera.chat/#ppc64)])

[[]][[comp.sys.powerpc.tech](news:comp.sys.powerpc.tech) ([weblink](https://www.novabbs.com/devel/thread.php?group=comp.sys.powerpc.tech))]

[[]][r/PowerPC](https://reddit.com/r/PowerPC)

-   [WiiBrew Assembler Tutorial](https://wiibrew.org/wiki/Assembler_Tutorial) --- a good general introduction to 32-bit PowerPC assembly language, albeit with a focus on some of the specifics of the [Nintendo Wii](https://en.wikipedia.org/wiki/Wii "wikipedia:Wii").
-   [*Programming Environments Manual for 32-Bit Implementations of the PowerPC Architecture*](https://www.nxp.com/files-static/product/doc/MPCFPE32B.pdf) --- NXP\'s manual for 32-bit variants of the Power ISA.

#### [PowerPC 64]

-   [*Power ISA Instruction Set Architecture*](https://openpowerfoundation.org/specifications/isa/) by the Open Power Foundation Instruction Set Architecture Technical Working Group --- extensive technical documentation on the Power ISA and its various revisions, PDF available. Covers both 32-bit and 64-bit PowerPC modes.

### [Digital Equipment Corporation]

The Alpha was a 64-bit RISC processor developed by [Digital Equipment Corporation](https://en.wikipedia.org/wiki/Digital_Equipment_Corporation "wikipedia:Digital Equipment Corporation") (DEC) and first introduced in 1992. It was designed for the minicomputer and mainframe market, not the home microcomputer market. The Alpha was discontinued after DEC was acquired by [Compaq](https://en.wikipedia.org/wiki/Compaq "wikipedia:Compaq") in 1998 in favor of Compaq continuing with the Intel [Itanium](https://wiki.gentoo.org/wiki/Project:IA64 "Project:IA64"). Today, interest in the Alpha line continues mostly among mainframe computer hobbyists, some of whom choose Gentoo Linux as their preferred operating system.

Alpha\'s design choices have a reputation for making certain kinds of programming errors much more obvious. Potentially dangerous memory access bugs that would go unnoticed on other architectures cause programs to segfault on this architecture. This is detailed in the [Gentoo\'s Alpha Porting Guide](https://wiki.gentoo.org/wiki/Project:Alpha/Porting_guide "Project:Alpha/Porting guide"). **Gentoo\'s Alpha project would welcome new contributors.** Developers are encouraged to compile their code against the Alpha --- which can be emulated with [qemu and chroot](https://wiki.gentoo.org/wiki/Embedded_Handbook/General/Compiling_with_qemu_user_chroot "Embedded Handbook/General/Compiling with qemu user chroot") --- as a means of bug-hunting.

#### [[Alpha](https://wiki.gentoo.org/wiki/Project:Alpha "Project:Alpha")]

[[]][[#alpha](ircs://irc.libera.chat/#alpha)] ([[webchat](https://web.libera.chat/#alpha)])

-   *Alpha RISC Architecture for Programmers* by James S. Evans and Richard H. Eckhouse --- highly detailed academic text on writing DEC Alpha assembly language.
-   *Alpha Architecture Handbook* by Digital Equipment Corporation --- the official Alpha handbook, freely available on the Digital.com website [circa 1998](https://web.archive.org/web/19981202111437/http://ftp.digital.com/pub/Digital/info/semiconductor/literature/dsc-library.html) shortly after its acquisition by Compaq. Site preserved by [Archive.org](https://archive.org).
-   *Alpha Architecture Reference Manual* edited by Richard L. Sites --- an official Alpha manual from DEC.
-   [*Alpha Assembly Language Guide*](https://www.cs.cmu.edu/afs/cs/academic/class/15213-f98/doc/alpha-guide.pdf) (PDF) by Randal E. Bryant --- a short tutorial detailing the inner workings of the Alpha processor.
-   *21164 Alpha Microprocessor Hardware Reference Manual* by Digital Equipment Corporation --- freely available on the Digital.com website [circa 1998](https://web.archive.org/web/19981202111437/http://ftp.digital.com/pub/Digital/info/semiconductor/literature/dsc-library.html) shortly after its acquisition by Compaq. Site preserved by [Archive.org](https://archive.org).
-   *Alpha 21164PC Microprocessor Hardware Reference Manual* by Digital Equipment Corporation --- freely available on the Digital.com website [circa 1998](https://web.archive.org/web/19981202111437/http://ftp.digital.com/pub/Digital/info/semiconductor/literature/dsc-library.html) shortly after its acquisition by Compaq. Site preserved by [Archive.org](https://archive.org).
-   [How much better was DEC Alpha than contemporaneous x86?](https://retrocomputing.stackexchange.com/questions/13611/how-much-better-was-dec-alpha-than-contemporaneous-x86) --- a StackExchange article detailing the strengths and weaknesses of the Alpha\'s design.

### [Hewlett-Packard]

[Hewlett-Packard](https://en.wikipedia.org/wiki/Hewlett-Packard "wikipedia:Hewlett-Packard") introduced the Hewlett Packard Precision Architecture (HPPA) in 1986. Its original incarnation has a mix of 32-bit and 64-bit registers, in 1996 its ISA was extended to a pure 64-bit design. It was intended for high end HP servers and workstations of its era. The HPPA line was discontinued in 2008 as it was displaced in its role by the Intel\'s Itanium before that architecture was also discontinued. Today there are older but functional HPPA workstations and servers that continue to see use past their end-of-life. Some owners of legacy HPPA hardware choose to run Gentoo Linux. Those who learn HPPA assembly language typically do so out of historical interest.

#### [[HPPA PA-RISC](https://wiki.gentoo.org/wiki/Project:HPPA "Project:HPPA")]

-   [OpenPA.Net](https://www.openpa.net/) --- a site dedicated to the history of the HPPA processor architecture. The site became the basis of the [*OpenPA: The book of PA-RISC*](https://www.openpa.net/print.html) by Bonn Weissmann.
-   [PA-RISC 1.1 Architecture and Instruction Set Reference Manual](https://web.archive.org/web/19970709184455/http://www.hp.com/nsa/main.html) --- HP\'s official reference manual from [HP.com](https://hp.com) circa 1998, courtesy of [Archive.org](https://archive.org).
-   *PA-RISC 2.0 Architecture and Instruction Set Reference Manual* --- HP\'s official reference manual for later iterations of the PA-RISC line of processors.

### [Intel]

[Intel](https://en.wikipedia.org/wiki/Intel "wikipedia:Intel") famously created the world\'s first CPU on an integrated package with the release of the [Intel 4004](https://en.wikipedia.org/wiki/Intel_4004 "wikipedia:Intel 4004"). Other companies followed suit and a short time later hobbyist computer kits became available sparking the home microcomputer revolution.

The x86 line are 64-bit descendants of the 16-bit Intel 8086. The x86 line remains a viable installation target for Gentoo Linux. Today the oldest Intel CPU that a modern Linux kernel can run on is an i486 --- though [this may soon shift](https://hackaday.com/2022/11/02/bye-bye-linux-on-the-486-will-we-miss-you/) to the Intel Pentium.

The 64-bit Intel Itanium was a CISC design originally intended for the high end server market. It intentionally broke backwards compatibility with the x86 line in order to make it easier to implement improvements in CPU design. The AMD64 is a 64-bit extension of the 32-bit x86 line. It was developed by [AMD](https://en.wikipedia.org/wiki/AMD "wikipedia:AMD") in 2000 and proved so successful that Intel licensed the technology from its competitor. Today, most Gentoo Linux installation targets are 64-bits and many of those are AMD64. As the Itanium was only recently discontinued, though less common than AMD64 PC\'s, it remains a viable installation target for Gentoo Linux.

Two main types of syntax:

-   AT&T (.att_syntax): parameter order is: source → destination.
-   Intel (.intel_syntax): parameter order is: destination ← source (divides to NASM-style and MASM/TASM style).

Knowledge of Intel assembly language is useful for a great many things, but especially compiler optimization, vulnerability analysis, and malware reverse engineering. All of these skills are in high demand.

#### [[x86](https://wiki.gentoo.org/wiki/Project:X86 "Project:X86")]

-   [Learn x86 Assembly Language](https://asmtutor.com/) --- a lengthy series of articles on x86 assembly divided into many small lessons.
-   [Wikibooks: x86 Assembly](https://en.wikibooks.org/wiki/X86_Assembly) --- a semi-complete free Wikibook on x86 assembly with detailed instructions on [making Linux system calls](https://en.wikibooks.org/wiki/X86_Assembly/Interfacing_with_Linux) from within assembly language programs.
-   [Rosetta Code: x86 Assembly](https://rosettacode.org/wiki/Category:X86_Assembly) --- links to articles on how to perform various programming tasks and build common data structures on that architecture.

#### [[AMD64](https://wiki.gentoo.org/wiki/Project:AMD64 "Project:AMD64")]

-   [*AMD64 Architecture Programmer's Manual Volume 1: Application Programming*](https://www.amd.com/content/dam/amd/en/documents/processor-tech-docs/programmer-references/24592.pdf)
-   [*AMD64 Architecture Programmer's Manual Volume 2: System Programming*](https://www.amd.com/content/dam/amd/en/documents/processor-tech-docs/programmer-references/24593.pdf)
-   [*AMD64 Architecture Programmer's Manual Volume 3: General-Purpose and System Instructions*](https://www.amd.com/content/dam/amd/en/documents/processor-tech-docs/programmer-references/24594.pdf)
-   [*AMD64 Architecture Programmer's Manual Volume 4: 128-Bit and 256-Bit Media Instructions*](https://www.amd.com/content/dam/amd/en/documents/processor-tech-docs/programmer-references/26568.pdf)
-   [*AMD64 Architecture Programmer's Manual Volume 5: 64-Bit Media and x87 Floating-Point Instructions*](https://www.amd.com/content/dam/amd/en/documents/processor-tech-docs/programmer-references/26569.pdf)

#### [[Itanium](https://wiki.gentoo.org/wiki/Project:IA64 "Project:IA64")]

** Note**\
The Linux [kernel](https://wiki.gentoo.org/wiki/Kernel "Kernel") dropped support for Intel Itanium in late 2023 and [glibc](https://wiki.gentoo.org/wiki/Glibc "Glibc") followed suit in early 2024. Without kernel support it is not possible to boot very recent versions of the Linux kernel on Itanium hardware. Although other [C](https://wiki.gentoo.org/wiki/C "C") runtimes exist, without glibc support maintaining IA64 as a C compilation target is *much* harder.\
\
For more information, see: *[Gentoo Linux drops IA-64 (Itanium) support.](https://www.gentoo.org/news/2024/08/14/Gentoo-drops-IA-64-support.html)*

-   [Intel Itanium Processor 9500 Series: Reference Manual](https://web.archive.org/web/20150525163055/http://www.intel.com/content/www/us/en/processors/itanium/itanium-9500-reference-manual.html?wapkw=intel+itanium+processor+family+reference+guide) --- Intel\'s official Itanium instruction set reference manual.

### [Loongson]

[[]][[#loongson](ircs://irc.libera.chat/#loongson)] ([[webchat](https://web.libera.chat/#loongson)])

[[]][r/loongson](https://reddit.com/r/loongson)

The first LoongArch CPU was released in 2021 by the privately owned but Chinese state-controlled company [Loongson Technology](https://en.wikipedia.org/wiki/Loongson "wikipedia:Loongson"). It is a 64-bit RISC design intended to compete with its modern Intel, ARM, and RISC-V counterparts domestically. Some server-class designs already exist and and future designs in defense and aerospace applications are anticipated. In addition Loongson intends to produce some LoonArch processors for some embedded applications and embrace and extend the [MIPS design](https://wiki.gentoo.org/wiki/Assembly_language#MIPS "Assembly language") for some others.

Learning LoongArch assembly language is a useful skill for any Gentoo user interested in the unique CPU design either as a learning exercise or one seeking to implement or improve a compiler on that platform as well as anyone interested in embedded aerospace or defense applications of this ISA. **Gentoo\'s LoongArch project is in its early days and would welcome new contributors.**

#### [[LoongArch](https://wiki.gentoo.org/wiki/Project:LoongArch "Project:LoongArch")]

-   [Kernel.org\'s Introduction to LoongArch](https://docs.kernel.org/loongarch/introduction.html)
-   [LoongArch Documentation](https://loongson.github.io/LoongArch-Documentation/README-EN.html) --- The official LoongArch ABI and instruction set documentation.
-   [The unofficial yet comprehensive FAQ for LoongArch](https://blog.xen0n.name/en/posts/tinkering/loongarch-faq/) --- an extensive FAQ written by Gentoo developer [Xen0n](https://wiki.gentoo.org/wiki/User:Xen0n "User:Xen0n") detailing the inner workings of the LoongArch design.
-   [List of LoongArch instructions](https://github.com/loongson-community/loongarch-opcodes) --- a resource produced by the community because the official LoongArch print manual has many errors and inconsistencies that were not caught prior to publication.

#### [[LoongISA](https://wiki.gentoo.org/wiki/Project:MIPS "Project:MIPS")]

The LoongISA is a superset of MIPS64, see the [MIPS Section](https://wiki.gentoo.org/wiki/Assembly_language#MIPS "Assembly language").

### [International Business Machines]

[International Business Machines](https://en.wikipedia.org/wiki/IBM "wikipedia:IBM") (IBM) introduced the System/390 mainframe series in 1990. It is an evolution of the [System/360](https://en.wikipedia.org/wiki/IBM_System/360_architecture "wikipedia:IBM System/360 architecture") with various models having different processor counts and system memory configurations based upon customer needs. The S/390 has the distinction of being the first high end mainframe build with processors implemented via [CMOS](https://en.wikipedia.org/wiki/CMOS "wikipedia:CMOS") fabrication. The S/390\'s architecture is multiple big endian 32-bit CISC processors with 64-bit floating point math support. Some models support as many as 10 single core processors and a (then staggering) 32-GB of RAM. The S/390 series was a highly successful product run and support was discontinued by IBM in 2004. Given the tendency of mainframe installations to greatly outlive their manufacturer support contracts it\'s no great surprise that some of these units remain in service. More than a few S/390 owners have chosen to migrate to Gentoo Linux for the remainder of their mainframe\'s useful service lives. Gentoo maintains a [[[sys-apps/s390-tools]](https://packages.gentoo.org/packages/sys-apps/s390-tools)[]] package which contains device drives and userspace tools unique to the architecture.

Those interested in the assembly language of the S/360 series are likely those with a history with --- or historical interest in --- mainframe architecture. **Gentoo\'s S/390 project would welcome new contributors!** For those without access to real hardware, the Hercules Emulator [[[app-emulation/hercules]](https://packages.gentoo.org/packages/app-emulation/hercules)[]], can handle most workloads on commonly available PC hardware.

#### [][[System/390](https://wiki.gentoo.org/wiki/Project:S390 "Project:S390")]

-   [Wikibooks: S/360 Assembly language](https://en.wikibooks.org/wiki/360_Assembly)
-   [Dave\'s z/Architecture Assembler FAQ](https://planetmvs.com/hlasm/s390faq.html)

### [MIPS Computer Systems]

[MIPS Technologies](https://en.wikipedia.org/wiki/MIPS_Technologies "wikipedia:MIPS Technologies") released the first MIPS microprocessor in 1985. Both 32-bit and 64-bit implementations of the ISA exist. It\'s an extremely well-studied design which has gone on to influence nearly all RISC designs that came after it. It originated as a high end sever design but found new life in later decades as a specifically embedded CPU. A great many network devices run MIPS processors.

Recently the MIPS corporation has shifted away from the MIPS architecture and has committed itself to designing RISC-V cores going forward. MIPS Open Architecture has a relatively permissive licensing terms and third parties, most notably Loongson, intend to continue to evolve the platform. MIPS remains a viable installation target for Gentoo Linux, that said **the Gentoo MIPS project welcomes new contributors.** Those wishing to learn MIPS assembly often do so in academic environments or as prospective embedded systems programmers, most commonly targeting network appliances.

#### [[MIPS](https://wiki.gentoo.org/wiki/Project:MIPS "Project:MIPS")]

[[]][r/mips64](https://reddit.com/r/mips64)

-   [MIPS32 official Architecture documentation](https://www.mips.com/products/architectures/mips32-2/).
-   [Wikibooks: MIPS Assembly](https://en.wikibooks.org/wiki/MIPS_Assembly).
-   [MIPS32 Instruction Set Quick Reference](https://courses.cs.duke.edu/spring20/compsci250d/MIPS32_QRC.pdf) (PDF) --- a printable MIPS32 instruction set cheat sheet.
-   [Rosetta Code: MIPS Assembly](https://rosettacode.org/wiki/Category:MIPS_Assembly) --- links to articles on how to perform various programming tasks and build common data structures on that architecture.

### [Sun Microsystems]

[Sun Microsystems](https://en.wikipedia.org/wiki/Sun_Microsystems "wikipedia:Sun Microsystems") released the first SPARC processor in 1987 for its line of servers. While both their designs have similarities, SPARC is more of a descendant of Berkeley RISC than it is MIPS. Early SPARC processors were 32-bit big endian processors. Later processors were biendian and 64-bit. Oracle, who acquired Sun, ceased development of the SPARC processor in 2017. The last remaining SPARC producer, Fujitsu, is currently in the process of ending production of SPARC hardware and shifting towards the production of ARM CPU\'s.

A large number of high end workstations and servers running SPARC processors exist on the secondary (used) market, most of them perfectly suitable as Gentoo installation targets. **The Gentoo SPARC team would welcome new contributors.** Knowledge of SPARC is useful to anyone who seeks to broaden their knowledge of the inner workings of an interesting RISC ISA.

#### [[SPARC](https://wiki.gentoo.org/wiki/Project:SPARC "Project:SPARC")]

[[]][[#sparc](ircs://irc.libera.chat/#sparc)] ([[webchat](https://web.libera.chat/#sparc)])

-   [SPARC Assembly Language Reference Manual](https://docs.oracle.com/cd/E19641-01/802-1947/802-1947.pdf) --- Sun\'s official assembly language reference manual for the SPARC architecture.
-   [Rosetta Code: SPARC_Assembly](https://rosettacode.org/wiki/Category:SPARC_Assembly) --- a handful of articles on SPARC assembly.

### [][University of California, Berkeley]

RISC-V began as a project for at the University of California, Berkeley in 2010 as an effort to produce an open standard ISA. There are 32-bit and 64-bit variants. In addition to the core instruction set, RISC-V\'s modular design allows it to be easily extended to add custom features. RISC-V is a workable installation target for Gentoo Linux, but it is not yet considered stable. **The Gentoo RISC-V project is seeking volunteers to join its ranks** as it\'s hard to keep up with everything happening in the RISC-V space. The RISC-V ISA is experiencing a tsunami of rapid growth in the single board computer and embedded markets. Server versions of the chip, including those that support virtualization, are already in development.

Those seeking to learn RISC-V assembly may do so for any number of reasons. A working knowledge of RISC-V assembly language can open doors in multiple market segments.

#### [[RISC-V](https://wiki.gentoo.org/wiki/Project:RISC-V "Project:RISC-V")]

[[]][[#riscv](ircs://irc.libera.chat/#riscv)] ([[webchat](https://web.libera.chat/#riscv)])

[[]][r/RISCV](https://reddit.com/r/RISCV)

Has its own syntax, not AT&T or Intel (from [comment](https://github.com/riscv-collab/riscv-gnu-toolchain/issues/1008#issuecomment-1006988287)):

> I\'d just call it \"RISC-V syntax\". No [\$] on register specifiers; operand order is normally [dest], [src].

-   [*The RISC-V Instruction Set Manual Volume I: User-Level ISA*](https://github.com/riscv/riscv-isa-manual/releases/download/Ratified-IMAFDQC/riscv-spec-20191213.pdf)
-   [The *RISC-V Instruction Set Manual Volume II: Privileged Specification*](https://github.com/riscv/riscv-isa-manual/releases/download/Priv-v1.12/riscv-privileged-20211203.pdf)
-   [Rosetta Code: RISC-V Assembly](https://rosettacode.org/wiki/Category:RISC-V_Assembly) --- links to articles on how to perform various programming tasks and build common data structures on that architecture.
-   [RISC-V assembly programmer\'s manual](https://github.com/riscv-non-isa/riscv-asm-manual/blob/master/riscv-asm.md) (CC-BY 4.0) --- official guide.
-   [RISC-V assembly language programming](https://github.com/johnwinans/rvalp) (CC-BY-4.0) --- book rvalp.pdf, including tables \"RV32I reference cards\".
-   [RISC-V dependent features](https://sourceware.org/binutils/docs/as/RISC_002dV_002dDependent.html) --- from \"Using GNU as\".
-   [RISC-V assembly style guide](https://opentitan.org/book/doc/contributing/style_guides/asm_coding_style.html) (Apache-2.0 license) --- from OpenTitan project.
-   [User:Vazhnov/PlatformIO + VIM + ccls + Sipeed Longan nano RISC-V](https://wiki.gentoo.org/wiki/User:Vazhnov/PlatformIO_%2B_VIM_%2B_ccls_%2B_Sipeed_Longan_nano_RISC-V "User:Vazhnov/PlatformIO + VIM + ccls + Sipeed Longan nano RISC-V") --- example

### [[Embedded Processors and Microcontrollers](https://wiki.gentoo.org/wiki/Project:Embedded "Project:Embedded")]

[[]][[#embedded](ircs://irc.libera.chat/#embedded)] ([[webchat](https://web.libera.chat/#embedded)])

[[]][[comp.arch.embedded](news:comp.arch.embedded) ([weblink](https://www.novabbs.com/devel/thread.php?group=comp.arch.embedded))]

[[]][r/embedded](https://reddit.com/r/embedded)

In modern usage a **microcontroller** is not just an ultra low-spec CPU contemporary standards. Modern microcontrollers are processors with their own RAM and ROM on a single package. This isn\'t quite the same thing as a System on a Chip, but the two concepts are similar and both exist with the goal of reducing total chip count to reduce production cost. A good many CPU\'s that are now only produced exclusively as micocontrolers or even just FPGA cores were once considered powerful enough to be the CPU of one or more lines of home computer. Edge cases exist, but in general most microcontrollers do not make good Gentoo Linux installation targets --- even with a [binhost](https://wiki.gentoo.org/wiki/Binary_package_guide "Binary package guide") providing the heavy lifting required to compile packages.

One of the few CPU\'s on this list that can *theoretically* support a Gentoo Linux install, provided it has enough RAM, is the [Motorola M68k](https://wiki.gentoo.org/wiki/Project:M68k "Project:M68k") but doing so is considered *highly* experimental.

#### [Atmel AVR]

[Atmel](https://en.wikipedia.org/wiki/Atmel "wikipedia:Atmel") introduced the AVR microcontroller in 1997 and is among the first microcontrollers to contain on-ship flash memory, a practice that is now standard. The original model is an 8-bit RISC design of which the ATmega8 variant, popularized by early Arduino models, is perhaps the best known. The 32-bit AVR32, also produced by Atmel, bears little actual resemblance to its 8-bit counterpart. While Atmel has largely switched to producing ARM processors, 8-bit AVR microcontrollers are still produced in large numbers. Those interested in early Arduino single board computers or hardware hacking more generally will likely be among those who find AVR assembly language useful.

-   [Atmel AVR Instruction Set Manual](https://ww1.microchip.com/downloads/en/devicedoc/atmel-0856-avr-instruction-set-manual.pdf) (PDF).
-   [Wikibooks: Embedded Systems --- Atmel AVR](https://en.wikibooks.org/wiki/Embedded_Systems/Atmel_AVR).

#### [Microchip Technology PIC]

[[]][[#pic](ircs://irc.libera.chat/#pic)] ([[webchat](https://web.libera.chat/#pic)])

-   [PIC Programming in Assembly](https://groups.csail.mit.edu/lbr/stack/pic/pic-prog-assembly.pdf) (PDF) --- a series of 12 tutorials in PIC microcontroller assembly.
-   [*dsPIC30F/33F Programmer's Reference Manual*](https://ww1.microchip.com/downloads/en/DeviceDoc/70157C.pdf) --- the official instruction manual for PIC microcontroller assembly language.

#### [MOS Technology 65*xx*]

[[]][[#6502](ircs://irc.libera.chat/#6502)] ([[webchat](https://web.libera.chat/#6502)])

[[]][r/mos_6502](https://reddit.com/r/mos_6502)

The [6502](https://en.wikipedia.org/wiki/MOS_Technology_6502 "wikipedia:MOS Technology 6502") was an early 8-bit processor produced by [MOS Technology](https://en.wikipedia.org/wiki/MOS_Technology "wikipedia:MOS Technology"). It was the first successful example of a simple \"low spec\" processor. As it was extraordinarily inexpensive to produce, consequently it made its way into dozens of 1970\'s and 1980\'s home computers. Eventually, MOS was acquired by [Commodore Semiconductor Group](https://en.wikipedia.org/wiki/Commodore_International "wikipedia:Commodore International") who produced a number of variants of the chip, notably the 6510 for the [Commodore 64](https://en.wikipedia.org/wiki/Commodore_64 "wikipedia:Commodore 64"). After Commodore\'s bankruptcy [Western Design Center](https://en.wikipedia.org/wiki/Western_Design_Center "wikipedia:Western Design Center") acquired the rights to the 6502. It now produces a number of variants of the processor, including 16-bit derivatives. The 6502 continues to be produced in great numbers and it is found in many embedded devices to this day. Today 65*xx* processors are embedded in thousands of devices, many of them peripherals. Static core variants of the processor are heavily used in implanted medical devices, due their ability to consume no power in a sleep state and wait for an externally triggered interrupt from an attached sensor. Those interested in 6502 assembly run the gamut from retrocomputing enthusiasts to hardware design engineers.

-   [6502.org](http://6502.org/) --- a resource for people interested in building hardware or writing software for the 6502 microprocessor and its relatives.
-   *Programming the 6502* by Rodnay Zaks --- generally considered \"the 6052 Bible.\" It was very often used in undergraduate courses on 6502 assembly programming. This text is widely available on the secondary (used) market.
-   [*NMOS 6510 Unintended Opcodes: No More Secrets, v0.96 (2021-12-24)*](https://codebase64.org/lib/exe/fetch.php?media=base:nomoresecrets-nmos6510unintendedopcodes-20212412.pdf) (PDF) --- provides unprecedented details into how the 6502/6510\'s (in)famous \"undocumented opcodes\" work. This text is only relevant for the NMOS variants of the 6502 and 6510, common in 1980\'s home computers. Modern CMOS derivatives of the 65*xx* produced by the [Western Design Center](https://en.wikipedia.org/wiki/Western_Design_Center "wikipedia:Western Design Center") removed these.
-   [Western Design Center 65*xx* Resources](https://www.westerndesigncenter.com/wdc/documentation.php) --- including datasheets and official manuals.
-   [Wikibooks 6502 Assembly](https://en.wikibooks.org/wiki/6502_Assembly) --- a long one-page primer on 6502 assembly.
-   [Nerdy Nights Tutorial](https://nerdy-nights.nes.science/#main_tutorial) --- a series of articles intended to bring the reader up to speed on the 6502 over the course of a few week. This article is popular with the NES and SNES development crowd.
-   [6502 Instruction Set](https://www.masswerk.at/6502/6502_instruction_set.html) --- a through and highly readable overview of the original 6502 processor\'s instructions, including undocumented instructions. The document does not cover the instructions added to CMOS variants of the chip.
-   [Rosetta Code: 6502 Assembly](https://rosettacode.org/wiki/Category:6502_Assembly) --- a fairly substantial introduction to 6502 assembly followed by links to articles on how to perform various programming tasks and build common data structures on that architecture.

##### [Emulators]

-   [lib6502](https://www.piumarta.com/software/lib6502/) --- C-based emulator.
-   [py65](https://github.com/mnaberez/py65) - Python-based emulator ([[[dev-python/py65::pypi]](https://gpo.zugaina.org/Overlays/pypi/dev-python/py65)[]]).
-   [cl-6502](https://github.com/redline6561/cl-6502) - Common-Lisp-based emulator.

#### [[Motorola M68k](https://wiki.gentoo.org/wiki/Project:M68k "Project:M68k")]

[[]][[#mac68k](ircs://irc.libera.chat/#mac68k)] ([[webchat](https://web.libera.chat/#mac68k)])

[[]][[comp.sys.m68k](news:comp.sys.m68k) ([weblink](https://www.novabbs.com/devel/thread.php?group=comp.sys.m68k))]

[[]][r/m68k](https://reddit.com/r/m68k)

[Motorola](https://en.wikipedia.org/wiki/Motorola "wikipedia:Motorola") produced the original [M68k](https://en.wikipedia.org/wiki/Motorola_68000_series "wikipedia:Motorola 68000 series") series of microprocessors. That IP was sold to [Freescale Semiconductor](https://en.wikipedia.org/wiki/Freescale_Semiconductor "wikipedia:Freescale Semiconductor") which produces the [Freescale 683XX](https://en.wikipedia.org/wiki/Freescale_683XX "wikipedia:Freescale 683XX") which is backwards compatible with the original M68k line and is still produced in large numbers. Freescale eventually merged with [NXP Semiconductor](https://en.wikipedia.org/wiki/NXP_Semiconductor "wikipedia:NXP Semiconductor"). Hence, NXP\'s website hosting content that asserts a Motorola or a Freescale copyright and references to Freescale processors with M68k instructions.

-   [*Motorola M68000 Family Programmer\'s Reference Manual*](https://www.nxp.com/docs/en/reference-manual/M68000PRM.pdf) by Motorola (PDF) --- The official programmer\'s reference manual.
-   [Rosetta Code: M68k Assembly](https://rosettacode.org/wiki/Category:6800_Assembly) --- links to articles on how to perform various programming tasks and build common data structures on that architecture.

#### [Zilog Z80]

[Zilog](https://en.wikipedia.org/wiki/Zilog "wikipedia:Zilog")\'s Z80 processor entered in serial production in 1976. Ever since, the chip has been in continuous production in various form factors. Early in its history, the Z80 was a major player in the business and home microcomputer market thanks to the rise of [CP/M](https://en.wikipedia.org/wiki/CP/M "wikipedia:CP/M"), an early operating system that became a standard for almost a decade. Today, the Z80 and its variants are found in the majority of consumer electronics either as the device\'s CPU or as a support processor. Z80 assembly language is a desirable skill for those seeking to develop skills useful to the consumer embedded electronics market segment.

-   *Programming the Z80* by Rodnay Zaks --- generally considered a seminal manual on the inner workings of the Z80. It was very often used in undergraduate courses on Z80 assembly programming. This text is widely available on the secondary (used) market.
-   [*The Undocumented Z80 Documented*](https://www.myquest.nl/z80undocumented/) by by Sean Young and Jan Wilmans --- a comprehensive analysis of unintentionally created opcodes on the Z80. Like its 6502 counterpart, it\'s mostly only relevant for early models of the processor.
-   [Rosetta Code: Z80 Assembly](https://rosettacode.org/wiki/Category:Z80_Assembly) --- a short introduction to Z80 assembly followed by links to articles on how to perform various programming tasks and build common data structures on that architecture.

### [Virtual Machine Assembly Languages]

The two most significant virtual machines that run byte code, effectively machine language for the VM, are Java and WebAssembly. Java, for better or worse, is ubiquitous in modern Enterprise computing. Further, use of Java is ubiquitous in mobile computing. While no CPU\'s presently exist that have an ISA that maps directly to Java byte code, Java performance is a major consideration for nearly all modern processor designs.

WebAssembly is a virtual machine execution environment primarily targeting modern Web Browsers. This is distinct from a web browsers two other virtual machines, those being its rendering engine and its JavaScript execution environment. WebAssembly is marketed as allowing web-based application code to be executed at near-native speed.

Direct assembly or disassembly is rare and primarily limited to debugging. In both cases, the respective virtual machine byte codes are primarily intended as compilation targets.

#### [[Java Bytecode](https://wiki.gentoo.org/wiki/Project:Java "Project:Java")]

[[]][[#java](ircs://irc.libera.chat/#java)] ([[webchat](https://web.libera.chat/#java)])

[[]][[comp.lang.java.help](news:comp.lang.java.help) ([weblink](https://www.novabbs.com/devel/thread.php?group=comp.lang.java.help))]

[[]][r/javahelp](https://reddit.com/r/javahelp)

-   [How to write a (toy) JVM](https://zserge.com/posts/jvm/) --- details the inner workings of the JVM.
-   [Chocopy Hacking Part 2: Compiling to JVM](https://yangdanny97.github.io/blog/2021/08/26/chocopy-jvm-backend)
-   [Wikipedia\'s list of List of Java Bytecode Instructions](https://en.wikipedia.org/wiki/List_of_Java_bytecode_instructions)

#### [WebAssembly]

[[]][[#wasm](ircs://irc.libera.chat/#wasm)] ([[webchat](https://web.libera.chat/#wasm)])

[[]][r/wasm](https://reddit.com/r/wasm)

-   [WebAssembly Specifications](https://webassembly.github.io/spec/) --- the official web assembly specification documents.
-   [*WebAssembly Reference Manual*](https://github.com/sunfishcode/wasm-reference-manual) --- An in-depth reference manual for those wishing to understand how the WebAssembly runtime works, or are writing a compiler, or want to try developing directly in WebAssembly.
-   [Mozilla\'s WebAssembly developer documentation](https://developer.mozilla.org/en-US/docs/WebAssembly)

#### [uxntal]

**uxntal** is an assembly language for [the Uxn virtual computer](https://100r.co/site/uxn.html).

-   [uxn design](https://100r.co/site/uxn_design.html) --- an introduction to the background and design of uxn.
-   [uxntal](https://wiki.xxiivv.com/site/uxntal.html) - an introduction to the uxntal language.
-   [Learn Uxntal in Y Minutes](https://learnxinyminutes.com/uxntal/) - uxntal page on \"Learn X in Y minutes\" site.

## [See also]

-   [Binutils](https://wiki.gentoo.org/wiki/Binutils "Binutils") --- a set of tools for creating and manipulating certain types of [binary files](https://en.wikipedia.org/wiki/binary_files "wikipedia:binary files").
-   [C](https://wiki.gentoo.org/wiki/C "C") --- a programming language developed for Bell Labs in the early 1970s
-   [C++](https://wiki.gentoo.org/wiki/C%2B%2B "C++") --- a general-purpose programming language that originated from C
-   [Fortran](https://wiki.gentoo.org/wiki/Fortran "Fortran") --- a general-purpose, compiled imperative programming language that is especially suited to numeric computation and scientific computing.
-   [Forth](https://wiki.gentoo.org/wiki/Forth "Forth") --- a heavily stack-oriented self-compiling procedural programming language that is only slightly more abstract than [assembly](https://wiki.gentoo.org/wiki/Assembly_language "Assembly language").
-   [Rust](https://wiki.gentoo.org/wiki/Rust "Rust") --- a general-purpose, multi-paradigm, compiled, programming language.

## [External resources]

-   [Rosetta Code](https://rosettacode.org/wiki/Rosetta_Code) --- How to perform many common tasks in an extraordinary range of programming languages.
-   [Build an 8-bit computer from scratch](https://eater.net/8bit) --- Details how to create a CPU from TTL logic chips, in the process defining a completely custom instruction set to go with it.
-   [How do CPUs read machine code?](https://www.youtube.com/watch?v=yl8vPW5hydQ) (YouTube)
-   [How To Write a Computer Emulator](https://fms.komkon.org/EMUL8/HOWTO.html) --- Tangential, but useful for solidifying various low-level concepts related to how CPU\'s and hardware timings. It discusses CPU and memory access operations in terms familiar to C programmers.