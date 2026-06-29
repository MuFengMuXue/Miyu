[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Racket&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Home](https://racket-lang.org/)

[[]][Official documentation](https://docs.racket-lang.org/)

[[]][Package information](https://packages.gentoo.org/packages/dev-scheme/racket)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Racket_(programming_language) "wikipedia:Racket (programming language)")

[[]][Official project wiki](https://github.com/racket/racket/wiki)

[[]][GitHub](https://github.com/racket/racket)

[[]][Bugs (upstream)](https://github.com/racket/racket/issues/)

[[]][[#racket](ircs://irc.libera.chat/#racket)] ([[webchat](https://web.libera.chat/#racket)])

[[]][Blog](https://blog.racket-lang.org/)

**Racket** is a general-purpose programming language designed for language-oriented programming, that is, the ability to implement other programming languages and DSLs. Racket is a descendant of [Scheme](https://wiki.gentoo.org/index.php?title=Scheme&action=edit&redlink=1 "Scheme (page does not exist)") which is itself a dialect of [Lisp](https://wiki.gentoo.org/wiki/Lisp "Lisp") that began development in 1995 and continues to this day.

## Contents

-   [[1] [Features]](#Features)
-   [[2] [Installation]](#Installation)
    -   [[2.1] [USE flags]](#USE_flags)
    -   [[2.2] [Emerge]](#Emerge)
-   [[3] [Removal]](#Removal)
    -   [[3.1] [Unmerge]](#Unmerge)
    -   [[3.2] [Cleanup]](#Cleanup)
-   [[4] [Installing Racket packages]](#Installing_Racket_packages)
    -   [[4.1] [Natively via Portage]](#Natively_via_Portage)
    -   [[4.2] [Via Racket\'s Package Manager, Raco]](#Via_Racket.27s_Package_Manager.2C_Raco)
-   [[5] [See Also]](#See_Also)
-   [[6] [External resources]](#External_resources)
    -   [[6.1] [Racket Community]](#Racket_Community)
    -   [[6.2] [Resources for Learning Racket]](#Resources_for_Learning_Racket)

## [Features]

Racket is considered to be an excellent language for learning computer science, specifically the discipline of compiler design. The language has both a runtime and a JIT (just in time) compiler. It has a very expressive macro engine that goes well beyond the typical text-replacement macros common to the [C](https://wiki.gentoo.org/wiki/C "C") preprocessor. Rather, racket macros are baked into Racket parser itself and can be used to extend the language and add new features on the fly.

Racket has its own package manager, [raco].

## [Installation]

### [USE flags]

### [USE flags for] [dev-scheme/racket](https://packages.gentoo.org/packages/dev-scheme/racket) [[]] [General purpose, multi-paradigm Lisp-Scheme programming language]

  ------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [`+chez`](https://packages.gentoo.org/useflags/+chez)         Build Racket on Chez (Racket CS)
  [`+doc`](https://packages.gentoo.org/useflags/+doc)           Add extra documentation (API, Javadoc, etc). It is recommended to enable per package instead of globally
  [`+futures`](https://packages.gentoo.org/useflags/+futures)   Enable racket/future library for fine-grained hardware parallelism
  [`+jit`](https://packages.gentoo.org/useflags/+jit)           Enable just-in-time compilation for improved performance. May prevent use of some PaX memory protection features in Gentoo Hardened.
  [`+places`](https://packages.gentoo.org/useflags/+places)     Enable racket/place library for share-nothing parallelism and message-passing communication. Compared to futures, places are heavyweight, but they have a simpler performance model.
  [`+threads`](https://packages.gentoo.org/useflags/+threads)   Enable support for green threads
  [`iconv`](https://packages.gentoo.org/useflags/iconv)         Enable support for the iconv character set conversion library
  [`minimal`](https://packages.gentoo.org/useflags/minimal)     Install a very minimal build (disables, for example, plugins, fonts, most drivers, non-critical features)
  [`ncurses`](https://packages.gentoo.org/useflags/ncurses)     Add ncurses support for expeditor (REPL expression editor)
  ------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-02-24 20:19] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

`root `[`#`]`emerge --ask dev-scheme/racket`

## [Removal]

### [Unmerge]

`root `[`#`]`emerge --ask --depclean --verbose dev-scheme/racket`

### [Cleanup]

If manually installing any Racket packages in the installation scope, then they might have created some files inside [/usr/share/racket/pkgs].

Those files can be cleaned up by removing them with [rm] as follows:

`root `[`#`]`rm -r /usr/share/racket/pkgs`

## [Installing Racket packages]

### [Natively via Portage]

To install Racket packages in the installation scope in a more controlled way, users may wish to use Portage for this task. Currently this is one of the aims of the \"[Gentoo-Racket](https://gentoo-racket.gitlab.io/)\" project.

Gentoo-Racket is maintaining the \"[Gentoo-Racket overlay](https://gitlab.com/gentoo-racket/gentoo-racket-overlay/)\" on the official GitLab instance.

The overlay can be installed by using the \"[Eselect/Repository eselect-repository](https://wiki.gentoo.org/wiki/Eselect/Repository "Eselect/Repository")\" tool:

`root `[`#`]`eselect repository enable racket-overlay`

### [][Via Racket\'s Package Manager, Raco]

Raco is the built-in package manager of Racket, it can install packages via the following:

`user `[`$`]`raco pkg install --user`

Please use the switch [\--user] to install packages in the *user scope*. Installation in user scope should be the default but it can be also configured to install packages globally, in the *installation scope*.

## [See Also]

-   [Raku](https://wiki.gentoo.org/wiki/Raku "Raku") --- a high-level, general-purpose, and gradually typed programming language with low boilerplate objects, optionally immutable data structures, and an advanced macro system.

## [External resources]

### [Racket Community]

-   The [Racket Subreddit](https://www.reddit.com/r/Racket/)

### [Resources for Learning Racket]

-   [Learn Racket in Y Minutes](https://learnxinyminutes.com/docs/racket/)
-   [Beau­tiful Racket](https://beautifulracket.com/) by Matthew Butt­erick