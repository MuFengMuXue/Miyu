This page contains [[changes](https://wiki.gentoo.org/index.php?title=Portage/Profiles&oldid=1437612&diff=1440133)] which are not marked for translation.

Other languages:

-   [English]
-   [magyar](https://wiki.gentoo.org/wiki/Portage/Profiles/hu "Profil (Portage) (19% translated)")
-   [日本語](https://wiki.gentoo.org/wiki/Portage/Profiles/ja "Portage/プロファイル (44% translated)")

**[Portage - the heart of Gentoo](https://wiki.gentoo.org/wiki/Portage "Portage")**\
[emerge](https://wiki.gentoo.org/wiki/Emerge "Emerge") --- [configuration](https://wiki.gentoo.org/wiki//etc/portage/make.conf "/etc/portage/make.conf") --- [ebuild repository](https://wiki.gentoo.org/wiki/Ebuild_repository "Ebuild repository") --- [dispatch-conf](https://wiki.gentoo.org/wiki/Dispatch-conf "Dispatch-conf")\
[\
[world file](https://wiki.gentoo.org/wiki/Selected-packages_set_(Portage) "Selected-packages set (Portage)") --- [USE flags](https://wiki.gentoo.org/wiki/USE_flag "USE flag") --- [ebuilds](https://wiki.gentoo.org/wiki/Ebuild "Ebuild") --- [profiles]\
[upgrades](https://wiki.gentoo.org/wiki/Upgrading_Gentoo "Upgrading Gentoo") --- [using testing packages](https://wiki.gentoo.org/wiki/Knowledge_Base:Accepting_a_keyword_for_a_single_package "Knowledge Base:Accepting a keyword for a single package") --- [Gentoo binhost](https://wiki.gentoo.org/wiki/Gentoo_Binary_Host_Quickstart "Gentoo Binary Host Quickstart")\
[tools](https://wiki.gentoo.org/wiki/Useful_Portage_tools "Useful Portage tools") --- [gentoolkit](https://wiki.gentoo.org/wiki/Gentoolkit "Gentoolkit") --- [eselect](https://wiki.gentoo.org/wiki/Eselect "Eselect")\
[Portage FAQ](https://wiki.gentoo.org/wiki/Project:Portage/FAQ "Project:Portage/FAQ") --- [cheat sheet](https://wiki.gentoo.org/wiki/Gentoo_Cheat_Sheet "Gentoo Cheat Sheet") --- [FAQ](https://wiki.gentoo.org/wiki/FAQ "FAQ")\
[all articles](https://wiki.gentoo.org/wiki/Category:Portage "Category:Portage")\
]

**Profiles**

**[Profiles]**

[Structure](https://wiki.gentoo.org/wiki/Portage/Profiles/Structure "Portage/Profiles/Structure")

[Custom profiles](https://wiki.gentoo.org/wiki/Portage/Profiles/Custom_profiles "Portage/Profiles/Custom profiles")

[Switching profiles](https://wiki.gentoo.org/wiki/Portage/Profiles/Switching_profiles "Portage/Profiles/Switching profiles")

**Customized profiles**

[Hardened desktop profiles](https://wiki.gentoo.org/wiki/Hardened_Desktop_Profiles "Hardened Desktop Profiles")

[Hardened Plasma profile](https://wiki.gentoo.org/wiki/KDE/Hardened_KDE_Plasma_profile "KDE/Hardened KDE Plasma profile")

[Hardened GNOME profiles](https://wiki.gentoo.org/wiki/GNOME/Guide/Hardened_GNOME_Profiles "GNOME/Guide/Hardened GNOME Profiles")

[Clang desktop profile](https://wiki.gentoo.org/wiki/LLVM/Clang/Desktop_profile "LLVM/Clang/Desktop profile")

[LTO profile](https://wiki.gentoo.org/wiki/LTO/LTO_profile "LTO/LTO profile")

**Profiles** are a core [Portage](https://wiki.gentoo.org/wiki/Portage "Portage") feature that allow the highly flexible Gentoo metadistribution to be primed for use on target systems. Profiles provide minimal workable baselines to fit system usage-requirements, and allow for a high-degree of customization. A profile is chosen [at installation time](https://wiki.gentoo.org/wiki/Handbook:AMD64/Installation/Base#Choosing_the_right_profile "Handbook:AMD64/Installation/Base"), though profiles can often be changed if requirements evolve.

Profiles determine compatible subsets of the metadistribution to provide the user with composable features. By compartmentalizing mutually exclusive components and configurations, they provide one of the pillars of Gentoo\'s extreme flexibility: 15 supported architectures, many subarchitectures, several platforms, a choice of libc, init systems, toolchains, optional hardening, combined with all the supported Gentoo use-cases - from server, to workstation, to embedded - require such a robust architecure as provided by profiles.

Technically, profiles define core low-level parameters on different system architectures, they can determine package availability, specify default states for [USE flags](https://wiki.gentoo.org/wiki/USE_flag "USE flag"), set default values for [/etc/portage/make.conf](https://wiki.gentoo.org/wiki//etc/portage/make.conf "/etc/portage/make.conf") variables, adjust the [set of system packages](https://wiki.gentoo.org/wiki/System_set_(Portage) "System set (Portage)"), determine default toolchains and core system libraries, amongst other things.

New profiles are [made available](https://wiki.gentoo.org/wiki/Upgrading_Gentoo "Upgrading Gentoo") when there are fundamental changes to the way Gentoo works, though such releases can be years apart: when the 23.0 profile was released, the previous profile (17.1) was nearly 6 years old. Be aware that many profiles are experimental, and thus can require involved and sometimes difficult work, so stable profiles should be used unless there is a specific requirement not to.

Some profiles can be switched easily when required, though certain profile changes will require more steps than just switching the profile, and a few specific profiles can be extremely difficult to switch between, and it is not possible to change to profiles with a different [ABI](https://wiki.gentoo.org/wiki/Application_binary_interface "Application binary interface") (e.g. pure LLVM or musl profiles) without a reinstall.

Profiles are defined on an [ebuild repository](https://wiki.gentoo.org/wiki/Ebuild_repository "Ebuild repository") basis; the ones from [the main repository](https://wiki.gentoo.org/wiki//var/db/repos/gentoo/profiles "/var/db/repos/gentoo/profiles") are maintained by the Gentoo developers, but users can [define their own](https://wiki.gentoo.org/wiki/Portage/Profiles/Custom_profiles "Portage/Profiles/Custom profiles").

** Important**\
When a profile update is released, only change profile *versions* after **reading and following the corresponding [news item](https://wiki.gentoo.org/wiki/Handbook:AMD64/Installation/Base#Reading_news_items "Handbook:AMD64/Installation/Base")**.

** See also**\
See the [Handbook](https://wiki.gentoo.org/wiki/Handbook:AMD64/Installation/Base#Choosing_the_right_profile "Handbook:AMD64/Installation/Base") has information on selecting profiles.

## Contents

-   [[1] [Profile stability]](#Profile_stability)
    -   [[1.1] [Stable (stable)]](#Stable_.28stable.29)
    -   [[1.2] [In-development (dev)]](#In-development_.28dev.29)
    -   [[1.3] [Experimental (exp)]](#Experimental_.28exp.29)
-   [[2] [Available profiles]](#Available_profiles)
    -   [[2.1] [OpenRC and systemd profiles]](#OpenRC_and_systemd_profiles)
    -   [[2.2] [Desktop profiles]](#Desktop_profiles)
    -   [[2.3] [Hardened profiles]](#Hardened_profiles)
    -   [[2.4] [amd64 multilib and no-multilib profiles]](#amd64_multilib_and_no-multilib_profiles)
    -   [[2.5] [split-usr profiles]](#split-usr_profiles)
    -   [[2.6] [Experimental and in-development profiles]](#Experimental_and_in-development_profiles)
-   [[3] [Switching profiles]](#Switching_profiles)
-   [[4] [Upgrading profiles]](#Upgrading_profiles)
-   [[5] [See also]](#See_also)
-   [[6] [External resources]](#External_resources)

## [Profile stability]

General-usage profiles are marked stable, only use other profiles if fully-cognizant of non-stable profile usage.

### [][Stable (stable)]

Stable profiles are fully tested and should provide a *just works* experience. Gentoo\'s CI checks that stable profiles have a sound dependency graph. All stable profiles are marked with \"*(stable)*\".

### [][In-development (dev)]

During the development process that aims to create stable profiles, work in progress profiles are marked as \"*(dev)*\". Gentoo\'s CI checks these profiles for issues in the dependency graph, but issues only a warning and not an error.

Users running these should only be doing so if they have a certain need that can only be resolved by using them.

### [][Experimental (exp)]

An experimental profile is, as the name suggests, an experiment. It may or may not result in a new \"permanent\" profile. These profiles are marked \"*(exp)*\".

Many profiles of exotic architectures are marked as experimental.

Experimental profiles should work, as they have undergone some level of testing. However, the fixes to make it run are normally included in testing keyword packages so a user of these should either be running `~ARCH` globally or at the very least be prepared to use [/etc/portage/package.accept_keywords](https://wiki.gentoo.org/wiki//etc/portage/package.accept_keywords "/etc/portage/package.accept keywords") to pull in the latest versions and fill a bug to [stable request](https://wiki.gentoo.org/wiki/Stable_request "Stable request") the package if found to be safe by the user.

In short, expect to have random issues when using these profiles.

## [Available profiles]

This section explains what some commonly encountered profiles are used for.

The full list of profiles for all architectures is [available in the Gentoo repository](https://gitweb.gentoo.org/repo/gentoo.git/tree/profiles/profiles.desc). As evident in the profile names from that list, the current profiles version for most architectures is version 23.0.

The most basic profiles available are `default/linux/<architecture>/23.0` and `default/linux/<architecture>/23.0/systemd`. These can for example be used for server systems, in container installations, or for machines that will have only a command line interface.

### [OpenRC and systemd profiles]

Profiles are split depending on which [init system](https://wiki.gentoo.org/wiki/Init_system "Init system") they use, into [OpenRC](https://wiki.gentoo.org/wiki/OpenRC "OpenRC") and [systemd](https://wiki.gentoo.org/wiki/Systemd "Systemd") variants. systemd profiles include the *systemd* qualifier, whereas OpenRC profiles are the ones that include no init system qualifier.

### [Desktop profiles]

Desktop profiles include the *desktop* qualifier, and are to be used for any graphical installation, whether using a [desktop environment](https://wiki.gentoo.org/wiki/Desktop_environment "Desktop environment"), [window manager](https://wiki.gentoo.org/wiki/Window_manager "Window manager"), [xorg](https://wiki.gentoo.org/wiki/Xorg "Xorg"), [wayland](https://wiki.gentoo.org/wiki/Wayland "Wayland"), etc.

The desktop profiles provide [GNOME](https://wiki.gentoo.org/wiki/GNOME "GNOME") and [Plasma](https://wiki.gentoo.org/wiki/KDE "KDE") variants - see the corresponding articles for details of setup using the correct profile.

These profiles only provide the bare minimum for desktop system usage, and are still as flexible as the less qualified profiles.

** Important**\
Failure to use a desktop profile on a graphical system will lead to a heavy setup and maintenance burden and various potential issues.

### [Hardened profiles]

Hardened profiles are available for [Hardened Gentoo](https://wiki.gentoo.org/wiki/Hardened_Gentoo "Hardened Gentoo") installations, though these require a more technical setup, and such systems have usage-constraints. These aren\'t used as frequently as non-hardened profiles.

### [amd64 multilib and no-multilib profiles]

For the **[amd64]** architecture, Gentoo provides support for the x86 architecture and it\'s x86_64 instruction set extension. For very specific use cases, users fully-cognizant of the constraints of constricting support to x86_64 only have the possibility to use the no-multilib profiles.

Note that no-multilib profiles are only provided for very specific use-cases, and are not advised for general use. Using these profiles needlessly can result in complex and time-consuming issues whenever still-common non x86_64 software needs to be used. Moving between no-multilib and standard profiles is practically impossible, and will usually require a full-system re-installation, so it\'s particularly important to never use these profiles unless they are specifically required.

### [split-usr profiles]

[Split [/usr]](https://wiki.gentoo.org/wiki/Split_/usr "Split /usr") profiles exist to support systems from before all data from [/bin], [/sbin], [/lib], and [/lib64] was merged into the [/usr/bin], [/usr/lib], and [/usr/lib64] directories.

### [Experimental and in-development profiles]

These profiles are often used by [testers](https://wiki.gentoo.org/wiki/Project:AMD64_Arch_Testers "Project:AMD64 Arch Testers"). They should only be used when specifically required, as stated above, for general-use pick a *stable* profile.

-   [LLVM](https://wiki.gentoo.org/wiki/LLVM "LLVM")
-   [musl](https://wiki.gentoo.org/wiki/Musl "Musl")
-   [Prefix](https://wiki.gentoo.org/wiki/Prefix "Prefix")
-   [[][[[x32]](https://en.wikipedia.org/wiki/x32_ABI "wikipedia:x32 ABI")[][[x32 ABI []](https://en.wikipedia.org/wiki/x32_ABI "wikipedia:x32 ABI")]][[[][0]]]], on **[amd64]**

## [Switching profiles]

Sometimes when the usage of a system changes, or when realizing that another profile is a better fit, it can be necessary to [switch profiles](https://wiki.gentoo.org/wiki/Portage/Profiles/Switching_profiles "Portage/Profiles/Switching profiles").

After the release of a new profile, profiles can need to be upgraded - see the [upgrading profiles](#Upgrading_profiles) section.

## [Upgrading profiles]

** Warning**\
Profile upgrades are not to be taken lightly. Make sure to read and follow proper instructions.

The user is informed of the availability of a profile update by the publication of a [news item](https://wiki.gentoo.org/wiki/Handbook:AMD64/Installation/Base#Reading_news_items "Handbook:AMD64/Installation/Base"), which will be reported after a Gentoo ebuild repository sync. This will include detailed instructions that should be properly followed. A profile upgrade is a non trivial operation and, as always, systems should be regularly [backed up](https://wiki.gentoo.org/wiki/Backup "Backup") - particularly before system changes.

See the article on [upgrading Gentoo](https://wiki.gentoo.org/wiki/Upgrading_Gentoo#Keeping_up_with_new_profiles "Upgrading Gentoo") for information on profile updates.

## [See also]

-   [/var/db/repos/gentoo/profiles](https://wiki.gentoo.org/wiki//var/db/repos/gentoo/profiles "/var/db/repos/gentoo/profiles") --- a directory that contains global [profiles](https://wiki.gentoo.org/wiki/Profile_(Portage) "Profile (Portage)") that are controlled by developers of the Gentoo ebuild repository (gentoo.git)
-   [Multilib layout](https://wiki.gentoo.org/wiki/Project:AMD64/Multilib_layout "Project:AMD64/Multilib layout") for **[amd64]** architecture.
-   [How to change to SELinux](https://wiki.gentoo.org/wiki/SELinux/Installation "SELinux/Installation")
-   [Upgrading Gentoo](https://wiki.gentoo.org/wiki/Upgrading_Gentoo#Updating_to_23.0_profile "Upgrading Gentoo")

## [External resources]

-   [Gentoo news: Profile upgrade to version 23.0 available](https://www.gentoo.org/support/news-items/2024-03-22-new-23-profiles.html)
-   [Gentoo: profiles and keywords rather than releases](https://blogs.gentoo.org/mgorny/2024/08/20/gentoo-profiles-and-keywords-rather-than-releases/)

For developers:

-   [Profiles section of Gentoo devmanual](https://devmanual.gentoo.org/profiles/index.html)
-   [Profiles section](https://projects.gentoo.org/pms/8/pms.html#x1-410005) of [Package Manager Specification](https://wiki.gentoo.org/wiki/Package_Manager_Specification "Package Manager Specification")
-   [Profiles directory section](https://projects.gentoo.org/pms/8/pms.html#x1-320004.4) of Package Manager Specification