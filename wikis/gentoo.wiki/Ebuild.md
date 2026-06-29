This page contains [[changes](https://wiki.gentoo.org/index.php?title=Ebuild&oldid=1402620&diff=1427138)] which are not marked for translation.

Other languages:

-   [Deutsch](https://wiki.gentoo.org/wiki/Ebuild/de "Ebuild (76% translated)")
-   [English]
-   [magyar](https://wiki.gentoo.org/wiki/Ebuild/hu "Ebuild (100% translated)")
-   [português do Brasil](https://wiki.gentoo.org/wiki/Ebuild/pt-br "Ebuild (6% translated)")
-   [svenska](https://wiki.gentoo.org/wiki/Ebuild/sv "Ebuild (12% translated)")
-   [русский](https://wiki.gentoo.org/wiki/Ebuild/ru "ebuild-файл (100% translated)")
-   [中文（中国大陆）‎](https://wiki.gentoo.org/wiki/Ebuild/zh-cn "Ebuild (59% translated)")
-   [日本語](https://wiki.gentoo.org/wiki/Ebuild/ja "ebuild (100% translated)")

**[Portage - the heart of Gentoo](https://wiki.gentoo.org/wiki/Portage "Portage")**\
[emerge](https://wiki.gentoo.org/wiki/Emerge "Emerge") --- [configuration](https://wiki.gentoo.org/wiki//etc/portage/make.conf "/etc/portage/make.conf") --- [ebuild repository](https://wiki.gentoo.org/wiki/Ebuild_repository "Ebuild repository") --- [dispatch-conf](https://wiki.gentoo.org/wiki/Dispatch-conf "Dispatch-conf")\
[\
[world file](https://wiki.gentoo.org/wiki/Selected-packages_set_(Portage) "Selected-packages set (Portage)") --- [USE flags](https://wiki.gentoo.org/wiki/USE_flag "USE flag") --- [ebuilds] --- [profiles](https://wiki.gentoo.org/wiki/Portage/Profiles "Portage/Profiles")\
[upgrades](https://wiki.gentoo.org/wiki/Upgrading_Gentoo "Upgrading Gentoo") --- [using testing packages](https://wiki.gentoo.org/wiki/Knowledge_Base:Accepting_a_keyword_for_a_single_package "Knowledge Base:Accepting a keyword for a single package") --- [Gentoo binhost](https://wiki.gentoo.org/wiki/Gentoo_Binary_Host_Quickstart "Gentoo Binary Host Quickstart")\
[tools](https://wiki.gentoo.org/wiki/Useful_Portage_tools "Useful Portage tools") --- [gentoolkit](https://wiki.gentoo.org/wiki/Gentoolkit "Gentoolkit") --- [eselect](https://wiki.gentoo.org/wiki/Eselect "Eselect")\
[Portage FAQ](https://wiki.gentoo.org/wiki/Project:Portage/FAQ "Project:Portage/FAQ") --- [cheat sheet](https://wiki.gentoo.org/wiki/Gentoo_Cheat_Sheet "Gentoo Cheat Sheet") --- [FAQ](https://wiki.gentoo.org/wiki/FAQ "FAQ")\
[all articles](https://wiki.gentoo.org/wiki/Category:Portage "Category:Portage")\
]

** Note**\
This article covers **ebuild files**, for the [ebuild] command, see the [ebuild command section](https://wiki.gentoo.org/wiki/Portage#ebuild "Portage") of the [Portage](https://wiki.gentoo.org/wiki/Portage "Portage") article.

**Resources**

[[]][Wikipedia](https://en.wikipedia.org/wiki/Ebuild "wikipedia:Ebuild")

[[]][Guide](//wiki.gentoo.org/index.php?title=Special:MyLanguage/Basic_guide_to_write_Gentoo_Ebuilds)

An **ebuild** file is a text file, usually stored in a [repository](https://wiki.gentoo.org/wiki/Ebuild_repository "Ebuild repository"), which identifies a specific software package and tells the Gentoo package manager how to handle it. Ebuilds adhere to a specific [EAPI](https://wiki.gentoo.org/wiki/EAPI "EAPI") version, and are standardized through the [Package Manager Specification](https://wiki.gentoo.org/wiki/Package_Manager_Specification "Package Manager Specification"):

> The ebuild file format is in its basic form a subset of the format of a bash script. The interpreter is assumed to be GNU bash

Ebuilds contain metadata about each version of a piece of available software (name, version number, license, home page address\...), dependency information (both build-time and run-time), and instructions on how to build and install the software (configure, compile, build, install, test\...).

The default location for ebuilds in Gentoo is the [Gentoo ebuild repository](https://wiki.gentoo.org/wiki/Ebuild_repository#The_Gentoo_ebuild_repository "Ebuild repository") ([[/var/db/repos/gentoo](https://wiki.gentoo.org/wiki//var/db/repos/gentoo "/var/db/repos/gentoo")/]).

** See also**\
See the [ebuild repository article](https://wiki.gentoo.org/wiki/Ebuild_repository "Ebuild repository") about what an ebuild repository is, the [creating an ebuild repository](https://wiki.gentoo.org/wiki/Creating_an_ebuild_repository "Creating an ebuild repository") article on how to create them, and the [basic guide to write Gentoo Ebuilds](https://wiki.gentoo.org/wiki/Basic_guide_to_write_Gentoo_Ebuilds "Basic guide to write Gentoo Ebuilds") for creating ebuilds to house in a repository.

## [[] Live ebuilds]

An ebuild is a **[live ebuild](https://wiki.gentoo.org/wiki/Live_ebuilds "Live ebuilds")** if the source is fetched from a revision control system (VCS). They tend to, but not necessarily, have the version number 9999 so that they can be easily distinguished from normal ebuilds based on upstream releases.

In a formal sense, an ebuild is *live* if it has a variable `PROPERTIES` with a value \"live\" inside it. If an ebuild inherits a VCS eclass (e.g. git-r3, mercurial, darcs), it will be live, because these eclasses have a line `PROPERTIES+=" live"`.

## [[] See also]

-   [Basic guide to write Gentoo Ebuilds](https://wiki.gentoo.org/wiki/Basic_guide_to_write_Gentoo_Ebuilds "Basic guide to write Gentoo Ebuilds") --- getting started writing **[ebuilds]**, to harness the power of [Portage](https://wiki.gentoo.org/wiki/Portage "Portage"), to install and manage even more software.
-   [Submitting ebuilds](https://wiki.gentoo.org/wiki/Submitting_ebuilds "Submitting ebuilds") --- explains how to submit ebuilds for inclusion in the [Gentoo ebuild repository](https://wiki.gentoo.org/wiki/Ebuild_repository#The_Gentoo_ebuild_repository "Ebuild repository")
-   [Package Manager Specification](https://wiki.gentoo.org/wiki/Package_Manager_Specification "Package Manager Specification") --- a standardization effort to ensure that the [ebuild] file format, the ebuild repository format (of which the Gentoo ebuild repository is the main incarnation), as well as behavior of the package managers interacting with these ebuilds is properly agreed upon and documented.
-   [Portage](https://wiki.gentoo.org/wiki/Portage "Portage") --- the official [package manager](https://en.wikipedia.org/wiki/Package_manager "wikipedia:Package manager") and [distribution system](https://www.gentoo.org/get-started/about/) for Gentoo.

## [[] External resources]

-   [ebuild eclass reference](https://devmanual.gentoo.org/eclass-reference/ebuild/index.html) in the developer manual
-   [ebuild-maintainer-quiz.txt](https://gitweb.gentoo.org/sites/projects/comrel.git/tree/recruiters/quizzes/ebuild-maintainer-quiz.txt) - Gentoo developer ebuild quiz
-   [ebuild command\'s man page](https://dev.gentoo.org/~zmedico/portage/doc/man/ebuild.1.html)
-   [ebuild file format man page](https://dev.gentoo.org/~zmedico/portage/doc/man/ebuild.5.html)
-   [Gentoo devmanual](https://devmanual.gentoo.org/index.html)
-   [Quickstart ebuild guide](https://devmanual.gentoo.org/quickstart/index.html) from the devmanual