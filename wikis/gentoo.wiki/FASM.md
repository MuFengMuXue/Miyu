[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=FASM&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Home](https://flatassembler.net/)

[[]][Wikipedia](https://en.wikipedia.org/wiki/FASM "wikipedia:FASM")

[[]][[#asm](ircs://irc.libera.chat/#asm)] ([[webchat](https://web.libera.chat/#asm)])

**FASM** is a fast assembly language compiler for the x86 architecture processors, which does multiple passes to optimize the size of generated machine code. It is self-compilable and versions for different operating systems are provided. All the versions are designed to be used from the system command line and they should not differ in behavior. This program is written by Tomasz Grysztar.

Actually 3 different flat assembly exist, the most famous and old one ***FASM***, the newer one ***FASMG*** and the most recent ***FASMG2***.

## [Installation]

### [Emerge]

To install dev-lang/fasm-bin or dev-lang/fasmg-bin, add [an overlay which provides them](https://gpo.zugaina.org/Search?search=fasm%7C).

Using [eselect repository](https://wiki.gentoo.org/wiki/Eselect/Repository "Eselect/Repository"):

`root `[`#`]`eselect repository add piniverlay git `[`https://github.com/pinicarus/gentoo-overlay.git`](https://github.com/pinicarus/gentoo-overlay.git)` `

`root `[`#`]`emaint sync -r piniverlay `

`root `[`#`]`emerge --ask fasm `

## [Usage]

To get information about optional settings after compilation, just type this command in a terminal:

`user `[`$`]`fasm`

    flat assembler  version 1.73.16
    usage: fasm <source> [output]
    optional settings:
     -m <limit>         set the limit in kilobytes for the available memory
     -p <limit>         set the maximum allowed number of passes
     -d <name>=<value>  define symbolic variable
     -s <file>          dump symbolic information for debugging

`user `[`$`]`fasmg `

flat assembler version g.jmhx

Usage: fasmg source \[output\] Optional settings:

       -p limit    Set the maximum allowed number of passes (default 100)
       -e limit    Set the maximum number of displayed errors (default 1)
       -r limit    Set the maximum depth of stack (default 10000)
       -v flag     Enable or disable showing all lines from the stack (default 0)
       -i command  Insert instruction at the beginning of source

-n Do not show logo nor summary