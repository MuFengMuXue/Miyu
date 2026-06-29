[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Psh&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

[] This article has been flagged for not conforming to the [wiki guidelines](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Guidelines "Gentoo Wiki:Guidelines") (no [lead in sentences](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Guidelines#Use_lead-in_sentences "Gentoo Wiki:Guidelines"), [empty sections](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Guidelines#Adding_new_sections "Gentoo Wiki:Guidelines")). Please [help Gentoo out](https://wiki.gentoo.org/wiki/Help_improve_Gentoo_by_getting_involved_with_documentation!#Make_articles_conform_to_the_guidelines "Help improve Gentoo by getting involved with documentation!") by starting fixing things.

**Resources**

[[![Gentoo peach graphic](/images/thumb/a/ad/Gentoo-logo-peach.svg/25px-Gentoo-logo-peach.svg.png)](https://wiki.gentoo.org/wiki/Project:Perl "Project:Perl")][Project](https://wiki.gentoo.org/wiki/Project:Perl "Project:Perl")

[[]][Home](https://gnp.github.io/psh/)

[[]][Package information](https://packages.gentoo.org/packages/app-shells/psh)

[[]][GitHub](https://github.com/gnp/psh)

[[]][Bugs (upstream)](https://github.com/gnp/psh/issues)

[[]][[#perl](ircs://irc.libera.chat/#perl)] ([[webchat](https://web.libera.chat/#perl)])

[[]][[#regex](ircs://irc.libera.chat/#regex)] ([[webchat](https://web.libera.chat/#regex)])

**[psh]** is a fast and and flexible shell with a [Perl 5](https://wiki.gentoo.org/wiki/Perl "Perl") syntax. Because it is written in Perl 5, [psh] has ready access to Perl\'s regular expression engine and flexible data structures. Additionally [psh] is very fast at mathematical operations, including floating point arithmetic which [Bash](https://wiki.gentoo.org/wiki/Bash "Bash") lacks entirely.

The Perl Shell is very \"old school\" in that it is not possible to configure it to use a Perl syntax newer than the interpreter\'s default. Thus, new features such as *say* are not available with a Perl 5.*x* interpreter, consistently [psh] has an early-90\'s Perl feel to it. Long standing Perl users may find this design decision \"retro\" but those coming from the perspective of either the modern Modern Perl movement or the [Raku](https://wiki.gentoo.org/wiki/Raku "Raku") programming language may find the experience to be jarring or limiting.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Environment variables]](#Environment_variables)
    -   [[2.2] [Files]](#Files)
-   [[3] [Removal]](#Removal)
    -   [[3.1] [Unmerge]](#Unmerge)
-   [[4] [See also]](#See_also)

## [Installation]

### [USE flags]

### [USE flags for] [app-shells/psh](https://packages.gentoo.org/packages/app-shells/psh) [[]] [Combines the interactive nature of a Unix shell with the power of Perl]

  ------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------
  [`examples`](https://packages.gentoo.org/useflags/examples)   Install examples, usually source code
  [`readline`](https://packages.gentoo.org/useflags/readline)   Enable support for libreadline, a GNU line-editing library that almost everyone wants
  [`test`](https://packages.gentoo.org/useflags/test)           Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  ------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2022-07-02 21:49] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

`root `[`#`]`emerge --ask app-shells/psh`

## [Configuration]

### [Environment variables]

### [Files]

-   [\~/.pshrc] - the user\'s shell profile.

## [Removal]

### [Unmerge]

`root `[`#`]`emerge --ask --depclean --verbose app-shell/psh`

## [See also]

-   [Bash](https://wiki.gentoo.org/wiki/Bash "Bash") --- the default shell on Gentoo systems and a popular [shell](https://wiki.gentoo.org/wiki/Shell "Shell") program found on many Linux systems.
-   [Busybox](https://wiki.gentoo.org/wiki/Busybox "Busybox") --- a utility that combines tiny versions of many common UNIX utilities into a *single, small executable*.
-   [Perl](https://wiki.gentoo.org/wiki/Perl "Perl") --- a general purpose interpreted programming language with a powerful regular expression engine.
-   [Raku](https://wiki.gentoo.org/wiki/Raku "Raku") --- a high-level, general-purpose, and gradually typed programming language with low boilerplate objects, optionally immutable data structures, and an advanced macro system.