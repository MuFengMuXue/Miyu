[[]][Home](//r-project.org)

[[]][Wikipedia](https://en.wikipedia.org/wiki/R_(programming_language) "wikipedia:R (programming language)")

[[]][[#R](ircs://irc.libera.chat/#R)] ([[webchat](https://web.libera.chat/#R)])

**R** is a programming language primarily for statistics and numerical analysis.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Compile flags for install.packages]](#Compile_flags_for_install.packages)
        -   [[2.1.1] [Example: Removing LTO]](#Example:_Removing_LTO)
-   [[3] [Integration with other programs]](#Integration_with_other_programs)
-   [[4] [Troubleshooting]](#Troubleshooting)
    -   [[4.1] [configure: error: Cannot run mixed C/Fortran code]](#configure:_error:_Cannot_run_mixed_C.2FFortran_code)
    -   [[4.2] [configure: error: Cannot compile a simple Fortran program]](#configure:_error:_Cannot_compile_a_simple_Fortran_program)

## [Installation]

### [USE flags]

### [USE flags for] [dev-lang/R](https://packages.gentoo.org/packages/dev-lang/R) [[]] [Language and environment for statistical computing and graphics]

  ------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------
  [`+libdeflate`](https://packages.gentoo.org/useflags/+libdeflate)   Use app-arch/libdeflate rather than virtual/zlib for lazy-loaded R objects.
  [`X`](https://packages.gentoo.org/useflags/X)                       Add support for X11
  [`cairo`](https://packages.gentoo.org/useflags/cairo)               Enable support for the cairo graphics library
  [`doc`](https://packages.gentoo.org/useflags/doc)                   Add extra documentation (API, Javadoc, etc). It is recommended to enable per package instead of globally
  [`icu`](https://packages.gentoo.org/useflags/icu)                   Enable ICU (Internationalization Components for Unicode) support, using dev-libs/icu
  [`java`](https://packages.gentoo.org/useflags/java)                 Add support for Java
  [`jpeg`](https://packages.gentoo.org/useflags/jpeg)                 Add JPEG image support
  [`lto`](https://packages.gentoo.org/useflags/lto)                   Enable Link-Time Optimization (LTO) to optimize the build
  [`minimal`](https://packages.gentoo.org/useflags/minimal)           Install a very minimal build (disables, for example, plugins, fonts, most drivers, non-critical features)
  [`nls`](https://packages.gentoo.org/useflags/nls)                   Add Native Language Support (using gettext - GNU locale utilities)
  [`openmp`](https://packages.gentoo.org/useflags/openmp)             Build support for the OpenMP (support parallel computing), requires \>=sys-devel/gcc-4.2 built with USE=\"openmp\"
  [`perl`](https://packages.gentoo.org/useflags/perl)                 Add optional support/bindings for the Perl language
  [`png`](https://packages.gentoo.org/useflags/png)                   Add support for libpng (PNG images)
  [`prefix`](https://packages.gentoo.org/useflags/prefix)             Defines if a Gentoo Prefix offset installation is used
  [`profile`](https://packages.gentoo.org/useflags/profile)           Add support for software performance analysis (will likely vary from ebuild to ebuild)
  [`readline`](https://packages.gentoo.org/useflags/readline)         Enable support for libreadline, a GNU line-editing library that almost everyone wants
  [`test`](https://packages.gentoo.org/useflags/test)                 Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  [`tiff`](https://packages.gentoo.org/useflags/tiff)                 Add support for the TIFF image format
  [`tk`](https://packages.gentoo.org/useflags/tk)                     Add support for Tk GUI toolkit
  ------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-20 01:26] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

`root `[`#`]`emerge --ask dev-lang/R`

## [Configuration]

### [Compile flags for install.packages]

At compile time, R remembers the `CFLAGS` and `CXXFLAGS` with which it was [configured](https://svn.r-project.org/R/trunk/etc/Makeconf.in), storing them in [\$R_HOME/etc/Makeconf]. However, certain [CRAN](https://en.wikipedia.org/wiki/R_package#Comprehensive_R_Archive_Network_(CRAN)) packages may fail to compile with said flags, even if R itself compiled smoothly.

To rectify this, either change R\'s flags via [[/etc/portage/package.env](https://wiki.gentoo.org/wiki//etc/portage/package.env "/etc/portage/package.env")], or work with the experimental [R overlay](https://wiki.gentoo.org/wiki/Project:Science/Overlay/R "Project:Science/Overlay/R").

#### [Example: Removing LTO]

Suppose that an attempt to install `ggplot2` via `install.packages("ggplot2")` caused a compile time error due to `-Werror=strict-aliasing`, which is associated with [LTO](https://wiki.gentoo.org/wiki/LTO#GCC_Systems "LTO"). To rectify this, use an env to demote this error to a warning. Since this warning often indicates LTO runtime issues, consider disabling `lto` as well.

[FILE] **`/etc/portage/env/no-lto`Removing LTO**

    # These warnings were promoted to errors as they indicate likely runtime
    # problems with LTO. Additively disable them since LTO is being removed.
    WARNING_FLAGS="-Wno-error=odr -Wno-error=lto-type-mismatch -Wno-error=strict-aliasing"

    CFLAGS="$ -fno-lto"
    CXXFLAGS="$ -fno-lto"
    FCFLAGS="$ -fno-lto"
    FFLAGS="$ -fno-lto"

    USE="$ -lto"

[FILE] **`/etc/portage/package.env/R`Removing LTO**

    dev-lang/R no-lto

Reemerge R to propagate these changes.

`root `[`#`]`emerge --ask dev-lang/R`

## [Integration with other programs]

ESS, or Emacs Speaks Statistics, is an Emacs mode that can edit R files and start R from within Emacs. To install:

`root `[`#`]`emerge --ask app-emacs/ess`

In Vim, the vim-r plugin integrates vim and R through [tmux] and provides support for editing R and send it to an R process. To install:

`root `[`#`]`emerge --ask app-vim/vim-r`

## [Troubleshooting]

### [][configure: error: Cannot run mixed C/Fortran code]

To resolve this, check if libf2c is installed in your system:

`root `[`#`]`find / -name libf2c.so`

If command shows no output, install libf2c and try emerging again:

`root `[`#`]`emerge --ask dev-libs/libf2c`

### [configure: error: Cannot compile a simple Fortran program]

This error can be caused by `FCFLAGS` and `FFLAGS` flags in `make.conf`, which are incompatible with Fortran compiler. To fix this, you need to manually select those flags in [/etc/portage/make.conf]:

[FILE] **`/etc/portage/make.conf`Setting FCFLAGS and FFLAGS**

    # =========Setting flags for Fortran compiler=========
    #
    FCFLAGS="-O2 -march=native"
    FFLAGS="$"