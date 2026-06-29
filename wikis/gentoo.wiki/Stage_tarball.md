This page contains [[changes](https://wiki.gentoo.org/index.php?title=Stage_file&oldid=1400571&diff=1440134)] which are not marked for translation.

Other languages:

-   [English]
-   [français](https://wiki.gentoo.org/wiki/Stage_file/fr "Stage tarball (16% translated)")
-   [magyar](https://wiki.gentoo.org/wiki/Stage_file/hu "Stage fájl (100% translated)")
-   [日本語](https://wiki.gentoo.org/wiki/Stage_file/ja "Stage ファイル (100% translated)")

A **stage file** (also known as a *stage tarball*) is an archive that contains all the files to run a minimal Gentoo environment, typically to serve as a seed for a Gentoo installation.

Gentoo provides a selection of stage 3 files for [download](https://www.gentoo.org/downloads/), to cater to different installation configurations, on supported architectures.

Other stage files are used for internal Gentoo Linux development purposes. Customized stage files can also be [created](#Creating_stage_files) for specific requirements, if needed.

** Note**\
Only *stage 3* files are used for installation, stages 1 and 2 are for development purposes only.

## Contents

-   [[1] [Official Gentoo stage files]](#Official_Gentoo_stage_files)
    -   [[1.1] [Choosing a stage file for installation]](#Choosing_a_stage_file_for_installation)
    -   [[1.2] [Desktop stages]](#Desktop_stages)
    -   [[1.3] [Experimental stages]](#Experimental_stages)
    -   [[1.4] [No-multilib stages]](#No-multilib_stages)
-   [[2] [Stages by number]](#Stages_by_number)
    -   [[2.1] [Stage 3]](#Stage_3)
    -   [[2.2] [Stage 4]](#Stage_4)
    -   [[2.3] [Internal development stages]](#Internal_development_stages)
        -   [[2.3.1] [Stage 1]](#Stage_1)
        -   [[2.3.2] [Stage 2]](#Stage_2)
-   [[3] [Creating stage files]](#Creating_stage_files)
-   [[4] [See also]](#See_also)
-   [[5] [External resources]](#External_resources)

## [Official Gentoo stage files]

[] This section is a **work in progress**; treat its contents with caution - [ris](https://wiki.gentoo.org/wiki/User:Ris "User:Ris") ([talk](https://wiki.gentoo.org/wiki/User_talk:Ris "User talk:Ris") \| [contribs](https://wiki.gentoo.org/wiki/Special:Contributions/ris "Special:Contributions/ris")).

Gentoo\'s [Release Engineering](https://wiki.gentoo.org/wiki/Project:RelEng "Project:RelEng") team offers stage 3 files for [download](https://www.gentoo.org/downloads/) for installing Gentoo Linux. They are distributed via the [mirror system](https://www.gentoo.org/downloads/mirrors/).

The Gentoo stage files are built for a given [architecture](https://wiki.gentoo.org/wiki/Handbook:Main_Page#Architectures "Handbook:Main Page") for selected [profiles](https://wiki.gentoo.org/wiki/Portage/Profiles "Portage/Profiles").

The internal system uses [Catalyst](https://wiki.gentoo.org/wiki/Catalyst "Catalyst") to create the stage files according to a set of [spec files](https://gitweb.gentoo.org/proj/releng.git/tree/releases/specs/amd64).

### [Choosing a stage file for installation]

First think about what a system will be used for, the two main consideration are:

-   If the installation is to be a desktop system to be used with a graphical interface, or system purely used form the Command Line Interface, such as a server system
-   Whether the system will use the OpenRC or systemd init system

The choice of stage 3 to use for installation is tightly coupled with what profile will be selected later on in the installation. While it\'s possible to easily switch between certain profiles after installation, other switches can be more involved (e.g. switching init systems), with some requiring substantial effort and consideration, or even be impossible without complete re-installation. Thus it is important to choose wisely, and conservative choices are recommend for anyone who doesn\'t have specifc needs that require other stage 3/profile choices.

** Important**\
Switching between some profiles can require substantial effort and consideration, for example switching init systems is difficult, and switching from `no-multilib` to `multilib` requires extensive Gentoo and low-level toolchain knowledge. It is not possible to change to profiles with different [ABIs](https://wiki.gentoo.org/wiki/ABI "ABI") (e.g. pure [LLVM](https://wiki.gentoo.org/wiki/LLVM "LLVM") or [musl](https://wiki.gentoo.org/wiki/Musl "Musl") profiles), and reinstallation would be the only way to move between such profiles.

** Note**\
The stage files described below will often be available only for certain architectures.

The most basic stages will only have the name of the init system in their name (OpenRC or systemd), *stage3-\<architecture\>-openrc* or *stage3-\<architecture\>-systemd*. These stages are for Command Line Interface only systems, such as for servers, for use in containers, etc.

### [Desktop stages]

Desktop stages target a desktop environments (graphical/GUI). The USE flags on desktop stage file are fine tuned to enable all the basic requirements a desktop system will need such as video and audio playback.

These stages include packages such as [[[llvm-core/llvm]](https://packages.gentoo.org/packages/llvm-core/llvm)[]] and [[[dev-lang/rust-bin]](https://packages.gentoo.org/packages/dev-lang/rust-bin)[]] and can save many hours off the install, over trying to convert one of the other stages to a desktop system.

These stage 3 files have the word \"desktop\" in their name.

### [Experimental stages]

These are often used by [testers](https://wiki.gentoo.org/wiki/Project:AMD64_Arch_Testers "Project:AMD64 Arch Testers"). They should only be used when specifically required, for general-use pick a *stable* stage file.

[LLVM](https://wiki.gentoo.org/wiki/LLVM "LLVM") and/or [Musl](https://wiki.gentoo.org/wiki/Musl "Musl") stages are for advanced and specific installs types. As a general rule thumb the user will know when there is a need for them, rather then looking for a need to use one.

Note that musl users will find many common programs no longer being able to work without the use of workarounds. [Steam](https://wiki.gentoo.org/wiki/Steam "Steam") is one of the common issues user have with not working under musl.

LLVM users will find many programs are no longer able to compile for various reasons. For that reason alone it is expected for users to be able to report issues, look for patches or write their own and report this back to Gentoo and upstream project where possible.

It is not possible to switch back to glibc or GCC system without reinstalling Gentoo.

### [No-multilib stages]

** Warning**\
Switching from `no-multilib` to `multilib` is difficult to the point that it is usually preferred to reinstall rather than to switch between these profiles.

** Tip**\
Using `multilib` targets makes it easier to switch profiles later, compared to `no-multilib`

The multilib profile uses 64-bit libraries when possible, and falls back to the 32-bit versions when necessary. This is an excellent option for the majority of installations because it provides a great amount of flexibility for customization in the future.

Selecting a no-multilib tarball to be the base of the system excludes 32-bit system libraries. This will stop some apps from working, such as most games on [Steam](https://wiki.gentoo.org/wiki/Steam "Steam"). There are workarounds for this, however they can be very involved, so if any use of 32 bit software might be required in the future, no-multilib stage file should not be used.

It should be noted that if a user wishs to switch back to multilib at a later time, then reinstalling is often the only practical way to do so.

## [Stages by number]

### [Stage 3]

Stage 3 files are available on main website\'s [downloads page](https://www.gentoo.org/downloads/) and are hosted on [distfiles.gentoo.org](https://distfiles.gentoo.org/releases/) (navigate to the [\<arch\>/autobuilds/] directory).

Downloading and decompressing a stage 3 file, as described in the handbook\'s [stage file section](https://wiki.gentoo.org/wiki/Handbook:AMD64/Installation/Stage "Handbook:AMD64/Installation/Stage"), will install an almost-complete and mostly-functional system (the most important parts still missing are a kernel and a bootloader).

** Tip**\
The *desktop* stage files provide extra packages to help setup desktop systems more easily. If planning on installing a desktop system, using a desktop [profile](https://wiki.gentoo.org/wiki/Profile_(Portage) "Profile (Portage)"), choose the corresponding archive.

** See also**\
See the handbook sections entitled [what are stage files?](https://wiki.gentoo.org/wiki/Handbook:AMD64/Installation/Media#What_are_stages_then.3F "Handbook:AMD64/Installation/Media") and [choosing a stage file](https://wiki.gentoo.org/wiki/Handbook:AMD64/Installation/Stage#Choosing_a_stage_file "Handbook:AMD64/Installation/Stage") for more information about stage 3 files.

Stage 3 files are compiled from stage 2 files, but contain a [\@system set](https://wiki.gentoo.org/wiki/System_set_(Portage) "System set (Portage)") of packages.

Not including sub-profiles, the base file used for the system set of all profiles can be found at: [[/var/db/repos/gentoo/profiles/base/packages](https://gitweb.gentoo.org/repo/gentoo.git/tree/profiles/base/packages)].

### [Stage 4]

** Important**\
A \"stage 4\" file is a loosely defined term that generally just means a stage 3 with \'extra bits\'.

Official \"stage 4\" files were [previously available](https://blog.mthode.org/posts/2016/Jan/stage4-tarballs-minimal-and-cloud/) in January 2016 for the **[amd64]** architecture.

A cloud \"stage 4\" has been created to aid in the process of virtual machine provisioning. These stage 4 files can be used with [diskimage-builder] (available via [[[app-emulation/diskimage-builder]](https://packages.gentoo.org/packages/app-emulation/diskimage-builder)[]]). See the [Gentoo README upstream](https://github.com/openstack/diskimage-builder/tree/master/diskimage_builder/elements/gentoo) and [official diskimage-builder documentation](https://docs.openstack.org/developer/diskimage-builder/) for more information.

[Catalyst](https://wiki.gentoo.org/wiki/Catalyst/Stage_Creation "Catalyst/Stage Creation") is a tool for power users to create a stage4 with all the packages they require by default.

### [Internal development stages]

** Note**\
These stages are used by Gentoo developers to bootstrap the system for release, and are generally not intended for other uses.

Being mostly for development purposes, stage 1 or stage 2 files are unavailable for download.

#### [Stage 1]

Stage 1 files are generated from a [packages.build] file. Each [system profile](https://wiki.gentoo.org/wiki/Profile_(Portage) "Profile (Portage)") may have a *slightly* different [packages.build] file:

-   [var/db/repos/gentoo/profiles/arch/riscv/packages.build]
-   [var/db/repos/gentoo/profiles/default/linux/musl/packages.build]
-   [var/db/repos/gentoo/profiles/default/linux/packages.build]
-   [var/db/repos/gentoo/profiles/default/linux/uclibc/packages.build]
-   [var/db/repos/gentoo/profiles/features/musl/packages.build]
-   [var/db/repos/gentoo/profiles/features/uclibc/packages.build]
-   [var/db/repos/gentoo/profiles/targets/systemd/packages.build]

#### [Stage 2]

Stage 2 files contain the same packages as a stage 1 file with one caveat: stage 2 files are compiled *from* a stage 1 file. This is to ensure the stage 1 file contains the tool chain necessary to reproduce itself.

## [Creating stage files]

Stage files are [generated with catalyst](https://wiki.gentoo.org/wiki/Catalyst/Stage_Creation "Catalyst/Stage Creation") using appropriate [specs files](https://wiki.gentoo.org/wiki/Catalyst#Specs_files "Catalyst").

## [See also]

-   [Bootable media](https://wiki.gentoo.org/wiki/Bootable_media "Bootable media") --- Gentoo offers **bootable media** that can be used to [install](https://wiki.gentoo.org/wiki/Installation "Installation"), maintain, or try out Gentoo Linux
-   [Installation](https://wiki.gentoo.org/wiki/Installation "Installation") --- an overview of the principles and practices of installing Gentoo on a running system.
-   [Live image](https://wiki.gentoo.org/wiki/Live_image "Live image") --- an operating system (OS) environment contained within a file that can be used to [boot](https://en.wikipedia.org/wiki/Booting "wikipedia:Booting") a system

## [External resources]

-   [https://www.gentoo.org/downloads/](https://www.gentoo.org/downloads/) - Gentoo download page with links to official stage files.