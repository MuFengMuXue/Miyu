[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=NQP&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

[[]][Package information](https://packages.gentoo.org/packages/dev-lang/nqp)

[[]][GitHub](https://github.com/Raku/nqp)

**NQP** is also known as \"Not Quite Perl\" is a lightweight [Raku](https://wiki.gentoo.org/wiki/Raku "Raku")-like environment for MoarVM, JVM, and other virtual machines.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Removal]](#Removal)
    -   [[2.1] [Unmerge]](#Unmerge)
-   [[3] [See Also]](#See_Also)
-   [[4] [External Resources]](#External_Resources)

## [Installation]

### [USE flags]

### [USE flags for] [dev-lang/nqp](https://packages.gentoo.org/packages/dev-lang/nqp) [[]] [Not Quite Perl, a Raku bootstrapping compiler]

  ------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------
  [`+moar`](https://packages.gentoo.org/useflags/+moar)   Build the MoarVM backend (experimental/broken)
  [`clang`](https://packages.gentoo.org/useflags/clang)   Toggle usage of the clang compiler in conjunction with MoarVM
  [`doc`](https://packages.gentoo.org/useflags/doc)       Add extra documentation (API, Javadoc, etc). It is recommended to enable per package instead of globally
  [`java`](https://packages.gentoo.org/useflags/java)     Add support for Java
  [`test`](https://packages.gentoo.org/useflags/test)     Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  ------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-03-09 10:38] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

Emerge the package base

`root `[`#`]`emerge --ask dev-lang/nqp`

## [Removal]

While NQP can be installed or removed on its own it\'s more typically handled as a dependency of [Rakudo](https://wiki.gentoo.org/wiki/Rakudo "Rakudo").

### [Unmerge]

`root `[`#`]`emerge --ask --depclean --verbose dev-lang/nqp`

## [See Also]

-   [Rakudo](https://wiki.gentoo.org/wiki/Rakudo "Rakudo") --- a compiler that implements the [Raku](https://wiki.gentoo.org/wiki/Raku "Raku") programming language.
-   [MoarVM](https://wiki.gentoo.org/wiki/MoarVM "MoarVM") --- [Rakudo](https://wiki.gentoo.org/wiki/Rakudo "Rakudo") compiler\'s virtual machine for the [Raku](https://wiki.gentoo.org/wiki/Raku "Raku") Programming Language.
-   [Zef](https://wiki.gentoo.org/index.php?title=Zef&action=edit&redlink=1 "Zef (page does not exist)")
-   [Perl](https://wiki.gentoo.org/wiki/Perl "Perl") --- a general purpose interpreted programming language with a powerful regular expression engine.

## [External Resources]