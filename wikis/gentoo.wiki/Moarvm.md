[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=MoarVM&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Home](https://www.moarvm.org/)

[[]][Wikipedia](https://en.wikipedia.org/wiki/MoarVM "wikipedia:MoarVM")

[[]][Package information](https://packages.gentoo.org/packages/dev-lang/moarvm)

[[]][GitHub](https://github.com/MoarVM/MoarVM)

**MoarVM** is the [Rakudo](https://wiki.gentoo.org/wiki/Rakudo "Rakudo") compiler\'s virtual machine for the [Raku](https://wiki.gentoo.org/wiki/Raku "Raku") Programming Language.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Environment variables]](#Environment_variables)
-   [[3] [Removal]](#Removal)
    -   [[3.1] [Unmerge]](#Unmerge)
-   [[4] [See Also]](#See_Also)
-   [[5] [External Resources]](#External_Resources)

## [Installation]

### [USE flags]

### [USE flags for] [dev-lang/moarvm](https://packages.gentoo.org/packages/dev-lang/moarvm) [[]] [A 6model-based VM for NQP and Raku]

  ------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [`+jit`](https://packages.gentoo.org/useflags/+jit)                 Enable Just-In-Time-Compiler. Has no effect except on AMD64 and Darwin.
  [`asan`](https://packages.gentoo.org/useflags/asan)                 Enable clang\'s Address Sanitizer functionality. Expect longer compile time.
  [`clang`](https://packages.gentoo.org/useflags/clang)               Use clang compiler instead of GCC
  [`debug`](https://packages.gentoo.org/useflags/debug)               Enable extra debug codepaths, like asserts and extra output. If you want to get meaningful backtraces see https://wiki.gentoo.org/wiki/Project:Quality_Assurance/Backtraces
  [`doc`](https://packages.gentoo.org/useflags/doc)                   Add extra documentation (API, Javadoc, etc). It is recommended to enable per package instead of globally
  [`optimize`](https://packages.gentoo.org/useflags/optimize)         Enable optimization via CFLAGS
  [`static-libs`](https://packages.gentoo.org/useflags/static-libs)   Build static versions of dynamic libraries as well
  [`ubsan`](https://packages.gentoo.org/useflags/ubsan)               Enable clang\'s Undefined Behavior Sanitizer functionality. Expect longer compile time.
  ------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-03-09 10:37] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

Emerge the package base

`root `[`#`]`emerge --ask dev-lang/moarvm`

## [Configuration]

### [Environment variables]

-   `MVM_JIT_DISABLE` (bool) Disables the just-in-time compiler. JIT compilation is enabled by default.
-   `MVM_SPESH_DISABLE` (bool) Disables the runtime bytecode optimizer. This optimization is enabled by default.
-   `MVM_SPESH_INLINE_DISABLE` (bool) Disables inlining of call frames by the bytecode optimizer. This optimization is enabled by default.
-   `MVM_SPESH_OSR_DISABLE` (bool) Disables the on-stack replacement of bytecode by the optimizer. This optimization is enabled by default.
-   `MVM_CROSS_THREAD_WRITE_LOG` (bool) Produce warnings when a thread does a write to an object it didn\'t allocate and doesn\'t have a lock for.
-   `MVM_CROSS_THREAD_WRITE_LOG_INCLUDE_LOCKED` (bool) Extend the above to include objects that are locked as well.

## [Removal]

MoarVM is a dependency of Rakudo, the Raku compiler. As such it\'s not typically installed or removed on its own.

### [Unmerge]

`root `[`#`]`emerge --ask --depclean --verbose dev-lang/moarvm`

## [See Also]

-   [Rakudo](https://wiki.gentoo.org/wiki/Rakudo "Rakudo") --- a compiler that implements the [Raku](https://wiki.gentoo.org/wiki/Raku "Raku") programming language.
-   [NQP](https://wiki.gentoo.org/wiki/NQP "NQP") --- a lightweight [Raku](https://wiki.gentoo.org/wiki/Raku "Raku")-like environment for MoarVM, JVM, and other virtual machines.
-   [Zef](https://wiki.gentoo.org/index.php?title=Zef&action=edit&redlink=1 "Zef (page does not exist)")
-   [Perl](https://wiki.gentoo.org/wiki/Perl "Perl") --- a general purpose interpreted programming language with a powerful regular expression engine.

## [External Resources]