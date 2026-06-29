Other languages:

-   [Deutsch](https://wiki.gentoo.org/wiki/ACCEPT_KEYWORDS/de "ACCEPT KEYWORDS/de (75% translated)")
-   [English]
-   [Nederlands](https://wiki.gentoo.org/wiki/ACCEPT_KEYWORDS/nl "ACCEPT KEYWORDS/nl (75% translated)")
-   [Türkçe](https://wiki.gentoo.org/wiki/ACCEPT_KEYWORDS/tr "ACCEPT KEYWORDS/tr (25% translated)")
-   [español](https://wiki.gentoo.org/wiki/ACCEPT_KEYWORDS/es "ACCEPT KEYWORDS/es (55% translated)")
-   [français](https://wiki.gentoo.org/wiki/ACCEPT_KEYWORDS/fr "ACCEPT KEYWORDS/fr (75% translated)")
-   [italiano](https://wiki.gentoo.org/wiki/ACCEPT_KEYWORDS/it "ACCEPT KEYWORDS/it (50% translated)")
-   [magyar](https://wiki.gentoo.org/wiki/ACCEPT_KEYWORDS/hu "ACCEPT KEYWORDS/hu (80% translated)")
-   [português](https://wiki.gentoo.org/wiki/ACCEPT_KEYWORDS/pt "ACCEPT KEYWORDS/pt (25% translated)")
-   [português do Brasil](https://wiki.gentoo.org/wiki/ACCEPT_KEYWORDS/pt-br "ACCEPT KEYWORDS/pt-br (50% translated)")
-   [svenska](https://wiki.gentoo.org/wiki/ACCEPT_KEYWORDS/sv "ACCEPT KEYWORDS/sv (50% translated)")
-   [čeština](https://wiki.gentoo.org/wiki/ACCEPT_KEYWORDS/cs "ACCEPT KEYWORDS/cs (5% translated)")
-   [русский](https://wiki.gentoo.org/wiki/ACCEPT_KEYWORDS/ru "ACCEPT KEYWORDS/ru (100% translated)")
-   [中文](https://wiki.gentoo.org/wiki/ACCEPT_KEYWORDS/zh "ACCEPT KEYWORDS/zh (5% translated)")
-   [中文（中国大陆）‎](https://wiki.gentoo.org/wiki/ACCEPT_KEYWORDS/zh-cn "ACCEPT KEYWORDS/zh-cn (50% translated)")
-   [日本語](https://wiki.gentoo.org/wiki/ACCEPT_KEYWORDS/ja "ACCEPT KEYWORDS/ja (100% translated)")
-   [한국어](https://wiki.gentoo.org/wiki/ACCEPT_KEYWORDS/ko "ACCEPT KEYWORDS/ko (40% translated)")

\

The `ACCEPT_KEYWORDS` variable informs the package manager which ebuilds\' [`KEYWORDS`](https://wiki.gentoo.org/wiki/KEYWORDS "KEYWORDS") values it is allowed to accept. This variable is used to select either [stable](https://wiki.gentoo.org/wiki/Handbook:X86/Portage/Branches#Stable "Handbook:X86/Portage/Branches") or [testing](https://wiki.gentoo.org/wiki/Handbook:X86/Portage/Branches#Testing "Handbook:X86/Portage/Branches") branch as default.

## Contents

-   [[1] [Where the variable is set?]](#Where_the_variable_is_set.3F)
-   [[2] [Stable and unstable keywords]](#Stable_and_unstable_keywords)
-   [[3] [See also]](#See_also)
-   [[4] [References]](#References)

## [][Where the variable is set?]

The variable is usually set through the Gentoo [profile](https://wiki.gentoo.org/wiki/Portage/Profiles "Portage/Profiles") but can be overruled *system wide* in [[/etc/portage/make.conf](https://wiki.gentoo.org/wiki//etc/portage/make.conf "/etc/portage/make.conf")], *per-package* in [[/etc/portage/package.accept_keywords](https://wiki.gentoo.org/wiki//etc/portage/package.accept_keywords "/etc/portage/package.accept keywords")], or even *for a single emerge* on the command line, though this is not recommended.

** Important**\
It is generally considered a bad idea to override the `ACCEPT_KEYWORDS` variable on the command line, such as by using [ACCEPT_KEYWORDS=\<keyword\> emerge -av \], as this is not persistent and might result in unwanted behavior from the package manager.

## [Stable and unstable keywords]

** Warning**\
A common misconception is that when a package requires testing, applying \~amd64 in make.conf seems like a solution, but instead it **may cause conflicts in future updates, and system breakage when attempting to downgrade glibc** since it applies to ALL packages to be on \~amd64. Refer to applying it to individual packages via package.accept_keywords directory.

The default value of most profiles\' `ACCEPT_KEYWORDS` variable is the architecture itself, like **[amd64]** or **[arm]**. In these cases, the package manager will only accept ebuilds whose `KEYWORDS` variable contains this architecture. If the user wants to be able to install and work with ebuilds that are not considered production-ready yet, they can add the same architecture but with the `~` prefix to it, like so:

[FILE] **[`/etc/portage/make.conf`](https://wiki.gentoo.org/wiki//etc/portage/make.conf "/etc/portage/make.conf")**

    ACCEPT_KEYWORDS="~amd64"

One should not specify the stable keyword (**[amd64]**) when adding the testing keyword (**[\~amd64]**) because `ACCEPT_KEYWORDS` is an incremental variable.

If the setting is not to be made system-wide, then it can be set per-package in the [package.accept_keywords] file or directory:

** Important**\
[/etc/portage/package.accept_keywords](https://wiki.gentoo.org/wiki//etc/portage/package.accept_keywords "/etc/portage/package.accept keywords") has a full overview of using this feature and the below should only be considered an overview.

[FILE] **[`/etc/portage/package.accept_keywords`](https://wiki.gentoo.org/wiki//etc/portage/package.accept_keywords "/etc/portage/package.accept keywords")**

    # games
    games-fps/doomsday ~amd64

In addition to the normal values from `ACCEPT_KEYWORDS`, [package.accept_keywords] supports three special tokens^[\[1\]](#cite_note-1)^:

-   `*` --- Package is visible if it is stable on any architecture.
-   `~*` --- Package is visible if it is in testing on any architecture.
-   `**` --- Package is always visible (`KEYWORDS` are ignored completely).

The last choice is useful for live package versions (e.g. SVN/Git/Mercurial package versions) because live ebuilds don\'t have a `KEYWORDS` variable.

** Note**\
The behavior of \~*arch* and \~\* differ: \~*arch* includes *arch*, \~\* doesn\'t include \*. To use the most recent version of a package which is marked stable or unstable on any architecture, specify \"\* \~\*\".

## [See also]

-   [/etc/portage/package.accept_keywords](https://wiki.gentoo.org/wiki//etc/portage/package.accept_keywords "/etc/portage/package.accept keywords") --- files or directories of files containing definitions for per-package `ACCEPT_KEYWORDS` statements.
-   [KEYWORDS](https://wiki.gentoo.org/wiki/KEYWORDS "KEYWORDS") --- the `KEYWORDS` variable informs in which [architectures](https://wiki.gentoo.org/wiki/Handbook:Main_Page#Architectures "Handbook:Main Page") the ebuild is stable or still in testing phase.
-   [Knowledge Base:Accepting a keyword for a single package](https://wiki.gentoo.org/wiki/Knowledge_Base:Accepting_a_keyword_for_a_single_package "Knowledge Base:Accepting a keyword for a single package")
-   [Knowledge Base:Accepting a keyword for all packages](https://wiki.gentoo.org/wiki/Knowledge_Base:Accepting_a_keyword_for_all_packages "Knowledge Base:Accepting a keyword for all packages")

## [References]

1.  [[[↑](#cite_ref-1)] [Gentoo Portage, [Manual page for Portage](https://dev.gentoo.org/~zmedico/portage/doc/man/portage.5.html). Retrieved on January 30th, 2015.]]