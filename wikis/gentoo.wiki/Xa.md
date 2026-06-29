[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Xa&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

[] This article has been flagged for not conforming to the [wiki guidelines](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Guidelines "Gentoo Wiki:Guidelines") ([missing lead-in sentences](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Guidelines#Use_lead-in_sentences "Gentoo Wiki:Guidelines")). Please [help Gentoo out](https://wiki.gentoo.org/wiki/Help_improve_Gentoo_by_getting_involved_with_documentation!#Make_articles_conform_to_the_guidelines "Help improve Gentoo by getting involved with documentation!") by starting fixing things.

**Resources**

[[]][Home](https://www.floodgap.com/retrotech/xa/)

[[]][Package information](https://packages.gentoo.org/packages/dev-embedded/xa)

[[]][[#asm](ircs://irc.libera.chat/#asm)] ([[webchat](https://web.libera.chat/#asm)])

**[xa]** is a high-speed, two-pass portable cross-assembler for the 6502 CPU with a C-like preprocessor. One of several popular 65xx assemblers, xa is written in C and released under the GPL-2. It has been in continuous development since 1989.

Other tools in the xa package are:

-   [file65] --- a tool for printing information about o65 object files.
-   [ldo65] --- a linker for o65 object files.
-   [printcbm] --- a simple CBM BASIC detokenizer similar to the far more powerful [petcat] proviced by [VICE](https://wiki.gentoo.org/wiki/VICE "VICE").
-   [reloc65] --- a relocator for o65 object files.
-   [uncpk] --- a c64 cpk archive manager.

While xa does not currently have a dissassembler as part of its suite, [dxa] is currently under development separately and will be merged into xa once it becomes stable.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Emerge]](#Emerge)
-   [[2] [Usage]](#Usage)
    -   [[2.1] [Invocation]](#Invocation)
-   [[3] [Removal]](#Removal)
    -   [[3.1] [Unmerge]](#Unmerge)
-   [[4] [See also]](#See_also)
-   [[5] [External resources]](#External_resources)

## [Installation]

### [Emerge]

`root `[`#`]`emerge --ask dev-embedded/xa`

## [Usage]

### [Invocation]

`user `[`$`]`xa --help`

    Usage: xa [options] file
    Cross-assembler for 65xx/R65C02/65816

     -v           verbose output
     -C           no CMOS-opcodes
     -W           no 65816-opcodes (default)
     -w           allow 65816-opcodes
     -B           show lines with block open/close
     -c           produce `o65' object instead of executable files (i.e. don't link)
     -o filename  sets output filename, default is `a.o65'
                    A filename of `-' sets stdout as output file
     -e filename  sets errorlog filename, default is none
     -l filename  sets labellist filename, default is none
     -r           adds crossreference list to labellist (if `-l' given)
     -M           allow ``:'' to appear in comments for MASM compatibility
     -R           start assembler in relocating mode
     -Llabel      defines `label' as absolute, undefined label even when linking
     -b? addr     set segment base address to integer value addr
                    `?' stands for t(ext), d(ata), b(ss) and z(ero) segment
                    (address can be given more than once, last one is used)
     -A addr      make text segment start at an address that when the _file_
                    starts at addr, relocation is not necessary. Overrides -bt
                    Other segments must be specified with `-b?'
     -G           suppress list of exported globals
     -p?          set preprocessor character to ?, default is #
     -DDEF=TEXT   defines a preprocessor replacement
     -Ocharset    set output charset (PETSCII, ASCII, etc.), case-sensitive
     -Idir        add directory `dir' to include path (before XAINPUT)
      --version   output version information and exit
      --help      display this help and exit
    == These options are deprecated and will be removed in 2.4+! ==
     -x           old filename behaviour (overrides `-o', `-e', `-l')
     -S           allow preprocessor substitution within strings

## [Removal]

### [Unmerge]

`root `[`#`]`emerge --ask --depclean --verbose dev-embedded/xa`

## [See also]

-   [VICE](https://wiki.gentoo.org/wiki/VICE "VICE") --- the **V**ersat**I**le **C**ommodore **E**mulator for Commodore computers of the 8-bit era

## [External resources]

-   [cc65](https://cc65.github.io/) --- a powerful [C](https://wiki.gentoo.org/wiki/C "C") cross compiler targeting most known 65*xx*-based computers.
-   [64tass](http://tass64.sourceforge.net/) --- an expressive 6502 assembler with a TASM-like syntax.
-   [Codebase64](https://codebase64.org/) --- a wiki devoted to C64 development.
-   [C64 Wiki](https://www.c64-wiki.com/) --- a wiki devoted the Commodore 64 more generally.