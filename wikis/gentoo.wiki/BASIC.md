[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=BASIC&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Wikipedia](https://en.wikipedia.org/wiki/Forth_(programming_language) "wikipedia:Forth (programming language)")

[[]][[#basic](ircs://irc.libera.chat/#basic)] ([[webchat](https://web.libera.chat/#basic)])

[[]][[#freebasic](ircs://irc.libera.chat/#freebasic)] ([[webchat](https://web.libera.chat/#freebasic)])

[[]][[comp.lang.basic.misc](news:comp.lang.basic.misc) ([weblink](https://www.novabbs.com/devel/thread.php?group=comp.lang.basic.misc))]

[[]][[alt.lang.basic](news:alt.lang.basic) ([weblink](https://www.novabbs.com/devel/thread.php?group=alt.lang.basic))]

[[]][r/Basic](https://reddit.com/r/Basic)

**BASIC**, short for **B**eginners **A**ll-**P**urpose **S**ymbolic **I**nstruction **C**ode, is a programming language that was created in 1964 to enable college and university students without a STEM background to write software. Early versions of BASIC were interpreted and ran on time-sharing mainframe systems. Code was often input on teletype systems --- essentially fancy printers that both displayed terminal output and took input from the user. Eventually this gave way to small \"glass teletypes,\" that is, early CRT monitors.

## Contents

-   [[1] [History]](#History)
-   [[2] [Modern Use]](#Modern_Use)
-   [[3] [BASIC on Gentoo]](#BASIC_on_Gentoo)
-   [[4] [See also]](#See_also)
-   [[5] [External resources]](#External_resources)

### [History]

The first dialects of BASIC were imperative in nature but not structured. That is, they lacked support for subroutines with signatures and return values. Use of line numbers as `GOTO` jump targets resulted in difficult to follow \"spaghetti code.\" Soon, on mainframe platforms at least, compiled dialects of BASIC became reasonably common. Some of these dialects retained the need for line-numbers, others used text-based line labels on an as-needed basis to allow the programmer to specify a jump target with a human readable name. This soon gave way to more structured ways of writing BASIC code.

From the late 1970\'s, at the dawn of the microcomputer revolution, early home-based computers with mere kilobytes of RAM often came with primitive versions of BASIC built into the system ROM. (A rare few preferred [Forth](https://wiki.gentoo.org/wiki/Forth "Forth") instead.) Most of these interpreters were extremely spartan, owing to the memory and processing limitations of the day. Some versions of BASIC supported only integer math, while others fully supported floating point arithmetic. Some systems even lacked support for lower-case letters. Nearly all had reverted to line-number only versions of BASIC that indirectly discouraged structured programming.

At the time BASIC was seen as the Esperanto of programming languages. In theory, it was a nearly universal programming language among microcomputers. In practice, a unified BASIC standard did not exist and each microcomputer manufacturer added its own proprietary extensions for various reasons. This resulted in many dialects of basic that were similar, but just different enough to cause headaches for programmers porting programs between systems. Worse, moving source code between similar systems was problematic for several reasons: First, BASIC programs were not typically stored in plain text, there were very often [tokenized](https://en.wikipedia.org/wiki/Lexical_analysis "wikipedia:Lexical analysis"). Each keyword corresponded to a single 8-bit value, typically somewhere between `0x80`--`0xff`, but keyword mappings to byte assignments were not standardized. Second, disk formats were nothing if not incompatible and computer networks were uncommon at the time. So, even if existing tokenized source code could be converted to the target format physically getting it onto the target platform had its own challenges. This very often lead to source code being printed out and manually retyped on the target system followed by *many* rounds of debugging.

Throughout the 1980\'s and 1990\'s BASIC began to evolve. Some versions of the language were embedded into larger applications, others were intended for business use and supported both structured programming and object oriented paradigms. By the dawn of the world wide web, BASIC had lost most of its market share except as an introductory language to teach novice programmers. Serious business application development had shifted from compiled BASIC to COBOL and then to Java. System administration and reporting tasks had shifted from interpreted dialects of BASIC to [Perl](https://wiki.gentoo.org/wiki/Perl "Perl") and shell scripts.

By the mid 1990\'s, these pressures forced BASIC to evolve. BASIC was forced to become structured, which allowed libraries (modules) to be shared among serious BASIC enthusiasts. Eventually, structured BASIC gave way to object oriented dialects of the language.

### [Modern Use]

The sun has not set on BASIC. While it is true that [Python](https://wiki.gentoo.org/wiki/Python "Python") has dethroned BASIC as the preferred introductory programming language, different BASIC dialects are still popular among some small business, hobbyists, and novice programmers. Perhaps surprisingly, modern BASIC dialects continue to live on and evolve in an embedded context within larger applications, most notably spreadsheets.

### [BASIC on Gentoo]

Gentoo has a number of BASIC interpreters and compilers, each with its own niche:

  ----------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Name                                                              Package                                                                                                                                                                                                                                                                                                                                                                                    Description
  bas                                                               [[[dev-lang/bas]](https://packages.gentoo.org/packages/dev-lang/bas)[]]                                 An open source classic BASIC dialect very much in the mold of the 1980\'s microcomputer era.
  bwbasic                                                           [[[dev-lang/bwbasic::myov]](https://repos.gentoo.org/#myov)[]]                                      A Bywater interpreter for the BASIC programming language.
  [FreeBASIC](https://wiki.gentoo.org/wiki/FreeBASIC "FreeBASIC")   [[[dev-lang/fbc::guru]](https://github.com/gentoo-mirror/guru/tree/master/dev-lang/fbc)[]]              A popular modern cross-platform Object Oriented BASIC compiler with an optional [QuickBASIC](https://en.wikipedia.org/wiki/QuickBASIC "wikipedia:QuickBASIC") compatibility mode.
  LibreOffice BASIC                                                 [[[app-office/libreoffice]](https://packages.gentoo.org/packages/app-office/libreoffice)[]]   An office suite with its own [dialect of BASIC](https://wiki.documentfoundation.org/Documentation/BASIC_Guide) for internal application scripting.
  mono-basic                                                        [[[dev-lang/mono-basic]](https://packages.gentoo.org/packages/dev-lang/mono-basic)[]]            Mono BASIC is an open source [VB.NET](https://en.wikipedia.org/wiki/Visual_Basic_(.NET) "wikipedia:Visual Basic (.NET)") compiler with full object oriented BASIC support that integrates well with other languages that use the [Mono](https://wiki.gentoo.org/index.php?title=Mono&action=edit&redlink=1 "Mono (page does not exist)") runtime.
  yabasic                                                           [[[dev-lang/yabasic::myov]](https://repos.gentoo.org/#myov)[]]                                      Traditional interpreter for the BASIC language.
  ----------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## [See also]

-   [Assembly Language](https://wiki.gentoo.org/wiki/Assembly_Language "Assembly Language") --- the lowest level of all programming languages, typically represented as a series of CPU architecture specific mnemonics and related operands.
-   [COBOL](https://wiki.gentoo.org/index.php?title=COBOL&action=edit&redlink=1 "COBOL (page does not exist)")
-   [Forth](https://wiki.gentoo.org/wiki/Forth "Forth") --- a heavily stack-oriented self-compiling procedural programming language that is only slightly more abstract than [assembly](https://wiki.gentoo.org/wiki/Assembly_language "Assembly language").
-   [FreeBASIC](https://wiki.gentoo.org/wiki/FreeBASIC "FreeBASIC") --- a modern, self-hosting, object oriented, [BASIC] compiler that is optionally backwards compatible with [QuickBASIC](https://en.wikipedia.org/wiki/QuickBASIC "wikipedia:QuickBASIC")
-   [FORTRAN](https://wiki.gentoo.org/index.php?title=FORTRAN&action=edit&redlink=1 "FORTRAN (page does not exist)")
-   [Pascal](https://wiki.gentoo.org/index.php?title=Pascal&action=edit&redlink=1 "Pascal (page does not exist)")

## [External resources]

-   [FreeBASIC Manual](https://www.freebasic.net/wiki/DocToc) --- an in-depth language reference for the FreeBASIC language.
-   [LibreOffice BASIC Programming Guide](https://wiki.documentfoundation.org/Documentation/BASIC_Guide) --- This dialect of BASIC is used extensively by LibreOffice as an embedded scripting language.
-   [C64 Wiki\'s BASIC v2 Guide](https://www.c64-wiki.com/wiki/BASIC) --- A detailed series of articles on a interpreted dialect of BASIC that was extremely popular in the early home microcomputing era of the late 1970\'s and early 1980\'s.
-   [BASIC Computer Games](https://github.com/coding-horror/basic-computer-games) --- ports of [David H. Ahl](https://en.wikipedia.org/wiki/David_H._Ahl "wikipedia:David H. Ahl")\'s tremendously influential *[BASIC Computer Games](https://en.wikipedia.org/wiki/BASIC_Computer_Games "wikipedia:BASIC Computer Games")* to modern memory-safe programming languages. Original BASIC sources receive bug fixes and quality of life improvements. Ports to other languages tend to be in modern [idiomatic](https://en.wikipedia.org/wiki/Programming_idiom "wikipedia:Programming idiom") programing styles of the target language with through comments to act a learning aid.
-   [Tokenized BASIC](http://fileformats.archiveteam.org/wiki/Tokenized_BASIC) (HTTP) --- details the structure of microcomputer BASIC file formats which usually represented BASIC keywords as single 8-bit values, called [tokens](https://en.wikipedia.org/wiki/Lexical_analysis "wikipedia:Lexical analysis"), to speed parsing and save memory.
-   [BASIC (Re)Numbering with Commodore](https://www.masswerk.at/nowgobang/2020/commodore-basic-renumber) --- A detailed analysis of BASIC lines as they exist in a linked-list of tokenized values. The article focuses on Commodore BASIC, but these implementation details were common to many early BASIC interpreters.