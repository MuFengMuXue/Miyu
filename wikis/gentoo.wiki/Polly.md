[[]][GitHub](https://github.com/llvm/llvm-project)

[[![Gentoo peach graphic](/images/thumb/a/ad/Gentoo-logo-peach.svg/25px-Gentoo-logo-peach.svg.png)](https://wiki.gentoo.org/wiki/Project:LLVM "Project:LLVM")][Project](https://wiki.gentoo.org/wiki/Project:LLVM "Project:LLVM")

Polly is a high-level loop and data-locality optimizer and optimization infrastructure for LLVM. It uses an abstract mathematical representation based on integer polyhedra to analyze and optimize the memory access pattern of a program. We currently perform classical loop transformations, especially tiling and loop fusion to improve data-locality. Polly can also exploit OpenMP level parallelism, expose SIMDization opportunities.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [package.env]](#package.env)

## [Installation]

** Important**\
Polly support for LLVM begins in LLVM 20.

### [USE flags]

### [USE flags for] [llvm-core/polly](https://packages.gentoo.org/packages/llvm-core/polly) [[]] [Polyhedral optimizations for LLVM]

  ----------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [`+debug`](https://packages.gentoo.org/useflags/+debug)           Enable extra debug codepaths, like asserts and extra output. If you want to get meaningful backtraces see https://wiki.gentoo.org/wiki/Project:Quality_Assurance/Backtraces
  [`test`](https://packages.gentoo.org/useflags/test)               Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  [`verify-sig`](https://packages.gentoo.org/useflags/verify-sig)   Verify upstream signatures on distfiles
  ----------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-21 09:37] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

First, emerge Polly:

`root `[`#`]`emerge --ask llvm-core/polly`

Next, emerge [[[llvm-core/clang-runtime\[polly\]]](https://packages.gentoo.org/packages/llvm-core/clang-runtime)[]]

This installs a file similar to the following:

[FILE] **`/etc/clang/20/gentoo-plugins.cfg`**

    # This file is used to load optional LLVM plugins.
    -fpass-plugin=LLVMPolly.so
    -fplugin=LLVMPolly.so

## [Configuration]

### [package.env]

[FILE] **`/etc/portage/env/polly`**

    COMMON_FLAGS="$ -mllvm -polly -mllvm -polly-vectorizer=stripmine -mllvm -polly-omp-backend=LLVM -mllvm -polly-parallel -mllvm -polly-num-threads=9 -mllvm -polly-scheduling=dynamic"
    CFLAGS="$"
    CXXFLAGS="$"
    FCFLAGS="$"
    FFLAGS="$"

[FILE] **`/etc/portage/package.env`Example**

    dev-lang/python polly # map the package you'd like to use polly with thereon.