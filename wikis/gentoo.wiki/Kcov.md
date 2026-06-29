[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Kcov&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Home](https://simonkagstrom.github.io/kcov/)

[[]][Package information](https://packages.gentoo.org/packages/dev-util/kcov)

[[]][GitHub](https://github.com/SimonKagstrom/kcov)

**kcov** is a [code coverage](https://en.wikipedia.org/wiki/Code_coverage "wikipedia:Code coverage") tool.

## [Installation]

### [USE flags]

### [USE flags for] [dev-util/kcov](https://packages.gentoo.org/packages/dev-util/kcov) [[]] [Kcov is a code coverage tester for compiled languages, Python and Bash]

  ----------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------
  [`test`](https://packages.gentoo.org/useflags/test)   Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  ----------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2025-11-04 09:36] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

`root `[`#`]`emerge --ask dev-util/kcov`

Versions below 42 require the following patch to be applied on musl-based systems:

[FILE] **`/etc/portage/patches/dev-util/kcov-40/ptrace.patch`**

    --- a/src/engines/ptrace_linux.cc
    +++ b/src/engines/ptrace_linux.cc
    @@ -8,6 +8,8 @@
     #  include <elf.h>
     #endif

    +typedef int __ptrace_request;
    +
     #include <dirent.h>
     #include <sched.h>
     #include <stdio.h>