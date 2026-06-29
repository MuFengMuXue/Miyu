[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Rakudo&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Home](https://rakudo.org/)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Rakudo "wikipedia:Rakudo")

[[]][Official documentation](https://rakudo.org/docs)

[[]][Package information](https://packages.gentoo.org/packages/dev-lang/rakudo)

[[]][GitHub](https://github.com/rakudo/rakudo/)

**Rakudo** is a compiler that implements the [Raku](https://wiki.gentoo.org/wiki/Raku "Raku") programming language. Rakudo targets Raku\'s native virtual machine [MoarVM](https://wiki.gentoo.org/wiki/MoarVM "MoarVM") as well as the [Java](https://wiki.gentoo.org/wiki/Java "Java") and [JavaScript](https://wiki.gentoo.org/index.php?title=JavaScript&action=edit&redlink=1 "JavaScript (page does not exist)") virtual machines.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Environment variables]](#Environment_variables)
        -   [[2.1.1] [Module loading]](#Module_loading)
        -   [[2.1.2] [Error handling]](#Error_handling)
        -   [[2.1.3] [Precompilation]](#Precompilation)
        -   [[2.1.4] [Line editor]](#Line_editor)
        -   [[2.1.5] [Miscellaneous]](#Miscellaneous)
    -   [[2.2] [Files]](#Files)
-   [[3] [Removal]](#Removal)
    -   [[3.1] [Unmerge]](#Unmerge)
-   [[4] [See Also]](#See_Also)
-   [[5] [External Resources]](#External_Resources)

## [Installation]

** Note**\
While installation and uninstallation of Rakudo is reliable, *reinstallation* can occasionally fail. If that happens just uninstall [[[dev-lang/rakudo]](https://packages.gentoo.org/packages/dev-lang/rakudo)[]] and install it again. This issue is being tracked via [[[bug #584394]](https://bugs.gentoo.org/show_bug.cgi?id=584394)[]].

### [USE flags]

### [USE flags for] [dev-lang/rakudo](https://packages.gentoo.org/packages/dev-lang/rakudo) [[]] [A compiler for the Raku programming language]

  ------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------
  [`+moar`](https://packages.gentoo.org/useflags/+moar)   Use the MoarVM as backend
  [`clang`](https://packages.gentoo.org/useflags/clang)   Use Clang to compile the MoarVM backend
  [`java`](https://packages.gentoo.org/useflags/java)     Add support for Java
  [`test`](https://packages.gentoo.org/useflags/test)     Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  ------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-03-09 10:38] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

Emerge the package base

`root `[`#`]`emerge --ask dev-lang/rakudo`

## [Configuration]

### [Environment variables]

#### [Module loading]

-   `RAKUDOLIB` (str) a comma-delimited path list for Raku modules.
-   `RAKUDO_MODULE_DEBUG` (bool) If true, extra debugging information is sent to STDERR.

#### [Error handling]

-   `RAKU_EXCEPTIONS_HANDLER` (str) define the exception handling class, defaults to [Exceptions::JSON] if undefined.
-   `RAKUDO_NO_DEPRECATIONS` (bool) If true, suppresses warnings when deprecated language features are used.
-   `RAKUDO_DEPRECATIONS_FATAL` (bool) If true, use of deprecated language features become fatal errors.
-   `RAKUDO_VERBOSE_STACKFRAME` (int) If true, provides stack frame information for debugging purposes out to a maximum specified number of lines of context.
-   `RAKUDO_BACKTRACE_SETTING` (bool) If true, [.setting] files are included in stack traces.

#### [Precompilation]

-   `RAKUDO_PREFIX` (str) When set, this will cause Raku to look for module repositories in a specified alternative location.
-   `RAKUDO_LOG_PRECOMP` (bool) If true, diagnostic information is emitted regarding Raku\'s precompilation process.

#### [Line editor]

-   `RAKUDO_LINE_EDITOR` (str) When set, this specifies the default line editor for Raku to use. When set to [none] Raku will not complain about the absence of a line editor. Currently, either [Readline] or [Linenoise] are expected values.
-   `RAKUDO_DISABLE_MULTILINE` (bool) disable multi-line input when Raku is in interactive mode.
-   `RAKUDO_HIST` (str) specifies the location of Raku\'s line editor history.

#### [Miscellaneous]

-   `RAKUDO_OPT` (str) set default command line options.
-   `RAKUDO_DEFAULT_READ_ELEMS` (int) When set, this defines the number of characters read by an [IO::Handle].
-   `RAKUDO_ERROR_COLOR` (bool) Controls whether compiler error output is color coded or not; defaults to true in POSIX environments.
-   `RAKUDO_MAX_THREADS` (int) Controls the maximum number of threads created by [ThreadPoolScheduler]; default 64.
-   `TMPDIR` (str) When set [IO::Spec::Unix.tmpdir] uses the specified alternative temporary directory; defaults to [/tmp].
-   `RAKUDO_SNAPPER` (float) Specifies the interval between virtual machine state snapshots created locally by the Rakudo compiler\'s [telemetry] class. This defaults to 0.1 or 10 snapshots per second.
-   `RAKUDO_HOME` (str) override Raku\'s installation path.
-   `NQP_HOME` (str) override NQP\'s installation path.

### [Files]

-   [\~/.raku/rakudo-history] Raku\'s history file used by the line editor when Raku is run interactively.

## [Removal]

### [Unmerge]

`root `[`#`]`emerge --ask --depclean --verbose dev-lang/rakudo`

## [See Also]

-   [Raku](https://wiki.gentoo.org/wiki/Raku "Raku") --- a high-level, general-purpose, and gradually typed programming language with low boilerplate objects, optionally immutable data structures, and an advanced macro system.
-   [NQP](https://wiki.gentoo.org/wiki/NQP "NQP") --- a lightweight [Raku](https://wiki.gentoo.org/wiki/Raku "Raku")-like environment for MoarVM, JVM, and other virtual machines.
-   [MoarVM](https://wiki.gentoo.org/wiki/MoarVM "MoarVM") --- [Rakudo] compiler\'s virtual machine for the [Raku](https://wiki.gentoo.org/wiki/Raku "Raku") Programming Language.
-   [Zef](https://wiki.gentoo.org/index.php?title=Zef&action=edit&redlink=1 "Zef (page does not exist)")
-   [Perl](https://wiki.gentoo.org/wiki/Perl "Perl") --- a general purpose interpreted programming language with a powerful regular expression engine.

## [External Resources]

-   [https://raku.guide](https://raku.guide), a quick overview of the Raku programming language.
-   [https://docs.raku.org/programs/03-environment-variables/](https://docs.raku.org/programs/03-environment-variables/)