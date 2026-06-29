Other languages:

-   [Deutsch](https://wiki.gentoo.org/wiki//etc/portage/make.conf/de "/etc/portage/make.conf (61% translated)")
-   [English]
-   [español](https://wiki.gentoo.org/wiki//etc/portage/make.conf/es "/etc/portage/make.conf (86% translated)")
-   [français](https://wiki.gentoo.org/wiki//etc/portage/make.conf/fr "/etc/portage/make.conf (96% translated)")
-   [italiano](https://wiki.gentoo.org/wiki//etc/portage/make.conf/it "/etc/portage/make.conf (12% translated)")
-   [magyar](https://wiki.gentoo.org/wiki//etc/portage/make.conf/hu "/etc/portage/make.conf (90% translated)")
-   [polski](https://wiki.gentoo.org/wiki//etc/portage/make.conf/pl "/etc/portage/make.conf (41% translated)")
-   [русский](https://wiki.gentoo.org/wiki//etc/portage/make.conf/ru "/etc/portage/make.conf (100% translated)")
-   [українська](https://wiki.gentoo.org/wiki//etc/portage/make.conf/uk "/etc/portage/make.conf (71% translated)")
-   [中文（中国大陆）‎](https://wiki.gentoo.org/wiki//etc/portage/make.conf/zh-cn "/etc/portage/make.conf (17% translated)")
-   [日本語](https://wiki.gentoo.org/wiki//etc/portage/make.conf/ja "/etc/portage/make.conf (100% translated)")

**[Portage - the heart of Gentoo](https://wiki.gentoo.org/wiki/Portage "Portage")**\
[emerge](https://wiki.gentoo.org/wiki/Emerge "Emerge") --- [configuration] --- [ebuild repository](https://wiki.gentoo.org/wiki/Ebuild_repository "Ebuild repository") --- [dispatch-conf](https://wiki.gentoo.org/wiki/Dispatch-conf "Dispatch-conf")\
[\
[world file](https://wiki.gentoo.org/wiki/Selected-packages_set_(Portage) "Selected-packages set (Portage)") --- [USE flags](https://wiki.gentoo.org/wiki/USE_flag "USE flag") --- [ebuilds](https://wiki.gentoo.org/wiki/Ebuild "Ebuild") --- [profiles](https://wiki.gentoo.org/wiki/Portage/Profiles "Portage/Profiles")\
[upgrades](https://wiki.gentoo.org/wiki/Upgrading_Gentoo "Upgrading Gentoo") --- [using testing packages](https://wiki.gentoo.org/wiki/Knowledge_Base:Accepting_a_keyword_for_a_single_package "Knowledge Base:Accepting a keyword for a single package") --- [Gentoo binhost](https://wiki.gentoo.org/wiki/Gentoo_Binary_Host_Quickstart "Gentoo Binary Host Quickstart")\
[tools](https://wiki.gentoo.org/wiki/Useful_Portage_tools "Useful Portage tools") --- [gentoolkit](https://wiki.gentoo.org/wiki/Gentoolkit "Gentoolkit") --- [eselect](https://wiki.gentoo.org/wiki/Eselect "Eselect")\
[Portage FAQ](https://wiki.gentoo.org/wiki/Project:Portage/FAQ "Project:Portage/FAQ") --- [cheat sheet](https://wiki.gentoo.org/wiki/Gentoo_Cheat_Sheet "Gentoo Cheat Sheet") --- [FAQ](https://wiki.gentoo.org/wiki/FAQ "FAQ")\
[all articles](https://wiki.gentoo.org/wiki/Category:Portage "Category:Portage")\
]

**[/etc/portage/make.conf]**, previously located at [/etc/make.conf], is the main configuration file used to customize the [Portage](https://wiki.gentoo.org/wiki/Portage "Portage") environment on a global level. The [/etc/portage](https://wiki.gentoo.org/wiki//etc/portage "/etc/portage") directory contains most other Portage configuration files.

Settings in [make.conf] will apply to every package that is emerged. These settings control many elements of Portage functionality such as global [USE flags](https://wiki.gentoo.org/wiki/USE_flag "USE flag"), [language (L10N)](https://wiki.gentoo.org/wiki/L10n "L10n") options, [Portage mirrors](https://wiki.gentoo.org/wiki/GENTOO_MIRRORS "GENTOO MIRRORS"), etc.

A very basic version gets installed [while extracting](https://wiki.gentoo.org/wiki/Handbook:AMD64/Installation/Stage#Unpacking_the_stage_file "Handbook:AMD64/Installation/Stage") the [Stage file](https://wiki.gentoo.org/wiki/Stage_file "Stage file"), and an example setup can be found at [/usr/share/portage/config/make.conf.example].

Like many Portage configuration files, [make.conf] can be a directory, and its contents will get summed together as if it were a single file.

** See also**\
The [Handbook](https://wiki.gentoo.org/wiki/Handbook "Handbook") covers using [make.conf], particularly in the [USE flags](https://wiki.gentoo.org/wiki/Handbook:AMD64/Working/USE "Handbook:AMD64/Working/USE"), [Portage features](https://wiki.gentoo.org/wiki/Handbook:AMD64/Working/Features "Handbook:AMD64/Working/Features") and [Variables](https://wiki.gentoo.org/wiki/Handbook:AMD64/Portage/Variables "Handbook:AMD64/Portage/Variables") sections. See [man make.conf] for comprehensive documentation.

## Contents

-   [[1] [Precedence]](#Precedence)
-   [[2] [Variables]](#Variables)
    -   [[2.1] [CHOST]](#CHOST)
    -   [[2.2] [CFLAGS and CXXFLAGS]](#CFLAGS_and_CXXFLAGS)
    -   [[2.3] [CONFIG_PROTECT]](#CONFIG_PROTECT)
    -   [[2.4] [FEATURES]](#FEATURES)
    -   [[2.5] [GENTOO_MIRRORS]](#GENTOO_MIRRORS)
    -   [[2.6] [MAKEOPTS]](#MAKEOPTS)
    -   [[2.7] [EMERGE_DEFAULT_OPTS]](#EMERGE_DEFAULT_OPTS)
    -   [[2.8] [PORTAGE_SCHEDULING_POLICY]](#PORTAGE_SCHEDULING_POLICY)
    -   [[2.9] [PORTAGE_TMPDIR]](#PORTAGE_TMPDIR)
    -   [[2.10] [DISTDIR]](#DISTDIR)
    -   [[2.11] [PKGDIR]](#PKGDIR)
    -   [[2.12] [USE]](#USE)
    -   [[2.13] [ACCEPT_LICENSE]](#ACCEPT_LICENSE)
    -   [[2.14] [USE_EXPAND]](#USE_EXPAND)
        -   [[2.14.1] [CPU_FLAGS\_\*]](#CPU_FLAGS_.2A)
        -   [[2.14.2] [INPUT_DEVICES]](#INPUT_DEVICES)
        -   [[2.14.3] [LINGUAS]](#LINGUAS)
        -   [[2.14.4] [L10N]](#L10N)
        -   [[2.14.5] [VIDEO_CARDS]](#VIDEO_CARDS)
-   [[3] [See also]](#See_also)
-   [[4] [External resources]](#External_resources)
-   [[5] [References]](#References)

## [[] Precedence]

The final Portage configuration is not only based on [make.conf]. Global settings defined in this file can be refined (or redefined) on a per-package basis in the [/etc/portage/package.use/] files as well as through environment variables. Default settings managed by the distribution are available as well (partially through the Portage package defaults, partially through the Gentoo [profile](https://wiki.gentoo.org/wiki/Profile_(Portage) "Profile (Portage)") that is in use).

** Note**\
Although Portage still supports the old [/etc/make.conf] file location, its use is discouraged in favor of [/etc/portage/make.conf]. When both files are available, the settings in [/etc/portage/make.conf] take precedence over those in [/etc/make.conf].

## [[] Variables]

There are many possible variables to customize in [make.conf]. Only the most commonly used ones are explained further within this article, with an example and a link to a more detailed article (if applicable). For more information, and the full list of variables, consult the [make.conf] [man page](https://wiki.gentoo.org/wiki/Man_page "Man page") by running:

`user `[`$`]`man make.conf`

Most variables are optional, can span multiple lines, but must not appear more than once.

** Note**\
Different configurations will require different variables to be set up. Do not treat the following examples as a definitive list, or a minimum set of requirements - set just the variables needed.

### [[] CHOST]

The `CHOST` variable is passed through the configure step of ebuilds to set the build-host of the system.

** Warning**\
[Portage profiles](https://wiki.gentoo.org/wiki/Profile_(Portage) "Profile (Portage)") already set the appropriate `CHOST` value, and updating it requires insight and experience in build chains.

** Note**\
Starting with profile version 23.0 it is recommended to not to list `CHOST` in the [make.conf] file.^[\[1\]](#cite_note-1)^

** See also**\
See the [`CHOST`](https://wiki.gentoo.org/wiki/CHOST "CHOST") article for more information.

### [[] CFLAGS and CXXFLAGS]

The `CFLAGS` and `CXXFLAGS` variables define the build and compile flags that will be used for all package deployments (some exceptions notwithstanding which filter out flags known to cause problems with the package). The `CFLAGS` variable is for C based applications, while `CXXFLAGS` is meant for C++ based applications. Most users will keep the content of both variables the same.

[FILE] **`/etc/portage/make.conf`Commonly used sane setting for CFLAGS and CXXFLAGS**

    CFLAGS="-march=native -O2 -pipe"
    CXXFLAGS="$"

** See also**\
For more information see the [GCC optimization](https://wiki.gentoo.org/wiki/GCC_optimization "GCC optimization") article, [safe CFLAGS](https://wiki.gentoo.org/wiki/Safe_CFLAGS "Safe CFLAGS"), and [CFLAGS and CXXFLAGS](https://wiki.gentoo.org/wiki/Handbook:AMD64/Installation/Stage#CFLAGS_and_CXXFLAGS "Handbook:AMD64/Installation/Stage") in the Gentoo Handbook. See also the [FAQ](https://wiki.gentoo.org/wiki/FAQ#Things_are_really_unstable_when_using_.27-O9_-ffast-math_-fomit-frame-pointer.27_optimizations._What_gives.3F "FAQ").

### [[] CONFIG_PROTECT]

The `CONFIG_PROTECT` variable contains a space-delimited list of files and directories that Portage will protect from automatic modification. Proposed changes to protected configuration locations will require manual merges from the system administrator (see [[dispatch-conf](https://wiki.gentoo.org/wiki/Dispatch-conf "Dispatch-conf")] or similar merge tools).

A current list of presently protected locations can be displayed with [[portageq](https://wiki.gentoo.org/wiki/Portageq "Portageq")]:

`user `[`$`]`portageq envvar CONFIG_PROTECT`

    /etc /usr/share/config /usr/share/gnupg/qualified.txt

Using [portageq] is a short hand alternative to running a regular expression search on verbose, informational output from the [emerge] command:

`user `[`$`]`emerge --verbose --info | grep -E '^CONFIG_PROTECT='`

    CONFIG_PROTECT="/etc /usr/share/config /usr/share/gnupg/qualified.txt"

Files or subdirectories defined within the `CONFIG_PROTECT` can be *excluded* from protection through the [`CONFIG_PROTECT_MASK`](https://wiki.gentoo.org/wiki/CONFIG_PROTECT_MASK "CONFIG PROTECT MASK") variable. Masking is useful when a parent directory should be protected, but a certain child directory beneath it.

The variable has a sane default setting handled by the Portage installation and the user\'s Gentoo [profile](https://wiki.gentoo.org/wiki/Portage/Profiles "Portage/Profiles"). It can be extended through the system environment (which is often used by applications that update the variable through their [/etc/env.d] file) and the user\'s [[/etc/portage/make.conf]] setting.

[FILE] **`/etc/portage/make.conf`Example `CONFIG_PROTECT` definitions**

    CONFIG_PROTECT="/var/bind"

See also the [Environment variables](https://wiki.gentoo.org/wiki/Handbook:AMD64/Working/EnvVar "Handbook:AMD64/Working/EnvVar") chapter in the Gentoo Handbook.

\

### [[] FEATURES]

The `FEATURES` variable contains a list of Portage features that the user wants enabled on the system, effectively influencing Portage\'s behavior. It is set by default via [/usr/share/portage/config/make.globals], but can be easily updated through [[/etc/portage/make.conf]]. Since this is an [incremental variable](https://dev.gentoo.org/~ulm/pms/head/pms.html#section-5.3.1), `FEATURES` values can be added without directly overriding the ones implemented through the Gentoo profile.

[FILE] **`/etc/portage/make.conf`Adding keepwork to FEATURES in Portage**

    FEATURES="keepwork"

For more information, please see [Portage features](https://wiki.gentoo.org/wiki/Handbook:AMD64/Working/Features "Handbook:AMD64/Working/Features") in the Gentoo Handbook and the [FEATURES](https://wiki.gentoo.org/wiki/FEATURES "FEATURES") article. For a complete list of available features, see [man 5 make.conf].

** See also**\
See the [FEATURES](https://wiki.gentoo.org/wiki/FEATURES "FEATURES") article for more information.

### [[] GENTOO_MIRRORS]

** See also**\
See the [GENTOO_MIRRORS](https://wiki.gentoo.org/wiki/GENTOO_MIRRORS "GENTOO MIRRORS") article.

### [[] MAKEOPTS]

The `MAKEOPTS` variable is used to specify arguments passed to [make] when packages are built from source. It defaults to `-j$(nproc) -l$(nproc)` if unset.

[FILE] **`/etc/portage/make.conf`Recommended setting for a dual-core processor with Hyper-Threading enabled with 8GB of RAM**

    # We recommend that the smaller of: number of threads, or ram/2GB is used.
    # So, for a dual-core processor w/ HT and 8GB of RAM, that's: min(4, 8) = 4
    MAKEOPTS="-j4 -l4"

** See also**\
See the [MAKEOPTS](https://wiki.gentoo.org/wiki/MAKEOPTS "MAKEOPTS") article for more information.

** Note**\
Read up on [`EMERGE_DEFAULT_OPTS`](https://wiki.gentoo.org/wiki//etc/portage/make.conf#EMERGE_DEFAULT_OPTS "/etc/portage/make.conf") as this variable influences build behavior as well.

### [[] EMERGE_DEFAULT_OPTS]

**EMERGE_DEFAULT_OPTS** is a variable for [Portage](https://wiki.gentoo.org/wiki/Portage "Portage") that defines entries to be appended to the [emerge] command line.

`EMERGE_DEFAULT_OPTS` allows for parallel [emerge] operations through the `--jobs ``N` and `--load-average ``X.Y` options. `EMERGE_DEFAULT_OPTS` is used by Portage to reference system load, or load average, and limit how many packages are built at a time.

To run up to three build jobs simultaneously:

[FILE] **`/etc/portage/make.conf`Enabling 3 parallel package builds**

    EMERGE_DEFAULT_OPTS="--jobs 3"

For more information, see the [EMERGE_DEFAULT_OPTS](https://wiki.gentoo.org/wiki/EMERGE_DEFAULT_OPTS "EMERGE DEFAULT OPTS") article.

### [[] PORTAGE_SCHEDULING_POLICY]

** See also**\
See the [Portage niceness](https://wiki.gentoo.org/wiki/Portage_niceness "Portage niceness") article.

### [[] PORTAGE_TMPDIR]

The `PORTAGE_TMPDIR` variable defines the location of the temporary files for Portage. The value defaults to [/var/tmp], resulting in [/var/tmp/portage] for the build location, [/var/tmp/ccache] for Portage\'s [ccache](https://wiki.gentoo.org/wiki/Handbook:AMD64/Working/Features#Caching_compilation_objects "Handbook:AMD64/Working/Features") support and so forth.

[FILE] **`/etc/portage/make.conf`Default PORTAGE_TMPDIR setting**

    PORTAGE_TMPDIR="/var/tmp"

On some systems, [/var/tmp/] may be mounted with the `noexec` option. The following error would be displayed by [emerge] when building packages:

`user `[`$`]`emerge --ask package`

    Can not execute files in /var/tmp/portage
    Likely cause is that you've mounted it with one of the
    following mount options: 'noexec', 'user', 'users'

    Please make sure that portage can execute files in this directory.

In this case, if removing the offending option from [/etc/fstab](https://wiki.gentoo.org/wiki//etc/fstab "/etc/fstab") isn\'t possible, `PORTAGE_TMPDIR` should be set to a different directory.

If enough memory is available, building packages can be accelerated by mounting `PORTAGE_TMPDIR` in RAM. See the article on [Portage TMPDIR on tmpfs](https://wiki.gentoo.org/wiki/Portage_TMPDIR_on_tmpfs "Portage TMPDIR on tmpfs") for more details.

### [[] DISTDIR]

The `DISTDIR` variable defines the location where Portage will store the downloaded source code archives. Its value defaults to [[/var/cache/distfiles](https://wiki.gentoo.org/wiki//var/cache/distfiles "/var/cache/distfiles")] on new installations. Previously the default was [\$/distfiles] which resolved to [/usr/portage/distfiles] by default.

Users can set the `DISTDIR` variable in [[/etc/portage/make.conf]]:

** Warning**\
**Only trusted users should be granted write access to `DISTDIR`\'s location**.

\

File integrity check and unpacking is a [non-atomic](https://bugs.gentoo.org/915330) operation, allowing for an attack where a file is swapped in between, possibly leading to compromise the system.

[FILE] **`/etc/portage/make.conf`Using a different DISTDIR location**

    DISTDIR=/var/gentoo/distfiles

For more information, please refer to the [DISTDIR](https://wiki.gentoo.org/wiki/DISTDIR "DISTDIR") article.

### [[] PKGDIR]

`PKGDIR` is the location [Portage](https://wiki.gentoo.org/wiki/Portage "Portage") keeps binary packages. By default, the location is set to [/var/cache/binpkgs].

Previously, binary packages were set to [\$/packages], which by default resolved to [/usr/portage/packages].

Run [man make.conf] for more information.

### [[] USE]

The `USE` variable allows the **system wide** setting or unsetting of [USE flags](https://wiki.gentoo.org/wiki/USE_flag "USE flag"). This variable is a space separated list and may span several lines.

[FILE] **`/etc/portage/make.conf`[Global USE flags example](https://wiki.gentoo.org/wiki/Handbook:AMD64/Working/USE#Declare_permanent_USE_flags "Handbook:AMD64/Working/USE")**

    USE="-kde -qt5 ldap"

** See also**\
See the article on [USE flags](https://wiki.gentoo.org/wiki/USE_flag "USE flag") for full explanation. See [per package control](https://wiki.gentoo.org/wiki/Handbook:AMD64/Working/USE#Declaring_USE_flags_for_individual_packages "Handbook:AMD64/Working/USE") of USE flags, and the [[/etc/portage/package.use](https://wiki.gentoo.org/wiki//etc/portage/package.use "/etc/portage/package.use")] file, about setting USE flags for an individual package.

** Note**\
Always consider whether it is worth setting a USE flag globally and what implications this will have on the system, or if it is preferable to just set a flag for one or several packages individually.

** Tip**\
A USE flag may be temporarily set on the command line to check what effect it will have, before permanently recording it in either [/etc/portage/make.conf] or [/etc/portage/package.use](https://wiki.gentoo.org/wiki//etc/portage/package.use "/etc/portage/package.use"): [USE=\"\[USE flag to test\]\" emerge \--pretend \--verbose \--update \--deep \--newuse world]

### [[] ACCEPT_LICENSE]

The `ACCEPT_LICENSE` variable tells Portage which software licenses are allowed to be installed on the system. Packages licensed under an agreement that has not been formally accepted by the system administrator will not be installed on the system.

See [license groups](https://wiki.gentoo.org/wiki/License_groups "License groups") for a categorical breakdown of available software licenses.

[FILE] **`/etc/portage/make.conf`To accept all [licenses](https://wiki.gentoo.org/wiki//var/db/repos/gentoo/licenses "/var/db/repos/gentoo/licenses") on all packages**

    ACCEPT_LICENSE="*"

The preferred way to accept all licenses is to set `-@EULA` which allows users to check over the terms of proprietary software.

[FILE] **`/etc/portage/make.conf`To accept all licenses on all packages except proprietary**

    ACCEPT_LICENSE="* -@EULA"

[FILE] **`/etc/portage/make.conf`To accept free software only**

    ACCEPT_LICENSE="-* @FREE"

### [[] USE_EXPAND]

** Important**\
In the past USE_EXPAND flags were set in [/etc/portage/make.conf] but this can lead to ordering issues with [Portage](https://wiki.gentoo.org/wiki/Portage "Portage"). Because of this, this article now uses the preferred method [/etc/portage/package.use].

The `USE_EXPAND` variable is a list set in [profiles/base/make.defaults](https://gitweb.gentoo.org/repo/gentoo.git/tree/profiles/base/make.defaults) as of Portage 2.0.51.20.^[\[2\]](#cite_note-2)^

#### [][[] CPU_FLAGS\_\*]

** See also**\
See the [CPU_FLAGS\_\*](https://wiki.gentoo.org/wiki/CPU_FLAGS_* "CPU FLAGS *") article for more information.

The `CPU_FLAGS_*` variables inform Portage about the CPU flags (features) permitted by the CPU. This information is used to optimize package builds specifically for the targeted features. The currently supported variables are `CPU_FLAGS_X86` (for **[amd64]** and **[x86]** architectures), `CPU_FLAGS_ARM` (for **[arm]** and **[arm64]** architectures), and `CPU_FLAGS_PPC` (for **[ppc]** and **[ppc64]** architectures).

The [cpuid2cpuflags] utility (found in the [[[app-portage/cpuid2cpuflags]](https://packages.gentoo.org/packages/app-portage/cpuid2cpuflags)[]] package) can be used to query a complete listing of CPU flags supported by the system\'s processor. After emerging the package, issue:

`user `[`$`]`cpuid2cpuflags`

    CPU_FLAGS_X86: aes avx f16c mmx mmxext pclmul popcnt sse sse2 sse3 sse4_1 sse4_2 ssse3

Place this string into [/etc/portage/packages.use] as is:

[FILE] **`/etc/portage/package.use/00cpu-flags`**

    */* CPU_FLAGS_X86: aes avx f16c mmx mmxext pclmul popcnt sse sse2 sse3 sse4_1 sse4_2 ssse3

#### [[] INPUT_DEVICES]

See the [make.conf](https://wiki.gentoo.org/wiki/Xorg/Guide#make.conf "Xorg/Guide") section of the Xorg/Guide article and the [possible values](https://packages.gentoo.org/useflags/input_devices_libinput).

#### [[] LINGUAS]

** See also**\
See [LINGUAS in the Localization guide.](https://wiki.gentoo.org/wiki/Localization/Guide#LINGUAS "Localization/Guide")

[FILE] **`/etc/portage/package.use/00local`**

    */* LINGUAS: de pt_BR en en_US en_GB

#### [[] L10N]

** See also**\
See [L10N in the localization guide](https://wiki.gentoo.org/wiki/Localization/Guide#L10N "Localization/Guide").

[FILE] **`/etc/portage/package.use/00local`**

    */* L10N: de pt-BR en en-US en-GB

** Note**\
While common two letter language codes (like `de` or `fr`) are identical in `LINGUAS` and `L10N`, more complex entries have a different syntax because `L10N` uses [IETF language tags](https://www.w3.org/International/articles/language-tags/) (aka BCP 47). For example, `pt_BR` and `sr@latin` in `LINGUAS` become `pt-BR` and `sr-Latn` in `L10N`, respectively.

#### [[] VIDEO_CARDS]

For possible values of this `USE_EXPAND` variable see [`VIDEO_CARDS`](https://packages.gentoo.org/useflags/expand#video_cards).

  -------------- ----------------------------------------- --------------------------------------------------------------------------------------------
  Machine        Discrete video card                       VIDEO_CARDS
  Intel x86      None                                      See [Intel#Feature support](https://wiki.gentoo.org/wiki/Intel#Feature_support "Intel")
  x86/ARM        Nvidia                                    `nvidia`
  Any            Nvidia except Maxwell, Pascal and Volta   `nouveau`
  Any            AMD since Sea Islands                     `amdgpu radeonsi`
  Any            ATI and older AMD                         See [radeon#Feature support](https://wiki.gentoo.org/wiki/Radeon#Feature_support "Radeon")
  Any            Intel                                     `intel`
  Raspberry Pi   N/A                                       `vc4`
  QEMU/KVM       Any                                       `virgl`
  WSL            Any                                       `d3d12`
  -------------- ----------------------------------------- --------------------------------------------------------------------------------------------

From the common combinations of machines and video cards, substitute the name of the driver(s) to be used.

Appropriate `VIDEO_CARDS` value(s) pull in the correct driver(s).

After changing `VIDEO_CARDS` values remember to update the system using the following command so the changes take effect:

[FILE] **`/etc/portage/package.use/00video`**

    */* VIDEO_CARDS: -* intel nouveau radeon radeonsi

`root `[`#`]`emerge --getbinpkg --ask --changed-use --deep @world`

Omit `--getbinpkg` to not use the configured binary package host.

For the average user, if a graphical desktop environment is to be used this variable *should* be explicitly defined. For further information see [the Xorg Guide make.conf section](https://wiki.gentoo.org/wiki/Xorg/Guide#make.conf "Xorg/Guide").

For more details see the [AMDGPU](https://wiki.gentoo.org/wiki/AMDGPU "AMDGPU"), [Intel](https://wiki.gentoo.org/wiki/Intel "Intel"), [Nouveau](https://wiki.gentoo.org/wiki/Nouveau "Nouveau"), or [NVIDIA](https://wiki.gentoo.org/wiki/NVIDIA "NVIDIA") articles.

## [[] See also]

-   [Portage variables (AMD64 Handbook)](https://wiki.gentoo.org/wiki/Handbook:AMD64/Portage/Variables "Handbook:AMD64/Portage/Variables")
-   [Portage features (AMD64 Handbook)](https://wiki.gentoo.org/wiki/Handbook:AMD64/Working/Features "Handbook:AMD64/Working/Features")
-   [Environment variables (AMD64 Handbook)](https://wiki.gentoo.org/wiki/Handbook:AMD64/Working/EnvVar "Handbook:AMD64/Working/EnvVar")
-   [Advanced Portage features (AMD64 Handbook)](https://wiki.gentoo.org/wiki/Handbook:AMD64/Portage/Advanced "Handbook:AMD64/Portage/Advanced")
-   [Emerge issues with having `/.git/index.lock` in root](https://bugs.gentoo.org/707930#c5)

## [[] External resources]

-   [make.conf - custom settings for Portage](https://devmanual.gentoo.org/eclass-reference/make.conf/index.html) - make.conf man page.

## [[] References]

1.  [[[↑](#cite_ref-1)] [[Profile upgrade to version 23.0 available](https://www.gentoo.org/support/news-items/2024-03-22-new-23-profiles.html), gentoo.org, March 22, 2024. Retrieved on March 24, 2024.]]
2.  [[[↑](#cite_ref-2)] [[https://devmanual.gentoo.org/general-concepts/use-flags/#use_expand-and-arch-use-flags](https://devmanual.gentoo.org/general-concepts/use-flags/#use_expand-and-arch-use-flags)]]