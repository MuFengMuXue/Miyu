[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=FreeBASIC&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Home](https://www.freebasic.net/)

[[]][Official documentation](https://www.freebasic.net/wiki/DocToc)

[[]][Wikipedia](https://en.wikipedia.org/wiki/FreeBASIC "wikipedia:FreeBASIC")

[[]][GitHub](https://github.com/freebasic/fbc)

[[]][[#freebasic](ircs://irc.libera.chat/#freebasic)] ([[webchat](https://web.libera.chat/#freebasic)])

**FreeBASIC** is a modern, self-hosting, object oriented, [BASIC](https://wiki.gentoo.org/wiki/BASIC "BASIC") compiler that is optionally backwards compatible with [QuickBASIC](https://en.wikipedia.org/wiki/QuickBASIC "wikipedia:QuickBASIC"). Nonetheless, FreeBASIC is an evolution of the BASIC programming language in its own right. While operating in native mode, FreeBASIC provides for namespaces, object oriented programming, memory pointers, function overloading, inline assembly, and a C-style preprocessor.

In QBASIC compatibility mode FreeBASIC is highly compatible with Microsoft QuickBASIC, allowing many legacy BASIC programs targeting the QuickBASIC interpreter to compile and run unaltered or with trivial modification. Additionally, there is a hybrid *fblite* mode that keeps some measure of QuickBASIC compatibility while enabling a subset of modern features from FreeBASIC\'s native mode. This permits the gradual modernization of an existing BASIC codebase.

FreeBASIC is a low-level compiler with capabilities similar to that of C. Unlike other BASIC dialects it is neither interpreted nor garbage collected. Its only runtime requirement is a C runtime library such as [glibc](https://wiki.gentoo.org/wiki/Glibc "Glibc"). Eventually this requirement will be phased out, in favor of its native runtime [fbrtLib](https://github.com/ImortisInglorian/fbrtLib). FreeBASIC runs on multiple platforms including Linux and Microsoft Windows; even the [MS-DOS](https://en.wikipedia.org/wiki/MS-DOS "wikipedia:MS-DOS") port is still maintained.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
-   [[2] [Usage]](#Usage)
    -   [[2.1] [Invocation]](#Invocation)
-   [[3] [Troubleshooting]](#Troubleshooting)
    -   [[3.1] [I Typed-In a BASIC Program From an Old Book and It Won\'t Compile!]](#I_Typed-In_a_BASIC_Program_From_an_Old_Book_and_It_Won.27t_Compile.21)
    -   [[3.2] [My QuickBASIC Source Code Fails to Compile]](#My_QuickBASIC_Source_Code_Fails_to_Compile)
    -   [[3.3] [I can\'t get Visual Basic or VB.Net Code to Compile with FreeBASIC]](#I_can.27t_get_Visual_Basic_or_VB.Net_Code_to_Compile_with_FreeBASIC)
-   [[4] [Removal]](#Removal)
    -   [[4.1] [Unmerge]](#Unmerge)
-   [[5] [See also]](#See_also)
-   [[6] [External Resources]](#External_Resources)

## [Installation]

First, enable [GURU](https://wiki.gentoo.org/wiki/Project:GURU/Information_for_End_Users "Project:GURU/Information for End Users"). Then, [accept](https://wiki.gentoo.org/wiki/Knowledge_Base:Accepting_a_keyword_for_a_single_package "Knowledge Base:Accepting a keyword for a single package") testing keyword for the packages:

[FILE] **`/etc/portage/package.accept_keywords`**

    dev-lang/fbc-bootstrap ~YOUR_CPU_ARCH
    dev-lang/fbc ~YOUR_CPU_ARCH

Finally, emerge the packages:

`root `[`#`]`emerge --ask dev-lang/fbc-bootstrap`

`root `[`#`]`emerge --ask dev-lang/fbc`

The reason for emerging dev-lang/fbc-bootstrap is because FreeBASIC requires FreeBASIC itself. The only purpose of dev-lang/fbc-bootstrap (Written in [C](https://wiki.gentoo.org/wiki/C "C")) is to be able to compile dev-lang/fbc. Once FreeBASIC is installed, dev-lang/fbc-bootstrap is no longer required as any recent version of FreeBASIC can be used to compile a more recent version:

`root `[`#`]`emerge --ask --depclean --verbose dev-lang/fbc-bootstrap`

### [USE flags]

Run [[equery](https://wiki.gentoo.org/wiki/Equery "Equery") uses dev-lang/fbc] command for the use flags:

-   X - Add support for [X11](https://wiki.gentoo.org/wiki/X11 "X11")
-   [gpm](https://wiki.gentoo.org/wiki/GPM "GPM") - Add support for [[[sys-libs/gpm]](https://packages.gentoo.org/packages/sys-libs/gpm)[]] (Console-based mouse driver)
-   libffi - Enable support for Foreign Function Interface library
-   opengl - Add support for [OpenGL](https://wiki.gentoo.org/wiki/OpenGL "OpenGL") (3D graphics)

## [Usage]

### [Invocation]

`user `[`$`]`fbc --help`

    usage: fbc [options] <input files>
    input files:
      *.a = static library, *.o = object file, *.bas = source
      *.rc = resource script, *.res = compiled resource (win32)
      *.xpm = icon resource (*nix/*bsd)
    options:
      @<file>          Read more command line arguments from a file
      -a <file>        Treat file as .o/.a input file
      -arch <type>     Set target architecture (default: 486)
      -asm att|intel   Set asm format (-gen gcc|llvm, x86 or x86_64 only)
      -b <file>        Treat file as .bas input file
      -c               Compile only, do not link
      -C               Preserve temporary .o files
      -d <name>[=<val>]  Add a global #define
      -dll             Same as -dylib
      -dylib           Create a DLL (win32) or shared library (*nix/*BSD)
      -e               Enable runtime error checking
      -ex              -e plus RESUME support
      -exx             -ex plus array bounds/null-pointer checking
      -export          Export symbols for dynamic linkage
      -forcelang <name>  Override #lang statements in source code
      -fpmode fast|precise  Select floating-point math accuracy/speed
      -fpu x87|sse     Set target FPU
      -g               Add debug info, enable __FB_DEBUG__, and enable assert()
      -gen gas|gcc|llvm  Select code generation backend
      [-]-help         Show this help output
      -i         Add an include file search path
      -include <file>  Pre-#include a file for each input .bas
      -l <name>        Link in a library
      -lang <name>     Select FB dialect: fb, deprecated, fblite, qb
      -lib             Create a static library
      -m <name>        Specify main module (default if not -c: first input .bas)
      -map <file>      Save linking map to file
      -maxerr <n>      Only show <n> errors
      -mt              Use thread-safe FB runtime
      -nodeflibs       Do not include the default libraries
      -noerrline       Do not show source context in error messages
      -noobjinfo       Do not read/write compile-time info from/to .o and .a files
      -nostrip         Do not strip symbol information from the output file
      -o <file>        Set .o (or -pp .bas) file name for prev/next input file
      -O <value>       Optimization level (default: 0)
      -p         Add a library search path
      -pic             Generate position-independent code (non-x86 Unix shared libs)
      -pp              Write out preprocessed input file (.pp.bas) only
      -prefix    Set the compiler prefix path
      -print host|target  Display host/target system name
      -print fblibdir  Display the compiler's lib/ path
      -print x         Display output binary/library file name (if known)
      -profile         Enable function profiling
      -r               Write out .asm/.c/.ll (-gen gas/gcc/llvm) only
      -rr              Write out the final .asm only
      -R               Preserve temporary .asm/.c/.ll/.def files
      -RR              Preserve the final .asm file
      -s console|gui   Select win32 subsystem
      -showincludes    Display a tree of file names of #included files
      -static          Prefer static libraries over dynamic ones when linking
      -strip           Omit all symbol information from the output file
      -t <value>       Set .exe stack size in kbytes, default: 1024 (win32/dos)
      -target <name>   Set cross-compilation target
      -title <name>    Set XBE display title (xbox)
      -v               Be verbose
      -vec <n>         Automatic vectorization level (default: 0)
      [-]-version      Show compiler version
      -w all|pedantic|<n>  Set min warning level: all, pedantic or a value
      -Wa <a,b,c>      Pass options to 'as'
      -Wc <a,b,c>      Pass options to 'gcc' (-gen gcc) or 'llc' (-gen llvm)
      -Wl <a,b,c>      Pass options to 'ld'
      -x <file>        Set output executable/library file name

## [Troubleshooting]

### [][I Typed-In a BASIC Program From an Old Book and It Won\'t Compile!]

Welcome to BASIC, a language with many *mostly* compatible dialects! Most likely you\'re copying from a text from either the early mainframe or early home microcomputer eras. Every platform made slight changes to its BASIC interpreter. In many cases it\'s as simple as a reserved keyword getting renamed to something else or a slight change in syntax.

Other times things can get quite complicated. Many early BASIC programs contained a lot of `PEEK` and `POKE` statements to directly manipulate the microcomputer\'s memory map. This was highly platform specific. If you only have handful of `PEEK` and `POKE` statements, try commenting them out and seeing if the program works without them.

A much more difficult scenario to deal with is if you have a program that has a few lines of BASIC to start but quickly sets up a loop to `POKE` `DATA` statements into memory that are all numeric constants. In this case, you most likely have a machine language program in disguise. In that case, you\'ll have to disassemble the `DATA` statement contents into CPU architecture specific assembly mnemonics, quite possibly by hand and run the result through an assembler. If the underlying assembly is for a different CPU architecture than you presently use --- which is quite possible --- you may end up having to port (rewrite) the code to a more convenient language.

### [My QuickBASIC Source Code Fails to Compile]

There are a small number of unavoidable differences between QBASIC and FreeBASIC. In most cases the fix is trivial, see the [Differences from QB](https://www.freebasic.net/wiki/LangQB) article on the FreeBASIC wiki.

### [][I can\'t get Visual Basic or VB.Net Code to Compile with FreeBASIC]

FreeBASIC has a special backwards compatibility mode for QuickBASIC, an MS-DOS era BASIC. It is not compatible with classic Visual BASIC (VB) or VB.Net, nor does it seek to be. Nonetheless, such codebases are not stranded, there are a few options here:

-   Visual BASIC 6 runs under [Wine](https://wiki.gentoo.org/wiki/Wine "Wine") unaltered. The resulting binaries will work on older versions of Windows, Windows 10 or 11 in Windows XP compatibility mode, or (very probably) under Wine. The tradeoffs are that while it\'s easy to get deploy the build environment and get it working, it is dependent upon an unmaintained compiler, and the resulting binaries are dependent upon an unmaintained runtime as well as being \"marooned\" on the 32-bit Intel x86 instruction set architecture. See [[[virtual/wine]](https://packages.gentoo.org/packages/virtual/wine)[]].
-   Project Mono, now part of the [Wine](https://wiki.gentoo.org/wiki/Wine "Wine") project, has a Visual BASIC implementation that is actively maintained. This should serve as a drop-in replacement for VB. This has the benefit of not requiring changes to an existing codebase and the resulting binary will run under Linux. The tradeoff is the Wine execution environment may or may not be stable enough for production, and the resulting binaries are still Intel x86 or amd64 only. See [[[dev-lang/mono-basic]](https://packages.gentoo.org/packages/dev-lang/mono-basic)[]].
-   [Gambas](https://gambaswiki.org/) is another open source option. It has the benefit of being cross-platform and partially VB6 compatible. While Gambas is not identical to VB6, most VB codebases can be adapted to it. The process is not trivial, but it is not especially difficult either. See the [Differences from Visual Basic](https://gambaswiki.org/wiki/doc/diffvb) guide on the Gambas wiki. The tradeoff here is some tedium upfront for a Linux-native codebase that can run on CPU architectures other than 32-bit Intel x86. Gentoo lacks an ebuild for Gambas at present.
-   Those seeking VB.Net compatibility should look at .NET Core, which is a cross-platform runtime developed by Microsoft. Note however that Microsoft has officially stated that VB.Net is still a supported language in the .NET Core ecosystem but VB.Net itself will \"not evolve further.\" The tradeoff here is VB.net is not [C#](https://wiki.gentoo.org/wiki/C-Sharp "C-Sharp"). It\'s reasonable to conclude that Microsoft will drop VB.Net support at some indeterminate future date. That said, the .NET Core SDK is under MIT license, so forking VB.Net is not out of the question. See [[[dev-dotnet/dotnet-sdk]](https://packages.gentoo.org/packages/dev-dotnet/dotnet-sdk)[]].

## [Removal]

### [Unmerge]

`root `[`#`]`emerge --ask --depclean --verbose dev-lang/fbc`

## [See also]

-   [Assembly Language](https://wiki.gentoo.org/wiki/Assembly_Language "Assembly Language") --- the lowest level of all programming languages, typically represented as a series of CPU architecture specific mnemonics and related operands.
-   [BASIC](https://wiki.gentoo.org/wiki/BASIC "BASIC") --- a programming language that was created in 1964
-   [COBOL](https://wiki.gentoo.org/index.php?title=COBOL&action=edit&redlink=1 "COBOL (page does not exist)")
-   [Forth](https://wiki.gentoo.org/wiki/Forth "Forth") --- a heavily stack-oriented self-compiling procedural programming language that is only slightly more abstract than [assembly](https://wiki.gentoo.org/wiki/Assembly_language "Assembly language").
-   [FORTRAN](https://wiki.gentoo.org/index.php?title=FORTRAN&action=edit&redlink=1 "FORTRAN (page does not exist)")
-   [Pascal](https://wiki.gentoo.org/index.php?title=Pascal&action=edit&redlink=1 "Pascal (page does not exist)")

## [External Resources]

-   [FreeBASIC.net](https://freebasic.net/)
-   [FreeBASIC Forums](https://www.freebasic.net/forum/)
-   [RosettaCode FreeBASIC](https://rosettacode.org/wiki/Category:FreeBASIC) --- examples of FreeBASIC performing common programming tasks.
-   [fbrtLib](https://github.com/ImortisInglorian/fbrtLib) --- the native FreeBASIC runtime currently in development, intended to eliminate dependency on glibc.
-   [Gambas](https://gambaswiki.org/) --- a cross-platform high level BASIC very similar to and semi-compatible with classic Visual BASIC (VB).