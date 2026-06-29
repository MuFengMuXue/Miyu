[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Configuration_file_management&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

Managing [configuration files](https://en.wikipedia.org/wiki/Configuration_file "wikipedia:Configuration file") is a key skill in system administration. Updated configuration files for core system software suites occasionally ship with new software releases. When available via a package upgrade, the newly updated configuration files from upstream will need to be reconciled with existing local configuration files in a sane manner.

If the system administrator has not modified the existing local configuration files, then generally newer files can be \'clobbered\' (overwritten) over older versions. Things become a little more complicated when existing configuration files are modified beyond their original content, and a newer file contains changes that should be merged into the original. That is where configuration management systems become helpful.

## Contents

-   [[1] [Available software]](#Available_software)
    -   [[1.1] [Included with Portage]](#Included_with_Portage)
    -   [[1.2] [Alternative software]](#Alternative_software)
-   [[2] [See also]](#See_also)
-   [[3] [External resources]](#External_resources)

## [Available software]

### [Included with Portage]

[Portage](https://wiki.gentoo.org/wiki/Portage "Portage") ships with one tool in order to help system administrators manage software on the system.

[[dispatch-conf](https://wiki.gentoo.org/wiki/Dispatch-conf "Dispatch-conf")]

### [Alternative software]

[[cfg-update](https://wiki.gentoo.org/wiki/Cfg-update "Cfg-update")]

## [See also]

-   [CONFIG_PROTECT](https://wiki.gentoo.org/wiki/CONFIG_PROTECT "CONFIG PROTECT") --- contains a space-delimited list of files and directories that Portage will protect from automatic modification.
-   [savedconfig](https://wiki.gentoo.org/wiki/Savedconfig "Savedconfig") --- a USE flag that preserves the saved configuration files upon package updates.

## [External resources]

-   [https://devmanual.gentoo.org/general-concepts/config-protect/index.html](https://devmanual.gentoo.org/general-concepts/config-protect/index.html)