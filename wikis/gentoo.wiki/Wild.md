[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Wild&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

[[]][GitHub](https://github.com/davidlattimore/wild)

[[]][Package information](https://packages.gentoo.org/packages/sys-devel/wild)

Wild is a linker written in Rust that aims to be very fast for iterative development.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [package.env]](#package.env)
-   [[3] [Usage]](#Usage)
    -   [[3.1] [Verifying a package used Wild]](#Verifying_a_package_used_Wild)
-   [[4] [Troubleshooting]](#Troubleshooting)
    -   [[4.1] [Known issues]](#Known_issues)
-   [[5] [See also]](#See_also)

## [Installation]

** Warning**\
Do not set this as a system-wide linker. Users that do this accept full responsibility for any breakage that may occur.

### [USE flags]

### [USE flags for] [sys-devel/wild](https://packages.gentoo.org/packages/sys-devel/wild) [[]] [A very fast linker for Linux]

  ------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [`debug`](https://packages.gentoo.org/useflags/debug)   Enable extra debug codepaths, like asserts and extra output. If you want to get meaningful backtraces see https://wiki.gentoo.org/wiki/Project:Quality_Assurance/Backtraces
  [`lto`](https://packages.gentoo.org/useflags/lto)       Build with the experimental LTO plugin support
  [`test`](https://packages.gentoo.org/useflags/test)     Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  ------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-03-03 21:44] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

`root `[`#`]`emerge --ask sys-devel/wild`

## [Configuration]

** Important**\
Currently, only [[[sys-devel/gcc:16]](https://packages.gentoo.org/packages/sys-devel/gcc)[]] has support for directly calling Wild via `-fuse-ld=wild`. Upstream has guidance for \<[[[sys-devel/gcc:16]](https://packages.gentoo.org/packages/sys-devel/gcc)[]] [here](https://github.com/davidlattimore/wild?tab=readme-ov-file#using-as-your-default-linker).

### [package.env]

To use [wild] on a select set of packages, make a file in [/etc/portage/env](https://wiki.gentoo.org/wiki//etc/portage/env "/etc/portage/env"):

[FILE] **`/etc/portage/env/wild`**

    LDFLAGS="$ -fuse-ld=wild"
    RUSTFLAGS="-Clinker=gcc -Clink-args=-fuse-ld=wild"

To apply this, create an entry in [/etc/portage/package.env](https://wiki.gentoo.org/wiki//etc/portage/package.env "/etc/portage/package.env"):

[FILE] **`/etc/portage/package.env/wild`**

    app-editors/nano wild

## [Usage]

### [Verifying a package used Wild]

** Note**\
By default, Portage will strip the .comment section from the binary, preventing one from verifying that Wild was used. To temporarily disable stripping, set `FEATURES="nostrip"`.

To verify that a package used Wild to link, use [readelf]:

`user `[`$`]`readelf --string-dump .comment /usr/bin/hyperfine`

    String dump of section '.comment':
      [     1]  GCC: (Gentoo 16.0.0_p20251130 p25) 16.0.0 20251130 (experimental)
      [    43]  rustc version 1.91.0 (f8297e351 2025-10-28)
      [    6f]  GCC: (Gentoo 16.0.0_p20251207 p26) 16.0.0 20251207 (experimental)
      [    b1]  Linker: Wild version 0.7.0 (6321c81fbcfda5604752ca3b889142a969e6c84b) (compatible with GNU linkers)

## [Troubleshooting]

### [Known issues]

-   `error: unrecognized option(s): --defsym=__gentoo_check_ldflags__=0` ([bug](https://bugs.gentoo.org/966883)) - Fixed [upstream](https://github.com/davidlattimore/wild/commit/f70a0f3ce3401ded8c232d20cd83506ceff4c5ca), awaiting release.
-   `error: -m elf_i386 is not yet supported` - Issue occurs in multilib packages with 32-bit enabled.

## [See also]

-   [LLD](https://wiki.gentoo.org/wiki/LLVM/LLD "LLVM/LLD") --- linker provided by the [LLVM](https://wiki.gentoo.org/wiki/LLVM "LLVM") project
-   [mold](https://wiki.gentoo.org/wiki/Mold "Mold") --- a linker that aims to provide drop-in compatibility with existing Unix linkers.