[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=LLVM/LLD&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[![Gentoo peach graphic](/images/thumb/a/ad/Gentoo-logo-peach.svg/25px-Gentoo-logo-peach.svg.png)](https://wiki.gentoo.org/wiki/Project:LLVM "Project:LLVM")][Project](https://wiki.gentoo.org/wiki/Project:LLVM "Project:LLVM")

[[]][Home](https://lld.llvm.org/)

[[]][Package information](https://packages.gentoo.org/packages/llvm-core/lld)

[[]][GitHub](https://github.com/llvm/llvm-project)

[[]][[#llvm](irc://irc.oftc.net/#llvm) (on [irc://irc.oftc.net](irc://irc.oftc.net)])

**LLD** is a linker provided by the [LLVM](https://wiki.gentoo.org/wiki/LLVM "LLVM") project and can be used as an alternative to the standard linker, BFD. It supports more modern features than BFD and tightly integrates with [Clang](https://wiki.gentoo.org/wiki/LLVM/Clang "LLVM/Clang") and the LLVM toolchain, especially when [link-time optimizing](https://wiki.gentoo.org/wiki/LTO "LTO") a system.

## [Installation]

### [USE flags]

### [USE flags for] [llvm-core/lld](https://packages.gentoo.org/packages/llvm-core/lld) [[]] [The LLVM linker (link editor)]

  ----------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [`+debug`](https://packages.gentoo.org/useflags/+debug)           Enable extra debug codepaths, like asserts and extra output. If you want to get meaningful backtraces see https://wiki.gentoo.org/wiki/Project:Quality_Assurance/Backtraces
  [`test`](https://packages.gentoo.org/useflags/test)               Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  [`verify-sig`](https://packages.gentoo.org/useflags/verify-sig)   Verify upstream signatures on distfiles
  [`zstd`](https://packages.gentoo.org/useflags/zstd)               Enable support for ZSTD compression
  ----------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-21 09:37] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

`root `[`#`]`emerge --ask llvm-core/lld`