** Warning**\
This page is a work in process by Gentoo wiki contributors. Anyone is welcome to help by creating articles (listed below) that do not exist on the wiki. Join [[#gentoo-wiki](ircs://irc.libera.chat/#gentoo-wiki)] ([[webchat](https://web.libera.chat/#gentoo-wiki)]) if you have any questions!

Please list topics that users of the Gentoo wiki would like to see added to the Gentoo wiki.

** See also**\
See also the [Stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub") category index page for articles that need expansion, the [Todo](https://wiki.gentoo.org/wiki/Category:Todo "Category:Todo") category for everything marked as needing work on the wiki, and the [help improve Gentoo by getting involved with documentation!](https://wiki.gentoo.org/wiki/Help_improve_Gentoo_by_getting_involved_with_documentation! "Help improve Gentoo by getting involved with documentation!") article.

If any pages requested here are found to already exist on the wiki, please cross them off the list or remove the corresponding entry.

** Tip**\
Before creating an article for a request on this page, it may be a good idea to check if such an article does not already exist - it could actually be this page that is out of date!

## Contents

-   [[1] [Gentoo development]](#Gentoo_development)
-   [[2] [Project and community]](#Project_and_community)
-   [[3] [Core system]](#Core_system)
    -   [[3.1] [Base system]](#Base_system)
    -   [[3.2] [Installation]](#Installation)
    -   [[3.3] [System tools and daemons]](#System_tools_and_daemons)
    -   [[3.4] [Virtualization, containers, chroots, etc.]](#Virtualization.2C_containers.2C_chroots.2C_etc.)
    -   [[3.5] [Provisioning tools]](#Provisioning_tools)
    -   [[3.6] [Configuration management tools]](#Configuration_management_tools)
-   [[4] [Software]](#Software)
    -   [[4.1] [Data compression]](#Data_compression)
    -   [[4.2] [Shell and terminal console]](#Shell_and_terminal_console)
    -   [[4.3] [Graphical]](#Graphical)
-   [[5] [Hardware]](#Hardware)
-   [[6] [Desktop]](#Desktop)
-   [[7] [Server and security]](#Server_and_security)
    -   [[7.1] [Continuous integration]](#Continuous_integration)
    -   [[7.2] [Static website engines]](#Static_website_engines)
    -   [[7.3] [XMPP servers]](#XMPP_servers)
    -   [[7.4] [Network services]](#Network_services)
-   [[8] [Redlinks]](#Redlinks)

## [Gentoo development]

-   [Resolving endianness issues in C](https://wiki.gentoo.org/index.php?title=Resolving_endianness_issues_in_C&action=edit&redlink=1 "Resolving endianness issues in C (page does not exist)") akin to the [Modern C porting](https://wiki.gentoo.org/wiki/Modern_C_porting "Modern C porting"), article. This should cover all of the ways endian issues can bite programmers and ebuild maintainers. As most software is written implicitly assuming a little-endian target such as [AMD64](https://wiki.gentoo.org/wiki/AMD64 "AMD64") or [ARM](https://wiki.gentoo.org/wiki/ARM "ARM") and this most commonly causes issues when compiling on [PPC](https://wiki.gentoo.org/wiki/PPC "PPC")/[PPC64](https://wiki.gentoo.org/wiki/PPC64 "PPC64"), so this should be the base case the article deals with. That said, other platforms (where different) and odd edge-cases should also get covered.

Sam suggested using the [Alpha porting guide](https://wiki.gentoo.org/wiki/Project:Alpha/Porting_guide "Project:Alpha/Porting guide") as a jumping off point.

-   Endianness articles for languages other than C, use [Resolving endianness issues in C](https://wiki.gentoo.org/index.php?title=Resolving_endianness_issues_in_C&action=edit&redlink=1 "Resolving endianness issues in C (page does not exist)") as a reference.
-   [Boost](https://wiki.gentoo.org/index.php?title=Boost&action=edit&redlink=1 "Boost (page does not exist)") - stub for [[[dev-libs/boost]](https://packages.gentoo.org/packages/dev-libs/boost)[]]. Users will see this package often, in updates, dependencies, etc. Might be nice to have at least a stub for it to explain what it is and give links to sites, docs, packages, etc. It would provide a root page for [Boost/How_build_systems_find_boost](https://wiki.gentoo.org/wiki/Boost/How_build_systems_find_boost "Boost/How build systems find boost") also.

## [Project and community]

-   [Introduction to Gentoo Linux](https://wiki.gentoo.org/index.php?title=Introduction_to_Gentoo_Linux&action=edit&redlink=1 "Introduction to Gentoo Linux (page does not exist)") (perhaps to replace [Benefits of Gentoo](https://wiki.gentoo.org/wiki/Benefits_of_Gentoo "Benefits of Gentoo")) - a more \"neutral\" description of differences between Gentoo and other distros is needed; not simply a \"pro/con\" style tit-for-tat, since what\'s a \"pro\" to one user may be a \"con\" for others. - In Process\... ( [Matthew Marchese (Maffblaster) ](https://wiki.gentoo.org/wiki/User:Maffblaster "User:Maffblaster"))

## [Core system]

### [Base system]

-   [RAID](https://wiki.gentoo.org/index.php?title=RAID&action=edit&redlink=1 "RAID (page does not exist)")
-   [mdadm](https://wiki.gentoo.org/wiki/Mdadm "Mdadm")

### [Installation]

-   [Multi-boot](https://wiki.gentoo.org/wiki/Multi-boot "Multi-boot") - A guide on how to boot multiple operating systems?- [YKalaf ](https://wiki.gentoo.org/index.php?title=User:YKalaf&action=edit&redlink=1 "User:YKalaf (page does not exist)")
-   [LiveDVD](https://wiki.gentoo.org/index.php?title=LiveDVD&action=edit&redlink=1 "LiveDVD (page does not exist)") - we have [LiveUSB](https://wiki.gentoo.org/wiki/LiveUSB "LiveUSB") and, say, [Project:RelEng/LiveDVD](https://wiki.gentoo.org/wiki/Project:RelEng/LiveDVD "Project:RelEng/LiveDVD") (and even [LiveDVD-Persistence-Mode](https://wiki.gentoo.org/wiki/LiveDVD-Persistence-Mode "LiveDVD-Persistence-Mode")!), but no dedicated article for the LiveDVD(s).

### [System tools and daemons]

*Currently no requested articles.*

### [][Virtualization, containers, chroots, etc.]

-   [Chroot Guide](https://wiki.gentoo.org/index.php?title=Chroot_Guide&action=edit&redlink=1 "Chroot Guide (page does not exist)") (to test self-written ebuilds) - In progress\... ( [Matthew Marchese (maffblaster) ](https://wiki.gentoo.org/wiki/User:Maffblaster "User:Maffblaster"))
    -   [Chroot](https://wiki.gentoo.org/wiki/Chroot "Chroot"), [x86 Chroot Guide (x86 Project)](https://wiki.gentoo.org/wiki/Project:X86/Chroot_Guide "Project:X86/Chroot Guide"), [32-bit Chroot Guide (AMD64 project)](https://wiki.gentoo.org/wiki/Project:AMD64/32-bit_Chroot_Guide "Project:AMD64/32-bit Chroot Guide"), [maybe use Schroot](https://wiki.debian.org/Schroot)
-   [Profile switching](https://wiki.gentoo.org/index.php?title=Profile_switching&action=edit&redlink=1 "Profile switching (page does not exist)") (Arch/Subarch, multilib,\...) -
    -   See [Project:Docker](https://wiki.gentoo.org/wiki/Project:Docker "Project:Docker") for the official Gentoo project.

### [Provisioning tools]

-   [Cobbler](https://wiki.gentoo.org/index.php?title=Cobbler&action=edit&redlink=1 "Cobbler (page does not exist)") -

### [Configuration management tools]

-   [Salt](https://wiki.gentoo.org/index.php?title=Salt&action=edit&redlink=1 "Salt (page does not exist)") -

## [Software]

### [Data compression]

-   [zpaq](https://wiki.gentoo.org/index.php?title=Zpaq&action=edit&redlink=1 "Zpaq (page does not exist)") - in progress ([User:Ng0/drafts/zpaq](https://wiki.gentoo.org/wiki/User:Ng0/drafts/zpaq "User:Ng0/drafts/zpaq") [ng0 ](https://wiki.gentoo.org/wiki/User:Ng0 "User:Ng0"))

### [Shell and terminal console]

*Currently no requested articles.*

### [Graphical]

-   [Playing DVDs and BluRays](https://wiki.gentoo.org/index.php?title=Playing_DVDs_and_BluRays&action=edit&redlink=1 "Playing DVDs and BluRays (page does not exist)") -

## [Hardware]

-   [Apcupsd](https://wiki.gentoo.org/index.php?title=Apcupsd&action=edit&redlink=1 "Apcupsd (page does not exist)"): an application for interacting with APC uninterruptible power supplies -

## [Desktop]

*Currently no requested articles.*

## [Server and security]

### [Continuous integration]

-   [TravisCI](https://wiki.gentoo.org/index.php?title=TravisCI&action=edit&redlink=1 "TravisCI (page does not exist)") -

### [Static website engines]

-   [Jekyll](https://wiki.gentoo.org/index.php?title=Jekyll&action=edit&redlink=1 "Jekyll (page does not exist)") -
-   [Pelican](https://wiki.gentoo.org/index.php?title=Pelican&action=edit&redlink=1 "Pelican (page does not exist)") -

### [XMPP servers]

-   [prosody](https://wiki.gentoo.org/index.php?title=Prosody&action=edit&redlink=1 "Prosody (page does not exist)") -

### [Network services]

-   [self-hosting email](https://wiki.gentoo.org/index.php?title=Self-hosting_email&action=edit&redlink=1 "Self-hosting email (page does not exist)") - a detailed guide on everything involved in deploying and maintaining an email server, issues with mail delivery and spam, etc. and how to overcome them. See [https://workaround.org/](https://workaround.org/) as a good example of this.
-   [udhcpc](https://wiki.gentoo.org/index.php?title=Udhcpc&action=edit&redlink=1 "Udhcpc (page does not exist)") -
-   [etherape](https://wiki.gentoo.org/index.php?title=Etherape&action=edit&redlink=1 "Etherape (page does not exist)") -
-   [firehol](https://wiki.gentoo.org/index.php?title=Firehol&action=edit&redlink=1 "Firehol (page does not exist)") -
-   [fwbuilder](https://wiki.gentoo.org/index.php?title=Fwbuilder&action=edit&redlink=1 "Fwbuilder (page does not exist)") -
-   [network namespaces](https://wiki.gentoo.org/index.php?title=Network_namespaces&action=edit&redlink=1 "Network namespaces (page does not exist)") - seems of interest both to Gentoo users, and to the larger Linux community. There doesn\'t seem to be much information available currently.
-   [rdesktop](https://wiki.gentoo.org/index.php?title=Rdesktop&action=edit&redlink=1 "Rdesktop (page does not exist)") with grdesktop section
-   [sanewall](https://wiki.gentoo.org/index.php?title=Sanewall&action=edit&redlink=1 "Sanewall (page does not exist)") -
-   [shorewall](https://wiki.gentoo.org/index.php?title=Shorewall&action=edit&redlink=1 "Shorewall (page does not exist)") -
-   [ufw-frontends](https://wiki.gentoo.org/index.php?title=Ufw-frontends&action=edit&redlink=1 "Ufw-frontends (page does not exist)") -
-   [zeroconf](https://wiki.gentoo.org/index.php?title=Zeroconf&action=edit&redlink=1 "Zeroconf (page does not exist)") -

## [Redlinks]

-   [Special:WantedPages](https://wiki.gentoo.org/wiki/Special:WantedPages "Special:WantedPages") - List generated by the wiki itself of [links that don\'t have a destination page](https://wiki.gentoo.org/wiki/Help:Links#Redlinks "Help:Links").