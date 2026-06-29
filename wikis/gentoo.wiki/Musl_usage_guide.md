[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Musl&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[![Gentoo peach graphic](/images/thumb/a/ad/Gentoo-logo-peach.svg/25px-Gentoo-logo-peach.svg.png)](https://wiki.gentoo.org/wiki/Project:Musl "Project:Musl")][Project](https://wiki.gentoo.org/wiki/Project:Musl "Project:Musl")

[[]][Home](https://musl.libc.org/)

[[]][Official documentation](https://musl.libc.org/manual.html)

[[]][Package information](https://packages.gentoo.org/packages/sys-libs/musl)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Musl "wikipedia:Musl")

[[]][Official project wiki](https://wiki.musl-libc.org/)

[[]][[#musl](ircs://irc.libera.chat/#musl)] ([[webchat](https://web.libera.chat/#musl)])

**musl** is a [standard C library](https://wiki.gentoo.org/wiki/Libc "Libc") implementation that strives to be lightweight and correct in the sense of standards. It is a replacement for the widely used [GNU C library](https://wiki.gentoo.org/wiki/Glibc "Glibc") (glibc).

musl is supported by Gentoo for most common CPUs on most [Architectures](https://wiki.gentoo.org/wiki/Handbook:Main_Page#Architectures "Handbook:Main Page").

This guide is about *using* musl libc, for a *development* guide, see [musl porting notes](https://wiki.gentoo.org/wiki/Musl_porting_notes "Musl porting notes").

** Important**\
Musl on Gentoo won\'t usually be the easiest path to follow. Most users will probably want a more standard [Glibc](https://wiki.gentoo.org/wiki/Glibc "Glibc") installation unless they have a specific reason not to.

\
Some packages don\'t currently support musl-based systems and simply won\'t compile, and some of the upstream projects for those packages may have no plans to support musl.\
\

musl-based [profiles](https://wiki.gentoo.org/wiki/Profile_(Portage) "Profile (Portage)") are currently labeled \"experimental\", i.e. [eselect profile list] would show \"(exp)\" after the profile name.

## Contents

-   [[1] [Installation]](#Installation)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Locales]](#Locales)
    -   [[2.2] [Timezones]](#Timezones)
        -   [[2.2.1] [Method 1: Setting TZ to a POSIX timezone code]](#Method_1:_Setting_TZ_to_a_POSIX_timezone_code)
        -   [[2.2.2] [Method 2: Setting TZ to binary timezone file path]](#Method_2:_Setting_TZ_to_binary_timezone_file_path)
-   [[3] [Usage]](#Usage)
    -   [[3.1] [Running glibc software on a musl-based system]](#Running_glibc_software_on_a_musl-based_system)
        -   [[3.1.1] [Flatpak]](#Flatpak)
        -   [[3.1.2] [Chroot]](#Chroot)
        -   [[3.1.3] [Distrobox]](#Distrobox)
-   [[4] [Troubleshooting]](#Troubleshooting)
    -   [[4.1] [Build failures]](#Build_failures)
    -   [[4.2] [Rust]](#Rust)
-   [[5] [See also]](#See_also)
-   [[6] [External resources]](#External_resources)

## [Installation]

Choosing musl over glibc has to be done at install time, because replacing the standard C library on an already installed system is not possible. This is done by unpacking the -musl [stage3](https://wiki.gentoo.org/wiki/Stage_file#Stage_3 "Stage file") tarball instead of the default glibc one.

The [install handbook](https://wiki.gentoo.org/wiki/Handbook:Main_Page "Handbook:Main Page") for the target architecture can be used as normal, except that generating locales is not necessary on musl libc.

## [Configuration]

### [Locales]

musl does not support [locales](https://wiki.gentoo.org/wiki/Localization/Guide#What_are_locales.3F "Localization/Guide") (at least not in the traditional way glibc would). However, it is still possible to install [[[sys-apps/musl-locales]](https://packages.gentoo.org/packages/sys-apps/musl-locales)[]] to at least have a [locale] binary on the system for compatibility:

`root `[`#`]`emerge --ask sys-apps/musl-locales`

Because of the limitations within musl, the [locale-gen] command is unavailable. To set a locale, first set *MUSL_LOCPATH* like:

[FILE] **`/etc/env.d/00local`Set MUSL_LOCPATH to the path of musl locales**

    MUSL_LOCPATH="/usr/share/i18n/locales/musl"

Then, to view available locales simply do:

`root `[`#`]`eselect locale list`

    Available targets for the LANG variable:
      [1]   C
      [2]   C.UTF-8
      [3]   sr_RS.UTF-8
      [4]   cs_CZ.UTF-8
      [5]   nb_NO.UTF-8
      [6]   de_DE.UTF-8
      [7]   sv_SE.UTF-8
      [8]   nl_NL.UTF-8
      [9]   fr_FR.UTF-8
      [10]  fi_FI.UTF-8
      [11]  en_GB.UTF-8
      [12]  it_IT.UTF-8
      [13]  pt_PT.UTF-8
      [14]  en_US.UTF-8
      [15]  de_CH.UTF-8
      [16]  es_ES.UTF-8 *
      [17]  pt_BR.UTF-8
      [18]  ru_RU.UTF-8
      [ ]   (free form)

And set the one from the available choices likewise.

** Note**\
Keep in mind that the desired locale may not be complete or even available.

### [Timezones]

By default, the [/usr/share/zoneinfo] directory is not populated with binary timezone files as it would be on a glibc system. This is because [[[sys-libs/timezone-data]](https://packages.gentoo.org/packages/sys-libs/timezone-data)[]] is not packaged with any of the musl stage3 builds, due to it going against how a timezone should be set on musl.

Changing the timezone must be done via setting the *TZ* variable according to the [POSIX timezone specification](https://pubs.opengroup.org/onlinepubs/9699919799/basedefs/V1_chap08.html#tag_08_03) in [/etc/env.d/00local] file.

** See also**\
[Defining variables globally](https://wiki.gentoo.org/wiki/Handbook:Parts/Working/EnvVar#Defining_variables_globally "Handbook:Parts/Working/EnvVar")

There are 2 methods of setting a timezone on musl.

#### [Method 1: Setting TZ to a POSIX timezone code]

A quick and easy way to get the proper `TZ` variable for the timezone, is to temporarily emerge [[[sys-libs/timezone-data]](https://packages.gentoo.org/packages/sys-libs/timezone-data)[]]:

`root `[`#`]`emerge --ask sys-libs/timezone-data`

Then grab the string at the end of the binary file for timezone of choice. This is the POSIX specification. In this example a value of `America/New_York` will be used:

`root `[`#`]`cat /usr/share/zoneinfo/America/New_York | tail -n 1`

    EST5EDT,M3.2.0,M11.1.0

Finally, edit the [/etc/env.d/00local] file, and specify the `TZ` value like so:

[FILE] **`/etc/env.d/00local`Setting TZ to the posix timezone specification for New York**

    TZ="EST5EDT,M3.2.0,M11.1.0"

And update the environment:

`root `[`#`]`env-update && source /etc/profile`

Remove [[[sys-libs/timezone-data]](https://packages.gentoo.org/packages/sys-libs/timezone-data)[]] package:

`root `[`#`]`emerge --ask --unmerge sys-libs/timezone-data`

#### [Method 2: Setting TZ to binary timezone file path]

This is the recommended option, as it is simple and reliable since it uses a binary timezone file instead of a posix timezone specification.

To set this up, simply install [[[sys-libs/timezone-data]](https://packages.gentoo.org/packages/sys-libs/timezone-data)[]] like so:

`root `[`#`]`emerge --ask sys-libs/timezone-data`

Then edit [/etc/env.d/00local] and set *TZ* to the path to the timezone of choice inside [/usr/share/zoneinfo] like so:

[FILE] **`/etc/env.d/00local`Setting TZ to the path of the binary timezone file of New York**

    TZ="/usr/share/zoneinfo/America/New_York"

** Note**\
For this method, the path does not have to be absolute. If an exact path is not given, musl will search for the timezone in /usr/share/zoneinfo, /share/zoneinfo, and /etc/zoneinfo. Any path with a dot in it will be rejected and ignored by musl.

And update the environment:

`root `[`#`]`env-update && source /etc/profile`

## [Usage]

### [Running glibc software on a musl-based system]

Some pieces of software are not yet compatible with musl libc. This is usually caused because:

1.  The software is closed source, so compiling for musl is not possible unless contacting the proprietor. Example: [[[www-client/google-chrome]](https://packages.gentoo.org/packages/www-client/google-chrome)[]]
2.  Upstream is not willing to support musl. Maintaining musl patches downstream involves a lot of hassle, and is usually not done. Example: [[[www-client/chromium]](https://packages.gentoo.org/packages/www-client/chromium)[]]

#### [Flatpak]

The easiest method of working around this is by using [Flatpak](https://wiki.gentoo.org/wiki/Flatpak "Flatpak"). Flatpak works by **sandboxing** applications and running them with provided runtimes. The runtimes include needed libraries such as glibc, and therefore applications will run as normal.

#### [Chroot]

Using [chroots](https://wiki.gentoo.org/wiki/Chroot "Chroot") is another method for running glibc programs. Chroot is used to change the apparent root directory, which means programs running inside the chroot will see another directory structure. In this case a normal Gentoo glibc installation can be installed on top of a Gentoo musl system. Using chroots for this purpose often requires setting up sound and graphics, instructions for this can be found at [Chroot#Sound and graphics](https://wiki.gentoo.org/wiki/Chroot#Sound_and_graphics "Chroot").

#### [Distrobox]

Unlike other listed methods [distrobox](https://wiki.gentoo.org/wiki/Distrobox "Distrobox") aims to utilize [docker](https://wiki.gentoo.org/wiki/Docker "Docker") or [podman](https://wiki.gentoo.org/wiki/Podman "Podman") containers to run desired software. By itself distrobox is a wrapper scripts for supported container engines. It\'s a lot easier to work with compared to chroot, but more complicated than flatpak. Distrobox containers by design get full access to user\'s home, sound, external storage and so on. Any preferred container image could be used.

## [Troubleshooting]

### [Build failures]

musl has a focus on being standards compliant and correct, which means that some packages can fail to build if they use non-standard functionality often referred to as extensions. Normally these are GNU extensions provided by glibc, which is the most widely used standard C library on Linux systems such as Gentoo.

The best way of dealing with these build failures is to fix them and report upstream. It is also a good idea to file a bug on the [Gentoo Bugzilla](https://bugs.gentoo.org/). More information regarding porting software to musl can be found here: [musl porting notes](https://wiki.gentoo.org/wiki/Musl_porting_notes "Musl porting notes"). For user convenience there are also standalone packages that provide functionality not included in musl, see [Musl_porting_notes#Standalone_packages](https://wiki.gentoo.org/wiki/Musl_porting_notes#Standalone_packages "Musl porting notes").

### [Rust]

On LLVM-based systems using musl, packages may break if [[[dev-lang/rust-bin]](https://packages.gentoo.org/packages/dev-lang/rust-bin)[]] is the active Rust installation due to compatibility issues arising from its binary nature and musl ([[[bug #912154]](https://bugs.gentoo.org/show_bug.cgi?id=912154)[]]).

Check which Rust installation is active:

`user `[`$`]`eselect rust list`

If `rust-bin` is active, the workaround is to emerge `dev-lang/rust` manually:

`root `[`#`]`emerge --ask --verbose dev-lang/rust`

Then, use `eselect rust` to set it active, and finally, attempt to re-emerge the affected package.

This may lead to a circular dependency that cannot be resolved. In this case [bootstrap Rust](https://wiki.gentoo.org/wiki/LLVM#Bootstrapping_Rust "LLVM").

## [See also]

-   [Catalyst/New Musl Stages Creation](https://wiki.gentoo.org/wiki/Catalyst/New_Musl_Stages_Creation "Catalyst/New Musl Stages Creation") --- intended for those that wish to **build [musl] stages** on architectures that don\'t have them built by the official Gentoo build server.
-   [Libc](https://wiki.gentoo.org/wiki/Libc "Libc") --- a software component that allows userspace applications to interact with operating system services.
-   [Musl porting notes](https://wiki.gentoo.org/wiki/Musl_porting_notes "Musl porting notes") --- pointers on getting software to compile with musl
-   [Musl porting notes/1.2.4](https://wiki.gentoo.org/wiki/Musl_porting_notes/1.2.4 "Musl porting notes/1.2.4")
-   [Project:Musl](https://wiki.gentoo.org/wiki/Project:Musl "Project:Musl")

## [External resources]

-   [voidnsrun](https://github.com/gch1p/voidnsrun) - Tool to run glibc programs on musl using mount namespaces and bind mounts
-   [Alpine software management guide](https://wiki.alpinelinux.org/wiki/Software_management) - guide on software management for musl based distribution. It\'s discouraged to blindly follow it, since Alpine is a binary distribution. Though it provides nice instructions for running binaries already compiled for glibc.