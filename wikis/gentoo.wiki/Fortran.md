[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Fortran&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Wikipedia](https://en.wikipedia.org/wiki/Fortran "wikipedia:Fortran")

[[]][[#fortran](ircs://irc.libera.chat/#fortran)] ([[webchat](https://web.libera.chat/#fortran)])

**Fortran** is a general-purpose, compiled imperative programming language that is especially suited to numeric computation and scientific computing.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [GCC]](#GCC)
    -   [[1.2] [Flang]](#Flang)
-   [[2] [References]](#References)

## [Installation]

### [GCC]

**gfortran** is [GCC](https://wiki.gentoo.org/wiki/GCC "GCC")\'s Fortran ^[\[1\]](#cite_note-1)^. Enable `fortran` to obtain **gfortran**.

If your package.use is a file:

[FILE] **`/etc/portage/package.use`**

    sys-devel/gcc fortran

If your package.use is a folder:

[FILE] **`/etc/portage/package.use/gcc-fortran`**

    sys-devel/gcc fortran

For more information, see this [wiki](https://gcc.gnu.org/wiki/GFortran).

### [Flang]

[Flang](https://github.com/llvm/llvm-project/tree/main/flang) is [LLVM](https://wiki.gentoo.org/wiki/LLVM "LLVM")\'s fortran compiler.

### [USE flags for] [llvm-runtimes/flang-rt](https://packages.gentoo.org/packages/llvm-runtimes/flang-rt) [[]] [LLVM\'s Fortran runtime]

  ----------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [`+debug`](https://packages.gentoo.org/useflags/+debug)           Enable extra debug codepaths, like asserts and extra output. If you want to get meaningful backtraces see https://wiki.gentoo.org/wiki/Project:Quality_Assurance/Backtraces
  [`test`](https://packages.gentoo.org/useflags/test)               Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  [`verify-sig`](https://packages.gentoo.org/useflags/verify-sig)   Verify upstream signatures on distfiles
  ----------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-21 09:37] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

Change the `FC` variable in [/etc/portage/make.conf] to select the Flang compiler.

[FILE] **`/etc/portage/make.conf`**

    FCFLAGS="$"
    FFLAGS="$"
    F77FLAGS="$"

    FC="flang"

## [References]

1.  [[[↑](#cite_ref-1)] [[https://gcc.gnu.org/fortran](https://gcc.gnu.org/fortran) Retrieved on Feb 2, 2023]]