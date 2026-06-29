[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Tcc&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Home](https://bellard.org/tcc/)

[[]][Official documentation](https://bellard.org/tcc/tcc-doc.html)

[[]][Package information](https://packages.gentoo.org/packages/dev-lang/tcc)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Tiny_C_Compiler "wikipedia:Tiny C Compiler")

The **Tiny C Compiler** also known as [tcc] is famously one of the smallest and fastest [C](https://wiki.gentoo.org/wiki/C "C") compilers ever written. In addition to being a full-fledged ANSI C and C99 compiler, [tcc] also supports an interpreted mode. It was originally designed to be deployed on system rescue disks in an era when such media were limited to 5¼″ (1.2MB) or 3½″ (1.44MB) floppy disks. As such, the [tcc] executable has historically hovered around 100kB in size. Even today on an amd64 system the executable hovers around 300kB in size.

One of the reasons for its speed is the fact that the Tiny C Compiler does not use byte code as intermediate representation during the compilation process. This has two consequences:

1.  It sacrifices advanced compiler optimizations that improve performance or size of the compiled executable. The resulting executable may have been compiled quickly but it\'s probably larger and less efficient than if it had been compiled with [[gcc](https://wiki.gentoo.org/wiki/C "C")] or [[clang](https://wiki.gentoo.org/wiki/LLVM/Clang "LLVM/Clang")].
2.  The compiler is architecture-bound to the x86 and amd64, arm, aarch64, riscv64 processors. The [tcc] compiler *might* compile on other architectures but it cannot generate native code for them.

Lesser-known among the features of The Tiny C Compiler is its ability to execute C code directly as if C were a scripting language, similar to [Perl](https://wiki.gentoo.org/wiki/Perl "Perl") or [Python](https://wiki.gentoo.org/wiki/Python "Python").

Though it tends to have a very long development cycle between releases, the Tiny C Compiler remains in active development. It has a dedicated [[git](https://wiki.gentoo.org/wiki/Git "Git")] repository located at [https://repo.or.cz/tinycc.git](https://repo.or.cz/tinycc.git).

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
    -   [[1.3] [Environment variables]](#Environment_variables)
-   [[2] [Usage]](#Usage)
    -   [[2.1] [Invocation]](#Invocation)
-   [[3] [Troubleshooting]](#Troubleshooting)
    -   [[3.1] [Inability to run tcc as a script]](#Inability_to_run_tcc_as_a_script)
-   [[4] [Removal]](#Removal)
    -   [[4.1] [Unmerge]](#Unmerge)
-   [[5] [See also]](#See_also)

## [Installation]

### [USE flags]

### [USE flags for] [dev-lang/tcc](https://packages.gentoo.org/packages/dev-lang/tcc) [[]] [A very small C compiler for ix86/amd64]

  ------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------
  [`hardened`](https://packages.gentoo.org/useflags/hardened)   Activate default security enhancements for toolchain (gcc, glibc, binutils)
  [`test`](https://packages.gentoo.org/useflags/test)           Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  ------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-25 03:25] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

`root `[`#`]`emerge --ask dev-lang/tcc`

### [Environment variables]

-   `CPATH` specifies a list of directories to be searched as if specified.
-   `C_INCLUDE_PATH` A colon-separated list of directories searched for include files.
-   `LIBRARY_PATH` A colon-separated list of directories searched for libraries.

## [Usage]

### [Invocation]

`user `[`$`]`tcc --help`

    Tiny C Compiler 0.9.28rc - Copyright (C) 2001-2006 Fabrice Bellard
    Usage: tcc [options...] [-o outfile] [-c] infile(s)...
           tcc [options...] -run infile (or --) [arguments...]
    General options:
      -c           compile only - generate an object file
      -o outfile   set output filename
      -run         run compiled source
      -fflag       set or reset (with 'no-' prefix) 'flag' (see tcc -hh)
      -Wwarning    set or reset (with 'no-' prefix) 'warning' (see tcc -hh)
      -w           disable all warnings
      -v --version show version
      -vv          show search paths or loaded files
      -h -hh       show this, show more help
      -bench       show compilation statistics
      -            use stdin pipe as infile
      @listfile    read arguments from listfile
    Preprocessor options:
      -Idir        add include path 'dir'
      -Dsym[=val]  define 'sym' with value 'val'
      -Usym        undefine 'sym'
      -E           preprocess only
      -nostdinc    do not use standard system include paths
    Linker options:
      -Ldir        add library path 'dir'
      -llib        link with dynamic or static library 'lib'
      -nostdlib    do not link with standard crt and libraries
      -r           generate (relocatable) object file
      -rdynamic    export all global symbols to dynamic linker
      -shared      generate a shared library/dll
      -soname      set name for shared library to be used at runtime
      -Wl,-opt[=val]  set linker option (see tcc -hh)
    Debugger options:
      -g           generate stab runtime debug info
      -gdwarf[-x]  generate dwarf runtime debug info
      -b           compile with built-in memory and bounds checker (implies -g)
      -bt[N]       link with backtrace (stack dump) support [show max N callers]
    Misc. options:
      -std=version define __STDC_VERSION__ according to version (c11/gnu11)
      -x[c|a|b|n]  specify type of the next infile (C,ASM,BIN,NONE)
      -Bdir        set tcc's private include/library dir
      -M[M]D       generate make dependency file [ignore system files]
      -M[M]        as above but no other output
      -MF file     specify dependency file name
      -m32/64      defer to i386/x86_64 cross compiler
    Tools:
      create library  : tcc -ar [crstvx] lib [files]

## [Troubleshooting]

### [Inability to run [tcc] as a script]

The Tiny C compiler can be run with a script if the proper shebang (#!) is set at the first line of the file. The official upstream documentation provides the shebang as:

`#!/usr/local/bin/tcc -run`

However, this is inaccurate on a Gentoo system. Presently, the [dev-lang/tcc] ebuild installs [tcc] to [/usr/bin], thus the shebang should be:

`#!/usr/bin/tcc -run`

If the script is going to be run on multiple systems where the path to [tcc] might change, the following shebang is also technically possible:

`#!/usr/bin/env -S tcc -run`

Note that the *-S* option is widely available on Linux but it may or may not be present on other operating systems such as macOS or any of the BSD\'s. Thus, while it is technically valid it should be used with caution in highly homogeneous environments.

In addition, it\'s also possible to make a file that is also a valid C source file with:

`//usr/bin/env tcc -run "$0" "$@" ; exit $?`

additional options can be hardcoded or specified in an environment variable:

`//usr/bin/env tcc -static "$TCC_OPTIONS" -run "$0" "$@"; exit $?`

## [Removal]

### [Unmerge]

`root `[`#`]`emerge --ask --depclean --verbose dev-lang/tcc`

## [See also]

-   [C](https://wiki.gentoo.org/wiki/C "C") --- a programming language developed for Bell Labs in the early 1970s
-   [Clang](https://wiki.gentoo.org/wiki/LLVM/Clang "LLVM/Clang") --- a C/C++/Objective-C/C++, CUDA, and RenderScript language front-end for the LLVM project